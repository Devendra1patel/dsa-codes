# Problem 4 : Given an array of n elements. Find two elements in the array such that their sum is equal to given
# element K.
def find(arr,index,y):
    for i in range(0,len(arr)):
        if(i == index ):
            i+=1
        if(y == arr[i]):
            return i
    return -1

def findEqual(arr,k):
    ans = []
    for i in range(0,len(arr)):
        y = k - arr[i]
        y = find(arr,i,y)
        if(y == -1):
            pass
        else:
            ans = {arr[i], arr[y]}
            return ans

# find([1,2,4,6,3,7,8],3,5)
print(findEqual([1,2,4,6,3,7,8],9))
        
    
    