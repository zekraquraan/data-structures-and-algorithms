import pytest

<<<<<<< HEAD
from linked_list.linked_list import LinkedList,Node

def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_single_node():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5


def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.head.value == 15
    assert ll.head.next.value == 10
    assert ll.head.next.next.value == 5

def test_includes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.includes(10) == True
    assert ll.includes(20) == False

def test_to_string():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"
=======
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
>>>>>>> origin/main
