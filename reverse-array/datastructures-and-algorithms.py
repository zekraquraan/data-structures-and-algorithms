def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        # Swap elements at opposite ends of the array
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr

input_array = [1, 2, 3, 4, 5]
output_array = reverseArray(input_array)
print(output_array)


def test_reverseArray():
    # Happy path test case
    input_arr = [1, 2, 3, 4, 5]
    expected_output = [5, 4, 3, 2, 1]
    assert reverseArray(input_arr) == expected_output

    # Test case with empty array
    input_arr = []
    expected_output = []
    assert reverseArray(input_arr) == expected_output

    # Test case with single element array
    input_arr = [1]
    expected_output = [1]
    assert reverseArray(input_arr) == expected_output

    # Test case with duplicate elements
    input_arr = [1, 2, 2, 3, 3, 3]
    expected_output = [3, 3, 3, 2, 2, 1]
    assert reverseArray(input_arr) == expected_output

    # Test case with non-numeric elements
    input_arr = ['a', 'b', 'c']
    expected_output = ['c', 'b', 'a']
    assert reverseArray(input_arr) == expected_output

    # Test case with mixed data types
    input_arr = [1, 'a', 2, 'b', 3]
    expected_output = [3, 'b', 2, 'a', 1]
    assert reverseArray(input_arr) == expected_output

