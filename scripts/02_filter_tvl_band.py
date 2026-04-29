"""Filter protocols by TVL band and presence of a declared GitHub org.

Usage:
    python3 scripts/02_filter_tvl_band.py --min 300000 --max 5000000

Reads:
    data/protocols.json
Writes:
    data/filtered.json — list of protocols in band with non-empty `github`
"""
import argparse, json, os, sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
IN = os.path.join(ROOT, "data", "protocols.json")
OUT = os.path.join(ROOT, "data", "filtered.json")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=300_000, help="min TVL in USD (default 300_000)")
    ap.add_argument("--max", type=float, default=5_000_000, help="max TVL in USD (default 5_000_000)")
    ap.add_argument("--require-github", action="store_true", default=True,
                    help="require non-empty github field (default True)")
    args = ap.parse_args()

    with open(IN) as f:
        protos = json.load(f)
    band = [p for p in protos
            if p.get("tvl") is not None
            and args.min <= p["tvl"] <= args.max]
    if args.require_github:
        band = [p for p in band if p.get("github")]
    band.sort(key=lambda p: -p["tvl"])

    with open(OUT, "w") as f:
        json.dump(band, f, indent=2)
    print(f"[filter] tvl ${args.min:,.0f}-${args.max:,.0f} | github required: {args.require_github}")
    print(f"[filter] {len(band)} protocols → {OUT}")

if __name__ == "__main__":
    main()
