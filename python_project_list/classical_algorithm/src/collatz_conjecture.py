"""
Collatz Conjecture

Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""

def collatz_function(n):
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            counter += 1
        else:
            n *= 3
            n += 1
            counter += 1
    return counter