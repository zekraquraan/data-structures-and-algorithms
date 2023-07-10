def insertion_sort(arr):
    for i in range(len(arr)):
        current_value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_value