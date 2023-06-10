import unittest
from trees_binary.trees import BinarySearchTree

class BinarySearchTreeTests(unittest.TestCase):
    def test_instantiating_empty_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)

    def test_instantiating_tree_with_single_root(self):
        tree = BinarySearchTree()
        tree.add(5)
        self.assertEqual(tree.root.value, 5)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_adding_left_and_right_child_to_node(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.right.value, 7)

    def test_preorder_traversal(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)
        expected_result = [5, 3, 2, 4, 7, 6, 8]
        self.assertEqual(tree.preorder_traversal(), expected_result)

    def test_inorder_traversal(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)
        expected_result = [2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(tree.inorder_traversal(), expected_result)

    def test_postorder_traversal(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)
        expected_result = [2, 4, 3, 6, 8, 7, 5]
        self.assertEqual(tree.postorder_traversal(), expected_result)

    def test_contains_existing_value(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)
        self.assertTrue(tree.contains(4))

    def test_contains_non_existing_value(self):
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)
        self.assertFalse(tree.contains(9))


if __name__ == '__main__':
    unittest.main()
