class Node:
    def __init__(self, value):
        """
        Initializes a Node object.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initializes an empty LinkedList object.
        """
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be appended.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def kth_from_end(self, k):
        """
        Returns the value of the node that is k places from the end of the linked list.

        Args:
            k: The distance from the end of the linked list. Must be a positive integer.

        Returns:
            The value of the node that is k places from the end of the linked list, or None if k is invalid.
        """
        if k <= 0:
            return None

        p1 = self.head
        p2 = self.head

        # Move p1 k places forward
        for _ in range(k):
            if p1 is None:
                return None
            p1 = p1.next

        # Move both pointers simultaneously until p1 reaches the end
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value
