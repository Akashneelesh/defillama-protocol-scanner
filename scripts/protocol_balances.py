"""Generic on-chain balance reader for DefiLlama protocol adapters.

This is a worked example that mirrors the DefiLlama adapter for one specific
protocol (Altitude.Fi) so anyone can fork the script and swap in another
protocol's vault config. The pattern: read totalSupply()/balanceOf() of the
contracts named in the DefiLlama adapter, multiply by the live price.

Usage:
    python3 scripts/protocol_balances.py --protocol altitude-fi
"""
import argparse, json, os, sys, urllib.request

ROOT = os.path.join(os.path.dirname(__file__), "..")

# Default RPC. Override with --rpc or env ETH_RPC.
DEFAULT_RPC = os.environ.get("ETH_RPC", "https://ethereum.publicnode.com")

# Worked example: Altitude.Fi vaults (mirrors DefiLlama adapter
# https://github.com/DefiLlama/DefiLlama-Adapters/blob/main/projects/altitude-fi/addresses.js)
ALTITUDE_VAULTS = [
    {"name": "wstethUsdc v1", "vault": "0x1f7d589e90e4E4FC1B15B3143a5c60F743C759b9",
     "supplyToken": "0x874566FfA8d837934aE85Db2209839F5Fb4E6b1d",
     "underlyingSupply": "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0",
     "underlyingSupplySymbol": "wstETH", "underlyingSupplyDecimals": 18,
     "debtToken": "0xd130a916dDbF1612C2F2FAAb6897210f056Ab29b",
     "underlyingBorrow": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
     "underlyingBorrowSymbol": "USDC", "underlyingBorrowDecimals": 6},
    {"name": "wstethUsdc v2", "vault": "0xaf6062222d00ac63477ad084ebd22a7821e5ee8d",
     "supplyToken": "0x5c58dffc753ba61e07a73a021f70366ab69c1f06",
     "underlyingSupply": "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0",
     "underlyingSupplySymbol": "wstETH", "underlyingSupplyDecimals": 18,
     "debtToken": "0x5717f3f1b566cf2f7113979fcd78d9416f5b0056",
     "underlyingBorrow": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
     "underlyingBorrowSymbol": "USDC", "underlyingBorrowDecimals": 6},
    {"name": "cbbtcUsdc v2", "vault": "0x550F8a1FFC921b9179267F9e7909FC68CE496A6b",
     "supplyToken": "0x2Ddd6d576615E6AFa823adeDDe8DC67198333169",
     "underlyingSupply": "0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf",
     "underlyingSupplySymbol": "cbBTC", "underlyingSupplyDecimals": 8,
     "debtToken": "0xDF612bf20C2A68730cEDC5056a1F1A90c6827e66",
     "underlyingBorrow": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
     "underlyingBorrowSymbol": "USDC", "underlyingBorrowDecimals": 6},
]

PROTOCOLS = {"altitude-fi": ALTITUDE_VAULTS}

UA = {"Content-Type": "application/json", "User-Agent": "defillama-protocol-scanner/1.0"}

def rpc(rpc_url, method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(rpc_url, data=body, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if "error" in d:
        raise RuntimeError(f"RPC error: {d['error']}")
    return d["result"]

def total_supply(rpc_url, token):
    return int(rpc(rpc_url, "eth_call", [{"to": token, "data": "0x18160ddd"}, "latest"]), 16)

def balance_of(rpc_url, token, owner):
    addr = owner.lower().replace("0x", "").rjust(64, "0")
    return int(rpc(rpc_url, "eth_call", [{"to": token, "data": "0x70a08231" + addr}, "latest"]), 16)

def coin_price(coin_id):
    url = f"https://coins.llama.fi/prices/current/{coin_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "defillama-protocol-scanner/1.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        d = json.load(r)
    return d["coins"].get(coin_id, {}).get("price")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--protocol", default="altitude-fi", choices=list(PROTOCOLS),
                    help="protocol slug (currently only altitude-fi is bundled)")
    ap.add_argument("--rpc", default=DEFAULT_RPC, help="Ethereum JSON-RPC URL")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    args = ap.parse_args()

    vaults = PROTOCOLS[args.protocol]
    symbols = sorted({v["underlyingSupplySymbol"] for v in vaults} |
                     {v["underlyingBorrowSymbol"] for v in vaults})
    addr_for_symbol = {}
    for v in vaults:
        addr_for_symbol[v["underlyingSupplySymbol"]] = v["underlyingSupply"]
        addr_for_symbol[v["underlyingBorrowSymbol"]] = v["underlyingBorrow"]
    prices = {s: coin_price(f"ethereum:{addr_for_symbol[s]}") for s in symbols}

    rows = []
    for v in vaults:
        st = total_supply(args.rpc, v["supplyToken"])
        dt = total_supply(args.rpc, v["debtToken"])
        dv = balance_of(args.rpc, v["debtToken"], v["vault"])
        users_borrow = dt - dv
        coll_amt = st / 10 ** v["underlyingSupplyDecimals"]
        borrow_amt = users_borrow / 10 ** v["underlyingBorrowDecimals"]
        rows.append({
            "vault_name": v["name"],
            "vault_address": v["vault"],
            "collateral_amount": coll_amt,
            "collateral_symbol": v["underlyingSupplySymbol"],
            "collateral_usd": coll_amt * prices[v["underlyingSupplySymbol"]],
            "borrow_amount": borrow_amt,
            "borrow_symbol": v["underlyingBorrowSymbol"],
            "borrow_usd": borrow_amt * prices[v["underlyingBorrowSymbol"]],
        })

    total_coll = sum(r["collateral_usd"] for r in rows)
    total_borrow = sum(r["borrow_usd"] for r in rows)
    tvl = total_coll - total_borrow

    if args.json:
        print(json.dumps({"protocol": args.protocol, "prices": prices,
                          "rows": rows, "tvl_usd": tvl,
                          "collateral_usd": total_coll, "borrow_usd": total_borrow}, indent=2))
        return

    print(f"protocol: {args.protocol}")
    print(f"prices: {prices}")
    print()
    print(f"{'Vault':<22} {'Collateral':>22} {'Coll USD':>14} {'Users Borrow':>20} {'Borrow USD':>14}")
    print("-" * 100)
    for r in rows:
        cs = f"{r['collateral_amount']:,.4f} {r['collateral_symbol']}"
        bs = f"{r['borrow_amount']:,.2f} {r['borrow_symbol']}"
        print(f"{r['vault_name']:<22} {cs:>22} {r['collateral_usd']:>14,.0f} {bs:>20} {r['borrow_usd']:>14,.0f}")
    print("-" * 100)
    print(f"{'TOTAL':<22} {'':>22} {total_coll:>14,.0f} {'':>20} {total_borrow:>14,.0f}")
    print()
    print(f"DefiLlama TVL (collateral - users' borrow) = ${tvl:,.0f}")

if __name__ == "__main__":
    main()
