# Challenge Title
Trees 

## Approach & Efficiency:

Node Class:

The Node class has three properties: value, left child node, and right child node.
The approach is straightforward as it involves creating a class with basic properties.


Binary Tree Class:

The Binary Tree class has a root node and three depth-first traversal methods: pre-order, in-order, and post-order.
Pre-order traversal visits the root node, then the left subtree, and finally the right subtree.
In-order traversal visits the left subtree, then the root node, and finally the right subtree.
Post-order traversal visits the left subtree, then the right subtree, and finally the root node.


Binary Search Tree Class:

The Binary Search Tree class is a subclass of the Binary Tree class and adds two additional methods: add and contains.
The add method adds a new node with the given value to the correct location in the binary search tree.
The contains method checks whether a value exists in the binary search tree at least once.



## big O :
Binary Tree Class:
The approach for each traversal method is recursive. Each method starts with the root node and recursively traverses the left and right subtrees in the specified order.
The efficiency of each traversal method is O(n), where n is the number of nodes in the binary tree. This is because each node is visited exactly once.

The approach for the add method is iterative, starting from the root node and traversing the tree until the appropriate location for the new node is found. The efficiency of the add method is O(log n) on average, where n is the number of nodes in the binary search tree. In the worst-case scenario, when the tree is unbalanced, the efficiency becomes O(n).
The approach for the contains method is similar to the add method, traversing the tree until the value is found or reaching a leaf node. The efficiency of the contains method is O(log n) on average, and O(n) in the worst case.

## Solution:
 [trees](./trees.py)
 pytest test_trees.py
 