# Challenge Title
linked list zip

## Whiteboard Process
![whiteboard](./wh1010.png)


## Approach & Efficiency
insert method: This method has a time complexity of O(1) since it simply creates a new node and updates the head attribute of the linked list. The space complexity is also O(1) since only one new node is created.

includes method: This method has a time complexity of O(n) in the worst case, where n is the number of nodes in the linked list. This is because we need to traverse the entire linked list to check whether a given value exists in it. The space complexity is O(1) since we only use a few variables to keep track of the current node and the result.

ToString method: This method has a time complexity of O(n) in the worst case, since we need to traverse the entire linked list to construct the string representation. The space complexity is O(n) since we create a new string object that contains all the values in the linked list.

append method is O(n), where n is the number of nodes in the linked list. This is because the method has to traverse the entire linked list to find the last node, so the time it takes to execute grows linearly with the size of the input. The space complexity is also O(1) since only one new node is created.

insert_before and Insert_After methods is O(n), where n is the number of nodes in the linked list. This is because in the worst case, the methods have to traverse the entire linked list to find the node with the specified value, so the time it takes to execute grows linearly with the size of the input. The space complexity is also O(1) since only one new node is created.

linked_list_kth methods is O(n^2), where n is the number of nodes in the linked list, the methods have to traverse the entire linked list to find the node with the specified value, and isert the value in the first index of the normal_list. The space complexity is also O(n) since new list is created.



## big O :
The time complexity of the linked_list_zip function is O(n),where n is the total number of nodes in both input linked lists.This is because the function traverses each node in the two lists exactly once while creating the merged list. The space complexity of the linked_list_zip function is O(n), because it creates a new empty list to store the merged node from two linked list.


## Solution
[solution](./linked_list_zip.py)
