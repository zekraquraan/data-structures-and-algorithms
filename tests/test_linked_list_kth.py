import pytest
from linked_list_kth.linked_list_kth import LinkedList

def test_kth_from_end_case1():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    assert linked_list.kth_from_end(5) is None

def test_kth_from_end_case2():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    assert linked_list.kth_from_end(4) == 1

def test_kth_from_end_case3():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    assert linked_list.kth_from_end(-2) is None

def test_kth_from_end_case4():
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.kth_from_end(1) == 1

def test_kth_from_end_case5():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    assert linked_list.kth_from_end(3) == 3

def test_kth_from_end_case6():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    assert linked_list.kth_from_end(0) is None

def test_kth_from_end_case7():
    linked_list = LinkedList()
    assert linked_list.kth_from_end(1) is None
