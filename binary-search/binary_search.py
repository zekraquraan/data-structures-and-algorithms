def BinarySearch(arr,x) :
    low=0
    high=len(arr)-1
    while low <= high :
        mid=low+(high-low)//2 
        if arr[mid]==x :
            return mid 
        elif arr[mid]<x :
            low=mid+1
        else :high=mid-1
    return -1

arr=[4,8,15,16,23,42]
x=23
result=BinarySearch(arr,x)
print (result)




    
