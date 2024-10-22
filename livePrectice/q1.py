arr = [1,9,4,23,2,99,100]
ind = 0
min = 9999999
def fun(arr,min,ind):
    if ind == len(arr) - 1:
        return min
    if min > arr[ind]:
        min = arr[ind]
        ind += 1
    print(ind,"-->",min)
    fun(arr,min,ind)

print(fun(arr,ind,min))
