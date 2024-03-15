## Common
- What?
  - gas is unit that measures the computational effort required to execute operations in EVM
  - gas fee is the amount of gas used to do some operation, multiplied by the cost / gas
- Why? need gas
  - to avoid EVM be spammed
  - avoid stuck in infinite loop
- How?
  - gas fee paid in native currency (ETH)
  - total gas pay is divided into 2: base fee and priority fee (or tip)
    - base fee is set by protocol, need to pay at least this number
    - priority fee is added by account to make it attractive to validators
Example:
    an operation has base fee is 10 gwei, tip 2 gwei and cost 21000 gas -> total fee = 21000*(10+2) = 252000 gwei = 0.000252 ETH
-> validator receipt tip = 42000 gwei, 210000 gwei is burned
  - user also can specify maximum limit fee willing to pay, as `maxFeePerGas`, any gas not used = max - (base fee + tip) is returned to user