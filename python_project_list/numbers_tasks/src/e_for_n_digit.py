from math import e
from decimal import Decimal, getcontext

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

def e_function(n):
    if n < 16 :
        return format(e, "." + str(n) + "f")
    getcontext().prec = n+10
    result = Decimal(1)
    for i in range(1, n + 10):
        result += Decimal(1) / factorial(i)
    return str(result)[:len(str(result)) - 9]

