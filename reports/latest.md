# Verified Open-Source DeFi Protocols

**Snapshot:** 2026-11-17
**Sources:** `https://api.llama.fi/protocols` + GitHub REST API `/users/{org}/repos`

## Verdict Summary

- **VERIFIED** — org has at least one contract-bearing repo: **141**
- **NO_CONTRACT_REPO** — org exists but only frontend/SDK/docs detected: **55**
- **ORG_404** — declared github org returns 404: **2**

## Classification heuristic

A repo is flagged as a contract repo if any of:
- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}
- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)
- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract
- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`

**Caveats:** GitHub's auto-detected primary language only; multi-language monorepos may be misclassified. Forks & archived repos are skipped. Manual spot-check is still recommended before forking or integrating with a protocol.

---

## VERIFIED — 141 protocols

| # | Protocol | TVL | Category | Chains | GitHub | Contract Repo(s) |
|---|---|---|---|---|---|---|
| 1 | **Harmonix Finance** | $4.98M | Yield | Hyperliquid L1, Arbitrum, Ethereum +1 | [harmonixfi](https://github.com/harmonixfi) | [core-smart-contract](https://github.com/harmonixfi/core-smart-contract) `TypeScript` ★0 |
| 2 | **Superfluid** | $4.93M | Payments | Base, Polygon, Optimism +7 | [superfluid-finance](https://github.com/superfluid-finance) | [averagex-contracts-cloned](https://github.com/superfluid-finance/averagex-contracts-cloned) `Solidity` ★7<br>[torex-basic-liquidity-mover](https://github.com/superfluid-finance/torex-basic-liquidity-mover) `Solidity` ★3 |
| 3 | **ICHI** | $4.82M | Liquidity Manager | Hedera, Base, Ethereum +24 | [ichifarm](https://github.com/ichifarm) | [ichi-farming](https://github.com/ichifarm/ichi-farming) `Solidity` ★7<br>[ichi-governance](https://github.com/ichifarm/ichi-governance) `Solidity` ★4<br>[ichi](https://github.com/ichifarm/ichi) `Solidity` ★3 +1 more |
| 4 | **Quarry** | $4.53M | Yield | Solana | [QuarryProtocol](https://github.com/QuarryProtocol) | [carrara](https://github.com/QuarryProtocol/carrara) `Move` ★3 |
| 5 | **Stakingverse** | $4.48M | Liquid Staking | Ethereum, LUKSO | [Stakingverse](https://github.com/Stakingverse) | [pool-contracts](https://github.com/Stakingverse/pool-contracts) `Solidity` ★2 |
| 6 | **Tinyman** | $4.32M | Dexs | Algorand | [tinymanorg](https://github.com/tinymanorg) | [tinyman-amm-contracts-v2](https://github.com/tinymanorg/tinyman-amm-contracts-v2) `Python` ★25<br>[tinyman-periphery-contracts-v2](https://github.com/tinymanorg/tinyman-periphery-contracts-v2) `Python` ★1<br>[tinyman-order-protocol](https://github.com/tinymanorg/tinyman-order-protocol) `Python` ★2 +1 more |
| 7 | **Pickle** | $4.24M | Yield Aggregator | Ethereum, Polygon, Optimism +9 | [pickle-finance](https://github.com/pickle-finance) | [protocol](https://github.com/pickle-finance/protocol) `Solidity` ★127<br>[contracts](https://github.com/pickle-finance/contracts) `` ★153<br>[saviour-scripts](https://github.com/pickle-finance/saviour-scripts) `Solidity` ★7 +2 more |
| 8 | **Easedefi.org** | $4.22M | Insurance | Ethereum | [EaseDeFi](https://github.com/EaseDeFi) | [arNFT](https://github.com/EaseDeFi/arNFT) `Solidity` ★7<br>[arNXMV2](https://github.com/EaseDeFi/arNXMV2) `Solidity` ★0<br>[arShield](https://github.com/EaseDeFi/arShield) `Solidity` ★0 +2 more |
| 9 | **Hakka Finance** | $3.96M | Derivatives | Ethereum, Binance | [hakkafinance](https://github.com/hakkafinance) | [hakka](https://github.com/hakkafinance/hakka) `Solidity` ★2<br>[blackholeswap](https://github.com/hakkafinance/blackholeswap) `Solidity` ★11<br>[BugBounty](https://github.com/hakkafinance/BugBounty) `Solidity` ★1 |
| 10 | **CLever** | $3.87M | Yield | Ethereum | [AladdinDAO](https://github.com/AladdinDAO) | [aladdin-v3-contracts](https://github.com/AladdinDAO/aladdin-v3-contracts) `TypeScript` ★61<br>[aladdin-v2-contracts](https://github.com/AladdinDAO/aladdin-v2-contracts) `Solidity` ★4<br>[fx-protocol-contracts](https://github.com/AladdinDAO/fx-protocol-contracts) `Solidity` ★18 +2 more |
| 11 | **Neverland** | $3.74M | Lending | Monad | [Neverland-Money](https://github.com/Neverland-Money) | [neverland-tokenomics](https://github.com/Neverland-Money/neverland-tokenomics) `Solidity` ★0<br>[neverland-wrapped-tokens](https://github.com/Neverland-Money/neverland-wrapped-tokens) `Solidity` ★1 |
| 12 | **Troves** | $3.72M | Yield | Starknet | [trovesfi](https://github.com/trovesfi) | [ekubo-cl-vaults](https://github.com/trovesfi/ekubo-cl-vaults) `Cairo` ★0<br>[vesu-strategies](https://github.com/trovesfi/vesu-strategies) `Cairo` ★0 |
| 13 | **AlphaX** | $3.59M | Derivatives | Binance, Ethereum, Arbitrum +1 | [AlphaX-Protocol](https://github.com/AlphaX-Protocol) | [AlphaX-Protocol-Contract-Tron](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract-Tron) `JavaScript` ★1<br>[AlphaX-Protocol-Contract](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract) `JavaScript` ★0 |
| 14 | **Stafi** | $3.41M | Liquid Staking | Ethereum, Solana, Binance +2 | [stafiprotocol](https://github.com/stafiprotocol) | [svm-staking-contracts](https://github.com/stafiprotocol/svm-staking-contracts) `Rust` ★1<br>[neutron-lsd-contracts](https://github.com/stafiprotocol/neutron-lsd-contracts) `Rust` ★0<br>[svm-lsd-contracts](https://github.com/stafiprotocol/svm-lsd-contracts) `Rust` ★0 +2 more |
| 15 | **Stride** | $3.31M | Liquid Staking | Osmosis, Berachain, Stride +14 | [Stride-Labs](https://github.com/Stride-Labs) | [hub-evm-fees](https://github.com/Stride-Labs/hub-evm-fees) `Solidity` ★0<br>[st-scaling-factor](https://github.com/Stride-Labs/st-scaling-factor) `Rust` ★0<br>[ica-oracle](https://github.com/Stride-Labs/ica-oracle) `Rust` ★0 |
| 16 | **xExchange** | $3.27M | Dexs | Elrond | [multiversx](https://github.com/multiversx) | [mx-chain-core-go](https://github.com/multiversx/mx-chain-core-go) `Go` ★11<br>[mx-contracts-rs](https://github.com/multiversx/mx-contracts-rs) `Rust` ★12<br>[mx-sdk-js-core](https://github.com/multiversx/mx-sdk-js-core) `TypeScript` ★73 |
| 17 | **Bunny** | $3.21M | Yield | Binance, Polygon | [PancakeBunny-finance](https://github.com/PancakeBunny-finance) | [qubit-finance](https://github.com/PancakeBunny-finance/qubit-finance) `Solidity` ★31<br>[Bunny](https://github.com/PancakeBunny-finance/Bunny) `Solidity` ★176<br>[PolygonBUNNY](https://github.com/PancakeBunny-finance/PolygonBUNNY) `Solidity` ★4 +1 more |
| 18 | **Hop Protocol** | $3.06M | Cross Chain Bridge | Ethereum, Optimism, Arbitrum +4 | [hop-protocol](https://github.com/hop-protocol) | [contracts](https://github.com/hop-protocol/contracts) `TypeScript` ★232<br>[messenger](https://github.com/hop-protocol/messenger) `Solidity` ★1<br>[rails](https://github.com/hop-protocol/rails) `Solidity` ★1 +1 more |
| 19 | **Reflect Tranches** | $3.00M | Yield | Solana | [palindrome-eng](https://github.com/palindrome-eng) | [contract-interfaces](https://github.com/palindrome-eng/contract-interfaces) `` ★0 |
| 20 | **OroSwap** | $2.71M | Dexs | ZIGChain | [oroswap](https://github.com/oroswap) | [oroswap-core](https://github.com/oroswap/oroswap-core) `Rust` ★0<br>[oro-evm](https://github.com/oroswap/oro-evm) `Solidity` ★0 |
| 21 | **Umia** | $2.52M | Launchpad | Base | [umiafinance](https://github.com/umiafinance) | [attestor-core](https://github.com/umiafinance/attestor-core) `TypeScript` ★1<br>[protocol](https://github.com/umiafinance/protocol) `Solidity` ★7 |
| 22 | **Bitflow** | $2.44M | Dexs | Stacks | [BitflowFinance](https://github.com/BitflowFinance) | [bitflow-dlmm](https://github.com/BitflowFinance/bitflow-dlmm) `Clarity` ★0<br>[bitflow](https://github.com/BitflowFinance/bitflow) `Clarity` ★4 |
| 23 | **Gamma** | $2.43M | Liquidity Manager | Ethereum, Binance, Polygon +33 | [GammaStrategies](https://github.com/GammaStrategies) | [gamma-univ4-limit-order-hook](https://github.com/GammaStrategies/gamma-univ4-limit-order-hook) `Solidity` ★5<br>[GammaV2](https://github.com/GammaStrategies/GammaV2) `Solidity` ★0<br>[eulerswap-delta-neutral-strategy](https://github.com/GammaStrategies/eulerswap-delta-neutral-strategy) `Solidity` ★3 +1 more |
| 24 | **Astroport** | $2.37M | Dexs | Terra2, Injective, Osmosis +2 | [astroport-fi](https://github.com/astroport-fi) | [astroport-core](https://github.com/astroport-fi/astroport-core) `Rust` ★168<br>[astro-generator-proxy-contracts](https://github.com/astroport-fi/astro-generator-proxy-contracts) `Rust` ★4<br>[astroport-on-osmosis](https://github.com/astroport-fi/astroport-on-osmosis) `Rust` ★0 |
| 25 | **Bio Protocol** | $2.28M | Launchpad | Ethereum, Base | [bio-xyz](https://github.com/bio-xyz) | [vesting-contracts](https://github.com/bio-xyz/vesting-contracts) `Solidity` ★2<br>[token-contracts](https://github.com/bio-xyz/token-contracts) `Solidity` ★1<br>[cerebrumdao-token](https://github.com/bio-xyz/cerebrumdao-token) `Solidity` ★0 +2 more |
| 26 | **LlamaPay** | $2.20M | Payments | Binance, Arbitrum, Ethereum +19 | [LlamaPay](https://github.com/LlamaPay) | [llamapay-v2](https://github.com/LlamaPay/llamapay-v2) `Solidity` ★40<br>[llamapay](https://github.com/LlamaPay/llamapay) `Solidity` ★188<br>[subscription-contracts](https://github.com/LlamaPay/subscription-contracts) `TypeScript` ★4 +2 more |
| 27 | **iAero Protocol** | $2.16M | Liquid Staking | Base | [iaeroProtocol](https://github.com/iaeroProtocol) | [ContractEventsBots](https://github.com/iaeroProtocol/ContractEventsBots) `JavaScript` ★0<br>[PerpBond](https://github.com/iaeroProtocol/PerpBond) `Solidity` ★0 |
| 28 | **Ostium** | $2.09M | Derivatives | Arbitrum | [0xOstium](https://github.com/0xOstium) | [smart-contracts-public](https://github.com/0xOstium/smart-contracts-public) `Solidity` ★14 |
| 29 | **Ledgity Yield** | $2.09M | Yield | Base, Linea, Arbitrum +2 | [LedgityLabs](https://github.com/LedgityLabs) | [ledgity-v2-contracts](https://github.com/LedgityLabs/ledgity-v2-contracts) `Solidity` ★2<br>[LDY-token](https://github.com/LedgityLabs/LDY-token) `Solidity` ★3 |
| 30 | **Kinza Finance** | $2.05M | Lending | Binance, Op_Bnb, Ethereum +1 | [Kinza-Finance](https://github.com/Kinza-Finance) | [omnichain-kBTC](https://github.com/Kinza-Finance/omnichain-kBTC) `Solidity` ★2<br>[KZA-1.0](https://github.com/Kinza-Finance/KZA-1.0) `Solidity` ★4<br>[kbBTC](https://github.com/Kinza-Finance/kbBTC) `Solidity` ★0 |
| 31 | **Goldfinch** | $2.03M | Uncollateralized Lending | Ethereum | [goldfinch-eng](https://github.com/goldfinch-eng) | [mono](https://github.com/goldfinch-eng/mono) `Solidity` ★65<br>[goldfinch-contracts](https://github.com/goldfinch-eng/goldfinch-contracts) `Solidity` ★58 |
| 32 | **Reflexer** | $1.89M | CDP | Ethereum | [reflexer-labs](https://github.com/reflexer-labs) | [geb-keeper-flash-proxy](https://github.com/reflexer-labs/geb-keeper-flash-proxy) `Solidity` ★4<br>[geb-darkfix](https://github.com/reflexer-labs/geb-darkfix) `Solidity` ★1<br>[merkle-distributor](https://github.com/reflexer-labs/merkle-distributor) `Solidity` ★7 +2 more |
| 33 | **QiDao** | $1.87M | CDP | Polygon, Base, Ethereum +11 | [0xlaozi](https://github.com/0xlaozi) | [qidao](https://github.com/0xlaozi/qidao) `Solidity` ★73 |
| 34 | **Yala** | $1.86M | CDP | Bitcoin, Ethereum | [yalaorg](https://github.com/yalaorg) | [yala-protocol-contracts](https://github.com/yalaorg/yala-protocol-contracts) `Solidity` ★13 |
| 35 | **DaVinciGraph** | $1.85M | Token Locker | Hedera | [DaVinciGraph](https://github.com/DaVinciGraph) | [DaVinciGraph-Token-Vesting-V2](https://github.com/DaVinciGraph/DaVinciGraph-Token-Vesting-V2) `Solidity` ★0<br>[DaVinciGraph-NFT-Locker-V2](https://github.com/DaVinciGraph/DaVinciGraph-NFT-Locker-V2) `Solidity` ★0<br>[DaVinciGraph-Black-Hole-V2](https://github.com/DaVinciGraph/DaVinciGraph-Black-Hole-V2) `Solidity` ★0 +2 more |
| 36 | **Trueo** | $1.85M | Prediction Market | Base | [trueo-protocol](https://github.com/trueo-protocol) | [trueo-contracts](https://github.com/trueo-protocol/trueo-contracts) `Solidity` ★17 |
| 37 | **OmniBTC** | $1.74M | Lending | Sui, Base, Arbitrum +5 | [OmniBTC](https://github.com/OmniBTC) | [OmniBridge](https://github.com/OmniBTC/OmniBridge) `Move` ★35<br>[Sui-AMM-swap](https://github.com/OmniBTC/Sui-AMM-swap) `Move` ★88<br>[Aptos-AMM-swap](https://github.com/OmniBTC/Aptos-AMM-swap) `Move` ★30 +2 more |
| 38 | **Flex** | $1.73M | Lending | Ethereum | [flexmeow](https://github.com/flexmeow) | [flex-allocator](https://github.com/flexmeow/flex-allocator) `Solidity` ★0<br>[flex-contracts](https://github.com/flexmeow/flex-contracts) `Solidity` ★5<br>[dutch-taker-contracts](https://github.com/flexmeow/dutch-taker-contracts) `Vyper` ★0 |
| 39 | **Magma** | $1.73M | Dexs | Sui | [MagmaFinanceIO](https://github.com/MagmaFinanceIO) | [magma_core_caps_interface](https://github.com/MagmaFinanceIO/magma_core_caps_interface) `Move` ★0<br>[magma_core_clmm_interface](https://github.com/MagmaFinanceIO/magma_core_clmm_interface) `Move` ★0<br>[magma-core-public](https://github.com/MagmaFinanceIO/magma-core-public) `Move` ★0 +2 more |
| 40 | **HiYield** | $1.73M | RWA | Avalanche, Canto | [lydialabs](https://github.com/lydialabs) | [waifu-token-hackathon](https://github.com/lydialabs/waifu-token-hackathon) `Solidity` ★0 |
| 41 | **Trisolaris** | $1.62M | Dexs | Aurora | [trisolaris-labs](https://github.com/trisolaris-labs) | [trisolaris_core](https://github.com/trisolaris-labs/trisolaris_core) `TypeScript` ★20 |
| 42 | **INIT Capital** | $1.59M | Lending | Mantle, Blast | [init-capital](https://github.com/init-capital) | [init-capital-contracts](https://github.com/init-capital/init-capital-contracts) `Solidity` ★0<br>[init-core-public](https://github.com/init-capital/init-core-public) `` ★0 |
| 43 | **LandX Finance** | $1.57M | RWA | Ethereum | [LandXit](https://github.com/LandXit) | [land-x-smart-contracts](https://github.com/LandXit/land-x-smart-contracts) `JavaScript` ★8 |
| 44 | **Angle** | $1.55M | CDP | Ethereum, Arbitrum, Polygon +5 | [AngleProtocol](https://github.com/AngleProtocol) | [merkl-contracts](https://github.com/AngleProtocol/merkl-contracts) `Solidity` ★89<br>[angle-multisig](https://github.com/AngleProtocol/angle-multisig) `Solidity` ★2<br>[borrow-contracts](https://github.com/AngleProtocol/borrow-contracts) `TypeScript` ★39 +2 more |
| 45 | **Ambient** | $1.52M | Dexs | Scroll, Ethereum, Plume Mainnet +4 | [CrocSwap](https://github.com/CrocSwap) | [CrocSwap-protocol](https://github.com/CrocSwap/CrocSwap-protocol) `TypeScript` ★79<br>[crocswap-router-compat](https://github.com/CrocSwap/crocswap-router-compat) `Solidity` ★0 |
| 46 | **NFTX** | $1.50M | NFT Marketplace | Ethereum, Arbitrum | [NFTX-project](https://github.com/NFTX-project) | [nftx-protocol-v3](https://github.com/NFTX-project/nftx-protocol-v3) `Solidity` ★21<br>[nftx-protocol-v2.1](https://github.com/NFTX-project/nftx-protocol-v2.1) `Solidity` ★1<br>[x-contracts](https://github.com/NFTX-project/x-contracts) `Solidity` ★32 +2 more |
| 47 | **Travessia Credit** | $1.43M | RWA | Ethereum, Avalanche, Polygon +2 | [RedVeil](https://github.com/RedVeil) | [Travessia-Commodity-Tracking](https://github.com/RedVeil/Travessia-Commodity-Tracking) `Solidity` ★0<br>[FixedForexUSDC](https://github.com/RedVeil/FixedForexUSDC) `Solidity` ★0<br>[YieldForge](https://github.com/RedVeil/YieldForge) `Solidity` ★0 +2 more |
| 48 | **Privacy Boost** | $1.43M | Privacy | Base, Optimism, Soneium | [sunnyside-io](https://github.com/sunnyside-io) | [privacy-boost-protocol](https://github.com/sunnyside-io/privacy-boost-protocol) `Solidity` ★15 |
| 49 | **deBridge** | $1.42M | Bridge | Ethereum, Binance, Arbitrum +3 | [debridge-finance](https://github.com/debridge-finance) | [debridge-contracts-v1](https://github.com/debridge-finance/debridge-contracts-v1) `JavaScript` ★59<br>[hardhat-debridge](https://github.com/debridge-finance/hardhat-debridge) `TypeScript` ★23<br>[denft](https://github.com/debridge-finance/denft) `Solidity` ★19 +2 more |
| 50 | **Hubble** | $1.37M | CDP | Solana | [hubbleprotocol](https://github.com/hubbleprotocol) | [solana-setup-action](https://github.com/hubbleprotocol/solana-setup-action) `Rust` ★1<br>[anchor-bpf-template](https://github.com/hubbleprotocol/anchor-bpf-template) `Rust` ★1 |
| 51 | **Swappi** | $1.37M | Dexs | Conflux | [swappidex](https://github.com/swappidex) | [swappi-periphery](https://github.com/swappidex/swappi-periphery) `Solidity` ★7<br>[swappi-farm](https://github.com/swappidex/swappi-farm) `Solidity` ★3<br>[swappi-core](https://github.com/swappidex/swappi-core) `TypeScript` ★5 |
| 52 | **Nami** | $1.35M | Dexs | Base, Robinhood Chain, Ethereum | [namifi](https://github.com/namifi) | [Nami-Protocol](https://github.com/namifi/Nami-Protocol) `Solidity` ★0 |
| 53 | **KaoyaSwap** | $1.32M | Dexs | Binance | [kaoya1125](https://github.com/kaoya1125) | [contracts](https://github.com/kaoya1125/contracts) `Solidity` ★0 |
| 54 | **MDEX** | $1.26M | Dexs | Binance, Bittorrent, Heco | [mdexSwap](https://github.com/mdexSwap) | [contracts](https://github.com/mdexSwap/contracts) `Solidity` ★135 |
| 55 | **SOFA.org** | $1.24M | Options | Ethereum, Arbitrum, Binance +1 | [sofa-org](https://github.com/sofa-org) | [sofa-protocol](https://github.com/sofa-org/sofa-protocol) `TypeScript` ★10 |
| 56 | **Yamato Protocol** | $1.21M | CDP | Ethereum | [DeFiGeek-Community](https://github.com/DeFiGeek-Community) | [yamato](https://github.com/DeFiGeek-Community/yamato) `Solidity` ★4<br>[yamato-commodities](https://github.com/DeFiGeek-Community/yamato-commodities) `Solidity` ★0<br>[ve-factory](https://github.com/DeFiGeek-Community/ve-factory) `Solidity` ★1 |
| 57 | **Lisk Bridge** | $1.13M | Canonical Bridge | Ethereum | [LiskHQ](https://github.com/LiskHQ) | [lisk-contracts](https://github.com/LiskHQ/lisk-contracts) `Solidity` ★17 |
| 58 | **Mitosis** | $1.13M | Onchain Capital Allocator | Binance, Linea, Arbitrum +9 | [mitosis-org](https://github.com/mitosis-org) | [protocol](https://github.com/mitosis-org/protocol) `Solidity` ★17<br>[dn404x](https://github.com/mitosis-org/dn404x) `Solidity` ★3<br>[protocol-dapp-template](https://github.com/mitosis-org/protocol-dapp-template) `Solidity` ★1 +1 more |
| 59 | **Angstrom** | $1.10M | Dexs | Ethereum | [SorellaLabs](https://github.com/SorellaLabs) | [l2-angstrom](https://github.com/SorellaLabs/l2-angstrom) `Solidity` ★4<br>[super-sol](https://github.com/SorellaLabs/super-sol) `Solidity` ★11 |
| 60 | **Augur** | $1.10M | Prediction Market | Ethereum | [AugurProject](https://github.com/AugurProject) | [augur-core](https://github.com/AugurProject/augur-core) `TypeScript` ★587<br>[Lituus-CS](https://github.com/AugurProject/Lituus-CS) `Solidity` ★0<br>[oracle-research](https://github.com/AugurProject/oracle-research) `Solidity` ★6 |
| 61 | **OpenBook** | $1.09M | Dexs | Solana | [openbook-dex](https://github.com/openbook-dex) | [openbook-v2](https://github.com/openbook-dex/openbook-v2) `Rust` ★262<br>[program](https://github.com/openbook-dex/program) `Rust` ★211 |
| 62 | **CityCoins** | $1.07M | Yield | Stacks | [citycoins](https://github.com/citycoins) | [protocol](https://github.com/citycoins/protocol) `Clarity` ★7<br>[protocol-api](https://github.com/citycoins/protocol-api) `TypeScript` ★1 |
| 63 | **CHATEAU** | $1.02M | RWA | Plasma | [chateau-capital](https://github.com/chateau-capital) | [ca](https://github.com/chateau-capital/ca) `Solidity` ★1 |
| 64 | **RealtyX** | $1.02M | RWA | Base, Plume Mainnet | [HomuraAcc](https://github.com/HomuraAcc) | [The-Realtyx-Smart-Contracts](https://github.com/HomuraAcc/The-Realtyx-Smart-Contracts) `Solidity` ★3 |
| 65 | **Kromatika** | $1.01M | Dexs | Optimism, Ethereum, Arbitrum +1 | [Kromatika-Finance](https://github.com/Kromatika-Finance) | [MetaSwap](https://github.com/Kromatika-Finance/MetaSwap) `Solidity` ★0 |
| 66 | **Wombat Exchange** | $992k | Dexs | Binance, Arbitrum, Avalanche +7 | [wombat-exchange](https://github.com/wombat-exchange) | [v1-core](https://github.com/wombat-exchange/v1-core) `Solidity` ★18 |
| 67 | **Isle Finance** | $958k | RWA | Hedera | [isle-labs](https://github.com/isle-labs) | [isle-enterprise-contract](https://github.com/isle-labs/isle-enterprise-contract) `Solidity` ★5 |
| 68 | **Overtime** | $943k | Prediction Market | Arbitrum, Base, Optimism +3 | [thales-markets](https://github.com/thales-markets) | [solana-contracts](https://github.com/thales-markets/solana-contracts) `JavaScript` ★0 |
| 69 | **SHUI** | $935k | Liquid Staking | Conflux | [Shui-LST](https://github.com/Shui-LST) | [shui-lsd-core](https://github.com/Shui-LST/shui-lsd-core) `Solidity` ★1 |
| 70 | **DefiChain DEX** | $931k | Dexs | DefiChain | [DeFiCh](https://github.com/DeFiCh) | [dfi-core](https://github.com/DeFiCh/dfi-core) `` ★0<br>[dfi-erc20](https://github.com/DeFiCh/dfi-erc20) `Solidity` ★0 |
| 71 | **Hyperion** | $892k | Dexs | Aptos | [Hyperionxyz](https://github.com/Hyperionxyz) | [pyth-dep](https://github.com/Hyperionxyz/pyth-dep) `Move` ★0<br>[dex-multiagent-example](https://github.com/Hyperionxyz/dex-multiagent-example) `Move` ★0<br>[hyperion-interface](https://github.com/Hyperionxyz/hyperion-interface) `Move` ★9 |
| 72 | **ForgeYields** | $888k | Onchain Capital Allocator | Starknet, Ethereum | [ForgeYields](https://github.com/ForgeYields) | [starknet_vault_kit](https://github.com/ForgeYields/starknet_vault_kit) `Cairo` ★12 |
| 73 | **Rari Capital** | $855k | Yield Aggregator | Ethereum, Arbitrum | [Rari-Capital](https://github.com/Rari-Capital) | [nova-interfaces](https://github.com/Rari-Capital/nova-interfaces) `Solidity` ★10<br>[nova-invariants](https://github.com/Rari-Capital/nova-invariants) `Solidity` ★6<br>[fuse-v1](https://github.com/Rari-Capital/fuse-v1) `Solidity` ★2 +2 more |
| 74 | **WanSwap Dex** | $850k | Dexs | Wanchain | [wanswap](https://github.com/wanswap) | [wasp-assist](https://github.com/wanswap/wasp-assist) `Solidity` ★1<br>[funny-auction-contracts](https://github.com/wanswap/funny-auction-contracts) `JavaScript` ★1<br>[wanswap-hive-contracts](https://github.com/wanswap/wanswap-hive-contracts) `Solidity` ★1 |
| 75 | **WingRiders** | $846k | Dexs | Cardano | [WingRiders](https://github.com/WingRiders) | [launchpad-contracts](https://github.com/WingRiders/launchpad-contracts) `Haskell` ★0<br>[rapid-dex-contracts](https://github.com/WingRiders/rapid-dex-contracts) `Aiken` ★0<br>[dex-v2-contracts](https://github.com/WingRiders/dex-v2-contracts) `Haskell` ★1 +2 more |
| 76 | **Mendi Finance** | $837k | Lending | Linea | [mendi-finance](https://github.com/mendi-finance) | [lending-protocol](https://github.com/mendi-finance/lending-protocol) `Solidity` ★5<br>[staking-protocol](https://github.com/mendi-finance/staking-protocol) `TypeScript` ★3 |
| 77 | **VETRO** | $824k | CDP | Ethereum | [vetro-protocol](https://github.com/vetro-protocol) | [Safe-guard](https://github.com/vetro-protocol/Safe-guard) `Solidity` ★1<br>[vetro-contracts](https://github.com/vetro-protocol/vetro-contracts) `Solidity` ★1 |
| 78 | **Kai Finance** | $817k | Leveraged Farming | Sui | [kunalabs-io](https://github.com/kunalabs-io) | [sui-smart-contracts](https://github.com/kunalabs-io/sui-smart-contracts) `Move` ★86 |
| 79 | **BlazeSwap** | $812k | Dexs | Flare, Songbird | [blazeswap](https://github.com/blazeswap) | [contracts](https://github.com/blazeswap/contracts) `TypeScript` ★6 |
| 80 | **Ellipsis Finance** | $801k | Dexs | Binance | [ellipsis-finance](https://github.com/ellipsis-finance) | [ellipsis-v2](https://github.com/ellipsis-finance/ellipsis-v2) `Solidity` ★13 |
| 81 | **ALEX** | $800k | Dexs | Stacks | [alexgo-io](https://github.com/alexgo-io) | [alex-v1](https://github.com/alexgo-io/alex-v1) `Clarity` ★41<br>[ord-bitcoincore-rpc](https://github.com/alexgo-io/ord-bitcoincore-rpc) `Rust` ★0<br>[alex-orderbook-public](https://github.com/alexgo-io/alex-orderbook-public) `Clarity` ★0 +2 more |
| 82 | **Twyne** | $792k | Lending | Ethereum | [0xTwyne](https://github.com/0xTwyne) | [twyne-contracts-v1](https://github.com/0xTwyne/twyne-contracts-v1) `Solidity` ★10<br>[aave-v3-aToken-wrapper](https://github.com/0xTwyne/aave-v3-aToken-wrapper) `Solidity` ★0<br>[twyne-shield](https://github.com/0xTwyne/twyne-shield) `Solidity` ★0 +2 more |
| 83 | **Suzaku** | $773k | Restaking | Avalanche | [suzaku-network](https://github.com/suzaku-network) | [suzaku-core](https://github.com/suzaku-network/suzaku-core) `Solidity` ★1<br>[suzaku-contracts-library](https://github.com/suzaku-network/suzaku-contracts-library) `Solidity` ★8<br>[suzaku-deployer](https://github.com/suzaku-network/suzaku-deployer) `Solidity` ★0 |
| 84 | **King Protocol** | $753k | Liquid Restaking | Ethereum | [King-Protocol](https://github.com/King-Protocol) | [king-cross-chain](https://github.com/King-Protocol/king-cross-chain) `Solidity` ★1<br>[king-vaults](https://github.com/King-Protocol/king-vaults) `Solidity` ★0 |
| 85 | **Pondo Protocol** | $738k | Liquid Staking | Aleo | [ProvableHQ](https://github.com/ProvableHQ) | [dynamic-fee-uniswap-hook](https://github.com/ProvableHQ/dynamic-fee-uniswap-hook) `Solidity` ★0 |
| 86 | **Teller** | $715k | Lending | Base, Ethereum, Arbitrum +6 | [teller-protocol](https://github.com/teller-protocol) | [teller-protocol-v2](https://github.com/teller-protocol/teller-protocol-v2) `Rust` ★17<br>[teller-protocol-v1](https://github.com/teller-protocol/teller-protocol-v1) `Solidity` ★106<br>[teller-tx-debug-suite](https://github.com/teller-protocol/teller-tx-debug-suite) `Solidity` ★0 +2 more |
| 87 | **B.Protocol** | $684k | Liquidations | Ethereum, Arbitrum, Polygon +1 | [backstop-protocol](https://github.com/backstop-protocol) | [ERC-7770](https://github.com/backstop-protocol/ERC-7770) `Solidity` ★0<br>[smart-ltv](https://github.com/backstop-protocol/smart-ltv) `Solidity` ★0<br>[B.Protocol-data](https://github.com/backstop-protocol/B.Protocol-data) `TypeScript` ★0 +2 more |
| 88 | **KEEP Network** | $676k | Cross Chain Bridge | Ethereum | [keep-network](https://github.com/keep-network) | [hardhat-helpers](https://github.com/keep-network/hardhat-helpers) `TypeScript` ★3<br>[contracts-migrate-action](https://github.com/keep-network/contracts-migrate-action) `` ★0 |
| 89 | **Lets Get HAI** | $666k | CDP | Optimism | [hai-on-op](https://github.com/hai-on-op) | [core](https://github.com/hai-on-op/core) `Solidity` ★40<br>[altar-of-rai-contracts](https://github.com/hai-on-op/altar-of-rai-contracts) `Solidity` ★0<br>[governance](https://github.com/hai-on-op/governance) `Solidity` ★0 |
| 90 | **ParyonUSD** | $657k | CDP | Bitcoincash | [ParyonUSD](https://github.com/ParyonUSD) | [contracts](https://github.com/ParyonUSD/contracts) `TypeScript` ★12<br>[verify_contract_deployment](https://github.com/ParyonUSD/verify_contract_deployment) `TypeScript` ★0 |
| 91 | **10KSwap** | $646k | Dexs | Starknet | [10k-swap](https://github.com/10k-swap) | [10k_swap-contracts](https://github.com/10k-swap/10k_swap-contracts) `Cairo` ★58 |
| 92 | **Kaskad** | $628k | Lending | Robinhood Chain, Igra | [Kaskad-Lending](https://github.com/Kaskad-Lending) | [kaskad-nuntius-contracts](https://github.com/Kaskad-Lending/kaskad-nuntius-contracts) `Solidity` ★1<br>[kaskad-pontifex](https://github.com/Kaskad-Lending/kaskad-pontifex) `Solidity` ★0<br>[kaskad-contracts](https://github.com/Kaskad-Lending/kaskad-contracts) `Solidity` ★0 |
| 93 | **Dinosaur Eggs** | $613k | Dexs | Binance | [Dinosaur-eggs](https://github.com/Dinosaur-eggs) | [core](https://github.com/Dinosaur-eggs/core) `Solidity` ★24 |
| 94 | **Honeyswap** | $610k | Dexs | xDai, Polygon | [1Hive](https://github.com/1Hive) | [fluid-proposals](https://github.com/1Hive/fluid-proposals) `Solidity` ★0<br>[honeyswap-limit-order-contracts](https://github.com/1Hive/honeyswap-limit-order-contracts) `Solidity` ★3<br>[deployments-aragon-os](https://github.com/1Hive/deployments-aragon-os) `TypeScript` ★0 |
| 95 | **Meson** | $603k | Cross Chain Bridge | Binance, Ethereum, BSquared +41 | [MesonFi](https://github.com/MesonFi) | [merlin-contracts](https://github.com/MesonFi/merlin-contracts) `Solidity` ★0 |
| 96 | **BearnFi** | $593k | Yield | Binance | [bearn-defi](https://github.com/bearn-defi) | [bearn-smartcontracts](https://github.com/bearn-defi/bearn-smartcontracts) `Solidity` ★6<br>[bdex-smartcontracts](https://github.com/bearn-defi/bdex-smartcontracts) `TypeScript` ★0<br>[bvaults-smartcontracts](https://github.com/bearn-defi/bvaults-smartcontracts) `Solidity` ★0 |
| 97 | **TermMax** | $589k | Lending | Ethereum, Berachain, Binance +6 | [term-structure](https://github.com/term-structure) | [termmax-contract-v2](https://github.com/term-structure/termmax-contract-v2) `Solidity` ★9<br>[termmax-contract](https://github.com/term-structure/termmax-contract) `Solidity` ★4<br>[TS-smart-contract](https://github.com/term-structure/TS-smart-contract) `TypeScript` ★2 |
| 98 | **Aurigami** | $565k | Lending | Aurora | [Aurigami-Finance](https://github.com/Aurigami-Finance) | [aurigami-smart-contracts](https://github.com/Aurigami-Finance/aurigami-smart-contracts) `Solidity` ★0 |
| 99 | **DIEM Relay** | $564k | Liquid Staking | Base | [Figu3](https://github.com/Figu3) | [clear-morpho-adapter](https://github.com/Figu3/clear-morpho-adapter) `Solidity` ★0<br>[diem-relay](https://github.com/Figu3/diem-relay) `Solidity` ★0<br>[sonic-earn-recovery-system](https://github.com/Figu3/sonic-earn-recovery-system) `Solidity` ★0 +2 more |
| 100 | **Trevee Earn** | $553k | Yield Aggregator | Sonic, Ethereum, Plasma | [Rings-Protocol](https://github.com/Rings-Protocol) | [rings-contracts](https://github.com/Rings-Protocol/rings-contracts) `Solidity` ★1<br>[rings-wrapper](https://github.com/Rings-Protocol/rings-wrapper) `Solidity` ★0 |
| 101 | **WePiggy** | $549k | Lending | Ethereum, Optimism, Arbitrum +9 | [WePiggy](https://github.com/WePiggy) | [wepiggy-contracts](https://github.com/WePiggy/wepiggy-contracts) `Solidity` ★20<br>[contract_addresses](https://github.com/WePiggy/contract_addresses) `` ★0<br>[wepiggy-contracts-optimism](https://github.com/WePiggy/wepiggy-contracts-optimism) `Solidity` ★0 +1 more |
| 102 | **VaultCraft** | $540k | Yield | Arbitrum, Ethereum, Polygon +4 | [Popcorn-Limited](https://github.com/Popcorn-Limited) | [gauges](https://github.com/Popcorn-Limited/gauges) `Solidity` ★0<br>[audit-04-24](https://github.com/Popcorn-Limited/audit-04-24) `Solidity` ★0<br>[xvcx-bridges](https://github.com/Popcorn-Limited/xvcx-bridges) `Solidity` ★0 +2 more |
| 103 | **Hemi Bridge** | $509k | Canonical Bridge | Ethereum | [hemilabs](https://github.com/hemilabs) | [fpmm](https://github.com/hemilabs/fpmm) `Solidity` ★1<br>[veHEMI](https://github.com/hemilabs/veHEMI) `Solidity` ★0<br>[hemi-token](https://github.com/hemilabs/hemi-token) `Solidity` ★0 +2 more |
| 104 | **Forest Road Vault** | $503k | RWA | Ethereum | [Forest-Road-Company](https://github.com/Forest-Road-Company) | [forest-road-vault](https://github.com/Forest-Road-Company/forest-road-vault) `Solidity` ★6 |
| 105 | **Zunami Protocol** | $496k | Yield Aggregator | Ethereum | [ZunamiProtocol](https://github.com/ZunamiProtocol) | [ZunamiProtocolV2](https://github.com/ZunamiProtocol/ZunamiProtocolV2) `TypeScript` ★1 |
| 106 | **yAxis** | $495k | Yield Aggregator | Ethereum | [yaxis-project](https://github.com/yaxis-project) | [yaxis-audit](https://github.com/yaxis-project/yaxis-audit) `Solidity` ★6<br>[metavault](https://github.com/yaxis-project/metavault) `Solidity` ★32 |
| 107 | **PsyOptions** | $484k | Options | Solana | [mithraiclabs](https://github.com/mithraiclabs) | [psyoracleutils](https://github.com/mithraiclabs/psyoracleutils) `Rust` ★2<br>[pyth-min](https://github.com/mithraiclabs/pyth-min) `Rust` ★0<br>[psy-macros](https://github.com/mithraiclabs/psy-macros) `Rust` ★1 |
| 108 | **Cover Protocol** | $480k | Insurance | Ethereum | [CoverProtocol](https://github.com/CoverProtocol) | [cover-token-mining](https://github.com/CoverProtocol/cover-token-mining) `Solidity` ★8<br>[cover-core-v1](https://github.com/CoverProtocol/cover-core-v1) `Solidity` ★19<br>[cover-rewards](https://github.com/CoverProtocol/cover-rewards) `Solidity` ★1 +1 more |
| 109 | **CANA Holdings California Carbon Credits** | $466k | RWA | Ethereum | [maseer-finance](https://github.com/maseer-finance) | [maseer-one](https://github.com/maseer-finance/maseer-one) `Solidity` ★0<br>[maseer-oracles](https://github.com/maseer-finance/maseer-oracles) `Solidity` ★0<br>[maseer-vest](https://github.com/maseer-finance/maseer-vest) `Solidity` ★0 |
| 110 | **ImmutableX** | $439k | NFT Marketplace | Ethereum | [immutable](https://github.com/immutable) | [imx-migration-contracts](https://github.com/immutable/imx-migration-contracts) `Solidity` ★2<br>[contracts](https://github.com/immutable/contracts) `Solidity` ★46<br>[zkevm-bridge-contracts](https://github.com/immutable/zkevm-bridge-contracts) `Solidity` ★18 +1 more |
| 111 | **MooniSwap** | $436k | Dexs | Ethereum | [1inch](https://github.com/1inch) | [swap-vm](https://github.com/1inch/swap-vm) `Solidity` ★48<br>[limit-order-protocol](https://github.com/1inch/limit-order-protocol) `JavaScript` ★316<br>[aqua](https://github.com/1inch/aqua) `Solidity` ★119 +2 more |
| 112 | **YFII** | $433k | Yield Aggregator | Ethereum | [yfii](https://github.com/yfii) | [yvault](https://github.com/yfii/yvault) `Solidity` ★60<br>[yficontract](https://github.com/yfii/yficontract) `JavaScript` ★16 |
| 113 | **RadioShack** | $427k | Dexs | Binance, Avalanche, Polygon +5 | [radioshackswap](https://github.com/radioshackswap) | [contracts](https://github.com/radioshackswap/contracts) `Solidity` ★2 |
| 114 | **Perpetual Protocol** | $423k | Derivatives | Ethereum, Optimism | [perpetual-protocol](https://github.com/perpetual-protocol) | [lugia-contract](https://github.com/perpetual-protocol/lugia-contract) `Solidity` ★1<br>[perp-curie-contract](https://github.com/perpetual-protocol/perp-curie-contract) `TypeScript` ★87<br>[perpetual-protocol](https://github.com/perpetual-protocol/perpetual-protocol) `TypeScript` ★167 +2 more |
| 115 | **PinkSwap** | $423k | Dexs | Binance | [pinkmoonfinance](https://github.com/pinkmoonfinance) | [pink-antibot-guide](https://github.com/pinkmoonfinance/pink-antibot-guide) `Solidity` ★52<br>[pinksale-contracts](https://github.com/pinkmoonfinance/pinksale-contracts) `Solidity` ★44 |
| 116 | **Nolus Protocol** | $410k | Lending | Solana, Nolus, Neutron +1 | [nolus-protocol](https://github.com/nolus-protocol) | [nolus-core](https://github.com/nolus-protocol/nolus-core) `Go` ★62 |
| 117 | **JPEG'd** | $405k | NFT Lending | Ethereum | [jpegd](https://github.com/jpegd) | [core](https://github.com/jpegd/core) `Solidity` ★12 |
| 118 | **Sherpa** | $401k | Onchain Capital Allocator | Ethereum, Base, Monad | [hedgemonyxyz](https://github.com/hedgemonyxyz) | [sherpa-vault-smartcontracts-v1.0](https://github.com/hedgemonyxyz/sherpa-vault-smartcontracts-v1.0) `Solidity` ★1 |
| 119 | **Tarot** | $389k | Lending | Base, Optimism, Fantom +10 | [tarot-finance](https://github.com/tarot-finance) | [tarot-core](https://github.com/tarot-finance/tarot-core) `JavaScript` ★17<br>[tarot-price-oracle](https://github.com/tarot-finance/tarot-price-oracle) `Solidity` ★8<br>[tarot-periphery](https://github.com/tarot-finance/tarot-periphery) `Solidity` ★9 +2 more |
| 120 | **Cyclone** | $386k | Yield | Binance, Ethereum, IoTeX +1 | [cycloneprotocol](https://github.com/cycloneprotocol) | [cyclone-contracts](https://github.com/cycloneprotocol/cyclone-contracts) `Solidity` ★65 |
| 121 | **Flipcash** | $383k | Launchpad | Solana | [code-payments](https://github.com/code-payments) | [ocp-client-protocol](https://github.com/code-payments/ocp-client-protocol) `Swift` ★0<br>[flipcash2-client-protocol](https://github.com/code-payments/flipcash2-client-protocol) `Swift` ★0<br>[flipcash-shared-core-spm](https://github.com/code-payments/flipcash-shared-core-spm) `Swift` ★0 +1 more |
| 122 | **Ante Finance** | $380k | Insurance | Ethereum, Binance, Avalanche +5 | [antefinance](https://github.com/antefinance) | [ante-v05-core](https://github.com/antefinance/ante-v05-core) `TypeScript` ★6<br>[ante-community-tests](https://github.com/antefinance/ante-community-tests) `Solidity` ★35<br>[ante-v06-core](https://github.com/antefinance/ante-v06-core) `TypeScript` ★1 |
| 123 | **Geode** | $379k | Liquid Staking | Avalanche | [Geodefi](https://github.com/Geodefi) | [Portal-Eth](https://github.com/Geodefi/Portal-Eth) `Solidity` ★3 |
| 124 | **SingularityDAO** | $374k | Yield | Ethereum, Binance | [Singularity-DAO](https://github.com/Singularity-DAO) | [hypercycle-token-contracts](https://github.com/Singularity-DAO/hypercycle-token-contracts) `JavaScript` ★0<br>[migration-contracts](https://github.com/Singularity-DAO/migration-contracts) `TypeScript` ★3<br>[sdao-token-contracts](https://github.com/Singularity-DAO/sdao-token-contracts) `Solidity` ★9 +2 more |
| 125 | **88mph** | $368k | Lending | Ethereum, Fantom, Avalanche +1 | [88mphapp](https://github.com/88mphapp) | [88mph-contracts](https://github.com/88mphapp/88mph-contracts) `Solidity` ★84<br>[88mph-gauge](https://github.com/88mphapp/88mph-gauge) `Vyper` ★0<br>[Phantasm](https://github.com/88mphapp/Phantasm) `Solidity` ★0 +1 more |
| 126 | **Scientix** | $366k | Synthetics | Binance | [ScientixFinance](https://github.com/ScientixFinance) | [scientix-contract](https://github.com/ScientixFinance/scientix-contract) `Solidity` ★3 |
| 127 | **FortiFi** | $365k | Yield Aggregator | Avalanche | [0xFortiFi](https://github.com/0xFortiFi) | [Moat-Contracts](https://github.com/0xFortiFi/Moat-Contracts) `Solidity` ★0<br>[FortiFi-Foundry](https://github.com/0xFortiFi/FortiFi-Foundry) `Solidity` ★0<br>[FortiFi-Vaults](https://github.com/0xFortiFi/FortiFi-Vaults) `Solidity` ★1 |
| 128 | **Swop** | $365k | Dexs | Waves, UNIT0 | [swopfi](https://github.com/swopfi) | [swopfi-smart-contracts](https://github.com/swopfi/swopfi-smart-contracts) `` ★11 |
| 129 | **Siren** | $361k | Options | Ethereum, Polygon, Arbitrum | [sirenmarkets](https://github.com/sirenmarkets) | [core](https://github.com/sirenmarkets/core) `TypeScript` ★41 |
| 130 | **Breadchain** | $360k | CDP | xDai | [BreadchainCoop](https://github.com/BreadchainCoop) | [sigstack-near](https://github.com/BreadchainCoop/sigstack-near) `Rust` ★0<br>[GrowKesennuma](https://github.com/BreadchainCoop/GrowKesennuma) `Solidity` ★0<br>[hats-delegated-security](https://github.com/BreadchainCoop/hats-delegated-security) `Solidity` ★0 +2 more |
| 131 | **Unicly** | $357k | Dexs | Ethereum | [uniclyNFT](https://github.com/uniclyNFT) | [unicly-core](https://github.com/uniclyNFT/unicly-core) `Solidity` ★9 |
| 132 | **Compound Blue** | $353k | Lending | Polygon | [papercliplabs](https://github.com/papercliplabs) | [nouns-town](https://github.com/papercliplabs/nouns-town) `Solidity` ★1 |
| 133 | **AggreLend** | $346k | Yield Aggregator | Solana | [AggreLend](https://github.com/AggreLend) | [kamino-finance-cpi-integration](https://github.com/AggreLend/kamino-finance-cpi-integration) `Rust` ★4<br>[drift-cpi-integration](https://github.com/AggreLend/drift-cpi-integration) `Rust` ★3<br>[marginfi-integration](https://github.com/AggreLend/marginfi-integration) `Rust` ★3 +1 more |
| 134 | **Narwhalswap** | $342k | Dexs | Binance | [narwhalswap](https://github.com/narwhalswap) | [thegrandbanks](https://github.com/narwhalswap/thegrandbanks) `Solidity` ★1<br>[contracts](https://github.com/narwhalswap/contracts) `Solidity` ★0<br>[nar-token](https://github.com/narwhalswap/nar-token) `Solidity` ★0 |
| 135 | **Dfyn Network** | $340k | Dexs | Polygon, Fantom, OKExChain | [dfyn](https://github.com/dfyn) | [dfyn-exchange](https://github.com/dfyn/dfyn-exchange) `Solidity` ★21<br>[dfyn-token](https://github.com/dfyn/dfyn-token) `Solidity` ★7<br>[dual-farm](https://github.com/dfyn/dual-farm) `Solidity` ★1 +2 more |
| 136 | **Ponder Finance** | $310k | Dexs | Bitkub | [ponderfinance](https://github.com/ponderfinance) | [protocol](https://github.com/ponderfinance/protocol) `Solidity` ★1<br>[usdp](https://github.com/ponderfinance/usdp) `Solidity` ★0 |
| 137 | **INFER** | $309k | CDP | Ethereum | [imdusd](https://github.com/imdusd) | [imdusd-peg-hook](https://github.com/imdusd/imdusd-peg-hook) `Solidity` ★0<br>[imdusd-v2-audit](https://github.com/imdusd/imdusd-v2-audit) `Solidity` ★0<br>[oracle-coop](https://github.com/imdusd/oracle-coop) `Solidity` ★0 +2 more |
| 138 | **Sigmausd** | $309k | Algo-Stables | Ergo | [anon-real](https://github.com/anon-real) | [contract-testing](https://github.com/anon-real/contract-testing) `Scala` ★6 |
| 139 | **BOB Fusion** | $307k | Farm | Ethereum | [bob-collective](https://github.com/bob-collective) | [wdk-protocol-swidge-gateway](https://github.com/bob-collective/wdk-protocol-swidge-gateway) `TypeScript` ★0<br>[bitcoin-spv](https://github.com/bob-collective/bitcoin-spv) `Solidity` ★5<br>[unite-defi-hackathon](https://github.com/bob-collective/unite-defi-hackathon) `Solidity` ★0 |
| 140 | **Swerve** | $305k | Dexs | Ethereum | [SwerveFinance](https://github.com/SwerveFinance) | [SwerveContracts](https://github.com/SwerveFinance/SwerveContracts) `` ★39 |
| 141 | **Sprinter** | $303k | Yield | Base | [sprintertech](https://github.com/sprintertech) | [sprinter-stash-contracts](https://github.com/sprintertech/sprinter-stash-contracts) `TypeScript` ★1<br>[deploy-safersafes](https://github.com/sprintertech/deploy-safersafes) `Solidity` ★0 |

---

## NO_CONTRACT_REPO — 55 protocols

These protocols declare a public github org but no contract-bearing repo was detected by the heuristic. Worth manual review before assuming closed-source.

| # | Protocol | TVL | Category | Chains | GitHub |
|---|---|---|---|---|---|
| 1 | LayerBank | $4.48M | Lending | Robinhood Chain, RSK, Linea +14 | [layerbank](https://github.com/layerbank) |
| 2 | Presto | $4.36M | Risk Curators | Ethereum | [prestolabs](https://github.com/prestolabs) |
| 3 | Mole | $4.26M | Yield | Sui, Aptos | [Mole-Fi](https://github.com/Mole-Fi) |
| 4 | Saber | $4.10M | Dexs | Solana | [saberdao](https://github.com/saberdao) |
| 5 | Nawa Protocol | $3.96M | RWA | ZIGChain, Ethereum, CORE | [NawaTeam](https://github.com/NawaTeam) |
| 6 | Bumpin Trade | $3.83M | Derivatives | Solana | [bumpin-exchange](https://github.com/bumpin-exchange) |
| 7 | Blueshift | $3.59M | Dexs | BOB, Kava, Polygon +2 | [blueshift-fi](https://github.com/blueshift-fi) |
| 8 | Arkis | $3.53M | Lending | Ethereum, Hyperliquid L1 | [ArkisXYZ](https://github.com/ArkisXYZ) |
| 9 | Splashing Stake | $3.52M | Liquid Staking | Sei | [SplashingStaking](https://github.com/SplashingStaking) |
| 10 | ICPSwap | $3.12M | Dexs | ICP | [ICPSwap-Labs](https://github.com/ICPSwap-Labs) |
| 11 | Surf Lending | $2.91M | Lending | Cardano | [flow-lending](https://github.com/flow-lending) |
| 12 | International Stable Currency | $2.40M | RWA | Solana | [TheISCTeam](https://github.com/TheISCTeam) |
| 13 | Indigo | $2.28M | CDP | Cardano | [IndigoProtocol](https://github.com/IndigoProtocol) |
| 14 | FluidTokens | $1.97M | Lending | Cardano | [FluidTokens](https://github.com/FluidTokens) |
| 15 | BTCD | $1.94M | Yield | Ethereum, Arbitrum | [BTCDLabs](https://github.com/BTCDLabs) |
| 16 | Permapod | $1.44M | Lending | ZIGChain | [permapod](https://github.com/permapod) |
| 17 | Tradecraft | $1.44M | Dexs | Canton | [tradecraft-fi](https://github.com/tradecraft-fi) |
| 18 | Mountain Protocol | $1.40M | RWA | Ethereum, zkSync Era, Arbitrum +3 | [mountainprotocol](https://github.com/mountainprotocol) |
| 19 | Surge Credit | $1.37M | Lending | Bitcoin, Base | [surgecredit](https://github.com/surgecredit) |
| 20 | PiggyBank | $1.35M | Yield | Solana | [zsociety-io](https://github.com/zsociety-io) |
| 21 | Baseline Protocol | $1.29M | Liquidity Manager | Ethereum, Base, Blast | [0xBaseline](https://github.com/0xBaseline) |
| 22 | Coffer Network | $1.20M | Bridge | Bitcoin | [coffer-network](https://github.com/coffer-network) |
| 23 | Decentralized Euro | $1.11M | CDP | Ethereum | [d-EURO](https://github.com/d-EURO) |
| 24 | Moola Market | $996k | Lending | Celo | [moolamarket](https://github.com/moolamarket) |
| 25 | Flexa | $882k | Payments | Ethereum | [flexahq](https://github.com/flexahq) |
| 26 | Pools Finance | $878k | Dexs | IOTA | [Pools-Finance](https://github.com/Pools-Finance) |
| 27 | Laine SOL | $866k | Liquid Staking | Solana | [laine-sa](https://github.com/laine-sa) |
| 28 | Scopuly | $842k | Dexs | Stellar | [Scopuly](https://github.com/Scopuly) |
| 29 | Reactor DEX | $809k | Dexs | Fuel | [Reactor-Fuel](https://github.com/Reactor-Fuel) |
| 30 | Ashswap | $787k | Dexs | Elrond | [ashswap](https://github.com/ashswap) |
| 31 | Saddle Finance | $784k | Dexs | Ethereum, Arbitrum, Optimism +4 | [saddle-finance](https://github.com/saddle-finance) |
| 32 | Bastion | $781k | Lending | Aurora | [bastionprotocol](https://github.com/bastionprotocol) |
| 33 | Pact | $761k | Dexs | Algorand | [pactfi](https://github.com/pactfi) |
| 34 | Clipper | $693k | Dexs | Ethereum, Base, Optimism +5 | [shipyard-software](https://github.com/shipyard-software) |
| 35 | xToken | $673k | Liquidity Manager | Ethereum, Optimism, Arbitrum +1 | [xtokenmarket](https://github.com/xtokenmarket) |
| 36 | Archer Exchange | $658k | Dexs | Solana | [SquareRoot-Labs](https://github.com/SquareRoot-Labs) |
| 37 | Liquidity House | $650k | Prediction Market | Etherlink | [liquidityhouse](https://github.com/liquidityhouse) |
| 38 | Swaylend | $642k | Lending | Fuel | [swaylend](https://github.com/swaylend) |
| 39 | Landshare | $621k | RWA | Binance | [ls-jordan](https://github.com/ls-jordan) |
| 40 | Kublerx | $616k | Dexs | Bitkub | [kublerxofficial](https://github.com/kublerxofficial) |
| 41 | InkySwap | $606k | Dexs | Ink | [InkySwap](https://github.com/InkySwap) |
| 42 | Rise.rich | $574k | Launchpad | Solana | [riserich](https://github.com/riserich) |
| 43 | tramplin.io | $517k | Staking Pool | Solana | [tramplin-io](https://github.com/tramplin-io) |
| 44 | TRUE DEX | $496k | Derivatives | Solana | [True-AI-Labs](https://github.com/True-AI-Labs) |
| 45 | Turtle Club | $494k | Onchain Capital Allocator | Ethereum, Avalanche, Linea | [Turtle-DAO](https://github.com/Turtle-DAO) |
| 46 | AirPuff | $493k | Leveraged Farming | Ethereum, Arbitrum, Mode +3 | [Airpuff](https://github.com/Airpuff) |
| 47 | Stella | $467k | Leveraged Farming | Arbitrum | [stellaxyz](https://github.com/stellaxyz) |
| 48 | Allstake | $463k | Restaking | Near, Ethereum, Solana | [allstake](https://github.com/allstake) |
| 49 | Ryze Protocol | $443k | Dexs | Base | [ryze-protocol](https://github.com/ryze-protocol) |
| 50 | DefiBox | $418k | Dexs | EOS, Binance, Wax | [DefiboxTeam](https://github.com/DefiboxTeam) |
| 51 | SHPRD | $381k | Indexes | Arbitrum, Ethereum | [stealth-defi](https://github.com/stealth-defi) |
| 52 | GnoSwap | $345k | Dexs | Gno.land | [gnoswap-labs](https://github.com/gnoswap-labs) |
| 53 | Beradrome | $341k | Yield | Berachain | [BeraLabs](https://github.com/BeraLabs) |
| 54 | xSigma | $317k | Dexs | Ethereum | [xSigmaLabs](https://github.com/xSigmaLabs) |
| 55 | Mobius Money | $317k | Dexs | Celo | [mobiusAMM](https://github.com/mobiusAMM) |

---

## ORG_404 — 2 protocols

- Beam Swap ($1.43M) — declared org: `['Merit-Circle']`
- AbstraDEX ($302k) — declared org: `['AbstraDex']`
