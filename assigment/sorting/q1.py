# Problem 1.Given an array of n numbers, give an algorithm which gives the element appearing maximum
# number of times?
def max_occurance(arr):
    dict = {}
    for i in range(0,len(arr)):
        
        if( dict.get(arr[i])!=None ):
            dict[arr[i]] = dict.get(arr[i])+1
         
        else:
            dict[arr[i]] = 1
    element = arr[0]
    for key in dict:
        if(dict[key] > dict[element] ):
            element = key
    return element

arr = [1,5,4,29,4,76,403,5,9]
print(max_occurance(arr))
