def rot(arr, k):

    for i in range(0,k):
        element = arr[len(arr)-1-i]
        for j in range(i,len(arr)-1):
            arr[len(arr)-1-j],arr[len(arr)-1-j+1] = arr[len(arr)-1-j+1], arr[len(arr)-1-j]

        arr[i]=element
    print(arr)

arr = [ 1,2,3,4,5,6]
k=2 
rot(arr,k)