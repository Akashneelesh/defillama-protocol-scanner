"""Fetch the full DefiLlama protocols list and save to data/protocols.json.

Usage:
    python3 scripts/01_fetch_protocols.py

Writes:
    data/protocols.json   — raw response from https://api.llama.fi/protocols
"""
import json, os, sys, urllib.request, time

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "protocols.json")
URL = "https://api.llama.fi/protocols"

def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    print(f"[fetch] GET {URL}")
    start = time.time()
    req = urllib.request.Request(URL, headers={"User-Agent": "defillama-protocol-scanner/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    with open(OUT, "w") as f:
        json.dump(data, f)
    print(f"[fetch] saved {len(data)} protocols to {OUT} in {time.time()-start:.1f}s")

if __name__ == "__main__":
    main()
