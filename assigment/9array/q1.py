# 1. Given an array, check if it contains any duplicates or not.
arr = [1, 2, 4, 2, 5, 9]
# Output = True

# method-1
def duplicate(arr):
       set1 = set(arr)
       print(set1)
       if(len(arr) == len(set1) ):
              return False
       else:
         return True
print(duplicate(arr))


def duplicate2(arr):
    obj = {}
    for i in range(len(arr)):
        if arr[i] in obj and  obj[arr[i]] == 1:
            return True
        obj[arr[i]] = 1
    return False
print(duplicate2(arr))
        
