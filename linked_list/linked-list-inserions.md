# Challenge Title
# linked-list-insertion


## Whiteboard Process

[whitboard_append](./append2.png)
[wh2_append](./append3.png)
[whitboard_after_before](./after%20befor2222222.png)
[wh_after_befor](./after_befor.png)
## Approach & Efficiency

# Append:

# Approach: Traverse the linked list until the last node is reached, then create a new node with the given value and make it the next node of the last node.
# Efficiency: This operation has a time complexity of O(n), where n is the number of nodes in the linked list. It requires traversing the entire list to reach the last node.

# Insert Before:

# Approach: Traverse the linked list and find the first node that has the specified value. Create a new node with the given new value and make it the next node of the node found. Adjust the references to correctly insert the new node before the found node.
# Efficiency: This operation has a time complexity of O(n), where n is the number of nodes in the linked list. In the worst case, it may need to traverse the entire list to find the node to insert before.

# Insert After:

# Approach: Traverse the linked list and find the first node that has the specified value. Create a new node with the given new value and make it the next node of the found node. Adjust the references to correctly insert the new node after the found node.
# Efficiency: This operation has a time complexity of O(n), where n is the number of nodes in the linked list. In the worst case, it may need to traverse the entire list to find the node to insert after.


## big O :
Append: O(n)

# The time complexity is O(n) because the algorithm needs to traverse the entire linked list to reach the last node and append the new node. The time taken increases linearly with the number of nodes in the list.
Insert Before: O(n)

# The time complexity is O(n) because in the worst case, the algorithm needs to traverse the entire linked list to find the node before which the new node is to be inserted. It involves searching for a specific value, which can take linear time.
Insert After: O(n)

# The time complexity is O(n) because in the worst case, the algorithm needs to traverse the entire linked list to find the node after which the new node is to be inserted. It involves searching for a specific value, which can take linear time.

## Solution
# pytest test_linked_list