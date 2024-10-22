# Q.4 Find the sum of the values of the array [92, 23, 15, -20, 10].
def findSum(arr,ind):
    if ind<= 0:
        return arr[ind]
    return arr[ind] + findSum(arr,ind-1)

arr =[92, 23, 15, -20, 10]
print(findSum(arr,len(arr)-1))