# Problem 14: Given a sorted array and a target value, return the index if the target is found. If not, return the
# index where it would be inserted.
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2

def findInsert(arr, num):
    length = len(arr)
    if length ==0:
        return -1
    for i in range(0, length):
        if num < arr[i]:
            return i
        if num == arr[i]:
            return i
        
print(findInsert([1,2,3,4,5,65,67],49))

