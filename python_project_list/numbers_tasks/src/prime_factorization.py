"""
Prime Factorization

Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""
def factorization(n):
    prime_numbers_stack = []
    i, m = 2, n
    while i <= (m / 2):
        if n % i == 0:
            prime_numbers_stack.append(i)
            n = n / i
        else:
            i += 1
    return prime_numbers_stack
