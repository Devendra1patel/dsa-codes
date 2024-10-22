def powerfun(value,pow):
    result = 1
    for i in range(1,pow):
        result = result*value
    return result

def armstrong(value,digits):
    if value//10 <= 0:
        return value
    return powerfun(value%10,digits) + armstrong(value//10,digits)
    

print(armstrong(153,3))