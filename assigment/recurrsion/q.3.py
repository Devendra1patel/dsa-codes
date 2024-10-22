# Q. 3 Print the max value of the array [ 13, 1, -3, 22, 5].
def maximum(arr,ind):
    if ind <= 0:
        return arr[ind]
    max = maximum(arr, ind-1)
    if max > arr[ind]:
        return max
    else:
        return arr[ind]
    '''
    --imporove code line
            return max(arr[ind],maximum(arr,ind-1))
    '''

print(maximum([3,400,2,8,40,0,23,4,200,],6))

# 