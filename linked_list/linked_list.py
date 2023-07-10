class Node:
<<<<<<< HEAD
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
=======
    def __init__(self, value):
        """
        Initialize a Node object with a given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList object with no head.
        """
        self.head = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the list.

        Args:
            value: The value to be appended.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, value):
        """
        Insert a new node with the given value at the beginning of the list.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_before(self, target_value, new_value):
        """
        Insert a new node with the new value before the node with the target value.

        If the target value is not found, the new node will not be inserted.

        Args:
            target_value: The value of the node before which the new node should be inserted.
            new_value: The value to be inserted.
        """
        new_node = Node(new_value)
        if not self.head:
            return
        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def insert_after(self, target_value, new_value):
        """
        Insert a new node with the new value after the node with the target value.

        If the target value is not found, the new node will not be inserted.

        Args:
            target_value: The value of the node after which the new node should be inserted.
            new_value: The value to be inserted.
        """
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def includes(self, value):
        """
        Check if the list contains a node with the given value.
>>>>>>> origin/main

        Args:
            value: The value to search for.

        Returns:
<<<<<<< HEAD
            True if a node with the value is found, False otherwise.
=======
            True if the value is found, False otherwise.
>>>>>>> origin/main
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
<<<<<<< HEAD
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list in the format:
            "{ value1 } -> { value2 } -> ... -> NULL"
        """
        if not self.head:
            return "NULL"

        current = self.head
=======
        Convert the linked list to a string representation.

        Returns:
            A string representation of the linked list.
        """
>>>>>>> origin/main
        result = ""
        current = self.head
        while current:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        result += "NULL"
        return result
