# DefiLlama Protocol Scanner

Find DeFi protocols in a chosen TVL band whose contracts appear to be open-sourced, and inspect any one of them on-chain to see exactly which contracts are holding the TVL.

The repo answers two questions end-to-end:

1. **Which protocols sit in TVL band $X–$Y across all chains, and have a public GitHub org with a contract-bearing repo?** → `scripts/run_pipeline.sh` produces a markdown report in `reports/`.
2. **For one specific protocol, what contracts hold its TVL right now and what are the live balances?** → `scripts/protocol_balances.py` reads the addresses straight from the DefiLlama adapter and queries Ethereum.

A worked example for **Altitude.Fi** is bundled.

---

## Quick start

```bash
git clone <your-fork-url> defillama-protocol-scanner
cd defillama-protocol-scanner

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Optional but recommended — raises GitHub rate limit from 60/hr to 5000/hr
export GH_TOKEN=$(gh auth token)   # any classic/fine-grained PAT works

# Default: TVL $300k–$5M
bash scripts/run_pipeline.sh

# Custom band
TVL_MIN=400000 TVL_MAX=10000000 bash scripts/run_pipeline.sh

# Inspect one protocol on-chain
python3 scripts/protocol_balances.py --protocol altitude-fi
```

Outputs:

- `data/protocols.json` — full DefiLlama protocols dump
- `data/filtered.json` — protocols inside the TVL band with a declared GitHub org
- `data/verified.json` — per-protocol verdict from inspecting each org's repos
- `reports/protocols-verified-open-source-YYYY-MM-DD.md` — dated report
- `reports/latest.md` — symlink-style copy of the latest report

---

## Requirements

- Python 3.10+
- `aiohttp` (in `requirements.txt`)
- A GitHub token (`GH_TOKEN` env var) — strongly recommended; the verifier hits 260+ orgs and the unauthenticated GitHub API limit is 60 requests/hour
- An Ethereum JSON-RPC URL for `protocol_balances.py` — defaults to `https://ethereum.publicnode.com` (free, no key); override via `--rpc` or the `ETH_RPC` env var

No paid APIs are required. Everything used is free:

| Service | What we call | Auth |
|---|---|---|
| DefiLlama | `https://api.llama.fi/protocols`, `/protocol/{slug}`, `https://coins.llama.fi/prices/current/{coinId}` | none |
| GitHub | `https://api.github.com/users/{org}/repos` | bearer token recommended |
| Ethereum | any public JSON-RPC (`eth_call` for `totalSupply`/`balanceOf`) | none for `publicnode.com` |

---

## How it works

### Stage 1 — fetch (`scripts/01_fetch_protocols.py`)

Pulls the full DefiLlama protocols list (one HTTP call, ~7 MB). Saves to `data/protocols.json`.

### Stage 2 — filter (`scripts/02_filter_tvl_band.py`)

Filters to protocols where `min_tvl ≤ tvl ≤ max_tvl` **and** the `github` field is non-empty.

> **Why not use DefiLlama's `openSource` boolean?** Because it's effectively unmaintained — only ~10 protocols across the entire $400k–$10M band have it set at all. The `github` field (a declared public org on the protocol's DefiLlama page) is populated for hundreds of protocols and is the only practical signal at scale.

### Stage 3 — verify (`scripts/03_verify_github.py`)

For each filtered protocol, calls `GET /users/{org}/repos` (works for both users and orgs), then classifies the org by inspecting each repo's primary language and name. A repo is flagged as a **contract repo** if any of:

- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}
- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)
- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract
- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`

Each protocol gets one of three verdicts:

| Verdict | Meaning |
|---|---|
| `VERIFIED` | The org has at least one contract-bearing repo |
| `NO_CONTRACT_REPO` | Org exists but only frontend/SDK/docs detected — manual review recommended |
| `ORG_404` | Declared org returns 404 (deleted, renamed) |

### Stage 4 — render (`scripts/04_render_report.py`)

Builds a markdown report of all three buckets, sorted by TVL.

### Bonus — on-chain inspection (`scripts/protocol_balances.py`)

Mirrors the structure of a DefiLlama adapter. For each vault in the protocol config, calls `totalSupply()` on the share token and `balanceOf()` on the debt token directly via `eth_call`, then multiplies by the live price from DefiLlama's coins API.

The bundled example (Altitude.Fi) reproduces DefiLlama's own TVL number to within a fraction of a percent. To add a new protocol:

1. Find the adapter in `https://github.com/DefiLlama/DefiLlama-Adapters/tree/main/projects/<slug>/`
2. Copy the vault address list into the `PROTOCOLS` dict in `scripts/protocol_balances.py`
3. Run `python3 scripts/protocol_balances.py --protocol <slug>`

