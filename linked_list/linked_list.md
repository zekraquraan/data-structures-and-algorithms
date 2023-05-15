# Challenge Title
# linked list

## Whiteboard Process
[](./wh1313.png)
حغ
## Approach & Efficiency
#  a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
#  Linked List class, include a head property.
# Upon instantiation, an empty Linked List should be created.
# The class should contain the following methods
# insert
# Arguments: value
# Returns: nothing


## big O :
## Insertion at the Head (insert method): O(1)
# The insertion at the head of a linked list has a constant time complexity since it involves updating the head reference and linking the new node to the previous head node. This operation does not depend on the size of the linked list and can be performed in constant time.

# Searching for a Value (includes method): O(n)
# The searching operation in a linked list requires traversing through the list from the head to the tail to check if the value exists. In the worst case, where the value is at the end of the list or does not exist, the algorithm will have to iterate over all the nodes. Hence, the time complexity is linear and proportional to the size of the linked list, denoted as O(n).

# String Representation (to_string method): O(n)
# Generating the string representation of a linked list involves iterating through each node and appending its value to the resulting string. This requires visiting each node once, resulting in a time complexity proportional to the size of the linked list, denoted as O(n).

# Overall, the time complexities for the operations in the Linked List implementation are:

# Insertion at the Head: O(1)
# Searching for a Value: O(n)
# String Representation: O(n)
# Adds a new node with that value to the head of the list with an O(1) Time performance.

## Solution
# pytest test_linked_list
[](../tests/test_linked_list.py)
