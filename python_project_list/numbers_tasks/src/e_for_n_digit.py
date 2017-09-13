"""
Find e to the Nth Digit

Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up
to that many decimal places. Keep a limit to how far the program will go.
"""

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

