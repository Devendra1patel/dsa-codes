
# this insertion sort algo code writen by me...
def insertion(arr):
    for i in range(0,len(arr)-1):
        val = arr[i+1]
        j=i
        lable = 1
        # for j in range(i,0,-1):
        while (j>=0 ):
            if val < arr[j]:
                lable=0
                arr[j+1] = arr[j]
            else:
                break
            j-=1
        if lable==0:
            arr[j+1] = val
                
    print(arr)


print(insertion([3,5,2,48,6,12,1]))
        