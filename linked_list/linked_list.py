class Node:
    """
    Node class represents a node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, value, _next=None):
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
            _next: Reference to the next node (default is None).
        """
        self.value = value
        self.next = _next


class LinkedList:
    """
    LinkedList class represents a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """

    def __init__(self, head=None):
        """
        Initializes a new instance of the LinkedList class.

        Args:
            head: The head node of the linked list (default is None).
        """
        self.head = head

    def insert(self, value):
        """
        Inserts a new node with the specified value at the beginning of the linked list.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """
        Checks if a node with the specified value exists in the linked list.

        Args:
            value: The value to search for.

        Returns:
            True if a node with the value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list in the format:
            "{ value1 } -> { value2 } -> ... -> NULL"
        """
        if not self.head:
            return "NULL"

        current = self.head
        result = ""
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result
