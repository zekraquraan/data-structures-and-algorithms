from linked_list.linked_list import Node, LinkedList


class LinkedListTests(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.to_string(), "NULL")

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.insert(3)
        linked_list.insert(2)
        linked_list.insert(1)
        self.assertEqual(linked_list.to_string(), "{ 1 } -> { 2 } -> { 3 } -> NULL")

    def test_includes(self):
        linked_list = LinkedList()
        linked_list.insert(3)
        linked_list.insert(2)
        linked_list.insert(1)
        self.assertTrue(linked_list.includes(2))
        self.assertFalse(linked_list.includes(4))

if __name__ == "__main__":
    unittest.main()
