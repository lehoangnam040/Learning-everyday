## Overview

- What?
  - an action initiated by an `EOA`
  - change the state of the EVM
- How?
  - need to be broadcast to the whole network
  - after broadcast, a validator will execute transaction and propagate the resulting state change to the rest of network
  - cost gas to be executed
- Types:
  - regular transaction: from an account to another
  - contract deployment transaction: a transaction WITHOUT `to`, data field = contract code
  - execution of a contract: a transaction that interacts with a deployed smart contract, `to` = SC address
- Fields in a transaction:
  - `from`: address of sender (`EOA`)
  - `to`: address of receiver
    - `EOA`: transfer value
    - `contract account`: execute contract code
  - `signature`: identifier of the sender, generated when using private key signs the transaction
  - `nonce`: sequentially incrementing counter
  - `value`: amount of ETH to transfer from sender to recipient
  - `input data`: arbitrary data
  - `gasLimit`: maximum amount of gas unit the can be consumed by the transaction
  - `maxPriorityFeePerGas`: maximum price of the consumed gas as a tip to the validator
  - `maxFeePerGas`: maximum fee / gas willing to be paid

## The data field

- first 4 bytes specify function to call, using the hash of function name and arguments
- the rest is the arguments
Example of this [transaction](https://etherscan.io/tx/0xd0dcbe007569fcfa1902dae0ab8b4e078efe42e231786312289b1eee5590f6a1):
- function hash is `0xa9059cbb` = `transfer(address,uint256)` in ABI
- rest of data is `0000000000000000000000004f6742badb049791cd9a37ea913f2bac38d01279000000000000000000000000000000000000000000000000000000003b0559f4`
  - address 20-byte integers = `0x4f6742bADB049791CD9A37ea913f2BAC38d01279`
  - value is `0x3b0559f4` = 990206452
  
## Life cycle

Once a transaction has been submitted:
- a transaction hash is generated
- a transaction is broadcasted to the network, added to the pool with all other pending network transactions
- a validator must pick this transaction and include it in a block in order to verify
- time pass, this block will be upgraded to "jusified" -> "finalized"