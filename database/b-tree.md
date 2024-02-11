# Binary search tree problems

- BST has the low fanout -> we have to perform re-balance tree frequently -> increase maintenance costs
- BST has the fanout of 2 -> need to perform O(log2-N) seeks to locate the searched element on disk -> want to reduce the number of seeks

-> B-tree combine the ideas of improvement: increase node fanout, reduce tree height, number of node pointers, and frequency of balancing operations


# Ubiquitous B-tree

- keys inside B-tree are sorted -> search costs logarithmic complexity
- split and merge operations help to restructure the tree to keep it balanced

# 