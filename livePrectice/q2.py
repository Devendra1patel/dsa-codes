arr = [ 20, 2, 4 ,5, 9, 10, 15]

def binary():
    
    mid = arr.len()/2
    if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
        return mid
    