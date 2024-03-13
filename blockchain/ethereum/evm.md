## Common
- What?
  - Ethereum is a distributed state machine
  - Ethereum's state is a large data structure: accounts, balances, machine state
  - Y(S, T) = S' : given old valid state `S`, with new set of valid transactions `T`, state transition func `Y` produce new valid state `S'`
  - state is an data structure called "modified Merkle Patricia trie"
- EVM instructions
  - EVM executes as a stack machine with depth of 1024 items
  - each item is 256-bit word
  - compiled smart contract bytecode executes as a number of EVM opcodes
- opcodes
  - each opcode consume a number of gas
Example: ADD cost 3 gas, MUL cost 5 gas, ... 