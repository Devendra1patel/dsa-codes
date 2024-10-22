'''
Q.5 Given a number n. Print if it is an armstrong number or not.An armstrong number is a number if the sum
of every digit in that number raised to the power of total digits in that number is equal to the number.
Example : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 hence 153 is an armstrong number. (Easy)
Input1 : 153
Output1 : Yes
Input 2 : 134
Output2 : No
'''  
def powerfun(value,pow):
    result = 1
    for i in range(1,pow+1):
        result = result*value
    return result

def subArmstrong(value,digits):
    if value//10 <= 0:
        return value
    return powerfun(value%10,digits) + armstrong(value//10,digits)

def armstrong(value,digits):
    result = subArmstrong(value,digits)
    if result == value:
        return "Yes"
    else:
        return "No"


print(armstrong(-153,3))