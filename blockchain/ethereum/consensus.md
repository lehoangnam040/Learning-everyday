## General
- What?
  - consensus is about general agreement between a group
  - in term of Ethereum, reaching consensus means that at least 66% nodes agree on the global state of the network
  - consensus mechanism refers to protocols, incentives and ideas that allow nodes reaching the consensus
- Consensus mechanism category
  - Proof-Of-Work (PoW)
    - previously, like Bitcoin, Ethereum used PoW
  - Proof-Of-State (PoS)
    - But now, Ethereum's using PoS
- Sybil resistance
  - it measures how a protocol fares against a Sybil attack
  - Sybil attacks are when ONE user pretends to be MANY users
  - PoW and PoS protect against this by making users spend a lots energy or resources -> this protections are economical defends to Sybil attack
- Chain selection rule
  - rule to decide which chain is the "correct" chain among multiple blocks exist in the same position
  - PoW uses "longest chain" with total cumulative PoW difficulty
  - PoS uses "longest chain" with accumulated sum of validators votes, weighted by validator ETH-stake balances.

## PoW and PoS
### PoW
- What? 
  - PoW is the underlying algorithm
- How? 
  - it sets difficulty and rules for the work miners
  - Mining is the "work", it's the adding valid blocks to the chain
    - Dagger-hashimoto
    - Ethash
  - PoW requires miners go through try-and-error to find the nonce for a block -> only blocks with valid nonce could be added
- Security
  - to create malicious invalid blocks, a malicious miner would have needed over 51% of the network to beat everyone else
  - it requires a lot of expensive computing power and it's over the benefit it could made the attack

### PoS
- What?
  - PoS is a way to prove that validators put their money into the network that can be destroyed if they acts dishonestly
- How?
  - validators stake capital (ETH) into a smart contract
  - then they are responsible for checking new blocks valid or not
  - if they try to defraud the network -> some or all staked ETH can be destroyed
- Validators
  - to become a validator, any user deposit 32 ETH into a deposit contract
  - run 3 software: execution client, consensus client and validator client
  - then, validator receive new blocks from peers -> re-execute to check valid -> send a vote across the network
- How transaction executed in PoS?
  - user create / sign a transaction -> making request to node via JSON-RPC with gas fee
  - the transaction is submitted to execution client to ensure enough ETH and signed with correct key
  - valid transaction is broadcasted to other nodes
  - 1 node in the network is selected (by RANDAO). this node build and broadcast next block to be added and update global state
    - execution client bring transactions from mempool to "execution payload" and execute locally -> state change
    - `state change` is passed to consensus client with informations: rewards, penalties, slashings -> "beacon block"
  - other nodes receive new "beacon block" -> pass to execution client -> re-execute locally -> valid or not
    - valid -> block is added to local database
  - the transaction is considered "finalized"
    - Once a transaction/block/epoch is finalized, it cannot be changed without a significant amount (>1/3) of staked ETH being destroyed.
    - 

### Pros & Cons
|       | PoW                                           | PoS
|------ |-----------------------------------------------|--------------------------------------------------------------------|
|  Pros |  don't need ETH to start                      | easier to be come validator, validator node can be run on a laptop |
|       |  it's easier to implement                     | offer greater crypto-economic security |
|       |  tried and tested with Bitcoin for many years | staking is more decentralize |
| Cons  | Uses so much energy                           | less battle-tested |
|       |                                               | more complex to implement |
|       |                                               | need run 3 software to work |
