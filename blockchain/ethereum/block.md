## Common
- Why
  - ensure whole network maintain a synchronized state
  - ensure whole network agree on history of transactions
- How
  - batch transactions into blocks
  - blocks are created and committed once every 12 sec -> slot
- What
  - blocks are strictly ordered
  - new block has a reference to its parent block
  - transactions within blocks are ordered as well
- Block size: target of 15M gas, up until limit of 30M gas

## Fields (https://ethereum.org/en/developers/docs/blocks/#block-anatomy)
- `slot`: time is divided up into 12 sec unit called `slots`
- `proposer_index`: id of validator
- `parent_root`: hash of preceding block
- `state_root`: root hash of the state object
- `body`:
  - ...
  - ...
  - `attestations`:
    - `aggregation_bits`
    - `signature`
    - `data`:
      - ...
      - ...
  - `execution_payload`:
    - ...
    - ...
    - `withdrawals`:
      - `address`
      - `amount`
      - `index`
      - `validatorIndex`

