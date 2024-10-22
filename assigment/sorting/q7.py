# Sort an array of 0’s, 1’s and 2’s [or R’s, G’s and B’s]: Given an array A[] consisting of 0’s, 1’s and
# 2’s, give an algorithm for sorting A[].The algorithm should put all 0’s first, then all 1’s and finally all 2’s at the
# end. Example Input = {0,1,1,0,1,2,1,2,0,0,0,1}, Output = {0,0,0,0,0,1,1,1,1,1,2,2}

def sortarr1(arr):
    ind = [-1,-1,-1]
    for i in range(len(arr)):
        if( arr[i]==0 ):
            del arr[i]
            print(arr)
            arr.insert(ind[0]+1,0)
            ind[0] = ind[0] + 1
            ind[1] +=1
            ind[2] +=1
            
        if( arr[i]==1 ):
            del arr[i]
            arr.insert(ind[1]+1,1)
            ind[1] +=1
            ind[2] +=1
            
        if( arr[i]==2 ):
            del arr[i]
            arr.insert(ind[2]+1,2)
            ind[2] +=1
    return arr
print(sortarr1([0,1,1,0,1,2,1,2,0,0,0,1]))