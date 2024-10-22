
# Problem 1.Given an array of n numbers, give an algorithm which gives the element appearing maximum
# number of times?




def selection(arr):
    for i in range(0,len(arr)):
        index = i
        for j in range(i+1,len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[index],arr[i] = arr[i],arr[index]
    print(arr)

print(selection([3,5,2,48,6,12,1]))