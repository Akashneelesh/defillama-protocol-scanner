# Verified Open-Source DeFi Protocols

**Snapshot:** 2026-11-07
**Sources:** `https://api.llama.fi/protocols` + GitHub REST API `/users/{org}/repos`

## Verdict Summary

- **VERIFIED** — org has at least one contract-bearing repo: **149**
- **NO_CONTRACT_REPO** — org exists but only frontend/SDK/docs detected: **57**
- **ORG_404** — declared github org returns 404: **3**

## Classification heuristic

A repo is flagged as a contract repo if any of:
- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}
- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)
- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract
- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`

**Caveats:** GitHub's auto-detected primary language only; multi-language monorepos may be misclassified. Forks & archived repos are skipped. Manual spot-check is still recommended before forking or integrating with a protocol.

---

## VERIFIED — 149 protocols

| # | Protocol | TVL | Category | Chains | GitHub | Contract Repo(s) |
|---|---|---|---|---|---|---|
| 1 | **Easedefi.org** | $4.94M | Insurance | Ethereum | [EaseDeFi](https://github.com/EaseDeFi) | [arNFT](https://github.com/EaseDeFi/arNFT) `Solidity` ★7<br>[arNXMV2](https://github.com/EaseDeFi/arNXMV2) `Solidity` ★0<br>[arShield](https://github.com/EaseDeFi/arShield) `Solidity` ★0 +2 more |
| 2 | **Hakka Finance** | $4.93M | Derivatives | Ethereum, Binance | [hakkafinance](https://github.com/hakkafinance) | [hakka](https://github.com/hakkafinance/hakka) `Solidity` ★2<br>[blackholeswap](https://github.com/hakkafinance/blackholeswap) `Solidity` ★11<br>[BugBounty](https://github.com/hakkafinance/BugBounty) `Solidity` ★1 |
| 3 | **Pickle** | $4.62M | Yield Aggregator | Ethereum, Polygon, Optimism +9 | [pickle-finance](https://github.com/pickle-finance) | [protocol](https://github.com/pickle-finance/protocol) `Solidity` ★127<br>[contracts](https://github.com/pickle-finance/contracts) `` ★153<br>[saviour-scripts](https://github.com/pickle-finance/saviour-scripts) `Solidity` ★7 +2 more |
| 4 | **Troves** | $4.40M | Yield | Starknet | [trovesfi](https://github.com/trovesfi) | [ekubo-cl-vaults](https://github.com/trovesfi/ekubo-cl-vaults) `Cairo` ★0<br>[vesu-strategies](https://github.com/trovesfi/vesu-strategies) `Cairo` ★0 |
| 5 | **Stakingverse** | $4.34M | Liquid Staking | Ethereum, LUKSO | [Stakingverse](https://github.com/Stakingverse) | [pool-contracts](https://github.com/Stakingverse/pool-contracts) `Solidity` ★2 |
| 6 | **Stafi** | $4.27M | Liquid Staking | Ethereum, Solana, Binance +2 | [stafiprotocol](https://github.com/stafiprotocol) | [svm-staking-contracts](https://github.com/stafiprotocol/svm-staking-contracts) `Rust` ★1<br>[neutron-lsd-contracts](https://github.com/stafiprotocol/neutron-lsd-contracts) `Rust` ★0<br>[svm-lsd-contracts](https://github.com/stafiprotocol/svm-lsd-contracts) `Rust` ★0 +2 more |
| 7 | **Stride** | $3.85M | Liquid Staking | Cosmos, HAQQ, Celestia +14 | [Stride-Labs](https://github.com/Stride-Labs) | [hub-evm-fees](https://github.com/Stride-Labs/hub-evm-fees) `Solidity` ★0<br>[st-scaling-factor](https://github.com/Stride-Labs/st-scaling-factor) `Rust` ★0<br>[ica-oracle](https://github.com/Stride-Labs/ica-oracle) `Rust` ★0 |
| 8 | **xExchange** | $3.71M | Dexs | Elrond | [multiversx](https://github.com/multiversx) | [mx-contracts-rs](https://github.com/multiversx/mx-contracts-rs) `Rust` ★12<br>[mx-chain-core-go](https://github.com/multiversx/mx-chain-core-go) `Go` ★12<br>[mx-sdk-js-core](https://github.com/multiversx/mx-sdk-js-core) `TypeScript` ★73 |
| 9 | **Bunny** | $3.66M | Yield | Binance, Polygon | [PancakeBunny-finance](https://github.com/PancakeBunny-finance) | [qubit-finance](https://github.com/PancakeBunny-finance/qubit-finance) `Solidity` ★31<br>[Bunny](https://github.com/PancakeBunny-finance/Bunny) `Solidity` ★176<br>[PolygonBUNNY](https://github.com/PancakeBunny-finance/PolygonBUNNY) `Solidity` ★4 +1 more |
| 10 | **Hop Protocol** | $3.49M | Cross Chain Bridge | Ethereum, Optimism, Arbitrum +4 | [hop-protocol](https://github.com/hop-protocol) | [contracts](https://github.com/hop-protocol/contracts) `TypeScript` ★232<br>[messenger](https://github.com/hop-protocol/messenger) `Solidity` ★1<br>[rails](https://github.com/hop-protocol/rails) `Solidity` ★1 +1 more |
| 11 | **Umia** | $3.48M | Launchpad | Base | [umiafinance](https://github.com/umiafinance) | [attestor-core](https://github.com/umiafinance/attestor-core) `TypeScript` ★1<br>[protocol](https://github.com/umiafinance/protocol) `Solidity` ★7 |
| 12 | **AlphaX** | $3.35M | Derivatives | Binance, Ethereum, Arbitrum +1 | [AlphaX-Protocol](https://github.com/AlphaX-Protocol) | [AlphaX-Protocol-Contract-Tron](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract-Tron) `JavaScript` ★1<br>[AlphaX-Protocol-Contract](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract) `JavaScript` ★0 |
| 13 | **OroSwap** | $3.24M | Dexs | ZIGChain | [oroswap](https://github.com/oroswap) | [oroswap-core](https://github.com/oroswap/oroswap-core) `Rust` ★0<br>[oro-evm](https://github.com/oroswap/oro-evm) `Solidity` ★0 |
| 14 | **iAero Protocol** | $2.97M | Liquid Staking | Base | [iaeroProtocol](https://github.com/iaeroProtocol) | [ContractEventsBots](https://github.com/iaeroProtocol/ContractEventsBots) `JavaScript` ★0<br>[PerpBond](https://github.com/iaeroProtocol/PerpBond) `Solidity` ★0 |
| 15 | **Reflect Tranches** | $2.87M | Yield | Solana | [palindrome-eng](https://github.com/palindrome-eng) | [contract-interfaces](https://github.com/palindrome-eng/contract-interfaces) `` ★0 |
| 16 | **Monolith Market** | $2.74M | CDP | Ethereum | [MonolithMarket](https://github.com/MonolithMarket) | [GovernanceFactory](https://github.com/MonolithMarket/GovernanceFactory) `Solidity` ★0<br>[Monolith](https://github.com/MonolithMarket/Monolith) `Solidity` ★1 |
| 17 | **Gamma** | $2.74M | Liquidity Manager | Ethereum, Binance, Polygon +33 | [GammaStrategies](https://github.com/GammaStrategies) | [gamma-univ4-limit-order-hook](https://github.com/GammaStrategies/gamma-univ4-limit-order-hook) `Solidity` ★5<br>[GammaV2](https://github.com/GammaStrategies/GammaV2) `Solidity` ★0<br>[eulerswap-delta-neutral-strategy](https://github.com/GammaStrategies/eulerswap-delta-neutral-strategy) `Solidity` ★3 +1 more |
| 18 | **Bio Protocol** | $2.73M | Launchpad | Ethereum, Base | [bio-xyz](https://github.com/bio-xyz) | [vesting-contracts](https://github.com/bio-xyz/vesting-contracts) `Solidity` ★2<br>[token-contracts](https://github.com/bio-xyz/token-contracts) `Solidity` ★1<br>[cerebrumdao-token](https://github.com/bio-xyz/cerebrumdao-token) `Solidity` ★0 +2 more |
| 19 | **Astroport** | $2.67M | Dexs | Terra2, Injective, Osmosis +2 | [astroport-fi](https://github.com/astroport-fi) | [astroport-core](https://github.com/astroport-fi/astroport-core) `Rust` ★168<br>[astro-generator-proxy-contracts](https://github.com/astroport-fi/astro-generator-proxy-contracts) `Rust` ★4<br>[astroport-on-osmosis](https://github.com/astroport-fi/astroport-on-osmosis) `Rust` ★0 |
| 20 | **Bitflow** | $2.66M | Dexs | Stacks | [BitflowFinance](https://github.com/BitflowFinance) | [bitflow-dlmm](https://github.com/BitflowFinance/bitflow-dlmm) `Clarity` ★0<br>[bitflow](https://github.com/BitflowFinance/bitflow) `Clarity` ★4 |
| 21 | **Wildcat Protocol** | $2.65M | Uncollateralized Lending | Ethereum, Plasma | [wildcat-finance](https://github.com/wildcat-finance) | [v2-protocol](https://github.com/wildcat-finance/v2-protocol) `Solidity` ★5<br>[collateral-contract](https://github.com/wildcat-finance/collateral-contract) `Solidity` ★1<br>[credit-default-swaps](https://github.com/wildcat-finance/credit-default-swaps) `Solidity` ★0 +2 more |
| 22 | **40 Acres** | $2.47M | Lending | Avalanche, Base, Optimism | [40-Acres](https://github.com/40-Acres) | [ace](https://github.com/40-Acres/ace) `Solidity` ★0<br>[loan-contracts](https://github.com/40-Acres/loan-contracts) `Solidity` ★1 |
| 23 | **Lisk Bridge** | $2.45M | Canonical Bridge | Ethereum | [LiskHQ](https://github.com/LiskHQ) | [lisk-contracts](https://github.com/LiskHQ/lisk-contracts) `Solidity` ★17 |
| 24 | **Ostium** | $2.43M | Derivatives | Arbitrum | [0xOstium](https://github.com/0xOstium) | [smart-contracts-public](https://github.com/0xOstium/smart-contracts-public) `Solidity` ★14 |
| 25 | **Kinza Finance** | $2.41M | Lending | Binance, Op_Bnb, Ethereum +1 | [Kinza-Finance](https://github.com/Kinza-Finance) | [omnichain-kBTC](https://github.com/Kinza-Finance/omnichain-kBTC) `Solidity` ★2<br>[KZA-1.0](https://github.com/Kinza-Finance/KZA-1.0) `Solidity` ★4<br>[kbBTC](https://github.com/Kinza-Finance/kbBTC) `Solidity` ★0 |
| 26 | **Reflexer** | $2.35M | CDP | Ethereum | [reflexer-labs](https://github.com/reflexer-labs) | [geb-keeper-flash-proxy](https://github.com/reflexer-labs/geb-keeper-flash-proxy) `Solidity` ★4<br>[geb-darkfix](https://github.com/reflexer-labs/geb-darkfix) `Solidity` ★1<br>[merkle-distributor](https://github.com/reflexer-labs/merkle-distributor) `Solidity` ★7 +2 more |
| 27 | **Yala** | $2.20M | CDP | Bitcoin, Ethereum | [yalaorg](https://github.com/yalaorg) | [yala-protocol-contracts](https://github.com/yalaorg/yala-protocol-contracts) `Solidity` ★13 |
| 28 | **Ledgity Yield** | $2.13M | Yield | Base, Linea, Arbitrum +2 | [LedgityLabs](https://github.com/LedgityLabs) | [ledgity-v2-contracts](https://github.com/LedgityLabs/ledgity-v2-contracts) `Solidity` ★2<br>[LDY-token](https://github.com/LedgityLabs/LDY-token) `Solidity` ★3 |
| 29 | **QiDao** | $2.11M | CDP | Polygon, Base, Ethereum +11 | [0xlaozi](https://github.com/0xlaozi) | [qidao](https://github.com/0xlaozi/qidao) `Solidity` ★73 |
| 30 | **Goldfinch** | $2.07M | Uncollateralized Lending | Ethereum | [goldfinch-eng](https://github.com/goldfinch-eng) | [mono](https://github.com/goldfinch-eng/mono) `Solidity` ★65<br>[goldfinch-contracts](https://github.com/goldfinch-eng/goldfinch-contracts) `Solidity` ★58 |
| 31 | **LlamaPay** | $2.06M | Payments | Binance, Arbitrum, Ethereum +19 | [LlamaPay](https://github.com/LlamaPay) | [llamapay-v2](https://github.com/LlamaPay/llamapay-v2) `Solidity` ★40<br>[llamapay](https://github.com/LlamaPay/llamapay) `Solidity` ★188<br>[subscription-contracts](https://github.com/LlamaPay/subscription-contracts) `TypeScript` ★4 +2 more |
| 32 | **Flex** | $1.96M | Lending | Ethereum | [flexmeow](https://github.com/flexmeow) | [flex-allocator](https://github.com/flexmeow/flex-allocator) `Solidity` ★0<br>[flex-contracts](https://github.com/flexmeow/flex-contracts) `Solidity` ★5<br>[dutch-taker-contracts](https://github.com/flexmeow/dutch-taker-contracts) `Vyper` ★0 |
| 33 | **OmniBTC** | $1.87M | Lending | Sui, Arbitrum, Base +5 | [OmniBTC](https://github.com/OmniBTC) | [OmniBridge](https://github.com/OmniBTC/OmniBridge) `Move` ★35<br>[Sui-AMM-swap](https://github.com/OmniBTC/Sui-AMM-swap) `Move` ★88<br>[Aptos-AMM-swap](https://github.com/OmniBTC/Aptos-AMM-swap) `Move` ★30 +2 more |
| 34 | **Trisolaris** | $1.87M | Dexs | Aurora | [trisolaris-labs](https://github.com/trisolaris-labs) | [trisolaris_core](https://github.com/trisolaris-labs/trisolaris_core) `TypeScript` ★20 |
| 35 | **NFTX** | $1.86M | NFT Marketplace | Ethereum, Arbitrum | [NFTX-project](https://github.com/NFTX-project) | [nftx-protocol-v3](https://github.com/NFTX-project/nftx-protocol-v3) `Solidity` ★21<br>[nftx-protocol-v2.1](https://github.com/NFTX-project/nftx-protocol-v2.1) `Solidity` ★1<br>[x-contracts](https://github.com/NFTX-project/x-contracts) `Solidity` ★32 +2 more |
| 36 | **DaVinciGraph** | $1.85M | Token Locker | Hedera | [DaVinciGraph](https://github.com/DaVinciGraph) | [DaVinciGraph-Token-Vesting-V2](https://github.com/DaVinciGraph/DaVinciGraph-Token-Vesting-V2) `Solidity` ★0<br>[DaVinciGraph-NFT-Locker-V2](https://github.com/DaVinciGraph/DaVinciGraph-NFT-Locker-V2) `Solidity` ★0<br>[DaVinciGraph-Black-Hole-V2](https://github.com/DaVinciGraph/DaVinciGraph-Black-Hole-V2) `Solidity` ★0 +2 more |
| 37 | **Ambient** | $1.80M | Dexs | Scroll, Ethereum, Plume Mainnet +4 | [CrocSwap](https://github.com/CrocSwap) | [CrocSwap-protocol](https://github.com/CrocSwap/CrocSwap-protocol) `TypeScript` ★79<br>[crocswap-router-compat](https://github.com/CrocSwap/crocswap-router-compat) `Solidity` ★0 |
| 38 | **Trueo** | $1.75M | Prediction Market | Base | [trueo-protocol](https://github.com/trueo-protocol) | [trueo-contracts](https://github.com/trueo-protocol/trueo-contracts) `Solidity` ★17 |
| 39 | **Magma** | $1.75M | Dexs | Sui | [MagmaFinanceIO](https://github.com/MagmaFinanceIO) | [magma_core_caps_interface](https://github.com/MagmaFinanceIO/magma_core_caps_interface) `Move` ★0<br>[magma_core_clmm_interface](https://github.com/MagmaFinanceIO/magma_core_clmm_interface) `Move` ★0<br>[magma-core-public](https://github.com/MagmaFinanceIO/magma-core-public) `Move` ★0 +2 more |
| 40 | **deBridge** | $1.74M | Bridge | Ethereum, Binance, Arbitrum +3 | [debridge-finance](https://github.com/debridge-finance) | [debridge-contracts-v1](https://github.com/debridge-finance/debridge-contracts-v1) `JavaScript` ★59<br>[hardhat-debridge](https://github.com/debridge-finance/hardhat-debridge) `TypeScript` ★23<br>[denft](https://github.com/debridge-finance/denft) `Solidity` ★19 +2 more |
| 41 | **HiYield** | $1.73M | RWA | Avalanche, Canto | [lydialabs](https://github.com/lydialabs) | [waifu-token-hackathon](https://github.com/lydialabs/waifu-token-hackathon) `Solidity` ★0 |
| 42 | **INIT Capital** | $1.69M | Lending | Mantle, Blast | [init-capital](https://github.com/init-capital) | [init-capital-contracts](https://github.com/init-capital/init-capital-contracts) `Solidity` ★0<br>[init-core-public](https://github.com/init-capital/init-core-public) `` ★0 |
| 43 | **Swappi** | $1.62M | Dexs | Conflux | [swappidex](https://github.com/swappidex) | [swappi-periphery](https://github.com/swappidex/swappi-periphery) `Solidity` ★7<br>[swappi-farm](https://github.com/swappidex/swappi-farm) `Solidity` ★3<br>[swappi-core](https://github.com/swappidex/swappi-core) `TypeScript` ★5 |
| 44 | **Angle** | $1.61M | CDP | Ethereum, Arbitrum, Polygon +5 | [AngleProtocol](https://github.com/AngleProtocol) | [merkl-contracts](https://github.com/AngleProtocol/merkl-contracts) `Solidity` ★87<br>[angle-multisig](https://github.com/AngleProtocol/angle-multisig) `Solidity` ★2<br>[borrow-contracts](https://github.com/AngleProtocol/borrow-contracts) `TypeScript` ★39 +2 more |
| 45 | **LandX Finance** | $1.56M | RWA | Ethereum | [LandXit](https://github.com/LandXit) | [land-x-smart-contracts](https://github.com/LandXit/land-x-smart-contracts) `JavaScript` ★8 |
| 46 | **KaoyaSwap** | $1.52M | Dexs | Binance | [kaoya1125](https://github.com/kaoya1125) | [contracts](https://github.com/kaoya1125/contracts) `Solidity` ★0 |
| 47 | **Yamato Protocol** | $1.51M | CDP | Ethereum | [DeFiGeek-Community](https://github.com/DeFiGeek-Community) | [yamato](https://github.com/DeFiGeek-Community/yamato) `Solidity` ★4<br>[yamato-commodities](https://github.com/DeFiGeek-Community/yamato-commodities) `Solidity` ★0<br>[ve-factory](https://github.com/DeFiGeek-Community/ve-factory) `Solidity` ★1 |
| 48 | **Privacy Boost** | $1.50M | Privacy | Base, Optimism, Soneium | [sunnyside-io](https://github.com/sunnyside-io) | [privacy-boost-protocol](https://github.com/sunnyside-io/privacy-boost-protocol) `Solidity` ★15 |
| 49 | **Twyne** | $1.47M | Lending | Ethereum | [0xTwyne](https://github.com/0xTwyne) | [twyne-contracts-v1](https://github.com/0xTwyne/twyne-contracts-v1) `Solidity` ★10<br>[aave-v3-aToken-wrapper](https://github.com/0xTwyne/aave-v3-aToken-wrapper) `Solidity` ★0<br>[twyne-shield](https://github.com/0xTwyne/twyne-shield) `Solidity` ★0 +2 more |
| 50 | **Hubble** | $1.44M | CDP | Solana | [hubbleprotocol](https://github.com/hubbleprotocol) | [solana-setup-action](https://github.com/hubbleprotocol/solana-setup-action) `Rust` ★1<br>[anchor-bpf-template](https://github.com/hubbleprotocol/anchor-bpf-template) `Rust` ★1 |
| 51 | **Travessia Credit** | $1.43M | RWA | Ethereum, Avalanche, Polygon +2 | [RedVeil](https://github.com/RedVeil) | [Travessia-Commodity-Tracking](https://github.com/RedVeil/Travessia-Commodity-Tracking) `Solidity` ★0<br>[FixedForexUSDC](https://github.com/RedVeil/FixedForexUSDC) `Solidity` ★0<br>[YieldForge](https://github.com/RedVeil/YieldForge) `Solidity` ★0 +2 more |
| 52 | **CityCoins** | $1.40M | Yield | Stacks | [citycoins](https://github.com/citycoins) | [protocol](https://github.com/citycoins/protocol) `Clarity` ★7<br>[protocol-api](https://github.com/citycoins/protocol-api) `TypeScript` ★1 |
| 53 | **Augur** | $1.37M | Prediction Market | Ethereum | [AugurProject](https://github.com/AugurProject) | [augur-core](https://github.com/AugurProject/augur-core) `TypeScript` ★588<br>[Lituus-CS](https://github.com/AugurProject/Lituus-CS) `Solidity` ★0<br>[oracle-research](https://github.com/AugurProject/oracle-research) `Solidity` ★6 |
| 54 | **MDEX** | $1.36M | Dexs | Binance, Bittorrent, Heco | [mdexSwap](https://github.com/mdexSwap) | [contracts](https://github.com/mdexSwap/contracts) `Solidity` ★135 |
| 55 | **Overtime** | $1.26M | Prediction Market | Arbitrum, Base, Optimism +3 | [thales-markets](https://github.com/thales-markets) | [solana-contracts](https://github.com/thales-markets/solana-contracts) `JavaScript` ★0 |
| 56 | **Mitosis** | $1.26M | Onchain Capital Allocator | Binance, Linea, Arbitrum +9 | [mitosis-org](https://github.com/mitosis-org) | [protocol](https://github.com/mitosis-org/protocol) `Solidity` ★17<br>[dn404x](https://github.com/mitosis-org/dn404x) `Solidity` ★3<br>[protocol-dapp-template](https://github.com/mitosis-org/protocol-dapp-template) `Solidity` ★1 +1 more |
| 57 | **SOFA.org** | $1.25M | Options | Ethereum, Arbitrum, Binance +1 | [sofa-org](https://github.com/sofa-org) | [sofa-protocol](https://github.com/sofa-org/sofa-protocol) `TypeScript` ★10 |
| 58 | **Cyclone** | $1.23M | Yield | Ethereum, Binance, IoTeX +1 | [cycloneprotocol](https://github.com/cycloneprotocol) | [cyclone-contracts](https://github.com/cycloneprotocol/cyclone-contracts) `Solidity` ★65 |
| 59 | **Butter Network** | $1.19M | Cross Chain Bridge | Ethereum, Tron, Binance +12 | [butternetwork](https://github.com/butternetwork) | [wdk-protocol-swidge-butter](https://github.com/butternetwork/wdk-protocol-swidge-butter) `TypeScript` ★0<br>[butter-router-contracts](https://github.com/butternetwork/butter-router-contracts) `JavaScript` ★8<br>[butter-core-near](https://github.com/butternetwork/butter-core-near) `Rust` ★1 +2 more |
| 60 | **SHUI** | $1.15M | Liquid Staking | Conflux | [Shui-LST](https://github.com/Shui-LST) | [shui-lsd-core](https://github.com/Shui-LST/shui-lsd-core) `Solidity` ★1 |
| 61 | **Kromatika** | $1.13M | Dexs | Optimism, Ethereum, Arbitrum +1 | [Kromatika-Finance](https://github.com/Kromatika-Finance) | [MetaSwap](https://github.com/Kromatika-Finance/MetaSwap) `Solidity` ★0 |
| 62 | **OpenBook** | $1.11M | Dexs | Solana | [openbook-dex](https://github.com/openbook-dex) | [openbook-v2](https://github.com/openbook-dex/openbook-v2) `Rust` ★261<br>[program](https://github.com/openbook-dex/program) `Rust` ★211 |
| 63 | **Hyperion** | $1.10M | Dexs | Aptos | [Hyperionxyz](https://github.com/Hyperionxyz) | [pyth-dep](https://github.com/Hyperionxyz/pyth-dep) `Move` ★0<br>[dex-multiagent-example](https://github.com/Hyperionxyz/dex-multiagent-example) `Move` ★0<br>[hyperion-interface](https://github.com/Hyperionxyz/hyperion-interface) `Move` ★9 |
| 64 | **DefiChain DEX** | $1.09M | Dexs | DefiChain | [DeFiCh](https://github.com/DeFiCh) | [dfi-core](https://github.com/DeFiCh/dfi-core) `` ★0<br>[dfi-erc20](https://github.com/DeFiCh/dfi-erc20) `Solidity` ★0 |
| 65 | **Wombat Exchange** | $1.04M | Dexs | Binance, Arbitrum, Avalanche +7 | [wombat-exchange](https://github.com/wombat-exchange) | [v1-core](https://github.com/wombat-exchange/v1-core) `Solidity` ★18 |
| 66 | **King Protocol** | $1.03M | Liquid Restaking | Ethereum | [King-Protocol](https://github.com/King-Protocol) | [king-cross-chain](https://github.com/King-Protocol/king-cross-chain) `Solidity` ★1<br>[king-vaults](https://github.com/King-Protocol/king-vaults) `Solidity` ★0 |
| 67 | **CHATEAU** | $1.02M | RWA | Plasma | [chateau-capital](https://github.com/chateau-capital) | [ca](https://github.com/chateau-capital/ca) `Solidity` ★1 |
| 68 | **RealtyX** | $1.02M | RWA | Base, Plume Mainnet | [HomuraAcc](https://github.com/HomuraAcc) | [The-Realtyx-Smart-Contracts](https://github.com/HomuraAcc/The-Realtyx-Smart-Contracts) `Solidity` ★3 |
| 69 | **ALEX** | $1.01M | Dexs | Stacks | [alexgo-io](https://github.com/alexgo-io) | [alex-v1](https://github.com/alexgo-io/alex-v1) `Clarity` ★41<br>[ord-bitcoincore-rpc](https://github.com/alexgo-io/ord-bitcoincore-rpc) `Rust` ★0<br>[alex-orderbook-public](https://github.com/alexgo-io/alex-orderbook-public) `Clarity` ★0 +2 more |
| 70 | **Mendi Finance** | $1.01M | Lending | Linea | [mendi-finance](https://github.com/mendi-finance) | [lending-protocol](https://github.com/mendi-finance/lending-protocol) `Solidity` ★5<br>[staking-protocol](https://github.com/mendi-finance/staking-protocol) `TypeScript` ★3 |
| 71 | **ForgeYields** | $986k | Onchain Capital Allocator | Starknet, Ethereum | [ForgeYields](https://github.com/ForgeYields) | [starknet_vault_kit](https://github.com/ForgeYields/starknet_vault_kit) `Cairo` ★12 |
| 72 | **WingRiders** | $981k | Dexs | Cardano | [WingRiders](https://github.com/WingRiders) | [launchpad-contracts](https://github.com/WingRiders/launchpad-contracts) `Haskell` ★0<br>[rapid-dex-contracts](https://github.com/WingRiders/rapid-dex-contracts) `Aiken` ★0<br>[dex-v2-contracts](https://github.com/WingRiders/dex-v2-contracts) `Haskell` ★1 +2 more |
| 73 | **Isle Finance** | $954k | RWA | Hedera | [isle-labs](https://github.com/isle-labs) | [isle-enterprise-contract](https://github.com/isle-labs/isle-enterprise-contract) `Solidity` ★5 |
| 74 | **ParyonUSD** | $945k | CDP | Bitcoincash | [ParyonUSD](https://github.com/ParyonUSD) | [contracts](https://github.com/ParyonUSD/contracts) `TypeScript` ★11<br>[verify_contract_deployment](https://github.com/ParyonUSD/verify_contract_deployment) `TypeScript` ★0 |
| 75 | **Rari Capital** | $922k | Yield Aggregator | Ethereum, Arbitrum | [Rari-Capital](https://github.com/Rari-Capital) | [nova-interfaces](https://github.com/Rari-Capital/nova-interfaces) `Solidity` ★10<br>[nova-invariants](https://github.com/Rari-Capital/nova-invariants) `Solidity` ★6<br>[fuse-v1](https://github.com/Rari-Capital/fuse-v1) `Solidity` ★2 +2 more |
| 76 | **WanSwap Dex** | $895k | Dexs | Wanchain | [wanswap](https://github.com/wanswap) | [wasp-assist](https://github.com/wanswap/wasp-assist) `Solidity` ★1<br>[funny-auction-contracts](https://github.com/wanswap/funny-auction-contracts) `JavaScript` ★1<br>[wanswap-hive-contracts](https://github.com/wanswap/wanswap-hive-contracts) `Solidity` ★1 |
| 77 | **CANA Holdings California Carbon Credits** | $894k | RWA | Ethereum | [maseer-finance](https://github.com/maseer-finance) | [maseer-one](https://github.com/maseer-finance/maseer-one) `Solidity` ★0<br>[maseer-oracles](https://github.com/maseer-finance/maseer-oracles) `Solidity` ★0<br>[maseer-vest](https://github.com/maseer-finance/maseer-vest) `Solidity` ★0 |
| 78 | **Kai Finance** | $849k | Leveraged Farming | Sui | [kunalabs-io](https://github.com/kunalabs-io) | [sui-smart-contracts](https://github.com/kunalabs-io/sui-smart-contracts) `Move` ★86 |
| 79 | **Lets Get HAI** | $844k | CDP | Optimism | [hai-on-op](https://github.com/hai-on-op) | [core](https://github.com/hai-on-op/core) `Solidity` ★40<br>[altar-of-rai-contracts](https://github.com/hai-on-op/altar-of-rai-contracts) `Solidity` ★0<br>[governance](https://github.com/hai-on-op/governance) `Solidity` ★0 |
| 80 | **VETRO** | $843k | CDP | Ethereum | [vetro-protocol](https://github.com/vetro-protocol) | [vetro-contracts](https://github.com/vetro-protocol/vetro-contracts) `Solidity` ★1 |
| 81 | **BlazeSwap** | $840k | Dexs | Flare, Songbird | [blazeswap](https://github.com/blazeswap) | [contracts](https://github.com/blazeswap/contracts) `TypeScript` ★6 |
| 82 | **KEEP Network** | $830k | Cross Chain Bridge | Ethereum | [keep-network](https://github.com/keep-network) | [hardhat-helpers](https://github.com/keep-network/hardhat-helpers) `TypeScript` ★3<br>[contracts-migrate-action](https://github.com/keep-network/contracts-migrate-action) `` ★0 |
| 83 | **B.Protocol** | $828k | Liquidations | Ethereum, Arbitrum, Polygon +1 | [backstop-protocol](https://github.com/backstop-protocol) | [ERC-7770](https://github.com/backstop-protocol/ERC-7770) `Solidity` ★0<br>[smart-ltv](https://github.com/backstop-protocol/smart-ltv) `Solidity` ★0<br>[B.Protocol-data](https://github.com/backstop-protocol/B.Protocol-data) `TypeScript` ★0 +2 more |
| 84 | **Teller** | $805k | Lending | Base, Ethereum, Arbitrum +6 | [teller-protocol](https://github.com/teller-protocol) | [teller-protocol-v2](https://github.com/teller-protocol/teller-protocol-v2) `Rust` ★17<br>[teller-protocol-v1](https://github.com/teller-protocol/teller-protocol-v1) `Solidity` ★106<br>[teller-tx-debug-suite](https://github.com/teller-protocol/teller-tx-debug-suite) `Solidity` ★0 +2 more |
| 85 | **Ellipsis Finance** | $802k | Dexs | Binance | [ellipsis-finance](https://github.com/ellipsis-finance) | [ellipsis-v2](https://github.com/ellipsis-finance/ellipsis-v2) `Solidity` ★13 |
| 86 | **Hemi Bridge** | $800k | Canonical Bridge | Ethereum | [hemilabs](https://github.com/hemilabs) | [fpmm](https://github.com/hemilabs/fpmm) `Solidity` ★1<br>[veHEMI](https://github.com/hemilabs/veHEMI) `Solidity` ★0<br>[hemi-token](https://github.com/hemilabs/hemi-token) `Solidity` ★0 +2 more |
| 87 | **10KSwap** | $716k | Dexs | Starknet | [10k-swap](https://github.com/10k-swap) | [10k_swap-contracts](https://github.com/10k-swap/10k_swap-contracts) `Cairo` ★58 |
| 88 | **Dinosaur Eggs** | $715k | Dexs | Binance | [Dinosaur-eggs](https://github.com/Dinosaur-eggs) | [core](https://github.com/Dinosaur-eggs/core) `Solidity` ★24 |
| 89 | **Suzaku** | $704k | Restaking | Avalanche | [suzaku-network](https://github.com/suzaku-network) | [suzaku-core](https://github.com/suzaku-network/suzaku-core) `Solidity` ★1<br>[suzaku-contracts-library](https://github.com/suzaku-network/suzaku-contracts-library) `Solidity` ★8<br>[suzaku-deployer](https://github.com/suzaku-network/suzaku-deployer) `Solidity` ★0 |
| 90 | **Honeyswap** | $691k | Dexs | xDai, Polygon | [1Hive](https://github.com/1Hive) | [fluid-proposals](https://github.com/1Hive/fluid-proposals) `Solidity` ★0<br>[honeyswap-limit-order-contracts](https://github.com/1Hive/honeyswap-limit-order-contracts) `Solidity` ★3<br>[deployments-aragon-os](https://github.com/1Hive/deployments-aragon-os) `TypeScript` ★0 |
| 91 | **TermMax** | $686k | Lending | Ethereum, Berachain, Binance +6 | [term-structure](https://github.com/term-structure) | [termmax-contract-v2](https://github.com/term-structure/termmax-contract-v2) `Solidity` ★9<br>[termmax-contract](https://github.com/term-structure/termmax-contract) `Solidity` ★4<br>[TS-smart-contract](https://github.com/term-structure/TS-smart-contract) `TypeScript` ★2 |
| 92 | **Kaskad** | $665k | Lending | Robinhood Chain, Igra | [Kaskad-Lending](https://github.com/Kaskad-Lending) | [kaskad-nuntius-contracts](https://github.com/Kaskad-Lending/kaskad-nuntius-contracts) `Solidity` ★1<br>[kaskad-pontifex](https://github.com/Kaskad-Lending/kaskad-pontifex) `Solidity` ★0<br>[kaskad-contracts](https://github.com/Kaskad-Lending/kaskad-contracts) `Solidity` ★0 |
| 93 | **WePiggy** | $658k | Lending | Ethereum, Optimism, Arbitrum +9 | [WePiggy](https://github.com/WePiggy) | [wepiggy-contracts](https://github.com/WePiggy/wepiggy-contracts) `Solidity` ★20<br>[contract_addresses](https://github.com/WePiggy/contract_addresses) `` ★0<br>[wepiggy-contracts-optimism](https://github.com/WePiggy/wepiggy-contracts-optimism) `Solidity` ★0 +1 more |
| 94 | **Meson** | $656k | Cross Chain Bridge | Ethereum, Merlin, BSquared +41 | [MesonFi](https://github.com/MesonFi) | [merlin-contracts](https://github.com/MesonFi/merlin-contracts) `Solidity` ★0 |
| 95 | **Aurigami** | $631k | Lending | Aurora | [Aurigami-Finance](https://github.com/Aurigami-Finance) | [aurigami-smart-contracts](https://github.com/Aurigami-Finance/aurigami-smart-contracts) `Solidity` ★0 |
| 96 | **Trevee Earn** | $601k | Yield Aggregator | Sonic, Ethereum, Plasma | [Rings-Protocol](https://github.com/Rings-Protocol) | [rings-contracts](https://github.com/Rings-Protocol/rings-contracts) `Solidity` ★1<br>[rings-wrapper](https://github.com/Rings-Protocol/rings-wrapper) `Solidity` ★0 |
| 97 | **BearnFi** | $596k | Yield | Binance | [bearn-defi](https://github.com/bearn-defi) | [bearn-smartcontracts](https://github.com/bearn-defi/bearn-smartcontracts) `Solidity` ★6<br>[bdex-smartcontracts](https://github.com/bearn-defi/bdex-smartcontracts) `TypeScript` ★0<br>[bvaults-smartcontracts](https://github.com/bearn-defi/bvaults-smartcontracts) `Solidity` ★0 |
| 98 | **Toucan Protocol** | $545k | RWA | Polygon, Celo, Base +1 | [ToucanProtocol](https://github.com/ToucanProtocol) | [contracts](https://github.com/ToucanProtocol/contracts) `Solidity` ★57<br>[dynamic-fee-pools](https://github.com/ToucanProtocol/dynamic-fee-pools) `Solidity` ★2 |
| 99 | **VaultCraft** | $544k | Yield | Arbitrum, Ethereum, Polygon +4 | [Popcorn-Limited](https://github.com/Popcorn-Limited) | [gauges](https://github.com/Popcorn-Limited/gauges) `Solidity` ★0<br>[audit-04-24](https://github.com/Popcorn-Limited/audit-04-24) `Solidity` ★0<br>[xvcx-bridges](https://github.com/Popcorn-Limited/xvcx-bridges) `Solidity` ★0 +2 more |
| 100 | **ImmutableX** | $544k | NFT Marketplace | Ethereum | [immutable](https://github.com/immutable) | [imx-migration-contracts](https://github.com/immutable/imx-migration-contracts) `Solidity` ★2<br>[contracts](https://github.com/immutable/contracts) `Solidity` ★46<br>[zkevm-bridge-contracts](https://github.com/immutable/zkevm-bridge-contracts) `Solidity` ★18 +1 more |
| 101 | **Bounce.Tech** | $540k | Derivatives | Hyperliquid L1 | [bounce-tech](https://github.com/bounce-tech) | [bounce-smart-contracts](https://github.com/bounce-tech/bounce-smart-contracts) `Solidity` ★3 |
| 102 | **PsyOptions** | $538k | Options | Solana | [mithraiclabs](https://github.com/mithraiclabs) | [psyoracleutils](https://github.com/mithraiclabs/psyoracleutils) `Rust` ★2<br>[pyth-min](https://github.com/mithraiclabs/pyth-min) `Rust` ★0<br>[psy-macros](https://github.com/mithraiclabs/psy-macros) `Rust` ★1 |
| 103 | **Zunami Protocol** | $534k | Yield Aggregator | Ethereum | [ZunamiProtocol](https://github.com/ZunamiProtocol) | [ZunamiProtocolV2](https://github.com/ZunamiProtocol/ZunamiProtocolV2) `TypeScript` ★1 |
| 104 | **DIEM Relay** | $531k | Liquid Staking | Base | [Figu3](https://github.com/Figu3) | [clear-morpho-adapter](https://github.com/Figu3/clear-morpho-adapter) `Solidity` ★0<br>[diem-relay](https://github.com/Figu3/diem-relay) `Solidity` ★0<br>[sonic-earn-recovery-system](https://github.com/Figu3/sonic-earn-recovery-system) `Solidity` ★0 +2 more |
| 105 | **yAxis** | $521k | Yield Aggregator | Ethereum | [yaxis-project](https://github.com/yaxis-project) | [yaxis-audit](https://github.com/yaxis-project/yaxis-audit) `Solidity` ★6<br>[metavault](https://github.com/yaxis-project/metavault) `Solidity` ★32 |
| 106 | **MooniSwap** | $510k | Dexs | Ethereum | [1inch](https://github.com/1inch) | [swap-vm](https://github.com/1inch/swap-vm) `Solidity` ★46<br>[aqua](https://github.com/1inch/aqua) `Solidity` ★119<br>[limit-order-protocol](https://github.com/1inch/limit-order-protocol) `JavaScript` ★314 +2 more |
| 107 | **JPEG'd** | $507k | NFT Lending | Ethereum | [jpegd](https://github.com/jpegd) | [core](https://github.com/jpegd/core) `Solidity` ★12 |
| 108 | **PinkSwap** | $499k | Dexs | Binance | [pinkmoonfinance](https://github.com/pinkmoonfinance) | [pink-antibot-guide](https://github.com/pinkmoonfinance/pink-antibot-guide) `Solidity` ★52<br>[pinksale-contracts](https://github.com/pinkmoonfinance/pinksale-contracts) `Solidity` ★44 |
| 109 | **RadioShack** | $487k | Dexs | Binance, Avalanche, Polygon +5 | [radioshackswap](https://github.com/radioshackswap) | [contracts](https://github.com/radioshackswap/contracts) `Solidity` ★2 |
| 110 | **Cover Protocol** | $481k | Insurance | Ethereum | [CoverProtocol](https://github.com/CoverProtocol) | [cover-token-mining](https://github.com/CoverProtocol/cover-token-mining) `Solidity` ★8<br>[cover-core-v1](https://github.com/CoverProtocol/cover-core-v1) `Solidity` ★19<br>[cover-rewards](https://github.com/CoverProtocol/cover-rewards) `Solidity` ★1 +1 more |
| 111 | **Tarot** | $476k | Lending | Base, Optimism, Fantom +10 | [tarot-finance](https://github.com/tarot-finance) | [tarot-core](https://github.com/tarot-finance/tarot-core) `JavaScript` ★17<br>[tarot-price-oracle](https://github.com/tarot-finance/tarot-price-oracle) `Solidity` ★8<br>[tarot-periphery](https://github.com/tarot-finance/tarot-periphery) `Solidity` ★9 +2 more |
| 112 | **Sherpa** | $470k | Onchain Capital Allocator | Ethereum, Base, Monad | [hedgemonyxyz](https://github.com/hedgemonyxyz) | [sherpa-vault-smartcontracts-v1.0](https://github.com/hedgemonyxyz/sherpa-vault-smartcontracts-v1.0) `Solidity` ★1 |
| 113 | **Ante Finance** | $459k | Insurance | Ethereum, Binance, Avalanche +5 | [antefinance](https://github.com/antefinance) | [ante-v05-core](https://github.com/antefinance/ante-v05-core) `TypeScript` ★6<br>[ante-community-tests](https://github.com/antefinance/ante-community-tests) `Solidity` ★35<br>[ante-v06-core](https://github.com/antefinance/ante-v06-core) `TypeScript` ★1 |
| 114 | **YFII** | $459k | Yield Aggregator | Ethereum | [yfii](https://github.com/yfii) | [yvault](https://github.com/yfii/yvault) `Solidity` ★60<br>[yficontract](https://github.com/yfii/yficontract) `JavaScript` ★16 |
| 115 | **Nolus Protocol** | $458k | Lending | Solana, Nolus, Neutron +1 | [nolus-protocol](https://github.com/nolus-protocol) | [nolus-core](https://github.com/nolus-protocol/nolus-core) `Go` ★62 |
| 116 | **Siren** | $451k | Options | Ethereum, Polygon, Arbitrum | [sirenmarkets](https://github.com/sirenmarkets) | [core](https://github.com/sirenmarkets/core) `TypeScript` ★41 |
| 117 | **EZManager** | $446k | Liquidity Manager | Base, Robinhood Chain, Hyperliquid L1 +3 | [EZManagerCL](https://github.com/EZManagerCL) | [EZManagerContracts](https://github.com/EZManagerCL/EZManagerContracts) `Solidity` ★0 |
| 118 | **Unicly** | $445k | Dexs | Ethereum | [uniclyNFT](https://github.com/uniclyNFT) | [unicly-core](https://github.com/uniclyNFT/unicly-core) `Solidity` ★9 |
| 119 | **Geode** | $440k | Liquid Staking | Avalanche | [Geodefi](https://github.com/Geodefi) | [Portal-Eth](https://github.com/Geodefi/Portal-Eth) `Solidity` ★3 |
| 120 | **Forest Road Vault** | $436k | RWA | Ethereum | [Forest-Road-Company](https://github.com/Forest-Road-Company) | [forest-road-vault](https://github.com/Forest-Road-Company/forest-road-vault) `Solidity` ★6 |
| 121 | **Perpetual Protocol** | $432k | Derivatives | Ethereum, Optimism | [perpetual-protocol](https://github.com/perpetual-protocol) | [lugia-contract](https://github.com/perpetual-protocol/lugia-contract) `Solidity` ★1<br>[perp-curie-contract](https://github.com/perpetual-protocol/perp-curie-contract) `TypeScript` ★87<br>[perpetual-protocol](https://github.com/perpetual-protocol/perpetual-protocol) `TypeScript` ★167 +2 more |
| 122 | **SingularityDAO** | $423k | Yield | Ethereum, Binance | [Singularity-DAO](https://github.com/Singularity-DAO) | [hypercycle-token-contracts](https://github.com/Singularity-DAO/hypercycle-token-contracts) `JavaScript` ★0<br>[migration-contracts](https://github.com/Singularity-DAO/migration-contracts) `TypeScript` ★3<br>[sdao-token-contracts](https://github.com/Singularity-DAO/sdao-token-contracts) `Solidity` ★9 +2 more |
| 123 | **Compound Blue** | $410k | Lending | Polygon | [papercliplabs](https://github.com/papercliplabs) | [nouns-town](https://github.com/papercliplabs/nouns-town) `Solidity` ★1 |
| 124 | **Flipcash** | $404k | Launchpad | Solana | [code-payments](https://github.com/code-payments) | [flipcash-shared-core-spm](https://github.com/code-payments/flipcash-shared-core-spm) `Swift` ★0<br>[flipcash2-client-protocol](https://github.com/code-payments/flipcash2-client-protocol) `Swift` ★0<br>[ocp-client-protocol](https://github.com/code-payments/ocp-client-protocol) `Swift` ★0 +1 more |
| 125 | **Narwhalswap** | $403k | Dexs | Binance | [narwhalswap](https://github.com/narwhalswap) | [thegrandbanks](https://github.com/narwhalswap/thegrandbanks) `Solidity` ★1<br>[contracts](https://github.com/narwhalswap/contracts) `Solidity` ★0<br>[nar-token](https://github.com/narwhalswap/nar-token) `Solidity` ★0 |
| 126 | **88mph** | $402k | Lending | Ethereum, Fantom, Avalanche +1 | [88mphapp](https://github.com/88mphapp) | [88mph-contracts](https://github.com/88mphapp/88mph-contracts) `Solidity` ★84<br>[88mph-gauge](https://github.com/88mphapp/88mph-gauge) `Vyper` ★0<br>[Phantasm](https://github.com/88mphapp/Phantasm) `Solidity` ★0 +1 more |
| 127 | **FortiFi** | $397k | Yield Aggregator | Avalanche | [0xFortiFi](https://github.com/0xFortiFi) | [Moat-Contracts](https://github.com/0xFortiFi/Moat-Contracts) `Solidity` ★0<br>[FortiFi-Foundry](https://github.com/0xFortiFi/FortiFi-Foundry) `Solidity` ★0<br>[FortiFi-Vaults](https://github.com/0xFortiFi/FortiFi-Vaults) `Solidity` ★1 |
| 128 | **Nami** | $387k | Dexs | Base, Ethereum, Robinhood Chain | [namifi](https://github.com/namifi) | [Nami-Protocol](https://github.com/namifi/Nami-Protocol) `Solidity` ★0 |
| 129 | **Swop** | $381k | Dexs | Waves, UNIT0 | [swopfi](https://github.com/swopfi) | [swopfi-smart-contracts](https://github.com/swopfi/swopfi-smart-contracts) `` ★11 |
| 130 | **Dfyn Network** | $370k | Dexs | Polygon, Fantom, OKExChain | [dfyn](https://github.com/dfyn) | [dfyn-exchange](https://github.com/dfyn/dfyn-exchange) `Solidity` ★21<br>[dfyn-token](https://github.com/dfyn/dfyn-token) `Solidity` ★7<br>[dual-farm](https://github.com/dfyn/dual-farm) `Solidity` ★1 +2 more |
| 131 | **BOB Fusion** | $366k | Farm | Ethereum | [bob-collective](https://github.com/bob-collective) | [wdk-protocol-swidge-gateway](https://github.com/bob-collective/wdk-protocol-swidge-gateway) `TypeScript` ★0<br>[bitcoin-spv](https://github.com/bob-collective/bitcoin-spv) `Solidity` ★5<br>[unite-defi-hackathon](https://github.com/bob-collective/unite-defi-hackathon) `Solidity` ★0 |
| 132 | **Scientix** | $366k | Synthetics | Binance | [ScientixFinance](https://github.com/ScientixFinance) | [scientix-contract](https://github.com/ScientixFinance/scientix-contract) `Solidity` ★3 |
| 133 | **HashKing** | $365k | Liquid Staking | Filecoin | [NodeDAO](https://github.com/NodeDAO) | [obelisk-network](https://github.com/NodeDAO/obelisk-network) `Solidity` ★0<br>[HashKing-FIL](https://github.com/NodeDAO/HashKing-FIL) `Solidity` ★1<br>[NodeDAO-Protocol](https://github.com/NodeDAO/NodeDAO-Protocol) `Solidity` ★2 +2 more |
| 134 | **Breadchain** | $360k | CDP | xDai | [BreadchainCoop](https://github.com/BreadchainCoop) | [etherform-playground](https://github.com/BreadchainCoop/etherform-playground) `Solidity` ★0<br>[saving-circles](https://github.com/BreadchainCoop/saving-circles) `Solidity` ★3<br>[avs-ecdsa-sol-sdk](https://github.com/BreadchainCoop/avs-ecdsa-sol-sdk) `Solidity` ★0 +2 more |
| 135 | **AggreLend** | $360k | Yield Aggregator | Solana | [AggreLend](https://github.com/AggreLend) | [kamino-finance-cpi-integration](https://github.com/AggreLend/kamino-finance-cpi-integration) `Rust` ★4<br>[drift-cpi-integration](https://github.com/AggreLend/drift-cpi-integration) `Rust` ★3<br>[marginfi-integration](https://github.com/AggreLend/marginfi-integration) `Rust` ★3 +1 more |
| 136 | **PieDAO** | $350k | Indexes | Ethereum | [pie-dao](https://github.com/pie-dao) | [pie-flash-loans-poc](https://github.com/pie-dao/pie-flash-loans-poc) `Solidity` ★9<br>[pie-oven](https://github.com/pie-dao/pie-oven) `Solidity` ★12<br>[auxo-vaults](https://github.com/pie-dao/auxo-vaults) `Solidity` ★16 +2 more |
| 137 | **Clarity** | $343k | DAO Service Provider | Cardano | [ClearContracts](https://github.com/ClearContracts) | [clearcontracts.github.io](https://github.com/ClearContracts/clearcontracts.github.io) `HTML` ★0<br>[clarity-clb](https://github.com/ClearContracts/clarity-clb) `Haskell` ★0 |
| 138 | **Goose Finance** | $336k | Farm | Binance | [goosedefi](https://github.com/goosedefi) | [goose-contracts-incubator](https://github.com/goosedefi/goose-contracts-incubator) `Solidity` ★9<br>[goose-contracts](https://github.com/goosedefi/goose-contracts) `Solidity` ★61 |
| 139 | **Definix** | $335k | Dexs | Binance, Klaytn | [thesixnetwork](https://github.com/thesixnetwork) | [six-protocol](https://github.com/thesixnetwork/six-protocol) `Go` ★1<br>[multicall3](https://github.com/thesixnetwork/multicall3) `Solidity` ★0<br>[cross-dev-contract](https://github.com/thesixnetwork/cross-dev-contract) `Solidity` ★0 +2 more |
| 140 | **BoringDAO** | $334k | Cross Chain Bridge | Litecoin, Polygon, Doge +17 | [BoringDAO](https://github.com/BoringDAO) | [boringDAO-contract](https://github.com/BoringDAO/boringDAO-contract) `Solidity` ★13<br>[smart-bridge-contract](https://github.com/BoringDAO/smart-bridge-contract) `TypeScript` ★2 |
| 141 | **Ponder Finance** | $332k | Dexs | Bitkub | [ponderfinance](https://github.com/ponderfinance) | [protocol](https://github.com/ponderfinance/protocol) `Solidity` ★1<br>[usdp](https://github.com/ponderfinance/usdp) `Solidity` ★0 |
| 142 | **Deriverse** | $331k | Dexs | Solana | [deriverse](https://github.com/deriverse) | [drv-smart-contract-common](https://github.com/deriverse/drv-smart-contract-common) `Rust` ★0 |
| 143 | **Sigmausd** | $331k | Algo-Stables | Ergo | [anon-real](https://github.com/anon-real) | [contract-testing](https://github.com/anon-real/contract-testing) `Scala` ★6 |
| 144 | **Moor** | $326k | CDP | Fuel | [Rig-Labs](https://github.com/Rig-Labs) | [smart-contracts](https://github.com/Rig-Labs/smart-contracts) `Sway` ★0 |
| 145 | **Opus** | $325k | CDP | Starknet | [lindy-labs](https://github.com/lindy-labs) | [opus_contracts](https://github.com/lindy-labs/opus_contracts) `Cairo` ★0<br>[opus_compose](https://github.com/lindy-labs/opus_compose) `Cairo` ★0<br>[wadray](https://github.com/lindy-labs/wadray) `Cairo` ★21 +2 more |
| 146 | **BabelFish** | $316k | Bridge | RSK | [BabelFishProtocol](https://github.com/BabelFishProtocol) | [governance-sc](https://github.com/BabelFishProtocol/governance-sc) `Solidity` ★0 |
| 147 | **Atrium** | $314k | Farm | Cardano | [atma-community](https://github.com/atma-community) | [staking-baskets](https://github.com/atma-community/staking-baskets) `Haskell` ★4 |
| 148 | **Sprinter** | $311k | Yield | Base | [sprintertech](https://github.com/sprintertech) | [sprinter-stash-contracts](https://github.com/sprintertech/sprinter-stash-contracts) `TypeScript` ★1<br>[deploy-safersafes](https://github.com/sprintertech/deploy-safersafes) `Solidity` ★0 |
| 149 | **Swerve** | $305k | Dexs | Ethereum | [SwerveFinance](https://github.com/SwerveFinance) | [SwerveContracts](https://github.com/SwerveFinance/SwerveContracts) `` ★39 |

---

## NO_CONTRACT_REPO — 57 protocols

These protocols declare a public github org but no contract-bearing repo was detected by the heuristic. Worth manual review before assuming closed-source.

| # | Protocol | TVL | Category | Chains | GitHub |
|---|---|---|---|---|---|
| 1 | Arkis | $4.86M | Lending | Ethereum, Hyperliquid L1 | [ArkisXYZ](https://github.com/ArkisXYZ) |
| 2 | Saber | $4.62M | Dexs | Solana | [saberdao](https://github.com/saberdao) |
| 3 | Presto | $4.35M | Risk Curators | Ethereum | [prestolabs](https://github.com/prestolabs) |
| 4 | Mole | $4.31M | Yield | Sui, Aptos | [Mole-Fi](https://github.com/Mole-Fi) |
| 5 | Blueshift | $4.25M | Dexs | BOB, Kava, Polygon +2 | [blueshift-fi](https://github.com/blueshift-fi) |
| 6 | Splashing Stake | $4.20M | Liquid Staking | Sei | [SplashingStaking](https://github.com/SplashingStaking) |
| 7 | Bumpin Trade | $4.11M | Derivatives | Solana | [bumpin-exchange](https://github.com/bumpin-exchange) |
| 8 | Liquidium | $4.08M | Lending | ICP | [Liquidium-Inc](https://github.com/Liquidium-Inc) |
| 9 | Nawa Protocol | $4.04M | RWA | ZIGChain, Ethereum, CORE | [NawaTeam](https://github.com/NawaTeam) |
| 10 | ICPSwap | $3.34M | Dexs | ICP | [ICPSwap-Labs](https://github.com/ICPSwap-Labs) |
| 11 | Indigo | $3.12M | CDP | Cardano | [IndigoProtocol](https://github.com/IndigoProtocol) |
| 12 | Surf Lending | $2.84M | Lending | Cardano | [flow-lending](https://github.com/flow-lending) |
| 13 | Cabal | $2.66M | Governance Incentives | Initia, Strat, Cabal | [0xCabal](https://github.com/0xCabal) |
| 14 | International Stable Currency | $2.44M | RWA | Solana | [TheISCTeam](https://github.com/TheISCTeam) |
| 15 | FluidTokens | $2.27M | Lending | Cardano | [FluidTokens](https://github.com/FluidTokens) |
| 16 | Baseline Protocol | $1.62M | Liquidity Manager | Ethereum, Base, Blast | [0xBaseline](https://github.com/0xBaseline) |
| 17 | Surge Credit | $1.61M | Lending | Bitcoin, Base | [surgecredit](https://github.com/surgecredit) |
| 18 | Tradecraft | $1.60M | Dexs | Canton | [tradecraft-fi](https://github.com/tradecraft-fi) |
| 19 | PiggyBank | $1.43M | Yield | Solana | [zsociety-io](https://github.com/zsociety-io) |
| 20 | Coffer Network | $1.42M | Bridge | Bitcoin | [coffer-network](https://github.com/coffer-network) |
| 21 | Mountain Protocol | $1.40M | RWA | Ethereum, zkSync Era, Arbitrum +3 | [mountainprotocol](https://github.com/mountainprotocol) |
| 22 | Permapod | $1.38M | Lending | ZIGChain | [permapod](https://github.com/permapod) |
| 23 | Liquidity House | $1.36M | Prediction Market | Etherlink | [liquidityhouse](https://github.com/liquidityhouse) |
| 24 | Decentralized Euro | $1.10M | CDP | Ethereum | [d-EURO](https://github.com/d-EURO) |
| 25 | Flexa | $1.09M | Payments | Ethereum | [flexahq](https://github.com/flexahq) |
| 26 | Laine SOL | $1.07M | Liquid Staking | Solana | [laine-sa](https://github.com/laine-sa) |
| 27 | Moola Market | $1.06M | Lending | Celo | [moolamarket](https://github.com/moolamarket) |
| 28 | Pools Finance | $1.03M | Dexs | IOTA | [Pools-Finance](https://github.com/Pools-Finance) |
| 29 | Scopuly | $956k | Dexs | Stellar | [Scopuly](https://github.com/Scopuly) |
| 30 | Saddle Finance | $906k | Dexs | Ethereum, Arbitrum, Optimism +4 | [saddle-finance](https://github.com/saddle-finance) |
| 31 | Reactor DEX | $906k | Dexs | Fuel | [Reactor-Fuel](https://github.com/Reactor-Fuel) |
| 32 | Pact | $862k | Dexs | Algorand | [pactfi](https://github.com/pactfi) |
| 33 | Bastion | $825k | Lending | Aurora | [bastionprotocol](https://github.com/bastionprotocol) |
| 34 | Ashswap | $823k | Dexs | Elrond | [ashswap](https://github.com/ashswap) |
| 35 | Pondo Protocol | $798k | Liquid Staking | Aleo | [ProvableHQ](https://github.com/ProvableHQ) |
| 36 | xToken | $769k | Liquidity Manager | Ethereum, Optimism, Arbitrum +1 | [xtokenmarket](https://github.com/xtokenmarket) |
| 37 | Swaylend | $763k | Lending | Fuel | [swaylend](https://github.com/swaylend) |
| 38 | Clipper | $754k | Dexs | Ethereum, Base, Optimism +5 | [shipyard-software](https://github.com/shipyard-software) |
| 39 | InkySwap | $745k | Dexs | Ink | [InkySwap](https://github.com/InkySwap) |
| 40 | tramplin.io | $669k | Staking Pool | Solana | [tramplin-io](https://github.com/tramplin-io) |
| 41 | Kublerx | $663k | Dexs | Bitkub | [kublerxofficial](https://github.com/kublerxofficial) |
| 42 | Landshare | $621k | RWA | Binance | [ls-jordan](https://github.com/ls-jordan) |
| 43 | AirPuff | $615k | Leveraged Farming | Ethereum, Arbitrum, Mode +3 | [Airpuff](https://github.com/Airpuff) |
| 44 | Archer Exchange | $578k | Dexs | Solana | [SquareRoot-Labs](https://github.com/SquareRoot-Labs) |
| 45 | Allstake | $571k | Restaking | Near, Ethereum, Solana | [allstake](https://github.com/allstake) |
| 46 | Rise.rich | $564k | Launchpad | Solana | [riserich](https://github.com/riserich) |
| 47 | Stella | $531k | Leveraged Farming | Arbitrum | [stellaxyz](https://github.com/stellaxyz) |
| 48 | Turtle Club | $512k | Onchain Capital Allocator | Ethereum, Avalanche, Linea | [Turtle-DAO](https://github.com/Turtle-DAO) |
| 49 | Ryze Protocol | $483k | Dexs | Base | [ryze-protocol](https://github.com/ryze-protocol) |
| 50 | DefiBox | $462k | Dexs | EOS, Binance, Wax | [DefiboxTeam](https://github.com/DefiboxTeam) |
| 51 | SHPRD | $386k | Indexes | Arbitrum, Ethereum | [stealth-defi](https://github.com/stealth-defi) |
| 52 | Beradrome | $384k | Yield | Berachain | [BeraLabs](https://github.com/BeraLabs) |
| 53 | Mobius Money | $336k | Dexs | Celo | [mobiusAMM](https://github.com/mobiusAMM) |
| 54 | ICDex | $322k | Dexs | ICP | [iclighthouse](https://github.com/iclighthouse) |
| 55 | xSigma | $317k | Dexs | Ethereum | [xSigmaLabs](https://github.com/xSigmaLabs) |
| 56 | OolongSwap | $307k | Dexs | Boba | [OolongSwap](https://github.com/OolongSwap) |
| 57 | TRUE DEX | $302k | Derivatives | Solana | [True-AI-Labs](https://github.com/True-AI-Labs) |

---

## ORG_404 — 3 protocols

- Goldsand by InshAllah ($313k) — declared org: `['inshallah-network']`
- AbstraDEX ($366k) — declared org: `['AbstraDex']`
- Beam Swap ($1.46M) — declared org: `['Merit-Circle']`
