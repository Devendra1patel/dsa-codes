'''Permutations of given Strin A permutation also called an “arrangement
number” or “order,” is a rearrangement of the elements of
an ordered list S into a one-to-one correspondence with S itself.
A string of length N has N! permutations.
Input: S = “ABC” Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB” '''

# this is my own logic -- need some improvements
def permutation(str , start):
    if start== len(str):
        print(str)
    else:
        str_list = list(str)
        for i in range(start, len(str_list)):
            str_list[start], str_list[i] =  str_list[i], str_list[start]
            str2 = "".join(str_list)
            permutation(str2, start+1)
    
permutation("abcd",0)