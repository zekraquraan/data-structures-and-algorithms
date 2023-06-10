class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self):
        result = []
        self._preorder_util(self.root, result)
        return result

    def _preorder_util(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_util(node.left, result)
            self._preorder_util(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_util(self.root, result)
        return result

    def _inorder_util(self, node, result):
        if node:
            self._inorder_util(node.left, result)
            result.append(node.value)
            self._inorder_util(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_util(self.root, result)
        return result

    def _postorder_util(self, node, result):
        if node:
            self._postorder_util(node.left, result)
            self._postorder_util(node.right, result)
            result.append(node.value)
class BinarySearchTree(BinaryTree):
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_util(self.root, value)

    def _add_util(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_util(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_util(node.right, value)

    def contains(self, value):
        return self._contains_util(self.root, value)

    def _contains_util(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains_util(node.left, value)
        else:
            return self._contains_util(node.right, value)


class KTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class KaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent=None):
        new_node = KTreeNode(value)
        
        if parent is None:
            if self.root is not None:
                raise ValueError("The tree already has a root.")
            self.root = new_node
        else:
            parent.children.append(new_node)

    def traverse(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)
            queue.extend(current.children)

        return result
