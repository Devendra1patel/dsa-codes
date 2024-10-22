# Given an array of n elements . Find three elements such that their sum is equal to the given number.


def equal(arr,sum):
    
    arr_obj = {}
    for i in range(len(arr)):
        arr_obj[arr[i]] = i
    print(arr_obj)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if( arr_obj.get(sum - (arr[i]+arr[j]), False) != False ):
                return [arr[i],arr[j], sum - (arr[i]+arr[j]) ]
        if(i == len(arr)-1):
            print("helllo",i,len(arr)-1)
            return False

print(equal([1,2,3,4,5,6,8,9,7], 10))
