## Types

Externally-owned account `EOA`: control with private key
`Contract account`: a smart contract deployed, control by code

## Fields
- nonce: a counter.
  - `EOA`: number of transactions sent from an EOA
  - `contract account`: number of contract created by a contract account
  - Why: ONLY 1 transaction with given nonce can be executed -> protect against replaying 
- balance: number of `wei` owned by this address
- codeHash: 
  - cannot be changed
  - `EOA`: hash of empty string
  - `contract account`: code of this contract
- storageRoot: a 256-bit hash