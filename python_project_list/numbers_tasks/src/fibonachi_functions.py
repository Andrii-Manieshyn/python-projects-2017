"""
Fibonacci Sequence

Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def fibonacci(n):
    f1, f2 = 0, 1
    for i in range(0, n):
        f1, f2 = f2, f1 + f2
    return f1
