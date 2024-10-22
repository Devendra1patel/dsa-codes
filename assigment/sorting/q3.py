# Problem 3 : Given an array of n positive numbers. All numbers occurs even number of times except 1 which
# occurs odd number of times. Find that number in O(n) time and O(1) space. Ex: [1,2,3,2,3,1,3]. 3 is repeats odd
# times.
def findOdd(arr):
    setoflist = set(arr)
    sumUniqe = 0
    sumAll = 0
    for ele in setoflist:
        sumUniqe = ele + sumUniqe
    for i in range(0,len(arr)):
        sumAll = arr[i] + sumAll
    y = sumAll - sumUniqe*2 
    return y
        
        
arr = [1,2,3,2,3,1,3]
print(findOdd(arr))