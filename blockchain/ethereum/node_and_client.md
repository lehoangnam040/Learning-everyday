- What?
  - node is an instance of Ethereum client software
- Category:
  - `execution client`: listens new transaction broadcasted in the network, executes in EVM, and holds the latest state and database
  - `consensus client`: implement PoS consensus algo, to agree on validated data
- Node types:
  - `Full node`:
    - can start from genesis block or start from recent block
    - stores full blockchain data
    - do job in block validation, verifies all blocks and states
    - serves network and provides data on request
  - `Archive node`:
    - is full node that every block from genesis
    - never delete any data
    - store everything and builds an archive of historical states
    - useful for block explorers, wallet vendors, chain analytics
  - `Light node`:
    - only download block headers
    - might run on mobile phones / embedded devices
    - do NOT participate in consensus
- Execution client:
  - Geth
  - Besu
  - Erigon
- Execution layer sync mode
  - full archive sync:
    - download all blocks
    - generates state incrementally by executing every block
    - minimize trust, highest security
  - full snap sync
    - start from "recent trusted block" instead of genesis
    - saves periodic checkpoints while deleting older data
  - light sync
    - download all block headers, data, but verify some randomly
- Consensus client:
  - Lighthouse
  - Lodestar
  - Nimbus
  - Prysm
  - Teku
- Consensus layer sync mode
  - Optimistic sync
  - Checkpoint sync