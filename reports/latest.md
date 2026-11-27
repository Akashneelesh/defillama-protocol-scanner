# Verified Open-Source DeFi Protocols

**Snapshot:** 2026-11-27
**Sources:** `https://api.llama.fi/protocols` + GitHub REST API `/users/{org}/repos`

## Verdict Summary

- **VERIFIED** — org has at least one contract-bearing repo: **137**
- **NO_CONTRACT_REPO** — org exists but only frontend/SDK/docs detected: **57**
- **ORG_404** — declared github org returns 404: **1**

## Classification heuristic

A repo is flagged as a contract repo if any of:
- Primary language ∈ {Solidity, Vyper, Move, Cairo, Huff, FunC, Tact, Sway, Clarity, Plutus, Haskell}
- Primary language = Rust **and** name/description contains a chain keyword (cosmwasm, anchor, near, solana, terra, injective, sei, osmosis)
- Primary language = TypeScript **and** name/description mentions hardhat, foundry, or smart-contract
- Repo name contains `contracts`, `protocol`, `core`, `hardhat`, `foundry`, `cosmwasm`, or `anchor`

**Caveats:** GitHub's auto-detected primary language only; multi-language monorepos may be misclassified. Forks & archived repos are skipped. Manual spot-check is still recommended before forking or integrating with a protocol.

---

## VERIFIED — 137 protocols

