# Challenge Title
stack and queue


## Whiteboard Process

## Approach & Efficiency
Stack:

Push operation: When pushing a new value onto the stack, a new node is created and its next pointer is set to the current top of the stack. The top pointer is then updated to point to the new node. This operation has a time complexity of O(1) since it takes a constant amount of time to perform, regardless of the size of the stack.

Pop operation: When popping a value from the stack, the value from the top node is retrieved, and the top pointer is updated to point to the next node in the stack. The popped value is returned. This operation also has a time complexity of O(1) as it takes a constant amount of time to perform.

Peek operation: The peek operation returns the value from the top node of the stack without modifying the stack. It simply returns the value stored in the top node. This operation has a time complexity of O(1) since it only requires accessing the value of the top node.

Is empty operation: The is_empty operation checks if the stack is empty by evaluating whether the top pointer is None. It returns a Boolean value indicating whether the stack is empty or not. This operation has a time complexity of O(1) as it only involves a single comparison.

Queue:

Enqueue operation: When enqueuing a new value into the queue, a new node is created and added to the back of the queue. If the queue is empty, both the front and back pointers are updated to point to the new node. Otherwise, the back pointer is updated to point to the new node, and the next pointer of the current back node is set to the new node. This operation has a time complexity of O(1) as it takes a constant amount of time to perform.

Dequeue operation: When dequeuing a value from the queue, the value from the front node is retrieved, and the front pointer is updated to point to the next node in the queue. If the front becomes None after updating, it means the queue is empty, and the back pointer is also set to None. The dequeued value is returned. This operation has a time complexity of O(1) as it takes a constant amount of time to perform.

Peek operation: The peek operation returns the value from the front node of the queue without modifying the queue. It simply returns the value stored in the front node. This operation has a time complexity of O(1) since it only requires accessing the value of the front node.

Is empty operation: The is_empty operation checks if the queue is empty by evaluating whether the front pointer is None. It returns a Boolean value indicating whether the queue is empty or not. This operation has a time complexity of O(1) as it only involves a single comparison.

In terms of efficiency, both the Stack and Queue implementations using a linked list have constant-time complexity (O(1)) for the core operations like push, pop, enqueue, and dequeue. These operations do not depend on the size of the stack or queue, as they only involve updating a few pointers. Thus, these implementations provide efficient and constant-time access to the top/front elements and support efficient insertion and removal of elements.









## big O :

For the Stack:

Push: O(1) - Adding a new element to the top of the stack takes constant time.
Pop: O(1) - Removing the top element from the stack also takes constant time.
Peek: O(1) - Accessing the value of the top element takes constant time.
Is empty: O(1) - Checking if the stack is empty can be done in constant time.
For the Queue:

Enqueue: O(1) - Adding a new element to the back of the queue takes constant time.
Dequeue: O(1) - Removing the front element from the queue also takes constant time.
Peek: O(1) - Accessing the value of the front element takes constant time.
Is empty: O(1) - Checking if the queue is empty can be done in constant time.
In both cases, the time complexity is constant (O(1)) for these operations because the underlying linked list allows for efficient insertion and removal at the respective ends (top/front).

## Solution:
pytest test_stack_and_queue