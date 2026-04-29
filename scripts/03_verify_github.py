"""For each filtered protocol, fetch its GitHub org's public repos and classify
whether at least one repo appears to host smart-contract source.

Usage:
    GH_TOKEN=$(gh auth token) python3 scripts/03_verify_github.py

Reads:
    data/filtered.json
Writes:
    data/verified.json
"""
import os, json, asyncio, aiohttp, sys, time, re

ROOT = os.path.join(os.path.dirname(__file__), "..")
IN = os.path.join(ROOT, "data", "filtered.json")
OUT = os.path.join(ROOT, "data", "verified.json")

TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
HEADERS = {"Accept": "application/vnd.github+json",
           "User-Agent": "defillama-protocol-scanner/1.0"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

CONTRACT_LANGS = {
    "Solidity", "Vyper", "Move", "Cairo", "Cairo 1.0", "Cairo 0",
    "Huff", "FunC", "Tact", "Sway", "Clarity", "Marlowe",
    "PlutusTx", "Plutus", "Haskell",
}
NAME_HINTS = re.compile(
    r"(?i)\b(contracts?|protocol|core|smart-?contract|onchain|on-chain|"
    r"solidity|move|cairo|cosmwasm|anchor|hardhat|foundry)\b"
)
RUST_HINTS = re.compile(
    r"(?i)\b(cosmwasm|anchor|near|solana|terra|injective|sei|osmosis)\b"
)

async def fetch_json(session, url, params, sem):
    for attempt in range(4):
        async with sem:
            try:
                async with session.get(url, params=params, timeout=30) as r:
                    if r.status == 200:
                        return await r.json(), None
                    if r.status == 404:
                        return None, "404"
                    if r.status in (403, 429):
                        await asyncio.sleep(2 ** (attempt + 1))
                    else:
                        return None, f"http {r.status}"
            except Exception as e:
                if attempt == 3:
                    return None, str(e)
                await asyncio.sleep(1 + attempt)
    return None, "max retries"

def classify(repos):
    if not repos:
        return "EMPTY_ORG", []
    contract_repos = []
    for rp in repos:
        if rp.get("fork") or rp.get("archived"):
            continue
        lang = rp.get("language") or ""
        name = rp.get("name") or ""
        desc = rp.get("description") or ""
        full = name + " " + desc
        why = None
        if lang in CONTRACT_LANGS:
            why = f"lang={lang}"
        elif lang == "Rust" and RUST_HINTS.search(full):
            why = "Rust+chain-keyword"
        elif lang == "TypeScript" and re.search(r"(?i)hardhat|foundry|smart-?contract", full):
            why = "TS+hardhat/foundry"
        elif re.search(r"(?i)contracts?|protocol|core|hardhat|foundry|cosmwasm|anchor", name):
            why = f"name-match: {name}"
        if why:
            contract_repos.append({
                "name": rp["full_name"],
                "lang": lang,
                "stars": rp.get("stargazers_count", 0),
                "url": rp.get("html_url"),
                "why": why,
            })
    return ("VERIFIED", contract_repos) if contract_repos else ("NO_CONTRACT_REPO", [])

async def check_org(session, org, sem):
    data, err = await fetch_json(
        session, f"https://api.github.com/users/{org}/repos",
        {"per_page": 100, "type": "public", "sort": "updated"}, sem
    )
    if err == "404":
        return "ORG_404", []
    if err:
        return f"ERR:{err}", []
    return classify(data)

async def process(session, p, sem, results):
    orgs = p.get("github") or []
    verdicts = []
    contract_repos = []
    for org in orgs:
        v, repos = await check_org(session, org, sem)
        verdicts.append((org, v))
        contract_repos.extend(repos)
    overall = "VERIFIED" if any(v == "VERIFIED" for _, v in verdicts) else \
              "ORG_404" if all(v == "ORG_404" for _, v in verdicts) else \
              "NO_CONTRACT_REPO"
    results[p["slug"]] = {
        "name": p["name"],
        "tvl": p["tvl"],
        "category": p.get("category"),
        "chains": p.get("chains"),
        "url": p.get("url"),
        "github": orgs,
        "org_verdicts": verdicts,
        "overall": overall,
        "contract_repos": contract_repos[:5],
    }

async def main():
    if not TOKEN:
        print("[verify] WARNING: no GH_TOKEN set — unauthenticated rate limit is 60/hr.", file=sys.stderr)
    with open(IN) as f:
        protos = json.load(f)
    print(f"[verify] verifying {len(protos)} protocols")
    results = {}
    sem = asyncio.Semaphore(15)
    start = time.time()
    conn = aiohttp.TCPConnector(limit=30)
    async with aiohttp.ClientSession(connector=conn, headers=HEADERS) as session:
        tasks = [process(session, p, sem, results) for p in protos]
        for i, t in enumerate(asyncio.as_completed(tasks)):
            await t
            if (i + 1) % 50 == 0:
                print(f"[verify] {i+1}/{len(protos)} done in {time.time()-start:.1f}s")
    with open(OUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[verify] saved {len(results)} → {OUT} in {time.time()-start:.1f}s")

if __name__ == "__main__":
    asyncio.run(main())
