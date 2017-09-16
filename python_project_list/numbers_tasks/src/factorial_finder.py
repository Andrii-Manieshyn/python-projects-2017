def factorial_recursive(n):
    if n != 1 :
        return factorial_recursive(n-1) * n
    return n

def factorial_loops(n):
    a, i = 1, 1
    while i <= n:
        a = a * i
        i += 1
    return a
