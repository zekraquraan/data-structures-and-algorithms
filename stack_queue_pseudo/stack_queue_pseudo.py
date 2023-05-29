class Stack:

    """Implementation of a Stack data structure."""

    def __init__(self):
        self.stack=[]

    def push(self,value):

        """Pushes a value onto the top of the stack."""

        self.stack.append(value)

    def pop(self):

        """Removes and returns the value at the top of the stack."""

        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):

        """Returns the value at the top of the stack without removing it."""

        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
        
    def is_empty(self):

        """Checks if the stack is empty."""

        return len(self.stack) == 0
    


    
class PseudoQueue:

    """Implementation of a queue using two stacks."""

    def __init__(self):
        """Initialize the PseudoQueue."""
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        """
        Inserts a value into the PseudoQueue using a first-in, first-out approach.

        Args:
            value: The value to be inserted into the PseudoQueue.
        """
        while not self.stack_1.is_empty():
            self.stack_2.push(self.stack_1.pop())
        self.stack_1.push(value)
        while not self.stack_2.is_empty():
            self.stack_1.push(self.stack_2.pop())

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue using a first-in, first-out approach.

        Returns:
            The value extracted from the PseudoQueue.

        Raises:
            IndexError: If the PseudoQueue is empty.
        """
        if not self.stack_1.is_empty():
            return self.stack_1.pop()
        else:
            raise IndexError("PseudoQueue is empty")



if __name__ == "__main__":
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(10)
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(20)
    print(pseudo_queue.dequeue())  # Output: 10
    print(pseudo_queue.dequeue())  # Output: 15
    print(pseudo_queue.dequeue())  # Output: 20

