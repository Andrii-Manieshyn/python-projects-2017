"""
Sieve of Eratosthenes

The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
"""

def sieve_of_eratosthenes(n):
    sieve = [i for i in range(1,n + 1)]
    i = 1
    stack_of_indexes = []
    while i < len(sieve):
        value = sieve[i]
        l = len(sieve)
        for j in range(sieve.index(value)+1, l):
            if sieve[j] % value == 0 :
                stack_of_indexes.append(j)
        i+=1

    for i in sorted(set(stack_of_indexes),reverse=True):
        del(sieve[i])
    return sieve