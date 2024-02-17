# Binary search tree problems

- BST has the low fanout -> we have to perform re-balance tree frequently -> increase maintenance costs
- BST has the fanout of 2 -> need to perform O(log2-N) seeks to locate the searched element on disk -> want to reduce the number of seeks

-> B-tree combine the ideas of improvement: increase node fanout, reduce tree height, number of node pointers, and frequency of balancing operations


# Ubiquitous B-tree

- keys inside B-tree are sorted -> search costs logarithmic complexity
- split and merge operations help to restructure the tree to keep it balanced

# On-disk B-tree implementations

- `Page header`: stores informations, metadata
- `Rightmost pointers`: pointer to child pages, it's stored separately since it's not paired with any key
- `High keys`: determine maximum allowed key can be stored in the node
- `Overflow pages`: allow us to store oversize and variable-size records using fixed-size page

- Root-to-leaf traversals:
  - `binary search`: search via pointers, since those are sorted, compare with key via indirection pointers
  - keep track of tree hierarchies: while traversing from root to leaf, we have to collect `in-memory breadcrumbs`

- optimization & maintenance techniques:
  - `rebalancing`: moves elements between neighboring nodes to reduce the number of split and merge
  - `right-only append`: appends new rightmost cell instead of spliting it
  - `bulk loading`: efficiently building B-trees from scratch from sorted data
  - `garbage collection`: rewrite pages, put cells in key order, and reclaims space