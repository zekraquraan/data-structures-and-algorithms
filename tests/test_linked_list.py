from linked_list.linked_list import Node, LinkedList
import unittest

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_empty_list(self):
        self.assertEqual(self.linked_list.to_string(), "NULL")

    def test_insert(self):
        self.linked_list.insert(3)
        self.linked_list.insert(2)
        self.linked_list.insert(1)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> { 2 } -> { 3 } -> NULL")

    def test_includes(self):
        self.linked_list.insert(3)
        self.linked_list.insert(2)
        self.linked_list.insert(1)
        self.assertTrue(self.linked_list.includes(2))
        self.assertFalse(self.linked_list.includes(4))

    def test_append(self):
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> NULL")

    def test_append_multiple_nodes(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> { 2 } -> { 3 } -> NULL")

    def test_insert_before_middle_node(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.insert_before(2, 5)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> { 5 } -> { 2 } -> { 3 } -> NULL")

    def test_insert_before_first_node(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.insert_before(1, 5)
        self.assertEqual(self.linked_list.to_string(), "{ 5 } -> { 1 } -> { 2 } -> NULL")

    def test_insert_after_middle_node(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.insert_after(2, 5)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> { 2 } -> { 5 } -> { 3 } -> NULL")

    def test_insert_after_last_node(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.insert_after(2, 5)
        self.assertEqual(self.linked_list.to_string(), "{ 1 } -> { 2 } -> { 5 } -> NULL")

if __name__ == '__main__':
    unittest.main()
