# Introduction

This is a tentative of implementation of a basic blockchain using Python 3.

# Source code explained

## the `Blockchain` class

### Variables:

- `chain`: List of blocks
- `pending_transaction`: List of transactions not yet added to a block

### Methods
- `new_block`: Method to add each block to the chain
- `new_transaction`: Method to add a transaction to the list of pending transactions
- `hash`: Method to generate a hash from a block
- `last_block`: Method property to get the last block of the chain

# Missing elements

- There is no condition to use `new_block` to create a new block. We do not make use of the `proof`.
- There is no fee for the miners.
- What about: count of transactions, public/private keys, merkle tree structure.