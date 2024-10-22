'''Problem 1 : Find the Rotation Count in Rotated Sorted array Input: arr[] = {15, 18, 2, 3, 6, 12}
            Output: 2 Explanation: Initial array must be {2, 3, 6, 12, 15, 18}.
            We get the given array after rotating the initial array twice. '''

''' 
def findRotation(arr):
    for i in range(1,len(arr)-1):
        if len(arr) == 2:
            if arr[0] <= arr[1]:
                return 0
            else:
                return 1
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return i
    if len(arr) == 1:
            return 0
    if arr[0] < arr[len(arr)]:
         return 0
    else:
         return len(arr)-1
        
arr = [13, 15, 18, 2]
print(findRotation(arr)) 

'''

#    --------------    -----------------------    --------------------------    --------------------

# Assignment 1 : Solve the same above problem with linear search approach | Tier 2 companies

'''

'''
# ------------------   -----------------------    --------------------------    --------------------
# Assignment 2: Solve the same problem with Binary Search Approach | FAANG

def searchBinary(arr, min, max):
    # if min < max :
    #     midle = (min+max)/2
    #     if arr[midle] < arr[midle-1] and arr[midle] < arr[midle+1] :
    #         return midle
    #     else:
    #         searchBinary(arr,min,midle)
    #         searchBinary(arr,midle,max)

# -------------------   ---------------------    --------------------------     --------------------
 '''   Problem 2 : Given an array of integers, print the array in such a way that the first element is first maximum and second element 
    is first minimum and so on.
    Examples : Input : arr[] = {7, 1, 2, 3, 4, 5, 6} Output : 7 1 6 2 5 3 4'''
 
def maxmin(arr):
    mm  = [0, 0]
    if len(arr) == 0:
        return [-1,-1]
    for i in range(1,len(arr)):
            if( arr[mm[0]] < arr[i] ):
               mm[0] = i
            if( arr[mm[1]] > arr[i]):
               mm[1] = i
    # print(mm)
    return mm

def wavearr(arr):
    newarr = []
    length = len(arr)
    for i in range(0,length//2):
        mm =  maxmin(arr)
        
        # if mm[0] == mm[1]:
        newarr.append(arr[mm[0]])
            
        newarr.append(arr[mm[1]])
        del arr[mm[0]]
        if(mm[0]< mm[1]):
            mm[1] = mm[1]-1
        if mm[0] != mm[1]:
            del arr[mm[1]]
        print("full- ",arr,"->",newarr,"--",mm)
        
    print(newarr)

wavearr([7, 1, 2, 3, 4, 5, 6])


        
        


# maxmin([3,54593,2485,4843734,493,34])
  
       

            




        