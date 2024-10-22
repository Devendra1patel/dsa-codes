# Problem 5 : Given an array of both positive and negative numbers, find two numbers such that their sum is
# closest to 0. Ex: [ 1 ,60 ,-10, 70, -80,85]. Ans : -80,85.

# def matchNum(arr):
#     last_dif = None
#     ele_set = [arr[0]]
#     for x  in range(1,len(arr)):
#         if last_dif == None:
#             last_dif = abs(ele_set[0] + arr[x])
#             ele_set.append(arr[x])
#         if abs(ele_set[1] + arr[x]) < last_dif:
#             last_dif  = abs(ele_set[1] + arr[x])
#             ele_set.pop(0)
#             ele_set.append(arr[x])
#     return ele_set
# arr_t = [ 1 ,60 ,-10, 70, -80,85]
# print(matchNum(arr_t))

def matchNum1(arr):
    if len(arr)<1:
        return None
    if len(arr) ==1:
        return arr[0]
    sum = None
    sum_ele = [arr[0]] 
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if(sum == None):
                sum = abs(arr[i] + arr[j])
                sum_ele.append(arr[j])
            elif abs(arr[i] + arr[j]) < sum :
                sum = abs(arr[i] + arr[j])
                sum_ele = []
                sum_ele = [arr[i], arr[j]]
                # sum_ele.append(arr[i])
                # sum_ele.append(arr[j])
                
    return sum_ele
                
print(matchNum1([ 1 ,60 ,-10, 70, -80,85]))
        
     
