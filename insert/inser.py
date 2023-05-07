import math

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def insert(arr, num):
    if len(arr)<2:
        arr.append(num)
        return arr
    
    
    size = len(arr)
    arr.append(num)
    
    i = size
    while i > math.ceil(size / 2):
        swap(arr, i, i-1)
        i -= 1
        
    return arr
    
print(insert([42, 18, 15, 42], 55))
print(insert([2, 4, 6,-8], 5))