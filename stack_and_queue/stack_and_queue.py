class Node:
    def __init__(self, value):
        """
        Initialize a Node with the given value.
        """
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """
        Initialize an empty Stack.
        """
        self.top = None

    def push(self, value):
        """
        Add a new node with the given value to the top of the stack.

        Args:
            value: The value to be added.

        Returns:
            None
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Remove and return the value from the node at the top of the stack.

        Returns:
            The value from the node at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        """
        Return the value from the node at the top of the stack without removing it.

        Returns:
            The value from the node at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None


class Queue:
    def __init__(self):
        """
        Initialize an empty Queue.
        """
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Add a new node with the given value to the back of the queue.

        Args:
            value: The value to be added.

        Returns:
            None
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Remove and return the value from the node at the front of the queue.

        Returns:
            The value from the node at the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return dequeued_value

    def peek(self):
        """
        Return the value from the node at the front of the queue without removing it.

        Returns:
            The value from the node at the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.is_empty())  # Output: False