| # | Protocol | TVL | Category | Chains | GitHub | Contract Repo(s) |
|---|---|---|---|---|---|---|
| 1 | **Harmonix Finance** | $4.55M | Yield | Hyperliquid L1, Arbitrum, Ethereum +1 | [harmonixfi](https://github.com/harmonixfi) | [core-smart-contract](https://github.com/harmonixfi/core-smart-contract) `TypeScript` ★0 |
| 2 | **Superfluid** | $4.55M | Payments | Base, Ethereum, Polygon +7 | [superfluid-finance](https://github.com/superfluid-finance) | [averagex-contracts-cloned](https://github.com/superfluid-finance/averagex-contracts-cloned) `Solidity` ★7<br>[torex-basic-liquidity-mover](https://github.com/superfluid-finance/torex-basic-liquidity-mover) `Solidity` ★3 |
| 3 | **Quarry** | $4.53M | Yield | Solana | [QuarryProtocol](https://github.com/QuarryProtocol) | [carrara](https://github.com/QuarryProtocol/carrara) `Move` ★3 |
| 4 | **ICHI** | $4.42M | Liquidity Manager | Hedera, Base, Ethereum +24 | [ichifarm](https://github.com/ichifarm) | [ichi-farming](https://github.com/ichifarm/ichi-farming) `Solidity` ★7<br>[ichi-governance](https://github.com/ichifarm/ichi-governance) `Solidity` ★4<br>[ichi](https://github.com/ichifarm/ichi) `Solidity` ★3 +1 more |
| 5 | **Tinyman** | $4.23M | Dexs | Algorand | [tinymanorg](https://github.com/tinymanorg) | [tinyman-amm-contracts-v2](https://github.com/tinymanorg/tinyman-amm-contracts-v2) `Python` ★25<br>[tinyman-periphery-contracts-v2](https://github.com/tinymanorg/tinyman-periphery-contracts-v2) `Python` ★1<br>[tinyman-order-protocol](https://github.com/tinymanorg/tinyman-order-protocol) `Python` ★2 +1 more |
| 6 | **Easedefi.org** | $4.19M | Insurance | Ethereum | [EaseDeFi](https://github.com/EaseDeFi) | [arNFT](https://github.com/EaseDeFi/arNFT) `Solidity` ★7<br>[arNXMV2](https://github.com/EaseDeFi/arNXMV2) `Solidity` ★0<br>[arShield](https://github.com/EaseDeFi/arShield) `Solidity` ★0 +2 more |
| 7 | **Pickle** | $4.12M | Yield Aggregator | Ethereum, Polygon, Optimism +9 | [pickle-finance](https://github.com/pickle-finance) | [protocol](https://github.com/pickle-finance/protocol) `Solidity` ★127<br>[contracts](https://github.com/pickle-finance/contracts) `` ★153<br>[saviour-scripts](https://github.com/pickle-finance/saviour-scripts) `Solidity` ★7 +2 more |
| 8 | **Neverland** | $4.05M | Lending | Monad | [Neverland-Money](https://github.com/Neverland-Money) | [neverland-tokenomics](https://github.com/Neverland-Money/neverland-tokenomics) `Solidity` ★0<br>[neverland-wrapped-tokens](https://github.com/Neverland-Money/neverland-wrapped-tokens) `Solidity` ★1 |
| 9 | **Stakingverse** | $3.97M | Liquid Staking | Ethereum, LUKSO | [Stakingverse](https://github.com/Stakingverse) | [pool-contracts](https://github.com/Stakingverse/pool-contracts) `Solidity` ★2 |
| 10 | **Hakka Finance** | $3.79M | Derivatives | Ethereum, Binance | [hakkafinance](https://github.com/hakkafinance) | [hakka](https://github.com/hakkafinance/hakka) `Solidity` ★2<br>[blackholeswap](https://github.com/hakkafinance/blackholeswap) `Solidity` ★11<br>[BugBounty](https://github.com/hakkafinance/BugBounty) `Solidity` ★1 |
| 11 | **AlphaX** | $3.65M | Derivatives | Binance, Ethereum, Tron +1 | [AlphaX-Protocol](https://github.com/AlphaX-Protocol) | [AlphaX-Protocol-Contract-Tron](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract-Tron) `JavaScript` ★1<br>[AlphaX-Protocol-Contract](https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract) `JavaScript` ★0 |
| 12 | **Troves** | $3.61M | Yield | Starknet | [trovesfi](https://github.com/trovesfi) | [ekubo-cl-vaults](https://github.com/trovesfi/ekubo-cl-vaults) `Cairo` ★0<br>[vesu-strategies](https://github.com/trovesfi/vesu-strategies) `Cairo` ★0 |
| 13 | **CLever** | $3.30M | Yield | Ethereum | [AladdinDAO](https://github.com/AladdinDAO) | [aladdin-v3-contracts](https://github.com/AladdinDAO/aladdin-v3-contracts) `TypeScript` ★61<br>[aladdin-v2-contracts](https://github.com/AladdinDAO/aladdin-v2-contracts) `Solidity` ★4<br>[fx-protocol-contracts](https://github.com/AladdinDAO/fx-protocol-contracts) `Solidity` ★18 +2 more |
| 14 | **Stafi** | $3.29M | Liquid Staking | Ethereum, Solana, Binance +2 | [stafiprotocol](https://github.com/stafiprotocol) | [svm-staking-contracts](https://github.com/stafiprotocol/svm-staking-contracts) `Rust` ★1<br>[neutron-lsd-contracts](https://github.com/stafiprotocol/neutron-lsd-contracts) `Rust` ★0<br>[svm-lsd-contracts](https://github.com/stafiprotocol/svm-lsd-contracts) `Rust` ★0 +2 more |
| 15 | **Bunny** | $3.13M | Yield | Binance, Polygon | [PancakeBunny-finance](https://github.com/PancakeBunny-finance) | [qubit-finance](https://github.com/PancakeBunny-finance/qubit-finance) `Solidity` ★31<br>[Bunny](https://github.com/PancakeBunny-finance/Bunny) `Solidity` ★176<br>[PolygonBUNNY](https://github.com/PancakeBunny-finance/PolygonBUNNY) `Solidity` ★4 +1 more |
| 16 | **xExchange** | $3.04M | Dexs | Elrond | [multiversx](https://github.com/multiversx) | [mx-chain-core-go](https://github.com/multiversx/mx-chain-core-go) `Go` ★11<br>[mx-contracts-rs](https://github.com/multiversx/mx-contracts-rs) `Rust` ★12<br>[mx-sdk-js-core](https://github.com/multiversx/mx-sdk-js-core) `TypeScript` ★73 |
| 17 | **Hop Protocol** | $3.00M | Cross Chain Bridge | Ethereum, Optimism, Arbitrum +4 | [hop-protocol](https://github.com/hop-protocol) | [contracts](https://github.com/hop-protocol/contracts) `TypeScript` ★232<br>[messenger](https://github.com/hop-protocol/messenger) `Solidity` ★1<br>[rails](https://github.com/hop-protocol/rails) `Solidity` ★1 +1 more |
| 18 | **Reflect Tranches** | $3.00M | Yield | Solana | [palindrome-eng](https://github.com/palindrome-eng) | [contract-interfaces](https://github.com/palindrome-eng/contract-interfaces) `` ★0 |
| 19 | **Bitflow** | $2.52M | Dexs | Stacks | [BitflowFinance](https://github.com/BitflowFinance) | [bitflow-dlmm](https://github.com/BitflowFinance/bitflow-dlmm) `Clarity` ★0<br>[bitflow](https://github.com/BitflowFinance/bitflow) `Clarity` ★4 |
| 20 | **OroSwap** | $2.46M | Dexs | ZIGChain | [oroswap](https://github.com/oroswap) | [oroswap-core](https://github.com/oroswap/oroswap-core) `Rust` ★0<br>[oro-evm](https://github.com/oroswap/oro-evm) `Solidity` ★0 |
| 21 | **Gamma** | $2.33M | Liquidity Manager | Ethereum, Binance, Polygon +33 | [GammaStrategies](https://github.com/GammaStrategies) | [gamma-univ4-limit-order-hook](https://github.com/GammaStrategies/gamma-univ4-limit-order-hook) `Solidity` ★5<br>[GammaV2](https://github.com/GammaStrategies/GammaV2) `Solidity` ★0<br>[eulerswap-delta-neutral-strategy](https://github.com/GammaStrategies/eulerswap-delta-neutral-strategy) `Solidity` ★3 +1 more |
| 22 | **Bio Protocol** | $2.16M | Launchpad | Ethereum, Base | [bio-xyz](https://github.com/bio-xyz) | [vesting-contracts](https://github.com/bio-xyz/vesting-contracts) `Solidity` ★2<br>[token-contracts](https://github.com/bio-xyz/token-contracts) `Solidity` ★1<br>[cerebrumdao-token](https://github.com/bio-xyz/cerebrumdao-token) `Solidity` ★0 +2 more |
| 23 | **Astroport** | $2.15M | Dexs | Terra2, Injective, Osmosis +2 | [astroport-fi](https://github.com/astroport-fi) | [astroport-core](https://github.com/astroport-fi/astroport-core) `Rust` ★168<br>[astro-generator-proxy-contracts](https://github.com/astroport-fi/astro-generator-proxy-contracts) `Rust` ★4<br>[astroport-on-osmosis](https://github.com/astroport-fi/astroport-on-osmosis) `Rust` ★0 |
| 24 | **LlamaPay** | $2.12M | Payments | Binance, Arbitrum, Ethereum +19 | [LlamaPay](https://github.com/LlamaPay) | [llamapay](https://github.com/LlamaPay/llamapay) `Solidity` ★187<br>[llamapay-v2](https://github.com/LlamaPay/llamapay-v2) `Solidity` ★40<br>[subscription-contracts](https://github.com/LlamaPay/subscription-contracts) `TypeScript` ★4 +2 more |
| 25 | **Flex** | $2.06M | Lending | Ethereum | [flexmeow](https://github.com/flexmeow) | [flex-allocator](https://github.com/flexmeow/flex-allocator) `Solidity` ★0<br>[flex-contracts](https://github.com/flexmeow/flex-contracts) `Solidity` ★5<br>[dutch-taker-contracts](https://github.com/flexmeow/dutch-taker-contracts) `Vyper` ★0 |
| 26 | **Ledgity Yield** | $2.02M | Yield | Base, Linea, Arbitrum +2 | [LedgityLabs](https://github.com/LedgityLabs) | [ledgity-v2-contracts](https://github.com/LedgityLabs/ledgity-v2-contracts) `Solidity` ★2<br>[LDY-token](https://github.com/LedgityLabs/LDY-token) `Solidity` ★3 |
| 27 | **iAero Protocol** | $2.01M | Liquid Staking | Base | [iaeroProtocol](https://github.com/iaeroProtocol) | [ContractEventsBots](https://github.com/iaeroProtocol/ContractEventsBots) `JavaScript` ★0<br>[PerpBond](https://github.com/iaeroProtocol/PerpBond) `Solidity` ★0 |
| 28 | **Goldfinch** | $2.00M | Uncollateralized Lending | Ethereum | [goldfinch-eng](https://github.com/goldfinch-eng) | [mono](https://github.com/goldfinch-eng/mono) `Solidity` ★65<br>[goldfinch-contracts](https://github.com/goldfinch-eng/goldfinch-contracts) `Solidity` ★58 |
| 29 | **Kinza Finance** | $1.91M | Lending | Binance, Op_Bnb, Ethereum +1 | [Kinza-Finance](https://github.com/Kinza-Finance) | [omnichain-kBTC](https://github.com/Kinza-Finance/omnichain-kBTC) `Solidity` ★2<br>[KZA-1.0](https://github.com/Kinza-Finance/KZA-1.0) `Solidity` ★4<br>[kbBTC](https://github.com/Kinza-Finance/kbBTC) `Solidity` ★0 |
| 30 | **Reflexer** | $1.81M | CDP | Ethereum | [reflexer-labs](https://github.com/reflexer-labs) | [geb-keeper-flash-proxy](https://github.com/reflexer-labs/geb-keeper-flash-proxy) `Solidity` ★4<br>[geb-darkfix](https://github.com/reflexer-labs/geb-darkfix) `Solidity` ★1<br>[merkle-distributor](https://github.com/reflexer-labs/merkle-distributor) `Solidity` ★7 +2 more |
| 31 | **QiDao** | $1.80M | CDP | Polygon, Base, Ethereum +11 | [0xlaozi](https://github.com/0xlaozi) | [qidao](https://github.com/0xlaozi/qidao) `Solidity` ★73 |
| 32 | **Ostium** | $1.79M | Derivatives | Arbitrum | [0xOstium](https://github.com/0xOstium) | [smart-contracts-public](https://github.com/0xOstium/smart-contracts-public) `Solidity` ★14 |
| 33 | **Yala** | $1.78M | CDP | Bitcoin, Ethereum | [yalaorg](https://github.com/yalaorg) | [yala-protocol-contracts](https://github.com/yalaorg/yala-protocol-contracts) `Solidity` ★13 |
| 34 | **Trueo** | $1.74M | Prediction Market | Base | [trueo-protocol](https://github.com/trueo-protocol) | [trueo-contracts](https://github.com/trueo-protocol/trueo-contracts) `Solidity` ★17 |
| 35 | **HiYield** | $1.73M | RWA | Avalanche, Canto | [lydialabs](https://github.com/lydialabs) | [waifu-token-hackathon](https://github.com/lydialabs/waifu-token-hackathon) `Solidity` ★0 |
| 36 | **OmniBTC** | $1.70M | Lending | Sui, Base, Arbitrum +5 | [OmniBTC](https://github.com/OmniBTC) | [OmniBridge](https://github.com/OmniBTC/OmniBridge) `Move` ★35<br>[Sui-AMM-swap](https://github.com/OmniBTC/Sui-AMM-swap) `Move` ★88<br>[Aptos-AMM-swap](https://github.com/OmniBTC/Aptos-AMM-swap) `Move` ★30 +2 more |
| 37 | **Trisolaris** | $1.62M | Dexs | Aurora | [trisolaris-labs](https://github.com/trisolaris-labs) | [trisolaris_core](https://github.com/trisolaris-labs/trisolaris_core) `TypeScript` ★20 |
| 38 | **Magma** | $1.60M | Dexs | Sui | [MagmaFinanceIO](https://github.com/MagmaFinanceIO) | [magma_core_caps_interface](https://github.com/MagmaFinanceIO/magma_core_caps_interface) `Move` ★0<br>[magma_core_clmm_interface](https://github.com/MagmaFinanceIO/magma_core_clmm_interface) `Move` ★0<br>[magma-core-public](https://github.com/MagmaFinanceIO/magma-core-public) `Move` ★0 +2 more |
| 39 | **Umia** | $1.58M | Launchpad | Base | [umiafinance](https://github.com/umiafinance) | [attestor-core](https://github.com/umiafinance/attestor-core) `TypeScript` ★1<br>[protocol](https://github.com/umiafinance/protocol) `Solidity` ★7 |
| 40 | **LandX Finance** | $1.58M | RWA | Ethereum | [LandXit](https://github.com/LandXit) | [land-x-smart-contracts](https://github.com/LandXit/land-x-smart-contracts) `JavaScript` ★8 |
| 41 | **INIT Capital** | $1.57M | Lending | Mantle, Blast | [init-capital](https://github.com/init-capital) | [init-capital-contracts](https://github.com/init-capital/init-capital-contracts) `Solidity` ★0<br>[init-core-public](https://github.com/init-capital/init-core-public) `` ★0 |
| 42 | **Angle** | $1.53M | CDP | Ethereum, Arbitrum, Polygon +5 | [AngleProtocol](https://github.com/AngleProtocol) | [merkl-contracts](https://github.com/AngleProtocol/merkl-contracts) `Solidity` ★90<br>[angle-multisig](https://github.com/AngleProtocol/angle-multisig) `Solidity` ★2<br>[borrow-contracts](https://github.com/AngleProtocol/borrow-contracts) `TypeScript` ★39 +2 more |
| 43 | **Ambient** | $1.47M | Dexs | Scroll, Ethereum, Plume Mainnet +4 | [CrocSwap](https://github.com/CrocSwap) | [CrocSwap-protocol](https://github.com/CrocSwap/CrocSwap-protocol) `TypeScript` ★79<br>[crocswap-router-compat](https://github.com/CrocSwap/crocswap-router-compat) `Solidity` ★0 |
| 44 | **NFTX** | $1.44M | NFT Marketplace | Ethereum, Arbitrum | [NFTX-project](https://github.com/NFTX-project) | [nftx-protocol-v3](https://github.com/NFTX-project/nftx-protocol-v3) `Solidity` ★21<br>[nftx-protocol-v2.1](https://github.com/NFTX-project/nftx-protocol-v2.1) `Solidity` ★1<br>[x-contracts](https://github.com/NFTX-project/x-contracts) `Solidity` ★32 +2 more |
| 45 | **Travessia Credit** | $1.44M | RWA | Ethereum, Avalanche, Polygon +2 | [RedVeil](https://github.com/RedVeil) | [Travessia-Commodity-Tracking](https://github.com/RedVeil/Travessia-Commodity-Tracking) `Solidity` ★0<br>[FixedForexUSDC](https://github.com/RedVeil/FixedForexUSDC) `Solidity` ★0<br>[YieldForge](https://github.com/RedVeil/YieldForge) `Solidity` ★0 +2 more |
| 46 | **Privacy Boost** | $1.41M | Privacy | Base, Optimism, Soneium | [sunnyside-io](https://github.com/sunnyside-io) | [privacy-boost-protocol](https://github.com/sunnyside-io/privacy-boost-protocol) `Solidity` ★15 |
| 47 | **deBridge** | $1.39M | Bridge | Ethereum, Binance, Arbitrum +3 | [debridge-finance](https://github.com/debridge-finance) | [debridge-contracts-v1](https://github.com/debridge-finance/debridge-contracts-v1) `JavaScript` ★60<br>[hardhat-debridge](https://github.com/debridge-finance/hardhat-debridge) `TypeScript` ★23<br>[de-solana-client](https://github.com/debridge-finance/de-solana-client) `Rust` ★3 +2 more |
| 48 | **Swappi** | $1.37M | Dexs | Conflux | [swappidex](https://github.com/swappidex) | [swappi-periphery](https://github.com/swappidex/swappi-periphery) `Solidity` ★7<br>[swappi-farm](https://github.com/swappidex/swappi-farm) `Solidity` ★3<br>[swappi-core](https://github.com/swappidex/swappi-core) `TypeScript` ★5 |
| 49 | **Hubble** | $1.37M | CDP | Solana | [hubbleprotocol](https://github.com/hubbleprotocol) | [solana-setup-action](https://github.com/hubbleprotocol/solana-setup-action) `Rust` ★1<br>[anchor-bpf-template](https://github.com/hubbleprotocol/anchor-bpf-template) `Rust` ★1 |
| 50 | **KaoyaSwap** | $1.27M | Dexs | Binance | [kaoya1125](https://github.com/kaoya1125) | [contracts](https://github.com/kaoya1125/contracts) `Solidity` ★0 |
| 51 | **MDEX** | $1.24M | Dexs | Binance, Bittorrent, Heco | [mdexSwap](https://github.com/mdexSwap) | [contracts](https://github.com/mdexSwap/contracts) `Solidity` ★135 |
| 52 | **SOFA.org** | $1.22M | Options | Ethereum, Arbitrum, Binance +1 | [sofa-org](https://github.com/sofa-org) | [sofa-protocol](https://github.com/sofa-org/sofa-protocol) `TypeScript` ★10 |
| 53 | **Yamato Protocol** | $1.16M | CDP | Ethereum | [DeFiGeek-Community](https://github.com/DeFiGeek-Community) | [yamato](https://github.com/DeFiGeek-Community/yamato) `Solidity` ★4<br>[yamato-commodities](https://github.com/DeFiGeek-Community/yamato-commodities) `Solidity` ★0<br>[ve-factory](https://github.com/DeFiGeek-Community/ve-factory) `Solidity` ★1 |
| 54 | **Lisk Bridge** | $1.12M | Canonical Bridge | Ethereum | [LiskHQ](https://github.com/LiskHQ) | [lisk-contracts](https://github.com/LiskHQ/lisk-contracts) `Solidity` ★17 |
| 55 | **Mitosis** | $1.09M | Onchain Capital Allocator | Binance, Linea, Arbitrum +9 | [mitosis-org](https://github.com/mitosis-org) | [protocol](https://github.com/mitosis-org/protocol) `Solidity` ★17<br>[dn404x](https://github.com/mitosis-org/dn404x) `Solidity` ★3<br>[protocol-dapp-template](https://github.com/mitosis-org/protocol-dapp-template) `Solidity` ★1 +1 more |
| 56 | **CityCoins** | $1.09M | Yield | Stacks | [citycoins](https://github.com/citycoins) | [protocol](https://github.com/citycoins/protocol) `Clarity` ★7<br>[protocol-api](https://github.com/citycoins/protocol-api) `TypeScript` ★1 |
| 57 | **OpenBook** | $1.08M | Dexs | Solana | [openbook-dex](https://github.com/openbook-dex) | [program](https://github.com/openbook-dex/program) `Rust` ★212<br>[openbook-v2](https://github.com/openbook-dex/openbook-v2) `Rust` ★263 |
| 58 | **Angstrom** | $1.08M | Dexs | Ethereum | [SorellaLabs](https://github.com/SorellaLabs) | [l2-angstrom](https://github.com/SorellaLabs/l2-angstrom) `Solidity` ★4<br>[super-sol](https://github.com/SorellaLabs/super-sol) `Solidity` ★11 |
| 59 | **Augur** | $1.05M | Prediction Market | Ethereum | [AugurProject](https://github.com/AugurProject) | [augur-core](https://github.com/AugurProject/augur-core) `TypeScript` ★585<br>[Lituus-CS](https://github.com/AugurProject/Lituus-CS) `Solidity` ★0<br>[oracle-research](https://github.com/AugurProject/oracle-research) `Solidity` ★6 |
| 60 | **Nami** | $1.04M | Dexs | Base, Robinhood Chain, Ethereum | [namifi](https://github.com/namifi) | [Nami-Protocol](https://github.com/namifi/Nami-Protocol) `Solidity` ★0 |
| 61 | **CHATEAU** | $1.02M | RWA | Plasma | [chateau-capital](https://github.com/chateau-capital) | [ca](https://github.com/chateau-capital/ca) `Solidity` ★1 |
| 62 | **RealtyX** | $1.02M | RWA | Base, Plume Mainnet | [HomuraAcc](https://github.com/HomuraAcc) | [The-Realtyx-Smart-Contracts](https://github.com/HomuraAcc/The-Realtyx-Smart-Contracts) `Solidity` ★3 |
| 63 | **Overtime** | $992k | Prediction Market | Arbitrum, Base, Optimism +3 | [thales-markets](https://github.com/thales-markets) | [solana-contracts](https://github.com/thales-markets/solana-contracts) `JavaScript` ★0 |
| 64 | **Kromatika** | $989k | Dexs | Optimism, Ethereum, Arbitrum +1 | [Kromatika-Finance](https://github.com/Kromatika-Finance) | [MetaSwap](https://github.com/Kromatika-Finance/MetaSwap) `Solidity` ★0 |
| 65 | **Wombat Exchange** | $983k | Dexs | Binance, Arbitrum, Avalanche +7 | [wombat-exchange](https://github.com/wombat-exchange) | [v1-core](https://github.com/wombat-exchange/v1-core) `Solidity` ★18 |
| 66 | **Isle Finance** | $961k | RWA | Hedera | [isle-labs](https://github.com/isle-labs) | [isle-enterprise-contract](https://github.com/isle-labs/isle-enterprise-contract) `Solidity` ★5 |
| 67 | **SHUI** | $956k | Liquid Staking | Conflux | [Shui-LST](https://github.com/Shui-LST) | [shui-lsd-core](https://github.com/Shui-LST/shui-lsd-core) `Solidity` ★1 |
| 68 | **ForgeYields** | $873k | Onchain Capital Allocator | Starknet, Ethereum | [ForgeYields](https://github.com/ForgeYields) | [starknet_vault_kit](https://github.com/ForgeYields/starknet_vault_kit) `Cairo` ★12 |
| 69 | **Hyperion** | $846k | Dexs | Aptos | [Hyperionxyz](https://github.com/Hyperionxyz) | [pyth-dep](https://github.com/Hyperionxyz/pyth-dep) `Move` ★0<br>[dex-multiagent-example](https://github.com/Hyperionxyz/dex-multiagent-example) `Move` ★0<br>[hyperion-interface](https://github.com/Hyperionxyz/hyperion-interface) `Move` ★9 |
| 70 | **Rari Capital** | $826k | Yield Aggregator | Ethereum, Arbitrum | [Rari-Capital](https://github.com/Rari-Capital) | [nova-interfaces](https://github.com/Rari-Capital/nova-interfaces) `Solidity` ★10<br>[nova-invariants](https://github.com/Rari-Capital/nova-invariants) `Solidity` ★6<br>[fuse-v1](https://github.com/Rari-Capital/fuse-v1) `Solidity` ★2 +2 more |
| 71 | **BlazeSwap** | $815k | Dexs | Flare, Songbird | [blazeswap](https://github.com/blazeswap) | [contracts](https://github.com/blazeswap/contracts) `TypeScript` ★6 |
| 72 | **Mendi Finance** | $811k | Lending | Linea | [mendi-finance](https://github.com/mendi-finance) | [lending-protocol](https://github.com/mendi-finance/lending-protocol) `Solidity` ★5<br>[staking-protocol](https://github.com/mendi-finance/staking-protocol) `TypeScript` ★3 |
| 73 | **VETRO** | $804k | CDP | Ethereum | [vetro-protocol](https://github.com/vetro-protocol) | [vetro-contracts](https://github.com/vetro-protocol/vetro-contracts) `Solidity` ★2<br>[Safe-guard](https://github.com/vetro-protocol/Safe-guard) `Solidity` ★1 |
| 74 | **Ellipsis Finance** | $801k | Dexs | Binance | [ellipsis-finance](https://github.com/ellipsis-finance) | [ellipsis-v2](https://github.com/ellipsis-finance/ellipsis-v2) `Solidity` ★13 |
| 75 | **Kai Finance** | $800k | Leveraged Farming | Sui | [kunalabs-io](https://github.com/kunalabs-io) | [sui-smart-contracts](https://github.com/kunalabs-io/sui-smart-contracts) `Move` ★86 |
| 76 | **ALEX** | $781k | Dexs | Stacks | [alexgo-io](https://github.com/alexgo-io) | [alex-v1](https://github.com/alexgo-io/alex-v1) `Clarity` ★41<br>[ord-bitcoincore-rpc](https://github.com/alexgo-io/ord-bitcoincore-rpc) `Rust` ★0<br>[alex-orderbook-public](https://github.com/alexgo-io/alex-orderbook-public) `Clarity` ★0 +2 more |
| 77 | **Twyne** | $763k | Lending | Ethereum | [0xTwyne](https://github.com/0xTwyne) | [twyne-contracts-v1](https://github.com/0xTwyne/twyne-contracts-v1) `Solidity` ★11<br>[aave-v3-aToken-wrapper](https://github.com/0xTwyne/aave-v3-aToken-wrapper) `Solidity` ★0<br>[twyne-shield](https://github.com/0xTwyne/twyne-shield) `Solidity` ★0 +2 more |
| 78 | **WingRiders** | $751k | Dexs | Cardano | [WingRiders](https://github.com/WingRiders) | [launchpad-contracts](https://github.com/WingRiders/launchpad-contracts) `Haskell` ★0<br>[rapid-dex-contracts](https://github.com/WingRiders/rapid-dex-contracts) `Aiken` ★0<br>[dex-v2-contracts](https://github.com/WingRiders/dex-v2-contracts) `Haskell` ★1 +2 more |
| 79 | **Suzaku** | $723k | Restaking | Avalanche | [suzaku-network](https://github.com/suzaku-network) | [suzaku-core](https://github.com/suzaku-network/suzaku-core) `Solidity` ★1<br>[suzaku-contracts-library](https://github.com/suzaku-network/suzaku-contracts-library) `Solidity` ★8<br>[suzaku-deployer](https://github.com/suzaku-network/suzaku-deployer) `Solidity` ★0 |
| 80 | **Teller** | $721k | Lending | Base, Ethereum, Arbitrum +6 | [teller-protocol](https://github.com/teller-protocol) | [teller-protocol-v2](https://github.com/teller-protocol/teller-protocol-v2) `Rust` ★17<br>[teller-protocol-v1](https://github.com/teller-protocol/teller-protocol-v1) `Solidity` ★106<br>[teller-tx-debug-suite](https://github.com/teller-protocol/teller-tx-debug-suite) `Solidity` ★0 +2 more |
| 81 | **DIEM Relay** | $706k | Liquid Staking | Base | [Figu3](https://github.com/Figu3) | [clear-morpho-adapter](https://github.com/Figu3/clear-morpho-adapter) `Solidity` ★0<br>[diem-relay](https://github.com/Figu3/diem-relay) `Solidity` ★0<br>[sonic-earn-recovery-system](https://github.com/Figu3/sonic-earn-recovery-system) `Solidity` ★0 +2 more |
| 82 | **Forest Road Vault** | $693k | RWA | Ethereum | [Forest-Road-Company](https://github.com/Forest-Road-Company) | [forest-road-vault](https://github.com/Forest-Road-Company/forest-road-vault) `Solidity` ★6 |
| 83 | **King Protocol** | $688k | Liquid Restaking | Ethereum | [King-Protocol](https://github.com/King-Protocol) | [king-cross-chain](https://github.com/King-Protocol/king-cross-chain) `Solidity` ★1<br>[king-vaults](https://github.com/King-Protocol/king-vaults) `Solidity` ★0 |
| 84 | **B.Protocol** | $678k | Liquidations | Ethereum, Arbitrum, Polygon +1 | [backstop-protocol](https://github.com/backstop-protocol) | [ERC-7770](https://github.com/backstop-protocol/ERC-7770) `Solidity` ★0<br>[smart-ltv](https://github.com/backstop-protocol/smart-ltv) `Solidity` ★0<br>[B.Protocol-data](https://github.com/backstop-protocol/B.Protocol-data) `TypeScript` ★0 +2 more |
| 85 | **KEEP Network** | $651k | Cross Chain Bridge | Ethereum | [keep-network](https://github.com/keep-network) | [hardhat-helpers](https://github.com/keep-network/hardhat-helpers) `TypeScript` ★3<br>[contracts-migrate-action](https://github.com/keep-network/contracts-migrate-action) `` ★0 |
| 86 | **Pondo Protocol** | $645k | Liquid Staking | Aleo | [ProvableHQ](https://github.com/ProvableHQ) | [dynamic-fee-uniswap-hook](https://github.com/ProvableHQ/dynamic-fee-uniswap-hook) `Solidity` ★0 |
| 87 | **Lets Get HAI** | $645k | CDP | Optimism | [hai-on-op](https://github.com/hai-on-op) | [core](https://github.com/hai-on-op/core) `Solidity` ★40<br>[altar-of-rai-contracts](https://github.com/hai-on-op/altar-of-rai-contracts) `Solidity` ★0<br>[governance](https://github.com/hai-on-op/governance) `Solidity` ★0 |
| 88 | **10KSwap** | $633k | Dexs | Starknet | [10k-swap](https://github.com/10k-swap) | [10k_swap-contracts](https://github.com/10k-swap/10k_swap-contracts) `Cairo` ★58 |
| 89 | **Meson** | $626k | Cross Chain Bridge | Binance, BSquared, Merlin +41 | [MesonFi](https://github.com/MesonFi) | [merlin-contracts](https://github.com/MesonFi/merlin-contracts) `Solidity` ★0 |
| 90 | **Kaskad** | $614k | Lending | Robinhood Chain, Igra | [Kaskad-Lending](https://github.com/Kaskad-Lending) | [kaskad-nuntius-contracts](https://github.com/Kaskad-Lending/kaskad-nuntius-contracts) `Solidity` ★1<br>[kaskad-pontifex](https://github.com/Kaskad-Lending/kaskad-pontifex) `Solidity` ★0<br>[kaskad-contracts](https://github.com/Kaskad-Lending/kaskad-contracts) `Solidity` ★0 |
| 91 | **Dinosaur Eggs** | $592k | Dexs | Binance | [Dinosaur-eggs](https://github.com/Dinosaur-eggs) | [core](https://github.com/Dinosaur-eggs/core) `Solidity` ★24 |
| 92 | **BearnFi** | $591k | Yield | Binance | [bearn-defi](https://github.com/bearn-defi) | [bearn-smartcontracts](https://github.com/bearn-defi/bearn-smartcontracts) `Solidity` ★6<br>[bdex-smartcontracts](https://github.com/bearn-defi/bdex-smartcontracts) `TypeScript` ★0<br>[bvaults-smartcontracts](https://github.com/bearn-defi/bvaults-smartcontracts) `Solidity` ★0 |
| 93 | **Honeyswap** | $589k | Dexs | xDai, Polygon | [1Hive](https://github.com/1Hive) | [fluid-proposals](https://github.com/1Hive/fluid-proposals) `Solidity` ★0<br>[honeyswap-limit-order-contracts](https://github.com/1Hive/honeyswap-limit-order-contracts) `Solidity` ★3<br>[deployments-aragon-os](https://github.com/1Hive/deployments-aragon-os) `TypeScript` ★0 |
| 94 | **ParyonUSD** | $580k | CDP | Bitcoincash | [ParyonUSD](https://github.com/ParyonUSD) | [contracts](https://github.com/ParyonUSD/contracts) `TypeScript` ★12<br>[verify_contract_deployment](https://github.com/ParyonUSD/verify_contract_deployment) `TypeScript` ★0 |
| 95 | **WanSwap Dex** | $579k | Dexs | Wanchain | [wanswap](https://github.com/wanswap) | [wasp-assist](https://github.com/wanswap/wasp-assist) `Solidity` ★1<br>[funny-auction-contracts](https://github.com/wanswap/funny-auction-contracts) `JavaScript` ★1<br>[wanswap-hive-contracts](https://github.com/wanswap/wanswap-hive-contracts) `Solidity` ★1 |
| 96 | **TermMax** | $572k | Lending | Ethereum, Berachain, Binance +6 | [term-structure](https://github.com/term-structure) | [termmax-contract-v2](https://github.com/term-structure/termmax-contract-v2) `Solidity` ★9<br>[termmax-contract](https://github.com/term-structure/termmax-contract) `Solidity` ★4<br>[TS-smart-contract](https://github.com/term-structure/TS-smart-contract) `TypeScript` ★2 |
| 97 | **Aurigami** | $554k | Lending | Aurora | [Aurigami-Finance](https://github.com/Aurigami-Finance) | [aurigami-smart-contracts](https://github.com/Aurigami-Finance/aurigami-smart-contracts) `Solidity` ★0 |
| 98 | **VaultCraft** | $540k | Yield | Arbitrum, Ethereum, Polygon +4 | [Popcorn-Limited](https://github.com/Popcorn-Limited) | [gauges](https://github.com/Popcorn-Limited/gauges) `Solidity` ★0<br>[audit-04-24](https://github.com/Popcorn-Limited/audit-04-24) `Solidity` ★0<br>[xvcx-bridges](https://github.com/Popcorn-Limited/xvcx-bridges) `Solidity` ★0 +2 more |
| 99 | **Trevee Earn** | $537k | Yield Aggregator | Sonic, Ethereum, Plasma | [Rings-Protocol](https://github.com/Rings-Protocol) | [rings-contracts](https://github.com/Rings-Protocol/rings-contracts) `Solidity` ★1<br>[rings-wrapper](https://github.com/Rings-Protocol/rings-wrapper) `Solidity` ★0 |
| 100 | **WePiggy** | $532k | Lending | Ethereum, Optimism, Arbitrum +9 | [WePiggy](https://github.com/WePiggy) | [wepiggy-contracts](https://github.com/WePiggy/wepiggy-contracts) `Solidity` ★20<br>[contract_addresses](https://github.com/WePiggy/contract_addresses) `` ★0<br>[wepiggy-contracts-optimism](https://github.com/WePiggy/wepiggy-contracts-optimism) `Solidity` ★0 +1 more |
| 101 | **Hemi Bridge** | $492k | Canonical Bridge | Ethereum | [hemilabs](https://github.com/hemilabs) | [fpmm](https://github.com/hemilabs/fpmm) `Solidity` ★1<br>[veHEMI](https://github.com/hemilabs/veHEMI) `Solidity` ★0<br>[hemi-token](https://github.com/hemilabs/hemi-token) `Solidity` ★0 +2 more |
| 102 | **Zunami Protocol** | $490k | Yield Aggregator | Ethereum | [ZunamiProtocol](https://github.com/ZunamiProtocol) | [ZunamiProtocolV2](https://github.com/ZunamiProtocol/ZunamiProtocolV2) `TypeScript` ★1 |
| 103 | **yAxis** | $488k | Yield Aggregator | Ethereum | [yaxis-project](https://github.com/yaxis-project) | [yaxis-audit](https://github.com/yaxis-project/yaxis-audit) `Solidity` ★6<br>[metavault](https://github.com/yaxis-project/metavault) `Solidity` ★32 |
| 104 | **PsyOptions** | $485k | Options | Solana | [mithraiclabs](https://github.com/mithraiclabs) | [psyoracleutils](https://github.com/mithraiclabs/psyoracleutils) `Rust` ★2<br>[pyth-min](https://github.com/mithraiclabs/pyth-min) `Rust` ★0<br>[psy-macros](https://github.com/mithraiclabs/psy-macros) `Rust` ★1 |
| 105 | **Cover Protocol** | $481k | Insurance | Ethereum | [CoverProtocol](https://github.com/CoverProtocol) | [cover-token-mining](https://github.com/CoverProtocol/cover-token-mining) `Solidity` ★8<br>[cover-core-v1](https://github.com/CoverProtocol/cover-core-v1) `Solidity` ★19<br>[cover-rewards](https://github.com/CoverProtocol/cover-rewards) `Solidity` ★1 +1 more |
| 106 | **YFII** | $432k | Yield Aggregator | Ethereum | [yfii](https://github.com/yfii) | [yvault](https://github.com/yfii/yvault) `Solidity` ★60<br>[yficontract](https://github.com/yfii/yficontract) `JavaScript` ★16 |
| 107 | **ImmutableX** | $424k | NFT Marketplace | Ethereum | [immutable](https://github.com/immutable) | [imx-migration-contracts](https://github.com/immutable/imx-migration-contracts) `Solidity` ★2<br>[contracts](https://github.com/immutable/contracts) `Solidity` ★46<br>[zkevm-bridge-contracts](https://github.com/immutable/zkevm-bridge-contracts) `Solidity` ★18 +1 more |
| 108 | **Perpetual Protocol** | $422k | Derivatives | Ethereum, Optimism | [perpetual-protocol](https://github.com/perpetual-protocol) | [perp-curie-periphery-contract](https://github.com/perpetual-protocol/perp-curie-periphery-contract) `TypeScript` ★16<br>[lugia-contract](https://github.com/perpetual-protocol/lugia-contract) `Solidity` ★1<br>[perp-curie-contract](https://github.com/perpetual-protocol/perp-curie-contract) `TypeScript` ★87 +2 more |
| 109 | **MooniSwap** | $419k | Dexs | Ethereum | [1inch](https://github.com/1inch) | [solana-fusion-protocol](https://github.com/1inch/solana-fusion-protocol) `TypeScript` ★6<br>[swap-vm](https://github.com/1inch/swap-vm) `Solidity` ★50<br>[limit-order-protocol](https://github.com/1inch/limit-order-protocol) `JavaScript` ★315 +2 more |
| 110 | **RadioShack** | $416k | Dexs | Binance, Avalanche, Polygon +5 | [radioshackswap](https://github.com/radioshackswap) | [contracts](https://github.com/radioshackswap/contracts) `Solidity` ★2 |
| 111 | **PinkSwap** | $405k | Dexs | Binance | [pinkmoonfinance](https://github.com/pinkmoonfinance) | [pink-antibot-guide](https://github.com/pinkmoonfinance/pink-antibot-guide) `Solidity` ★52<br>[pinksale-contracts](https://github.com/pinkmoonfinance/pinksale-contracts) `Solidity` ★44 |
| 112 | **JPEG'd** | $390k | NFT Lending | Ethereum | [jpegd](https://github.com/jpegd) | [core](https://github.com/jpegd/core) `Solidity` ★12 |
| 113 | **Nolus Protocol** | $375k | Lending | Nolus, Solana, Neutron +1 | [nolus-protocol](https://github.com/nolus-protocol) | [nolus-core](https://github.com/nolus-protocol/nolus-core) `Go` ★62 |
| 114 | **Cyclone** | $374k | Yield | Binance, Ethereum, IoTeX +1 | [cycloneprotocol](https://github.com/cycloneprotocol) | [cyclone-contracts](https://github.com/cycloneprotocol/cyclone-contracts) `Solidity` ★65 |
| 115 | **Flipcash** | $373k | Launchpad | Solana | [code-payments](https://github.com/code-payments) | [code-vm](https://github.com/code-payments/code-vm) `Rust` ★64<br>[ocp-client-protocol](https://github.com/code-payments/ocp-client-protocol) `Swift` ★0<br>[flipcash2-client-protocol](https://github.com/code-payments/flipcash2-client-protocol) `Swift` ★0 +1 more |
| 116 | **Tarot** | $372k | Lending | Base, Optimism, Fantom +10 | [tarot-finance](https://github.com/tarot-finance) | [tarot-core](https://github.com/tarot-finance/tarot-core) `JavaScript` ★17<br>[tarot-price-oracle](https://github.com/tarot-finance/tarot-price-oracle) `Solidity` ★8<br>[tarot-periphery](https://github.com/tarot-finance/tarot-periphery) `Solidity` ★9 +2 more |
| 117 | **Scientix** | $367k | Synthetics | Binance | [ScientixFinance](https://github.com/ScientixFinance) | [scientix-contract](https://github.com/ScientixFinance/scientix-contract) `Solidity` ★3 |
| 118 | **Ante Finance** | $364k | Insurance | Ethereum, Binance, Avalanche +5 | [antefinance](https://github.com/antefinance) | [ante-v05-core](https://github.com/antefinance/ante-v05-core) `TypeScript` ★6<br>[ante-community-tests](https://github.com/antefinance/ante-community-tests) `Solidity` ★35<br>[ante-v06-core](https://github.com/antefinance/ante-v06-core) `TypeScript` ★1 |
| 119 | **SingularityDAO** | $364k | Yield | Ethereum, Binance | [Singularity-DAO](https://github.com/Singularity-DAO) | [hypercycle-token-contracts](https://github.com/Singularity-DAO/hypercycle-token-contracts) `JavaScript` ★0<br>[migration-contracts](https://github.com/Singularity-DAO/migration-contracts) `TypeScript` ★3<br>[sdao-token-contracts](https://github.com/Singularity-DAO/sdao-token-contracts) `Solidity` ★9 +2 more |
| 120 | **88mph** | $362k | Lending | Ethereum, Fantom, Avalanche +1 | [88mphapp](https://github.com/88mphapp) | [88mph-contracts](https://github.com/88mphapp/88mph-contracts) `Solidity` ★83<br>[88mph-gauge](https://github.com/88mphapp/88mph-gauge) `Vyper` ★0<br>[Phantasm](https://github.com/88mphapp/Phantasm) `Solidity` ★0 +1 more |
| 121 | **Compound Blue** | $362k | Lending | Polygon | [papercliplabs](https://github.com/papercliplabs) | [nouns-town](https://github.com/papercliplabs/nouns-town) `Solidity` ★1 |
| 122 | **Swop** | $361k | Dexs | Waves, UNIT0 | [swopfi](https://github.com/swopfi) | [swopfi-smart-contracts](https://github.com/swopfi/swopfi-smart-contracts) `` ★11 |
| 123 | **Geode** | $360k | Liquid Staking | Avalanche | [Geodefi](https://github.com/Geodefi) | [Portal-Eth](https://github.com/Geodefi/Portal-Eth) `Solidity` ★3 |
| 124 | **FortiFi** | $355k | Yield Aggregator | Avalanche | [0xFortiFi](https://github.com/0xFortiFi) | [Moat-Contracts](https://github.com/0xFortiFi/Moat-Contracts) `Solidity` ★0<br>[FortiFi-Foundry](https://github.com/0xFortiFi/FortiFi-Foundry) `Solidity` ★0<br>[FortiFi-Vaults](https://github.com/0xFortiFi/FortiFi-Vaults) `Solidity` ★1 |
| 125 | **Deriverse** | $354k | Dexs | Solana | [deriverse](https://github.com/deriverse) | [drv-smart-contract-common](https://github.com/deriverse/drv-smart-contract-common) `Rust` ★0 |
| 126 | **Breadchain** | $353k | CDP | xDai | [BreadchainCoop](https://github.com/BreadchainCoop) | [sigstack-near](https://github.com/BreadchainCoop/sigstack-near) `Rust` ★0<br>[GrowKesennuma](https://github.com/BreadchainCoop/GrowKesennuma) `Solidity` ★0<br>[hats-delegated-security](https://github.com/BreadchainCoop/hats-delegated-security) `Solidity` ★0 +2 more |
| 127 | **AggreLend** | $344k | Yield Aggregator | Solana | [AggreLend](https://github.com/AggreLend) | [kamino-finance-cpi-integration](https://github.com/AggreLend/kamino-finance-cpi-integration) `Rust` ★4<br>[drift-cpi-integration](https://github.com/AggreLend/drift-cpi-integration) `Rust` ★3<br>[marginfi-integration](https://github.com/AggreLend/marginfi-integration) `Rust` ★3 +1 more |
| 128 | **Siren** | $342k | Options | Ethereum, Polygon, Arbitrum | [sirenmarkets](https://github.com/sirenmarkets) | [core](https://github.com/sirenmarkets/core) `TypeScript` ★41 |
| 129 | **Unicly** | $342k | Dexs | Ethereum | [uniclyNFT](https://github.com/uniclyNFT) | [unicly-core](https://github.com/uniclyNFT/unicly-core) `Solidity` ★9 |
| 130 | **Dfyn Network** | $333k | Dexs | Polygon, Fantom, OKExChain | [dfyn](https://github.com/dfyn) | [dfyn-exchange](https://github.com/dfyn/dfyn-exchange) `Solidity` ★21<br>[dfyn-token](https://github.com/dfyn/dfyn-token) `Solidity` ★7<br>[dual-farm](https://github.com/dfyn/dual-farm) `Solidity` ★1 +2 more |
| 131 | **Narwhalswap** | $328k | Dexs | Binance | [narwhalswap](https://github.com/narwhalswap) | [thegrandbanks](https://github.com/narwhalswap/thegrandbanks) `Solidity` ★1<br>[contracts](https://github.com/narwhalswap/contracts) `Solidity` ★0<br>[nar-token](https://github.com/narwhalswap/nar-token) `Solidity` ★0 |
| 132 | **Sherpa** | $327k | Onchain Capital Allocator | Ethereum, Base, Monad | [hedgemonyxyz](https://github.com/hedgemonyxyz) | [sherpa-vault-smartcontracts-v1.0](https://github.com/hedgemonyxyz/sherpa-vault-smartcontracts-v1.0) `Solidity` ★1 |
| 133 | **Sigmausd** | $310k | Algo-Stables | Ergo | [anon-real](https://github.com/anon-real) | [contract-testing](https://github.com/anon-real/contract-testing) `Scala` ★6 |
| 134 | **Ponder Finance** | $302k | Dexs | Bitkub | [ponderfinance](https://github.com/ponderfinance) | [protocol](https://github.com/ponderfinance/protocol) `Solidity` ★1<br>[usdp](https://github.com/ponderfinance/usdp) `Solidity` ★0 |
| 135 | **Sprinter** | $302k | Yield | Base | [sprintertech](https://github.com/sprintertech) | [sprinter-stash-contracts](https://github.com/sprintertech/sprinter-stash-contracts) `TypeScript` ★1<br>[deploy-safersafes](https://github.com/sprintertech/deploy-safersafes) `Solidity` ★0 |
| 136 | **Swerve** | $301k | Dexs | Ethereum | [SwerveFinance](https://github.com/SwerveFinance) | [SwerveContracts](https://github.com/SwerveFinance/SwerveContracts) `` ★39 |
| 137 | **Opus** | $301k | CDP | Starknet | [lindy-labs](https://github.com/lindy-labs) | [opus_contracts](https://github.com/lindy-labs/opus_contracts) `Cairo` ★0<br>[opus_compose](https://github.com/lindy-labs/opus_compose) `Cairo` ★0<br>[wadray](https://github.com/lindy-labs/wadray) `Cairo` ★21 +2 more |

---

## NO_CONTRACT_REPO — 57 protocols

These protocols declare a public github org but no contract-bearing repo was detected by the heuristic. Worth manual review before assuming closed-source.

| # | Protocol | TVL | Category | Chains | GitHub |
|---|---|---|---|---|---|
| 1 | Autofarm | $4.91M | Yield Aggregator | Binance, Polygon, Cronos +17 | [autofarmnetwork](https://github.com/autofarmnetwork) |
| 2 | WaterNeuron | $4.86M | Liquid Staking | ICP | [WaterNeuron](https://github.com/WaterNeuron) |
| 3 | Mole | $4.24M | Yield | Sui, Aptos | [Mole-Fi](https://github.com/Mole-Fi) |
| 4 | Saber | $4.10M | Dexs | Solana | [saberdao](https://github.com/saberdao) |
| 5 | Nawa Protocol | $3.97M | RWA | ZIGChain, Ethereum, CORE | [NawaTeam](https://github.com/NawaTeam) |
| 6 | LayerBank | $3.93M | Lending | Robinhood Chain, RSK, Linea +14 | [layerbank](https://github.com/layerbank) |
| 7 | Bumpin Trade | $3.84M | Derivatives | Solana | [bumpin-exchange](https://github.com/bumpin-exchange) |
| 8 | Splashing Stake | $3.51M | Liquid Staking | Sei | [SplashingStaking](https://github.com/SplashingStaking) |
| 9 | Blueshift | $3.46M | Dexs | BOB, Kava, Polygon +2 | [blueshift-fi](https://github.com/blueshift-fi) |
| 10 | Surf Lending | $2.76M | Lending | Cardano | [flow-lending](https://github.com/flow-lending) |
| 11 | International Stable Currency | $2.41M | RWA | Solana | [TheISCTeam](https://github.com/TheISCTeam) |
| 12 | Indigo | $2.40M | CDP | Cardano | [IndigoProtocol](https://github.com/IndigoProtocol) |
| 13 | Presto | $2.36M | Risk Curators | Ethereum | [prestolabs](https://github.com/prestolabs) |
| 14 | ICPSwap | $2.05M | Dexs | ICP | [ICPSwap-Labs](https://github.com/ICPSwap-Labs) |
| 15 | FluidTokens | $2.00M | Lending | Cardano | [FluidTokens](https://github.com/FluidTokens) |
| 16 | BTCD | $1.80M | Yield | Ethereum, Arbitrum | [BTCDLabs](https://github.com/BTCDLabs) |
| 17 | Arkis | $1.69M | Lending | Ethereum, Hyperliquid L1 | [ArkisXYZ](https://github.com/ArkisXYZ) |
| 18 | Surge Credit | $1.47M | Lending | Bitcoin, Base | [surgecredit](https://github.com/surgecredit) |
| 19 | Permapod | $1.41M | Lending | ZIGChain | [permapod](https://github.com/permapod) |
| 20 | Mountain Protocol | $1.40M | RWA | Ethereum, zkSync Era, Arbitrum +3 | [mountainprotocol](https://github.com/mountainprotocol) |
| 21 | PiggyBank | $1.33M | Yield | Solana | [zsociety-io](https://github.com/zsociety-io) |
| 22 | Tradecraft | $1.32M | Dexs | Canton | [tradecraft-fi](https://github.com/tradecraft-fi) |
| 23 | Decentralized Euro | $1.16M | CDP | Ethereum | [d-EURO](https://github.com/d-EURO) |
| 24 | Coffer Network | $1.15M | Bridge | Bitcoin | [coffer-network](https://github.com/coffer-network) |
| 25 | Baseline Protocol | $1.11M | Liquidity Manager | Ethereum, Base, Blast | [0xBaseline](https://github.com/0xBaseline) |
| 26 | Cabal | $1.07M | Governance Incentives | Initia, Cabal, Strat | [0xCabal](https://github.com/0xCabal) |
| 27 | Pact | $985k | Dexs | Algorand | [pactfi](https://github.com/pactfi) |
| 28 | Moola Market | $980k | Lending | Celo | [moolamarket](https://github.com/moolamarket) |
| 29 | Laine SOL | $911k | Liquid Staking | Solana | [laine-sa](https://github.com/laine-sa) |
| 30 | Flexa | $815k | Payments | Ethereum | [flexahq](https://github.com/flexahq) |
| 31 | Archer Exchange | $790k | Dexs | Solana | [SquareRoot-Labs](https://github.com/SquareRoot-Labs) |
| 32 | Ashswap | $779k | Dexs | Elrond | [ashswap](https://github.com/ashswap) |
| 33 | Reactor DEX | $779k | Dexs | Fuel | [Reactor-Fuel](https://github.com/Reactor-Fuel) |
| 34 | Bastion | $773k | Lending | Aurora | [bastionprotocol](https://github.com/bastionprotocol) |
| 35 | Saddle Finance | $759k | Dexs | Ethereum, Arbitrum, Optimism +4 | [saddle-finance](https://github.com/saddle-finance) |
| 36 | TRUE DEX | $735k | Derivatives | Solana | [True-AI-Labs](https://github.com/True-AI-Labs) |
| 37 | Scopuly | $693k | Dexs | Stellar | [Scopuly](https://github.com/Scopuly) |
| 38 | xToken | $648k | Liquidity Manager | Ethereum, Optimism, Arbitrum +1 | [xtokenmarket](https://github.com/xtokenmarket) |
| 39 | Swaylend | $622k | Lending | Fuel | [swaylend](https://github.com/swaylend) |
| 40 | Landshare | $621k | RWA | Binance | [ls-jordan](https://github.com/ls-jordan) |
| 41 | Kublerx | $607k | Dexs | Bitkub | [kublerxofficial](https://github.com/kublerxofficial) |
| 42 | Rise.rich | $584k | Launchpad | Solana | [riserich](https://github.com/riserich) |
| 43 | InkySwap | $574k | Dexs | Ink | [InkySwap](https://github.com/InkySwap) |
| 44 | tramplin.io | $528k | Staking Pool | Solana | [tramplin-io](https://github.com/tramplin-io) |
| 45 | Turtle Club | $490k | Onchain Capital Allocator | Ethereum, Avalanche, Linea | [Turtle-DAO](https://github.com/Turtle-DAO) |
| 46 | Allstake | $480k | Restaking | Near, Ethereum, Solana | [allstake](https://github.com/allstake) |
| 47 | AirPuff | $475k | Leveraged Farming | Ethereum, Arbitrum, Mode +3 | [Airpuff](https://github.com/Airpuff) |
| 48 | Clipper | $472k | Dexs | Ethereum, Base, Optimism +5 | [shipyard-software](https://github.com/shipyard-software) |
| 49 | Stella | $457k | Leveraged Farming | Arbitrum | [stellaxyz](https://github.com/stellaxyz) |
| 50 | Ryze Protocol | $438k | Dexs | Base | [ryze-protocol](https://github.com/ryze-protocol) |
| 51 | DefiBox | $406k | Dexs | EOS, Binance, Wax | [DefiboxTeam](https://github.com/DefiboxTeam) |
| 52 | SHPRD | $379k | Indexes | Arbitrum, Ethereum | [stealth-defi](https://github.com/stealth-defi) |
| 53 | Beradrome | $326k | Yield | Berachain | [BeraLabs](https://github.com/BeraLabs) |
| 54 | Tacit | $322k | Privacy | Ethereum, Base, Robinhood Chain | [src-company](https://github.com/src-company) |
| 55 | xSigma | $317k | Dexs | Ethereum | [xSigmaLabs](https://github.com/xSigmaLabs) |
| 56 | GnoSwap | $315k | Dexs | Gno.land | [gnoswap-labs](https://github.com/gnoswap-labs) |
| 57 | Mobius Money | $314k | Dexs | Celo | [mobiusAMM](https://github.com/mobiusAMM) |

---

## ORG_404 — 1 protocols

- Beam Swap ($1.31M) — declared org: `['Merit-Circle']`
