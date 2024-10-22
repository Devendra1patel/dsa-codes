# Problem 2 : We are given a list of n-1 integers and these integers are in the range of 1 to n . There are no
# duplicates in the list. One of the integers is missing in the list. Give an algorithm to find that element Ex:
# [1,2,4,6,3,7,8] 5 is the missing num.

def findmissing(arr):
    dict = {}
    for i in range(0,len(arr)):
        dict[arr[i]] = 1
    for i in range(1,len(arr)+2):
       if (dict.get(i)==None):
           return i
arr = [1,2,4,6,3,7,8]
print(findmissing(arr))
