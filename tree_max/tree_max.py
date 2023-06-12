class BinaryTree:
    """
    A class representing a binary tree.

    Attributes:
        value (number): The value stored in the node.
        left (BinaryTree): The left child of the node.
        right (BinaryTree): The right child of the node.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the BinaryTree class.

        Args:
            value (number): The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def findMaximumValue(self):
        """
        Finds the maximum value stored in the binary tree.

        Returns:
            number: The maximum value in the binary tree.
        """
        stack = [self]  # Start with the root node
        max_value = float('-inf')

        while stack:
            node = stack.pop()

            if node.value > max_value:
                max_value = node.value

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return max_value


tree = BinaryTree(10)
tree.left = BinaryTree(5)
tree.right = BinaryTree(15)
tree.left.left = BinaryTree(3)
tree.left.right = BinaryTree(7)
tree.right.left = BinaryTree(12)
tree.right.right = BinaryTree(20)

max_value = tree.findMaximumValue()
print(max_value)  # Output: 20

