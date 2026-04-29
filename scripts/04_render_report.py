"""Render the verified.json into a markdown report under reports/.

Usage:
    python3 scripts/04_render_report.py
"""
import json, os, datetime

ROOT = os.path.join(os.path.dirname(__file__), "..")
IN = os.path.join(ROOT, "data", "verified.json")
TODAY = datetime.date.today().isoformat()
OUT = os.path.join(ROOT, "reports", f"protocols-verified-open-source-{TODAY}.md")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def fmt_tvl(t):
    return f"${t/1_000_000:.2f}M" if t >= 1_000_000 else f"${t/1_000:.0f}k"

def fmt_chains(c):
    if not c:
        return "—"
    return ", ".join(c[:3]) + (f" +{len(c)-3}" if len(c) > 3 else "")

def fmt_repos(repos):
    if not repos:
        return "—"
    parts = []
    for rp in repos[:3]:
        short = rp["name"].split("/")[-1]
        parts.append(f"[{short}]({rp['url']}) `{rp['lang']}` ★{rp['stars']}")
    extra = "" if len(repos) <= 3 else f" +{len(repos)-3} more"
    return "<br>".join(parts) + extra

def main():
    with open(IN) as f:
        r = json.load(f)
    verified = sorted([v for v in r.values() if v["overall"] == "VERIFIED"], key=lambda v: -v["tvl"])
    no_repo = sorted([v for v in r.values() if v["overall"] == "NO_CONTRACT_REPO"], key=lambda v: -v["tvl"])
    not_found = [v for v in r.values() if v["overall"] == "ORG_404"]

    lines = []
    lines.append(f"# Verified Open-Source DeFi Protocols")
    lines.append("")
    lines.append(f"**Snapshot:** {TODAY}")
    lines.append(f"**Sources:** `https://api.llama.fi/protocols` + GitHub REST API `/users/{{org}}/repos`")
    lines.append("")
    lines.append("## Verdict Summary")
    lines.append("")
    lines.append(f"- **VERIFIED** — org has at least one contract-bearing repo: **{len(verified)}**")
    lines.append(f"- **NO_CONTRACT_REPO** — org exists but only frontend/SDK/docs detected: **{len(no_repo)}**")
    lines.append(f"- **ORG_404** — declared github org returns 404: **{len(not_found)}**")
    lines.append("")
    lines.append("## Classification heuristic")
    lines.append("")
    lines.append("A repo is flagged as a contract repo if any of:")
    lines.append("- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}")
    lines.append("- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)")
    lines.append("- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract")
    lines.append("- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`")
    lines.append("")
    lines.append("**Caveats:** GitHub's auto-detected primary language only; multi-language monorepos may be misclassified. Forks & archived repos are skipped. Manual spot-check is still recommended before forking or integrating with a protocol.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## VERIFIED — {len(verified)} protocols")
    lines.append("")
    lines.append("| # | Protocol | TVL | Category | Chains | GitHub | Contract Repo(s) |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, v in enumerate(verified, 1):
        gh = ", ".join(f"[{g}](https://github.com/{g})" for g in v["github"][:2])
        lines.append(f"| {i} | **{v['name']}** | {fmt_tvl(v['tvl'])} | {v.get('category') or '—'} | {fmt_chains(v.get('chains'))} | {gh} | {fmt_repos(v['contract_repos'])} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## NO_CONTRACT_REPO — {len(no_repo)} protocols")
    lines.append("")
    lines.append("These protocols declare a public github org but no contract-bearing repo was detected by the heuristic. Worth manual review before assuming closed-source.")
    lines.append("")
    lines.append("| # | Protocol | TVL | Category | Chains | GitHub |")
    lines.append("|---|---|---|---|---|---|")
    for i, v in enumerate(no_repo, 1):
        gh = ", ".join(f"[{g}](https://github.com/{g})" for g in v["github"][:2])
        lines.append(f"| {i} | {v['name']} | {fmt_tvl(v['tvl'])} | {v.get('category') or '—'} | {fmt_chains(v.get('chains'))} | {gh} |")
    lines.append("")
    if not_found:
        lines.append("---")
        lines.append("")
        lines.append(f"## ORG_404 — {len(not_found)} protocols")
        lines.append("")
        for v in not_found:
            lines.append(f"- {v['name']} ({fmt_tvl(v['tvl'])}) — declared org: `{v['github']}`")
        lines.append("")

    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    # Also update reports/latest.md
    latest = os.path.join(ROOT, "reports", "latest.md")
    with open(latest, "w") as f:
        f.write("\n".join(lines))
    print(f"[render] wrote {OUT}")
    print(f"[render] wrote {latest}")
    print(f"[render] VERIFIED={len(verified)} NO_CONTRACT_REPO={len(no_repo)} ORG_404={len(not_found)}")

if __name__ == "__main__":
    main()
