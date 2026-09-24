# Verified Open-Source DeFi Protocols

**Snapshot:** 2026-09-24
**Sources:** `https://api.llama.fi/protocols` + GitHub REST API `/users/{org}/repos`

## Verdict Summary

- **VERIFIED** — org has at least one contract-bearing repo: **161**
- **NO_CONTRACT_REPO** — org exists but only frontend/SDK/docs detected: **68**
- **ORG_404** — declared github org returns 404: **3**

## Classification heuristic

A repo is flagged as a contract repo if any of:
- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}
- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)
- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract
- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`

**Caveats:** GitHub's auto-detected primary language only; multi-language monorepos may be misclassified. Forks & archived repos are skipped. Manual spot-check is still recommended before forking or integrating with a protocol.

---

## VERIFIED — 161 protocols

| # | Protocol | TVL | Category | Chains | GitHub | Contract Repo(s) |
|---|---|---|---|---|---|---|
| 1 | **Stability** | $4.60M | Liquidity Manager | Sonic, Base, Polygon +1 | [stabilitydao](https://github.com/stabilitydao) | [stability-contracts](https://github.com/stabilitydao/stability-contracts) `Solidity` ★32<br>[inception-contracts](https://github.com/stabilitydao/inception-contracts) `Solidity` ★12 |
| 2 | **OroSwap** | $4.47M | Dexs | ZIGChain | [oroswap](https://github.com/oroswap) | [oro-evm](https://github.com/oroswap/oro-evm) `Solidity` ★0<br>[oroswap-core](https://github.com/oroswap/oroswap-core) `Rust` ★0 |
| 3 | **Bunny** | $4.31M | Yield | Binance, Polygon | [PancakeBunny-finance](https://github.com/PancakeBunny-finance) | [Bunny](https://github.com/PancakeBunny-finance/Bunny) `Solidity` ★175<br>[qubit-finance](https://github.com/PancakeBunny-finance/qubit-finance) `Solidity` ★31<br>[PolygonBUNNY](https://github.com/PancakeBunny-finance/PolygonBUNNY) `Solidity` ★4 +1 more |
| 4 | **Mangrove** | $4.28M | Dexs | Blast, Arbitrum | [mangrovedao](https://github.com/mangrovedao) | [vaults-v2-chainlink-adapter](https://github.com/mangrovedao/vaults-v2-chainlink-adapter) `Solidity` ★0<br>[mangrove-strats](https://github.com/mangrovedao/mangrove-strats) `Solidity` ★2<br>[mangrove-core](https://github.com/mangrovedao/mangrove-core) `Solidity` ★49 +2 more |
| 5 | **xExchange** | $4.19M | Dexs | Elrond | [multiversx](https://github.com/multiversx) | [mx-chain-core-go](https://github.com/multiversx/mx-chain-core-go) `Go` ★12<br>[mx-sdk-js-core](https://github.com/multiversx/mx-sdk-js-core) `TypeScript` ★73<br>[mx-contracts-rs](https://github.com/multiversx/mx-contracts-rs) `Rust` ★13 |
| 6 | **Bio Protocol** | $3.94M | Launchpad | Ethereum, Base | [bio-xyz](https://github.com/bio-xyz) | [vesting-contracts](https://github.com/bio-xyz/vesting-contracts) `Solidity` ★2<br>[token-contracts](https://github.com/bio-xyz/token-contracts) `Solidity` ★1<br>[cerebrumdao-token](https://github.com/bio-xyz/cerebrumdao-token) `Solidity` ★0 +2 more |
| 7 | **Hop Protocol** | $3.93M | Cross Chain Bridge | Ethereum, Optimism, Arbitrum +4 | [hop-protocol](https://github.com/hop-protocol) | [contracts](https://github.com/hop-protocol/contracts) `TypeScript` ★232<br>[messenger](https://github.com/hop-protocol/messenger) `Solidity` ★1<br>[rails](https://github.com/hop-protocol/rails) `Solidity` ★1 +1 more |
| 8 | **Astroport** | $3.60M | Dexs | Terra2, Injective, Osmosis +2 | [astroport-fi](https://github.com/astroport-fi) | [astroport-core](https://github.com/astroport-fi/astroport-core) `Rust` ★169<br>[astro-generator-proxy-contracts](https://github.com/astroport-fi/astro-generator-proxy-contracts) `Rust` ★4<br>[astroport-on-osmosis](https://github.com/astroport-fi/astroport-on-osmosis) `Rust` ★0 |
| 9 | **Umia** | $3.45M | Launchpad | Base | [umiafinance](https://github.com/umiafinance) | [protocol](https://github.com/umiafinance/protocol) `Solidity` ★3 |
| 10 | **deBridge** | $3.29M | Bridge | Binance, Ethereum, Arbitrum +3 | [debridge-finance](https://github.com/debridge-finance) | [debridge-contracts-v1](https://github.com/debridge-finance/debridge-contracts-v1) `JavaScript` ★59<br>[hardhat-debridge](https://github.com/debridge-finance/hardhat-debridge) `TypeScript` ★23<br>[denft](https://github.com/debridge-finance/denft) `Solidity` ★19 +2 more |
| 11 | **iAero Protocol** | $3.28M | Liquid Staking | Base | [iaeroProtocol](https://github.com/iaeroProtocol) | [ContractEventsBots](https://github.com/iaeroProtocol/ContractEventsBots) `JavaScript` ★0<br>[PerpBond](https://github.com/iaeroProtocol/PerpBond) `Solidity` ★0 |
| 12 | **Gamma** | $3.23M | Liquidity Manager | Ethereum, Binance, Polygon +33 | [GammaStrategies](https://github.com/GammaStrategies) | [gamma-univ4-limit-order-hook](https://github.com/GammaStrategies/gamma-univ4-limit-order-hook) `Solidity` ★5<br>[GammaV2](https://github.com/GammaStrategies/GammaV2) `Solidity` ★0<br>[eulerswap-delta-neutral-strategy](https://github.com/GammaStrategies/eulerswap-delta-neutral-strategy) `Solidity` ★3 +1 more |
| 13 | **Keep3r Network** | $3.21M | Derivatives | Ethereum | [keep3r-network](https://github.com/keep3r-network) | [StakingRewardsV3](https://github.com/keep3r-network/StakingRewardsV3) `Solidity` ★8<br>[keep3r.network](https://github.com/keep3r-network/keep3r.network) `Solidity` ★369<br>[OptionsLM](https://github.com/keep3r-network/OptionsLM) `Solidity` ★29 |
| 14 | **Kinza Finance** | $3.14M | Lending | Binance, Op_Bnb, Ethereum +1 | [Kinza-Finance](https://github.com/Kinza-Finance) | [omnichain-kBTC](https://github.com/Kinza-Finance/omnichain-kBTC) `Solidity` ★2<br>[KZA-1.0](https://github.com/Kinza-Finance/KZA-1.0) `Solidity` ★4<br>[kbBTC](https://github.com/Kinza-Finance/kbBTC) `Solidity` ★0 |
| 15 | **Bitflow** | $3.11M | Dexs | Stacks | [BitflowFinance](https://github.com/BitflowFinance) | [bitflow-dlmm](https://github.com/BitflowFinance/bitflow-dlmm) `Clarity` ★0<br>[bitflow](https://github.com/BitflowFinance/bitflow) `Clarity` ★4<br>[appleswap](https://github.com/BitflowFinance/appleswap) `Clarity` ★2 |
| 16 | **WingRiders** | $3.06M | Dexs | Cardano | [WingRiders](https://github.com/WingRiders) | [launchpad-contracts](https://github.com/WingRiders/launchpad-contracts) `Haskell` ★0<br>[rapid-dex-contracts](https://github.com/WingRiders/rapid-dex-contracts) `Aiken` ★0<br>[dex-v2-contracts](https://github.com/WingRiders/dex-v2-contracts) `Haskell` ★1 +2 more |
| 17 | **Reflexer** | $2.84M | CDP | Ethereum | [reflexer-labs](https://github.com/reflexer-labs) | [geb-keeper-flash-proxy](https://github.com/reflexer-labs/geb-keeper-flash-proxy) `Solidity` ★3<br>[geb-darkfix](https://github.com/reflexer-labs/geb-darkfix) `Solidity` ★1<br>[merkle-distributor](https://github.com/reflexer-labs/merkle-distributor) `Solidity` ★7 +2 more |
| 18 | **AlphaX** | $2.77M | Derivatives | Binance, Ethereum, Arbitrum +1 | [AlphaX-Protocol](https://github.com/AlphaX-Protocol) | [AlphaX-Protocol-Contract-Tron](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract-Tron) `JavaScript` ★1<br>[AlphaX-Protocol-Contract](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract) `JavaScript` ★0 |
| 19 | **Ledgity Yield** | $2.47M | Yield | Base, Linea, Arbitrum +2 | [LedgityLabs](https://github.com/LedgityLabs) | [ledgity-v2-contracts](https://github.com/LedgityLabs/ledgity-v2-contracts) `Solidity` ★2<br>[LDY-token](https://github.com/LedgityLabs/LDY-token) `Solidity` ★3 |
| 20 | **Hyperion** | $2.46M | Dexs | Aptos | [Hyperionxyz](https://github.com/Hyperionxyz) | [pyth-dep](https://github.com/Hyperionxyz/pyth-dep) `Move` ★0<br>[dex-multiagent-example](https://github.com/Hyperionxyz/dex-multiagent-example) `Move` ★0<br>[hyperion-interface](https://github.com/Hyperionxyz/hyperion-interface) `Move` ★9 |
| 21 | **Yala** | $2.44M | CDP | Bitcoin, Ethereum | [yalaorg](https://github.com/yalaorg) | [yala-protocol-contracts](https://github.com/yalaorg/yala-protocol-contracts) `Solidity` ★13 |
| 22 | **QiDao** | $2.39M | CDP | Polygon, Base, Ethereum +11 | [0xlaozi](https://github.com/0xlaozi) | [qidao](https://github.com/0xlaozi/qidao) `Solidity` ★73 |
| 23 | **Ambient** | $2.36M | Dexs | Scroll, Blast, Ethereum +4 | [CrocSwap](https://github.com/CrocSwap) | [CrocSwap-protocol](https://github.com/CrocSwap/CrocSwap-protocol) `TypeScript` ★79<br>[crocswap-router-compat](https://github.com/CrocSwap/crocswap-router-compat) `Solidity` ★0 |
| 24 | **NFTX** | $2.19M | NFT Marketplace | Ethereum, Arbitrum | [NFTX-project](https://github.com/NFTX-project) | [nftx-protocol-v3](https://github.com/NFTX-project/nftx-protocol-v3) `Solidity` ★21<br>[nftx-protocol-v2.1](https://github.com/NFTX-project/nftx-protocol-v2.1) `Solidity` ★1<br>[x-contracts](https://github.com/NFTX-project/x-contracts) `Solidity` ★32 +2 more |
| 25 | **Goldfinch** | $2.14M | Uncollateralized Lending | Ethereum | [goldfinch-eng](https://github.com/goldfinch-eng) | [mono](https://github.com/goldfinch-eng/mono) `Solidity` ★66<br>[goldfinch-contracts](https://github.com/goldfinch-eng/goldfinch-contracts) `Solidity` ★58 |
| 26 | **Augur** | $2.11M | Prediction Market | Ethereum | [AugurProject](https://github.com/AugurProject) | [augur-core](https://github.com/AugurProject/augur-core) `TypeScript` ★587<br>[Lituus-CS](https://github.com/AugurProject/Lituus-CS) `Solidity` ★0<br>[oracle-research](https://github.com/AugurProject/oracle-research) `Solidity` ★6 |
| 27 | **Trisolaris** | $2.11M | Dexs | Aurora | [trisolaris-labs](https://github.com/trisolaris-labs) | [trisolaris_core](https://github.com/trisolaris-labs/trisolaris_core) `TypeScript` ★20 |
| 28 | **INIT Capital** | $2.10M | Lending | Mantle, Blast | [init-capital](https://github.com/init-capital) | [init-capital-contracts](https://github.com/init-capital/init-capital-contracts) `Solidity` ★0<br>[init-core-public](https://github.com/init-capital/init-core-public) `` ★0 |
| 29 | **LlamaPay** | $2.07M | Payments | Binance, Arbitrum, Ethereum +19 | [LlamaPay](https://github.com/LlamaPay) | [llamapay](https://github.com/LlamaPay/llamapay) `Solidity` ★188<br>[llamapay-v2](https://github.com/LlamaPay/llamapay-v2) `Solidity` ★41<br>[subscription-contracts](https://github.com/LlamaPay/subscription-contracts) `TypeScript` ★4 +2 more |
| 30 | **Ionic Protocol** | $2.04M | Lending | Mode, Base, Lisk +3 | [ionicprotocol](https://github.com/ionicprotocol) | [monorepo](https://github.com/ionicprotocol/monorepo) `Solidity` ★33<br>[debt-token](https://github.com/ionicprotocol/debt-token) `Solidity` ★0<br>[ionic-token](https://github.com/ionicprotocol/ionic-token) `Solidity` ★0 +2 more |
| 31 | **OmniBTC** | $1.98M | Lending | Sui, Arbitrum, Base +5 | [OmniBTC](https://github.com/OmniBTC) | [OmniBridge](https://github.com/OmniBTC/OmniBridge) `Move` ★34<br>[Sui-AMM-swap](https://github.com/OmniBTC/Sui-AMM-swap) `Move` ★88<br>[Aptos-AMM-swap](https://github.com/OmniBTC/Aptos-AMM-swap) `Move` ★30 +2 more |
| 32 | **Swappi** | $1.94M | Dexs | Conflux | [swappidex](https://github.com/swappidex) | [swappi-periphery](https://github.com/swappidex/swappi-periphery) `Solidity` ★7<br>[swappi-farm](https://github.com/swappidex/swappi-farm) `Solidity` ★3<br>[swappi-core](https://github.com/swappidex/swappi-core) `TypeScript` ★5 |
| 33 | **Angle** | $1.86M | CDP | Ethereum, Arbitrum, Polygon +5 | [AngleProtocol](https://github.com/AngleProtocol) | [merkl-contracts](https://github.com/AngleProtocol/merkl-contracts) `Solidity` ★83<br>[angle-multisig](https://github.com/AngleProtocol/angle-multisig) `Solidity` ★1<br>[borrow-contracts](https://github.com/AngleProtocol/borrow-contracts) `TypeScript` ★38 +2 more |
| 34 | **DaVinciGraph** | $1.85M | Token Locker | Hedera | [DaVinciGraph](https://github.com/DaVinciGraph) | [DaVinciGraph-Token-Vesting-V2](https://github.com/DaVinciGraph/DaVinciGraph-Token-Vesting-V2) `Solidity` ★0<br>[DaVinciGraph-NFT-Locker-V2](https://github.com/DaVinciGraph/DaVinciGraph-NFT-Locker-V2) `Solidity` ★0<br>[DaVinciGraph-Black-Hole-V2](https://github.com/DaVinciGraph/DaVinciGraph-Black-Hole-V2) `Solidity` ★0 +2 more |
| 35 | **B.Protocol** | $1.83M | Liquidations | Ethereum, Arbitrum, Polygon +1 | [backstop-protocol](https://github.com/backstop-protocol) | [ERC-7770](https://github.com/backstop-protocol/ERC-7770) `Solidity` ★0<br>[smart-ltv](https://github.com/backstop-protocol/smart-ltv) `Solidity` ★0<br>[B.Protocol-data](https://github.com/backstop-protocol/B.Protocol-data) `TypeScript` ★0 +2 more |
| 36 | **Yamato Protocol** | $1.82M | CDP | Ethereum | [DeFiGeek-Community](https://github.com/DeFiGeek-Community) | [yamato](https://github.com/DeFiGeek-Community/yamato) `Solidity` ★4<br>[yamato-commodities](https://github.com/DeFiGeek-Community/yamato-commodities) `Solidity` ★0<br>[ve-factory](https://github.com/DeFiGeek-Community/ve-factory) `Solidity` ★1 |
| 37 | **HiYield** | $1.72M | RWA | Avalanche, Canto | [lydialabs](https://github.com/lydialabs) | [waifu-token-hackathon](https://github.com/lydialabs/waifu-token-hackathon) `Solidity` ★0 |
| 38 | **KaoyaSwap** | $1.67M | Dexs | Binance | [kaoya1125](https://github.com/kaoya1125) | [contracts](https://github.com/kaoya1125/contracts) `Solidity` ★0 |
| 39 | **FanX Protocol** | $1.66M | Dexs | Chiliz | [FanX-Protocol](https://github.com/FanX-Protocol) | [mixed-quoter](https://github.com/FanX-Protocol/mixed-quoter) `Solidity` ★0<br>[kayen-dex-contract](https://github.com/FanX-Protocol/kayen-dex-contract) `Solidity` ★0<br>[kayen-contracts](https://github.com/FanX-Protocol/kayen-contracts) `Solidity` ★0 |
| 40 | **Magma** | $1.65M | Dexs | Sui | [MagmaFinanceIO](https://github.com/MagmaFinanceIO) | [magma_core_caps_interface](https://github.com/MagmaFinanceIO/magma_core_caps_interface) `Move` ★0<br>[magma_core_clmm_interface](https://github.com/MagmaFinanceIO/magma_core_clmm_interface) `Move` ★0<br>[magma-core-public](https://github.com/MagmaFinanceIO/magma-core-public) `Move` ★0 +2 more |
| 41 | **LandX Finance** | $1.64M | RWA | Ethereum | [LandXit](https://github.com/LandXit) | [land-x-smart-contracts](https://github.com/LandXit/land-x-smart-contracts) `JavaScript` ★8 |
| 42 | **Twyne** | $1.62M | Lending | Ethereum | [0xTwyne](https://github.com/0xTwyne) | [twyne-contracts-v1](https://github.com/0xTwyne/twyne-contracts-v1) `Solidity` ★10<br>[aave-v3-aToken-wrapper](https://github.com/0xTwyne/aave-v3-aToken-wrapper) `Solidity` ★0<br>[twyne-shield](https://github.com/0xTwyne/twyne-shield) `Solidity` ★0 +2 more |
| 43 | **Hubble** | $1.55M | CDP | Solana | [hubbleprotocol](https://github.com/hubbleprotocol) | [solana-setup-action](https://github.com/hubbleprotocol/solana-setup-action) `Rust` ★1<br>[anchor-bpf-template](https://github.com/hubbleprotocol/anchor-bpf-template) `Rust` ★1 |
| 44 | **Privacy Boost** | $1.55M | Privacy | Base, Optimism, Soneium | [sunnyside-io](https://github.com/sunnyside-io) | [privacy-boost-protocol](https://github.com/sunnyside-io/privacy-boost-protocol) `Solidity` ★12 |
| 45 | **Butter Network** | $1.52M | Cross Chain Bridge | Ethereum, Tron, Binance +12 | [butternetwork](https://github.com/butternetwork) | [wdk-protocol-swidge-butter](https://github.com/butternetwork/wdk-protocol-swidge-butter) `TypeScript` ★0<br>[butter-router-contracts](https://github.com/butternetwork/butter-router-contracts) `JavaScript` ★8<br>[butter-core-near](https://github.com/butternetwork/butter-core-near) `Rust` ★1 +2 more |
| 46 | **King Protocol** | $1.51M | Liquid Restaking | Ethereum | [King-Protocol](https://github.com/King-Protocol) | [king-cross-chain](https://github.com/King-Protocol/king-cross-chain) `Solidity` ★1<br>[king-vaults](https://github.com/King-Protocol/king-vaults) `Solidity` ★0 |
| 47 | **MDEX** | $1.47M | Dexs | Binance, Bittorrent, Heco | [mdexSwap](https://github.com/mdexSwap) | [contracts](https://github.com/mdexSwap/contracts) `Solidity` ★135 |
| 48 | **Cyclone** | $1.47M | Yield | Ethereum, Binance, IoTeX +1 | [cycloneprotocol](https://github.com/cycloneprotocol) | [cyclone-contracts](https://github.com/cycloneprotocol/cyclone-contracts) `Solidity` ★63 |
| 49 | **SOFA.org** | $1.47M | Options | Ethereum, Arbitrum, Binance +1 | [sofa-org](https://github.com/sofa-org) | [sofa-protocol](https://github.com/sofa-org/sofa-protocol) `TypeScript` ★10 |
| 50 | **Mitosis** | $1.42M | Onchain Capital Allocator | Binance, Linea, Arbitrum +9 | [mitosis-org](https://github.com/mitosis-org) | [protocol](https://github.com/mitosis-org/protocol) `Solidity` ★17<br>[dn404x](https://github.com/mitosis-org/dn404x) `Solidity` ★3<br>[protocol-dapp-template](https://github.com/mitosis-org/protocol-dapp-template) `Solidity` ★1 +1 more |
| 51 | **SHUI** | $1.31M | Liquid Staking | Conflux | [Shui-LST](https://github.com/Shui-LST) | [shui-lsd-core](https://github.com/Shui-LST/shui-lsd-core) `Solidity` ★1 |
| 52 | **Scream** | $1.29M | Lending | Fantom | [Scream-Finance](https://github.com/Scream-Finance) | [scream-protocol](https://github.com/Scream-Finance/scream-protocol) `Solidity` ★26<br>[scream-protocol-v3](https://github.com/Scream-Finance/scream-protocol-v3) `TypeScript` ★0 |
| 53 | **ForgeYields** | $1.26M | Onchain Capital Allocator | Starknet, Ethereum | [ForgeYields](https://github.com/ForgeYields) | [starknet_vault_kit](https://github.com/ForgeYields/starknet_vault_kit) `Cairo` ★11 |
| 54 | **CityCoins** | $1.26M | Yield | Stacks | [citycoins](https://github.com/citycoins) | [protocol](https://github.com/citycoins/protocol) `Clarity` ★7<br>[protocol-api](https://github.com/citycoins/protocol-api) `TypeScript` ★1 |
| 55 | **ALEX** | $1.26M | Dexs | Stacks | [alexgo-io](https://github.com/alexgo-io) | [alex-v1](https://github.com/alexgo-io/alex-v1) `Clarity` ★41<br>[ord-bitcoincore-rpc](https://github.com/alexgo-io/ord-bitcoincore-rpc) `Rust` ★0<br>[alex-orderbook-public](https://github.com/alexgo-io/alex-orderbook-public) `Clarity` ★0 +2 more |
| 56 | **Kromatika** | $1.25M | Dexs | Optimism, Ethereum, Arbitrum +1 | [Kromatika-Finance](https://github.com/Kromatika-Finance) | [MetaSwap](https://github.com/Kromatika-Finance/MetaSwap) `Solidity` ★0 |
| 57 | **Mendi Finance** | $1.24M | Lending | Linea | [mendi-finance](https://github.com/mendi-finance) | [lending-protocol](https://github.com/mendi-finance/lending-protocol) `Solidity` ★5<br>[staking-protocol](https://github.com/mendi-finance/staking-protocol) `TypeScript` ★3 |
| 58 | **DefiChain DEX** | $1.24M | Dexs | DefiChain | [DeFiCh](https://github.com/DeFiCh) | [dfi-core](https://github.com/DeFiCh/dfi-core) `` ★0<br>[dfi-erc20](https://github.com/DeFiCh/dfi-erc20) `Solidity` ★0 |
| 59 | **Soroswap** | $1.22M | Dexs | Stellar | [soroswap](https://github.com/soroswap) | [core](https://github.com/soroswap/core) `Rust` ★22<br>[utility-contracts](https://github.com/soroswap/utility-contracts) `Rust` ★0 |
| 60 | **Rari Capital** | $1.18M | Yield Aggregator | Ethereum, Arbitrum | [Rari-Capital](https://github.com/Rari-Capital) | [nova-interfaces](https://github.com/Rari-Capital/nova-interfaces) `Solidity` ★10<br>[nova-invariants](https://github.com/Rari-Capital/nova-invariants) `Solidity` ★6<br>[fuse-v1](https://github.com/Rari-Capital/fuse-v1) `Solidity` ★2 +2 more |
| 61 | **OpenBook** | $1.16M | Dexs | Solana | [openbook-dex](https://github.com/openbook-dex) | [openbook-v2](https://github.com/openbook-dex/openbook-v2) `Rust` ★261<br>[program](https://github.com/openbook-dex/program) `Rust` ★211 |
| 62 | **Fiamma** | $1.15M | Bridge | Bitcoin | [fiamma-chain](https://github.com/fiamma-chain) | [btc-light-client](https://github.com/fiamma-chain/btc-light-client) `Solidity` ★0<br>[bitvm-bridge-contracts-solana](https://github.com/fiamma-chain/bitvm-bridge-contracts-solana) `Rust` ★1<br>[solana-client-sdk](https://github.com/fiamma-chain/solana-client-sdk) `Rust` ★0 +2 more |
| 63 | **Lets Get HAI** | $1.14M | CDP | Optimism | [hai-on-op](https://github.com/hai-on-op) | [core](https://github.com/hai-on-op/core) `Solidity` ★40<br>[altar-of-rai-contracts](https://github.com/hai-on-op/altar-of-rai-contracts) `Solidity` ★0<br>[governance](https://github.com/hai-on-op/governance) `Solidity` ★0 |
| 64 | **BabelFish** | $1.11M | Bridge | RSK | [BabelFishProtocol](https://github.com/BabelFishProtocol) | [governance-sc](https://github.com/BabelFishProtocol/governance-sc) `Solidity` ★0 |
| 65 | **Flex** | $1.11M | Lending | Ethereum | [flexmeow](https://github.com/flexmeow) | [flex-allocator](https://github.com/flexmeow/flex-allocator) `Solidity` ★0<br>[flex-contracts](https://github.com/flexmeow/flex-contracts) `Solidity` ★5<br>[dutch-taker-contracts](https://github.com/flexmeow/dutch-taker-contracts) `Vyper` ★0 |
| 66 | **Kai Finance** | $1.08M | Leveraged Farming | Sui | [kunalabs-io](https://github.com/kunalabs-io) | [sui-smart-contracts](https://github.com/kunalabs-io/sui-smart-contracts) `Move` ★85 |
| 67 | **Bounce.Tech** | $1.07M | Derivatives | Hyperliquid L1 | [bounce-tech](https://github.com/bounce-tech) | [bounce-smart-contracts](https://github.com/bounce-tech/bounce-smart-contracts) `Solidity` ★3 |
| 68 | **Overtime** | $1.06M | Prediction Market | Arbitrum, Base, Optimism +3 | [thales-markets](https://github.com/thales-markets) | [solana-contracts](https://github.com/thales-markets/solana-contracts) `JavaScript` ★0 |
| 69 | **Wombat Exchange** | $1.06M | Dexs | Binance, Arbitrum, Avalanche +7 | [wombat-exchange](https://github.com/wombat-exchange) | [v1-core](https://github.com/wombat-exchange/v1-core) `Solidity` ★18 |
| 70 | **Teller** | $1.05M | Lending | Base, Ethereum, Arbitrum +6 | [teller-protocol](https://github.com/teller-protocol) | [teller-protocol-v2](https://github.com/teller-protocol/teller-protocol-v2) `Rust` ★17<br>[teller-protocol-v1](https://github.com/teller-protocol/teller-protocol-v1) `Solidity` ★106<br>[teller-tx-debug-suite](https://github.com/teller-protocol/teller-tx-debug-suite) `Solidity` ★0 +2 more |
| 71 | **WanSwap Dex** | $1.04M | Dexs | Wanchain | [wanswap](https://github.com/wanswap) | [wasp-assist](https://github.com/wanswap/wasp-assist) `Solidity` ★1<br>[funny-auction-contracts](https://github.com/wanswap/funny-auction-contracts) `JavaScript` ★1<br>[wanswap-hive-contracts](https://github.com/wanswap/wanswap-hive-contracts) `Solidity` ★1 |
| 72 | **CHATEAU** | $1.02M | RWA | Plasma | [chateau-capital](https://github.com/chateau-capital) | [ca](https://github.com/chateau-capital/ca) `Solidity` ★1 |
| 73 | **RealtyX** | $1.02M | RWA | Base, Plume Mainnet | [HomuraAcc](https://github.com/HomuraAcc) | [The-Realtyx-Smart-Contracts](https://github.com/HomuraAcc/The-Realtyx-Smart-Contracts) `Solidity` ★3 |
| 74 | **Reflect Tranches** | $1.02M | Yield | Solana | [palindrome-eng](https://github.com/palindrome-eng) | [contract-interfaces](https://github.com/palindrome-eng/contract-interfaces) `` ★0 |
| 75 | **BlazeSwap** | $1.00M | Dexs | Flare, Songbird | [blazeswap](https://github.com/blazeswap) | [contracts](https://github.com/blazeswap/contracts) `TypeScript` ★5 |
| 76 | **ParyonUSD** | $967k | CDP | Bitcoincash | [ParyonUSD](https://github.com/ParyonUSD) | [verify_contract_deployment](https://github.com/ParyonUSD/verify_contract_deployment) `TypeScript` ★0<br>[contracts](https://github.com/ParyonUSD/contracts) `TypeScript` ★11 |
| 77 | **KEEP Network** | $967k | Cross Chain Bridge | Ethereum | [keep-network](https://github.com/keep-network) | [hardhat-helpers](https://github.com/keep-network/hardhat-helpers) `TypeScript` ★3<br>[contracts-migrate-action](https://github.com/keep-network/contracts-migrate-action) `` ★0 |
| 78 | **Trevee Earn** | $963k | Yield Aggregator | Sonic, Ethereum, Plasma | [Rings-Protocol](https://github.com/Rings-Protocol) | [rings-contracts](https://github.com/Rings-Protocol/rings-contracts) `Solidity` ★1<br>[rings-wrapper](https://github.com/Rings-Protocol/rings-wrapper) `Solidity` ★0 |
| 79 | **Isle Finance** | $931k | RWA | Hedera | [isle-labs](https://github.com/isle-labs) | [isle-enterprise-contract](https://github.com/isle-labs/isle-enterprise-contract) `Solidity` ★5 |
| 80 | **Kaskad** | $905k | Lending | Igra | [Kaskad-Lending](https://github.com/Kaskad-Lending) | [kaskad-contracts](https://github.com/Kaskad-Lending/kaskad-contracts) `Solidity` ★0<br>[kaskad-nuntius-contracts](https://github.com/Kaskad-Lending/kaskad-nuntius-contracts) `Solidity` ★0 |
| 81 | **Kolibri** | $901k | CDP | Tezos | [Hover-Labs](https://github.com/Hover-Labs) | [kolibri-contracts](https://github.com/Hover-Labs/kolibri-contracts) `Python` ★8<br>[LP-Token-Contracts](https://github.com/Hover-Labs/LP-Token-Contracts) `Python` ★1<br>[break-glass-contracts](https://github.com/Hover-Labs/break-glass-contracts) `Python` ★0 |
| 82 | **Suzaku** | $889k | Restaking | Avalanche | [suzaku-network](https://github.com/suzaku-network) | [suzaku-core](https://github.com/suzaku-network/suzaku-core) `Solidity` ★1<br>[suzaku-contracts-library](https://github.com/suzaku-network/suzaku-contracts-library) `Solidity` ★8<br>[suzaku-deployer](https://github.com/suzaku-network/suzaku-deployer) `Solidity` ★0 |
| 83 | **Azuro** | $881k | Prediction Market | Polygon, Base, Linea +3 | [Azuro-protocol](https://github.com/Azuro-protocol) | [protocol-docs](https://github.com/Azuro-protocol/protocol-docs) `` ★1<br>[OpenRandom](https://github.com/Azuro-protocol/OpenRandom) `Solidity` ★1 |
| 84 | **Hemi** | $858k | Canonical Bridge | Ethereum | [hemilabs](https://github.com/hemilabs) | [veHEMI](https://github.com/hemilabs/veHEMI) `Solidity` ★0<br>[hemi-token](https://github.com/hemilabs/hemi-token) `Solidity` ★0<br>[vusd-stablecoin](https://github.com/hemilabs/vusd-stablecoin) `Solidity` ★4 +2 more |
| 85 | **Dinosaur Eggs** | $846k | Dexs | Binance | [Dinosaur-eggs](https://github.com/Dinosaur-eggs) | [core](https://github.com/Dinosaur-eggs/core) `Solidity` ★24 |
| 86 | **Trueo** | $843k | Prediction Market | Base | [trueo-protocol](https://github.com/trueo-protocol) | [trueo-contracts](https://github.com/trueo-protocol/trueo-contracts) `Solidity` ★14 |
| 87 | **CANA Holdings California Carbon Credits** | $809k | RWA | Ethereum | [maseer-finance](https://github.com/maseer-finance) | [maseer-one](https://github.com/maseer-finance/maseer-one) `Solidity` ★0<br>[maseer-oracles](https://github.com/maseer-finance/maseer-oracles) `Solidity` ★0<br>[maseer-vest](https://github.com/maseer-finance/maseer-vest) `Solidity` ★0 |
| 88 | **Cover Protocol** | $809k | Insurance | Ethereum | [CoverProtocol](https://github.com/CoverProtocol) | [cover-token-mining](https://github.com/CoverProtocol/cover-token-mining) `Solidity` ★8<br>[cover-core-v1](https://github.com/CoverProtocol/cover-core-v1) `Solidity` ★19<br>[cover-rewards](https://github.com/CoverProtocol/cover-rewards) `Solidity` ★1 +1 more |
| 89 | **Ellipsis Finance** | $806k | Dexs | Binance | [ellipsis-finance](https://github.com/ellipsis-finance) | [ellipsis-v2](https://github.com/ellipsis-finance/ellipsis-v2) `Solidity` ★13 |
| 90 | **10KSwap** | $781k | Dexs | Starknet | [10k-swap](https://github.com/10k-swap) | [10k_swap-contracts](https://github.com/10k-swap/10k_swap-contracts) `Cairo` ★58 |
| 91 | **Tarot** | $772k | Lending | Base, Fantom, Optimism +10 | [tarot-finance](https://github.com/tarot-finance) | [tarot-core](https://github.com/tarot-finance/tarot-core) `JavaScript` ★17<br>[tarot-price-oracle](https://github.com/tarot-finance/tarot-price-oracle) `Solidity` ★8<br>[tarot-periphery](https://github.com/tarot-finance/tarot-periphery) `Solidity` ★9 +2 more |
| 92 | **WePiggy** | $765k | Lending | Ethereum, Arbitrum, Optimism +9 | [WePiggy](https://github.com/WePiggy) | [wepiggy-contracts](https://github.com/WePiggy/wepiggy-contracts) `Solidity` ★20<br>[contract_addresses](https://github.com/WePiggy/contract_addresses) `` ★0<br>[wepiggy-contracts-optimism](https://github.com/WePiggy/wepiggy-contracts-optimism) `Solidity` ★0 +1 more |
| 93 | **Honeyswap** | $744k | Dexs | xDai, Polygon | [1Hive](https://github.com/1Hive) | [fluid-proposals](https://github.com/1Hive/fluid-proposals) `Solidity` ★0<br>[honeyswap-limit-order-contracts](https://github.com/1Hive/honeyswap-limit-order-contracts) `Solidity` ★3<br>[deployments-aragon-os](https://github.com/1Hive/deployments-aragon-os) `TypeScript` ★0 |
| 94 | **Travessia Credit** | $742k | RWA | Ethereum, Monad | [RedVeil](https://github.com/RedVeil) | [Travessia-Commodity-Tracking](https://github.com/RedVeil/Travessia-Commodity-Tracking) `Solidity` ★0<br>[FixedForexUSDC](https://github.com/RedVeil/FixedForexUSDC) `Solidity` ★0<br>[YieldForge](https://github.com/RedVeil/YieldForge) `Solidity` ★0 +2 more |
| 95 | **Aurigami** | $707k | Lending | Aurora | [Aurigami-Finance](https://github.com/Aurigami-Finance) | [aurigami-smart-contracts](https://github.com/Aurigami-Finance/aurigami-smart-contracts) `Solidity` ★0 |
| 96 | **ImmutableX** | $654k | NFT Marketplace | Ethereum | [immutable](https://github.com/immutable) | [imx-migration-contracts](https://github.com/immutable/imx-migration-contracts) `Solidity` ★2<br>[contracts](https://github.com/immutable/contracts) `Solidity` ★46<br>[zkevm-bridge-contracts](https://github.com/immutable/zkevm-bridge-contracts) `Solidity` ★18 +1 more |
| 97 | **Meson** | $646k | Cross Chain Bridge | Merlin, BSquared, Ethereum +41 | [MesonFi](https://github.com/MesonFi) | [merlin-contracts](https://github.com/MesonFi/merlin-contracts) `Solidity` ★0 |
| 98 | **JPEG'd** | $621k | NFT Lending | Ethereum | [jpegd](https://github.com/jpegd) | [core](https://github.com/jpegd/core) `Solidity` ★12 |
| 99 | **PsyOptions** | $615k | Options | Solana | [mithraiclabs](https://github.com/mithraiclabs) | [psyoracleutils](https://github.com/mithraiclabs/psyoracleutils) `Rust` ★2<br>[pyth-min](https://github.com/mithraiclabs/pyth-min) `Rust` ★0<br>[psy-macros](https://github.com/mithraiclabs/psy-macros) `Rust` ★1 |
| 100 | **VETRO** | $611k | CDP | Ethereum | [vetro-protocol](https://github.com/vetro-protocol) | [vetro-contracts](https://github.com/vetro-protocol/vetro-contracts) `Solidity` ★2 |
| 101 | **AgentFi** | $606k | AI Agents | Blast | [AgentFi](https://github.com/AgentFi) | [agentfi-contracts-blast](https://github.com/AgentFi/agentfi-contracts-blast) `TypeScript` ★4<br>[agentfi-contracts](https://github.com/AgentFi/agentfi-contracts) `` ★0 |
| 102 | **BearnFi** | $599k | Yield | Binance | [bearn-defi](https://github.com/bearn-defi) | [bearn-smartcontracts](https://github.com/bearn-defi/bearn-smartcontracts) `Solidity` ★6<br>[bdex-smartcontracts](https://github.com/bearn-defi/bdex-smartcontracts) `TypeScript` ★0<br>[bvaults-smartcontracts](https://github.com/bearn-defi/bvaults-smartcontracts) `Solidity` ★0 |
| 103 | **EZManager** | $577k | Liquidity Manager | Base, Robinhood Chain, Hyperliquid L1 +3 | [EZManagerCL](https://github.com/EZManagerCL) | [EZManagerContracts](https://github.com/EZManagerCL/EZManagerContracts) `Solidity` ★0 |
| 104 | **Zunami Protocol** | $572k | Yield Aggregator | Ethereum | [ZunamiProtocol](https://github.com/ZunamiProtocol) | [ZunamiProtocolV2](https://github.com/ZunamiProtocol/ZunamiProtocolV2) `TypeScript` ★1 |
| 105 | **Sigmausd** | $567k | Algo-Stables | Ergo | [anon-real](https://github.com/anon-real) | [contract-testing](https://github.com/anon-real/contract-testing) `Scala` ★6 |
| 106 | **Siren** | $566k | Options | Ethereum, Polygon, Arbitrum | [sirenmarkets](https://github.com/sirenmarkets) | [core](https://github.com/sirenmarkets/core) `TypeScript` ★40 |
| 107 | **PinkSwap** | $557k | Dexs | Binance | [pinkmoonfinance](https://github.com/pinkmoonfinance) | [pinksale-contracts](https://github.com/pinkmoonfinance/pinksale-contracts) `Solidity` ★44<br>[pink-antibot-guide](https://github.com/pinkmoonfinance/pink-antibot-guide) `Solidity` ★51 |
| 108 | **VaultCraft** | $549k | Yield | Arbitrum, Ethereum, Polygon +4 | [Popcorn-Limited](https://github.com/Popcorn-Limited) | [gauges](https://github.com/Popcorn-Limited/gauges) `Solidity` ★0<br>[audit-04-24](https://github.com/Popcorn-Limited/audit-04-24) `Solidity` ★0<br>[xvcx-bridges](https://github.com/Popcorn-Limited/xvcx-bridges) `Solidity` ★0 +2 more |
| 109 | **Ante Finance** | $547k | Insurance | Ethereum, Binance, Avalanche +5 | [antefinance](https://github.com/antefinance) | [ante-v05-core](https://github.com/antefinance/ante-v05-core) `TypeScript` ★6<br>[ante-community-tests](https://github.com/antefinance/ante-community-tests) `Solidity` ★35<br>[ante-v06-core](https://github.com/antefinance/ante-v06-core) `TypeScript` ★1 |
| 110 | **Geode** | $543k | Liquid Staking | Avalanche | [Geodefi](https://github.com/Geodefi) | [Portal-Eth](https://github.com/Geodefi/Portal-Eth) `Solidity` ★3 |
| 111 | **Toucan Protocol** | $542k | RWA | Polygon, Celo, Base +1 | [ToucanProtocol](https://github.com/ToucanProtocol) | [contracts](https://github.com/ToucanProtocol/contracts) `Solidity` ★57<br>[dynamic-fee-pools](https://github.com/ToucanProtocol/dynamic-fee-pools) `Solidity` ★2 |
| 112 | **yAxis** | $539k | Yield Aggregator | Ethereum | [yaxis-project](https://github.com/yaxis-project) | [yaxis-audit](https://github.com/yaxis-project/yaxis-audit) `Solidity` ★6<br>[metavault](https://github.com/yaxis-project/metavault) `Solidity` ★32 |
| 113 | **Unicly** | $535k | Dexs | Ethereum | [uniclyNFT](https://github.com/uniclyNFT) | [unicly-core](https://github.com/uniclyNFT/unicly-core) `Solidity` ★9 |
| 114 | **MooniSwap** | $532k | Dexs | Ethereum | [1inch](https://github.com/1inch) | [swap-vm](https://github.com/1inch/swap-vm) `Solidity` ★43<br>[limit-order-protocol](https://github.com/1inch/limit-order-protocol) `JavaScript` ★312<br>[aqua](https://github.com/1inch/aqua) `Solidity` ★112 +2 more |
| 115 | **DIEM Relay** | $517k | Liquid Staking | Base | [Figu3](https://github.com/Figu3) | [diem-relay](https://github.com/Figu3/diem-relay) `Solidity` ★0<br>[sonic-earn-recovery-system](https://github.com/Figu3/sonic-earn-recovery-system) `Solidity` ★0<br>[splusd-v2](https://github.com/Figu3/splusd-v2) `Solidity` ★0 +2 more |
| 116 | **RadioShack** | $508k | Dexs | Binance, Avalanche, Polygon +5 | [radioshackswap](https://github.com/radioshackswap) | [contracts](https://github.com/radioshackswap/contracts) `Solidity` ★2 |
| 117 | **Splice Finance** | $504k | Yield | Blast, Mode | [splice-finance](https://github.com/splice-finance) | [contracts-public](https://github.com/splice-finance/contracts-public) `Solidity` ★1 |
| 118 | **Sherlock** | $487k | Insurance | Ethereum | [sherlock-protocol](https://github.com/sherlock-protocol) | [sherlock-ctf-0x0](https://github.com/sherlock-protocol/sherlock-ctf-0x0) `Solidity` ★113<br>[sherlock-v2-core](https://github.com/sherlock-protocol/sherlock-v2-core) `JavaScript` ★26<br>[sherlock-v1-core](https://github.com/sherlock-protocol/sherlock-v1-core) `JavaScript` ★1 +1 more |
| 119 | **Atrium** | $481k | Farm | Cardano | [atma-community](https://github.com/atma-community) | [staking-baskets](https://github.com/atma-community/staking-baskets) `Haskell` ★4 |
| 120 | **Sherpa** | $480k | Onchain Capital Allocator | Ethereum, Base, Monad | [hedgemonyxyz](https://github.com/hedgemonyxyz) | [sherpa-vault-smartcontracts-v1.0](https://github.com/hedgemonyxyz/sherpa-vault-smartcontracts-v1.0) `Solidity` ★1 |
| 121 | **UFarm Digital** | $480k | Onchain Capital Allocator | Ethereum, Arbitrum | [UFarmDigital](https://github.com/UFarmDigital) | [UFarm-EVM-Contracts](https://github.com/UFarmDigital/UFarm-EVM-Contracts) `TypeScript` ★2 |
| 122 | **YFII** | $471k | Yield Aggregator | Ethereum | [yfii](https://github.com/yfii) | [yvault](https://github.com/yfii/yvault) `Solidity` ★60<br>[yficontract](https://github.com/yfii/yficontract) `JavaScript` ★16 |
| 123 | **SingularityDAO** | $466k | Yield | Ethereum, Binance | [Singularity-DAO](https://github.com/Singularity-DAO) | [hypercycle-token-contracts](https://github.com/Singularity-DAO/hypercycle-token-contracts) `JavaScript` ★0<br>[migration-contracts](https://github.com/Singularity-DAO/migration-contracts) `TypeScript` ★3<br>[sdao-token-contracts](https://github.com/Singularity-DAO/sdao-token-contracts) `Solidity` ★9 +2 more |
| 124 | **Choice Exchange** | $463k | Dexs | Injective | [choice-exchange](https://github.com/choice-exchange) | [choice_v2_contracts](https://github.com/choice-exchange/choice_v2_contracts) `Solidity` ★0<br>[infinity-core](https://github.com/choice-exchange/infinity-core) `Solidity` ★0<br>[infinity-periphery](https://github.com/choice-exchange/infinity-periphery) `Solidity` ★0 +2 more |
| 125 | **FortiFi** | $451k | Yield Aggregator | Avalanche | [0xFortiFi](https://github.com/0xFortiFi) | [Moat-Contracts](https://github.com/0xFortiFi/Moat-Contracts) `Solidity` ★0<br>[FortiFi-Foundry](https://github.com/0xFortiFi/FortiFi-Foundry) `Solidity` ★0<br>[FortiFi-Vaults](https://github.com/0xFortiFi/FortiFi-Vaults) `Solidity` ★1 |
| 126 | **Clarity** | $450k | DAO Service Provider | Cardano | [ClearContracts](https://github.com/ClearContracts) | [clearcontracts.github.io](https://github.com/ClearContracts/clearcontracts.github.io) `HTML` ★0<br>[clarity-clb](https://github.com/ClearContracts/clarity-clb) `Haskell` ★0 |
| 127 | **Narwhalswap** | $450k | Dexs | Binance | [narwhalswap](https://github.com/narwhalswap) | [thegrandbanks](https://github.com/narwhalswap/thegrandbanks) `Solidity` ★1<br>[contracts](https://github.com/narwhalswap/contracts) `Solidity` ★0<br>[nar-token](https://github.com/narwhalswap/nar-token) `Solidity` ★0 |
| 128 | **88mph** | $442k | Lending | Ethereum, Fantom, Avalanche +1 | [88mphapp](https://github.com/88mphapp) | [88mph-contracts](https://github.com/88mphapp/88mph-contracts) `Solidity` ★84<br>[88mph-gauge](https://github.com/88mphapp/88mph-gauge) `Vyper` ★0<br>[Phantasm](https://github.com/88mphapp/Phantasm) `Solidity` ★0 +1 more |
| 129 | **Perpetual Protocol** | $442k | Derivatives | Ethereum, Optimism | [perpetual-protocol](https://github.com/perpetual-protocol) | [perpetual-protocol](https://github.com/perpetual-protocol/perpetual-protocol) `TypeScript` ★168<br>[perp-curie-contract](https://github.com/perpetual-protocol/perp-curie-contract) `TypeScript` ★89<br>[perp-curie-periphery-contract](https://github.com/perpetual-protocol/perp-curie-periphery-contract) `TypeScript` ★15 +2 more |
| 130 | **HashKing** | $438k | Liquid Staking | Filecoin | [NodeDAO](https://github.com/NodeDAO) | [obelisk-network](https://github.com/NodeDAO/obelisk-network) `Solidity` ★0<br>[HashKing-FIL](https://github.com/NodeDAO/HashKing-FIL) `Solidity` ★1<br>[NodeDAO-Protocol](https://github.com/NodeDAO/NodeDAO-Protocol) `Solidity` ★2 +2 more |
| 131 | **Definix** | $437k | Dexs | Binance, Klaytn | [thesixnetwork](https://github.com/thesixnetwork) | [six-protocol](https://github.com/thesixnetwork/six-protocol) `Go` ★1<br>[multicall3](https://github.com/thesixnetwork/multicall3) `Solidity` ★0<br>[cross-dev-contract](https://github.com/thesixnetwork/cross-dev-contract) `Solidity` ★0 +2 more |
| 132 | **BoringDAO** | $434k | Cross Chain Bridge | Litecoin, Polygon, Doge +17 | [BoringDAO](https://github.com/BoringDAO) | [boringDAO-contract](https://github.com/BoringDAO/boringDAO-contract) `Solidity` ★13<br>[smart-bridge-contract](https://github.com/BoringDAO/smart-bridge-contract) `TypeScript` ★2 |
| 133 | **BOB Fusion** | $431k | Farm | Ethereum | [bob-collective](https://github.com/bob-collective) | [wdk-protocol-swidge-gateway](https://github.com/bob-collective/wdk-protocol-swidge-gateway) `TypeScript` ★1<br>[fusion-lock](https://github.com/bob-collective/fusion-lock) `Solidity` ★1<br>[bitcoin-spv](https://github.com/bob-collective/bitcoin-spv) `Solidity` ★5 +2 more |
| 134 | **Goose Finance** | $427k | Farm | Binance | [goosedefi](https://github.com/goosedefi) | [goose-contracts-incubator](https://github.com/goosedefi/goose-contracts-incubator) `Solidity` ★9<br>[goose-contracts](https://github.com/goosedefi/goose-contracts) `Solidity` ★61 |
| 135 | **ErgoDEX** | $425k | Dexs | Ergo | [spectrum-finance](https://github.com/spectrum-finance) | [cardano-dex-contracts](https://github.com/spectrum-finance/cardano-dex-contracts) `Haskell` ★35<br>[cardano-dex-backend](https://github.com/spectrum-finance/cardano-dex-backend) `Haskell` ★15<br>[cardano-dex-sdk-haskell](https://github.com/spectrum-finance/cardano-dex-sdk-haskell) `Haskell` ★7 +2 more |
| 136 | **Altitude.Fi** | $424k | Lending | Ethereum | [altitude-fi](https://github.com/altitude-fi) | [altitude-v2](https://github.com/altitude-fi/altitude-v2) `Solidity` ★3 |
| 137 | **PieDAO** | $415k | Indexes | Ethereum | [pie-dao](https://github.com/pie-dao) | [pie-flash-loans-poc](https://github.com/pie-dao/pie-flash-loans-poc) `Solidity` ★9<br>[pie-oven](https://github.com/pie-dao/pie-oven) `Solidity` ★12<br>[auxo-vaults](https://github.com/pie-dao/auxo-vaults) `Solidity` ★16 +2 more |
| 138 | **sICX** | $409k | Liquid Staking | Icon | [icon-project](https://github.com/icon-project) | [devportal](https://github.com/icon-project/devportal) `Solidity` ★12<br>[java-score-examples](https://github.com/icon-project/java-score-examples) `Java` ★15<br>[javaee-scorex](https://github.com/icon-project/javaee-scorex) `Java` ★2 |
| 139 | **Compound Blue** | $408k | Lending | Polygon | [papercliplabs](https://github.com/papercliplabs) | [nouns-town](https://github.com/papercliplabs/nouns-town) `Solidity` ★1 |
| 140 | **KSwap Finance** | $408k | Dexs | OKExChain | [kswap-finance](https://github.com/kswap-finance) | [kswap-dex](https://github.com/kswap-finance/kswap-dex) `Solidity` ★7 |
| 141 | **Dfyn Network** | $406k | Dexs | Polygon, Fantom, OKExChain | [dfyn](https://github.com/dfyn) | [dfyn-exchange](https://github.com/dfyn/dfyn-exchange) `Solidity` ★21<br>[dfyn-token](https://github.com/dfyn/dfyn-token) `Solidity` ★7<br>[dual-farm](https://github.com/dfyn/dual-farm) `Solidity` ★1 +2 more |
| 142 | **Breadchain** | $401k | CDP | xDai | [BreadchainCoop](https://github.com/BreadchainCoop) | [saving-circles](https://github.com/BreadchainCoop/saving-circles) `Solidity` ★2<br>[builders-dollar](https://github.com/BreadchainCoop/builders-dollar) `Solidity` ★3<br>[bread](https://github.com/BreadchainCoop/bread) `Solidity` ★1 +2 more |
| 143 | **The Rig** | $388k | Liquid Staking | Fuel | [Rig-Labs](https://github.com/Rig-Labs) | [smart-contracts](https://github.com/Rig-Labs/smart-contracts) `Sway` ★0 |
| 144 | **Knit Finance** | $384k | Bridge | Ethereum, Polygon, Kava +15 | [KnitFinance](https://github.com/KnitFinance) | [Cexdex.app](https://github.com/KnitFinance/Cexdex.app) `Solidity` ★0 |
| 145 | **Octus Bridge** | $383k | Bridge | Avalanche, Binance, Ethereum +3 | [broxus](https://github.com/broxus) | [octusbridge-contracts](https://github.com/broxus/octusbridge-contracts) `TypeScript` ★10<br>[everscale-yield-farming](https://github.com/broxus/everscale-yield-farming) `Solidity` ★6<br>[tip3jetton](https://github.com/broxus/tip3jetton) `Solidity` ★2 +2 more |
| 146 | **Moor** | $380k | CDP | Fuel | [Rig-Labs](https://github.com/Rig-Labs) | [smart-contracts](https://github.com/Rig-Labs/smart-contracts) `Sway` ★0 |
| 147 | **AggreLend** | $372k | Yield Aggregator | Solana | [AggreLend](https://github.com/AggreLend) | [kamino-finance-cpi-integration](https://github.com/AggreLend/kamino-finance-cpi-integration) `Rust` ★4<br>[drift-cpi-integration](https://github.com/AggreLend/drift-cpi-integration) `Rust` ★3<br>[marginfi-integration](https://github.com/AggreLend/marginfi-integration) `Rust` ★3 +1 more |
| 148 | **Scientix** | $367k | Synthetics | Binance | [ScientixFinance](https://github.com/ScientixFinance) | [scientix-contract](https://github.com/ScientixFinance/scientix-contract) `Solidity` ★3 |
| 149 | **Hord** | $361k | Liquid Staking | Ethereum | [hord](https://github.com/hord) | [farming-geyser](https://github.com/hord/farming-geyser) `Solidity` ★6 |
| 150 | **RAGE Protocol** | $359k | Onchain Capital Allocator | Base | [ultraroundMoney](https://github.com/ultraroundMoney) | [hestia](https://github.com/ultraroundMoney/hestia) `Solidity` ★1<br>[hestia-mine](https://github.com/ultraroundMoney/hestia-mine) `Solidity` ★0<br>[circle-temple](https://github.com/ultraroundMoney/circle-temple) `Solidity` ★0 +1 more |
| 151 | **Nomad** | $359k | Bridge | Ethereum, Moonbeam, Milkomeda +1 | [nomad-xyz](https://github.com/nomad-xyz) | [ExcessivelySafeCall](https://github.com/nomad-xyz/ExcessivelySafeCall) `Solidity` ★244<br>[monorepo](https://github.com/nomad-xyz/monorepo) `Solidity` ★124 |
| 152 | **Ponder Finance** | $358k | Dexs | Bitkub | [ponderfinance](https://github.com/ponderfinance) | [protocol](https://github.com/ponderfinance/protocol) `Solidity` ★1<br>[usdp](https://github.com/ponderfinance/usdp) `Solidity` ★0 |
| 153 | **DDEX** | $351k | Dexs | Ethereum | [HydroProtocol](https://github.com/HydroProtocol) | [protocol](https://github.com/HydroProtocol/protocol) `JavaScript` ★103<br>[contract-interactions](https://github.com/HydroProtocol/contract-interactions) `JavaScript` ★6<br>[protocol-tron](https://github.com/HydroProtocol/protocol-tron) `JavaScript` ★7 |
| 154 | **Rigoblock** | $340k | Onchain Capital Allocator | Hyperliquid L1, Ethereum, Arbitrum +4 | [RigoBlock](https://github.com/RigoBlock) | [v3-contracts](https://github.com/RigoBlock/v3-contracts) `Solidity` ★10<br>[zrx-staking-rebalance](https://github.com/RigoBlock/zrx-staking-rebalance) `Solidity` ★1<br>[contracts](https://github.com/RigoBlock/contracts) `JavaScript` ★1 +2 more |
| 155 | **Opus** | $336k | CDP | Starknet | [lindy-labs](https://github.com/lindy-labs) | [opus_contracts](https://github.com/lindy-labs/opus_contracts) `Cairo` ★0<br>[opus_compose](https://github.com/lindy-labs/opus_compose) `Cairo` ★0<br>[wadray](https://github.com/lindy-labs/wadray) `Cairo` ★21 +2 more |
| 156 | **Nolus Protocol** | $330k | Lending | Solana, Nolus, Neutron +1 | [nolus-protocol](https://github.com/nolus-protocol) | [nolus-core](https://github.com/nolus-protocol/nolus-core) `Go` ★62 |
| 157 | **Swop** | $325k | Dexs | Waves, UNIT0 | [swopfi](https://github.com/swopfi) | [swopfi-smart-contracts](https://github.com/swopfi/swopfi-smart-contracts) `` ★11 |
| 158 | **Abyss** | $321k | Yield | Sui | [abyss-protocol](https://github.com/abyss-protocol) | [abyss-vaults](https://github.com/abyss-protocol/abyss-vaults) `Move` ★3 |
| 159 | **Sprinter** | $311k | Yield | Base | [sprintertech](https://github.com/sprintertech) | [sprinter-stash-contracts](https://github.com/sprintertech/sprinter-stash-contracts) `TypeScript` ★1<br>[deploy-safersafes](https://github.com/sprintertech/deploy-safersafes) `Solidity` ★0 |
| 160 | **Swerve** | $305k | Dexs | Ethereum | [SwerveFinance](https://github.com/SwerveFinance) | [SwerveContracts](https://github.com/SwerveFinance/SwerveContracts) `` ★38 |
| 161 | **ENKI Protocol** | $303k | Liquid Staking | Metis | [ENKIXYZ](https://github.com/ENKIXYZ) | [enki-token](https://github.com/ENKIXYZ/enki-token) `Solidity` ★1 |

---

## NO_CONTRACT_REPO — 68 protocols

These protocols declare a public github org but no contract-bearing repo was detected by the heuristic. Worth manual review before assuming closed-source.

| # | Protocol | TVL | Category | Chains | GitHub |
|---|---|---|---|---|---|
| 1 | Blueshift | $4.69M | Dexs | BOB, Kava, Polygon +2 | [blueshift-fi](https://github.com/blueshift-fi) |
| 2 | Bumpin Trade | $4.49M | Derivatives | Solana | [bumpin-exchange](https://github.com/bumpin-exchange) |
| 3 | Mole | $4.42M | Yield | Sui, Aptos | [Mole-Fi](https://github.com/Mole-Fi) |
| 4 | Indigo | $4.31M | CDP | Cardano | [IndigoProtocol](https://github.com/IndigoProtocol) |
| 5 | Liquidium | $4.25M | Lending | ICP | [Liquidium-Inc](https://github.com/Liquidium-Inc) |
| 6 | Nawa Protocol | $4.00M | RWA | ZIGChain, Ethereum, CORE | [NawaTeam](https://github.com/NawaTeam) |
| 7 | ICPSwap | $3.94M | Dexs | ICP | [ICPSwap-Labs](https://github.com/ICPSwap-Labs) |
| 8 | Presto | $3.33M | Risk Curators | Ethereum | [prestolabs](https://github.com/prestolabs) |
| 9 | Surf Lending | $3.20M | Lending | Cardano | [flow-lending](https://github.com/flow-lending) |
| 10 | Sonic ICP | $3.03M | Dexs | ICP | [Psychedelic](https://github.com/Psychedelic) |
| 11 | FluidTokens | $2.93M | Lending | Cardano | [FluidTokens](https://github.com/FluidTokens) |
| 12 | LayerBank | $2.47M | Lending | RSK, Manta, BOB +14 | [layerbank](https://github.com/layerbank) |
| 13 | International Stable Currency | $2.42M | RWA | Solana | [TheISCTeam](https://github.com/TheISCTeam) |
| 14 | Dnax | $2.23M | Dexs | Binance | [CarbonDeploy](https://github.com/CarbonDeploy) |
| 15 | Revault | $2.23M | Yield | Binance | [revault](https://github.com/revault) |
| 16 | Cabal | $2.13M | Governance Incentives | Initia, Strat, Cabal | [0xCabal](https://github.com/0xCabal) |
| 17 | Baseline Protocol | $2.03M | Liquidity Manager | Ethereum, Base, Blast | [0xBaseline](https://github.com/0xBaseline) |
| 18 | PiggyBank | $1.71M | Yield | Solana | [zsociety-io](https://github.com/zsociety-io) |
| 19 | Coffer Network | $1.58M | Bridge | Bitcoin | [coffer-network](https://github.com/coffer-network) |
| 20 | Japan Staked SOL | $1.49M | Liquid Staking | Solana | [DawnLabsTech](https://github.com/DawnLabsTech) |
| 21 | Rise.rich | $1.43M | Launchpad | Solana | [riserich](https://github.com/riserich) |
| 22 | Mountain Protocol | $1.40M | RWA | Ethereum, zkSync Era, Arbitrum +3 | [mountainprotocol](https://github.com/mountainprotocol) |
| 23 | Laine SOL | $1.38M | Liquid Staking | Solana | [laine-sa](https://github.com/laine-sa) |
| 24 | Surge Credit | $1.34M | Lending | Base, Bitcoin | [surgecredit](https://github.com/surgecredit) |
| 25 | Amply Finance | $1.30M | Lending | Cronos zkEVM | [AmplyFinance-Defi](https://github.com/AmplyFinance-Defi) |
| 26 | Liquidity House | $1.27M | Prediction Market | Etherlink | [liquidityhouse](https://github.com/liquidityhouse) |
| 27 | Arkadiko | $1.25M | CDP | Stacks | [arkadiko-dao](https://github.com/arkadiko-dao) |
| 28 | Pools Finance | $1.24M | Dexs | IOTA | [Pools-Finance](https://github.com/Pools-Finance) |
| 29 | Moola Market | $1.22M | Lending | Celo | [moolamarket](https://github.com/moolamarket) |
| 30 | Rook | $1.20M | Dexs | Ethereum | [keeperdao](https://github.com/keeperdao) |
| 31 | Scopuly | $1.16M | Dexs | Stellar | [Scopuly](https://github.com/Scopuly) |
| 32 | Decentralized Euro | $1.11M | CDP | Ethereum | [d-EURO](https://github.com/d-EURO) |
| 33 | Pact | $1.03M | Dexs | Algorand | [pactfi](https://github.com/pactfi) |
| 34 | Saddle Finance | $1.01M | Dexs | Ethereum, Arbitrum, Optimism +4 | [saddle-finance](https://github.com/saddle-finance) |
| 35 | tramplin.io | $1.01M | Staking Pool | Solana | [tramplin-io](https://github.com/tramplin-io) |
| 36 | Reactor DEX | $989k | Dexs | Fuel | [Reactor-Fuel](https://github.com/Reactor-Fuel) |
| 37 | Archer Exchange | $945k | Dexs | Solana | [SquareRoot-Labs](https://github.com/SquareRoot-Labs) |
| 38 | InkySwap | $921k | Dexs | Ink | [InkySwap](https://github.com/InkySwap) |
| 39 | Swaylend | $895k | Lending | Fuel | [swaylend](https://github.com/swaylend) |
| 40 | Ashswap | $872k | Dexs | Elrond | [ashswap](https://github.com/ashswap) |
| 41 | Bastion | $871k | Lending | Aurora | [bastionprotocol](https://github.com/bastionprotocol) |
| 42 | xToken | $852k | Liquidity Manager | Ethereum, Optimism, Arbitrum +1 | [xtokenmarket](https://github.com/xtokenmarket) |
| 43 | Pondo Protocol | $839k | Liquid Staking | Aleo | [ProvableHQ](https://github.com/ProvableHQ) |
| 44 | Flexa | $833k | Payments | Ethereum | [flexahq](https://github.com/flexahq) |
| 45 | Clipper | $819k | Dexs | Ethereum, Base, Optimism +5 | [shipyard-software](https://github.com/shipyard-software) |
| 46 | Allstake | $772k | Restaking | Near, Solana, Ethereum | [allstake](https://github.com/allstake) |
| 47 | Turtle Club | $736k | Onchain Capital Allocator | Ethereum, Avalanche, Linea | [Turtle-DAO](https://github.com/Turtle-DAO) |
| 48 | AirPuff | $735k | Leveraged Farming | Ethereum, Arbitrum, Mode +3 | [Airpuff](https://github.com/Airpuff) |
| 49 | Kublerx | $717k | Dexs | Bitkub | [kublerxofficial](https://github.com/kublerxofficial) |
| 50 | Muscadine | $704k | Risk Curators | Base | [Muscadine-Labs](https://github.com/Muscadine-Labs) |
| 51 | Pyron | $637k | Lending | Fogo | [pyron-finance](https://github.com/pyron-finance) |
| 52 | Arkis | $637k | Lending | Ethereum, Hyperliquid L1 | [ArkisXYZ](https://github.com/ArkisXYZ) |
| 53 | Landshare | $621k | RWA | Binance | [ls-jordan](https://github.com/ls-jordan) |
| 54 | ICDex | $557k | Dexs | ICP | [iclighthouse](https://github.com/iclighthouse) |
| 55 | Ryze Protocol | $528k | Dexs | Base | [ryze-protocol](https://github.com/ryze-protocol) |
| 56 | DefiBox | $503k | Dexs | EOS, Binance, Wax | [DefiboxTeam](https://github.com/DefiboxTeam) |
| 57 | Beradrome | $494k | Yield | Berachain | [BeraLabs](https://github.com/BeraLabs) |
| 58 | Stella | $443k | Leveraged Farming | Arbitrum | [stellaxyz](https://github.com/stellaxyz) |
| 59 | SHPRD | $423k | Indexes | Arbitrum, Ethereum | [stealth-defi](https://github.com/stealth-defi) |
| 60 | Almanak | $385k | Onchain Capital Allocator | Ethereum, Base | [almanak-co](https://github.com/almanak-co) |
| 61 | Mobius Money | $366k | Dexs | Celo | [mobiusAMM](https://github.com/mobiusAMM) |
| 62 | OolongSwap | $359k | Dexs | Boba | [OolongSwap](https://github.com/OolongSwap) |
| 63 | OnX Finance | $340k | Yield Aggregator | Ethereum, Polygon, Fantom +1 | [onx-finance](https://github.com/onx-finance) |
| 64 | SteakBank Finance | $329k | Liquid Staking | Binance | [steakbankfinance](https://github.com/steakbankfinance) |
| 65 | Adrena Protocol | $325k | Derivatives | Solana | [AdrenaFoundation](https://github.com/AdrenaFoundation) |
| 66 | xSigma | $317k | Dexs | Ethereum | [xSigmaLabs](https://github.com/xSigmaLabs) |
| 67 | Permapod | $312k | Lending | ZIGChain | [permapod](https://github.com/permapod) |
| 68 | Acre | $305k | Yield | Ethereum | [acre-btc](https://github.com/acre-btc) |

---

## ORG_404 — 3 protocols

- Goldsand by InshAllah ($374k) — declared org: `['inshallah-network']`
- AbstraDEX ($418k) — declared org: `['AbstraDex']`
- Beam Swap ($1.05M) — declared org: `['Merit-Circle']`
