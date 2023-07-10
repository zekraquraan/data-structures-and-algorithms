def reverseArray(arr):
    n = len(arr)
    for i in range(n // 2):
        # Swap elements at opposite ends of the array
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr

input_array = [1, 2, 3, 4, 5]
output_array = reverseArray(input_array)
print(output_array)


    

   

