---
title: Binary Search Tree
---

A binary search tree is a binary tree (each element having at most two child nodes) and requires all parents to be greater than their left child nodes and less than or equal to their right child node.

## 2-3 Tree

A 2-3 tree is a binary search tree that allows a node to have store two values. Upon insertion of a value that is a candidate of a 2-value node, certain resolutions must be made such that the following property is attained

* Tree is follows binary search tree
* Upon insertion, the tree cannot change in height unless all nodes are have 2 values.

### Insertion

The insertion algorithm goes as so:

1. Follow the BST insertion rule until all nodes are filled. When this happens move to step 2.
2. Insert the element into the node it last traversed
3. If conflicted with a 2-value node, take the median value and bump it to the parent. The remain two values, split it into two separate nodes.
4. Bubble up repeating step 3 until there is no conflicts.