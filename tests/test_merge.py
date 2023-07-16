import pytest
from sorting.megre.merge import merge_sort


def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    arr = merge_sort(arr)
    assert arr == expected_result

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    expected_result = [1, 2, 3, 4, 5]
    arr = merge_sort(arr)
    assert arr == expected_result

def test_random_array():
    arr = [10, 2, 7, 1, 5]
    expected_result = [1, 2, 5, 7, 10]
    arr = merge_sort(arr)
    assert arr == expected_result


def test_negative_numbers():
    arr = [-5, -2, -8, -1, -3]
    expected_result = [-8, -5, -3, -2, -1]
    arr = merge_sort(arr)
    assert arr == expected_result


def test_reverse_sorted_large_array():
    arr = list(range(1000, 0, -1))
    expected_result = list(range(1, 1001))
    arr = merge_sort(arr)
    assert arr == expected_result

def test_single_element_array():
    arr = [42]
    expected_result = [42]
    arr = merge_sort(arr)
    assert arr == expected_result