---

## Caveats — read before relying on the output

- **"Verified" ≠ "fully open-sourced contracts."** It means the org has a public repo whose name or primary language strongly suggests contracts. The repo could still be incomplete, out of date, or unrelated to the deployed bytecode.
- **Language detection is GitHub's auto-guess.** A monorepo where contracts are a small subfolder under a TypeScript app may be misclassified.
- **Verifying that on-chain bytecode matches a repo is a separate step.** Use Etherscan's "verified source" or a Forge build-and-compare for any protocol you plan to fork or integrate with.
- **DefiLlama's `github` field can be wrong.** It's user/team-submitted. Some orgs are deleted, renamed, or never existed — those land in `ORG_404`.

---

## Cron job — automate the refresh

You have three options.

### Option A — GitHub Actions (recommended; no machine to keep running)

A workflow is included at `.github/workflows/refresh.yml`. It runs daily at 03:30 UTC, regenerates the report, and commits it back to the repo. No setup beyond pushing the repo:

```bash
git push origin main
# then in GitHub: Actions tab → enable workflows
```

To run it manually with custom TVL bounds: **Actions → Daily refresh → Run workflow**.

The workflow uses the built-in `secrets.GITHUB_TOKEN` for both the GitHub API rate limit and to push the committed report back. No personal token needed.

### Option B — local cron (macOS/Linux)

Edit your crontab:

```bash
crontab -e
```

Add a line like:

```cron
30 3 * * * cd /absolute/path/to/defillama-protocol-scanner && /usr/bin/env bash scripts/run_pipeline.sh >> /tmp/scanner.log 2>&1
```

If you use `gh` for auth, the script will pick up `gh auth token` automatically. Otherwise hardcode it:

```cron
30 3 * * * cd /path && GH_TOKEN=ghp_xxx bash scripts/run_pipeline.sh >> /tmp/scanner.log 2>&1
```

> macOS note: cron needs Full Disk Access on modern macOS — System Settings → Privacy & Security → Full Disk Access → add `/usr/sbin/cron`. For an interactive scheduler that doesn't need this, see Option C.

### Option C — macOS launchd

Create `~/Library/LaunchAgents/com.user.defillama-scanner.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>          <string>com.user.defillama-scanner</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>-lc</string>
    <string>cd /absolute/path/to/defillama-protocol-scanner && bash scripts/run_pipeline.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>3</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>/tmp/scanner.log</string>
  <key>StandardErrorPath</key><string>/tmp/scanner.err</string>
</dict>
</plist>
```

Load it:

```bash
launchctl load ~/Library/LaunchAgents/com.user.defillama-scanner.plist
```

---

## Repo layout

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── .github/workflows/refresh.yml      # daily GitHub Actions refresh
├── scripts/
│   ├── 01_fetch_protocols.py          # GET /protocols
│   ├── 02_filter_tvl_band.py          # TVL band + has-github filter
│   ├── 03_verify_github.py            # parallel GH API repo classification
│   ├── 04_render_report.py            # write markdown report
│   ├── protocol_balances.py           # on-chain TVL composition for one protocol
│   └── run_pipeline.sh                # 1→2→3→4 end-to-end
├── data/                              # raw + filtered + verified JSON (gitignored)
└── reports/                           # dated markdown reports
```

---

## License

MIT.
