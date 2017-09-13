"""
Next Prime Number

Have the program find prime numbers until the user chooses to stop asking for the next one.

Solution is quite sophisticated but I just wanted to use Generator and yield.
No tests, just console input and output.
"""

from numbers_tasks.src.prime_factorization import factorization

def next_prime_number():
    i = 1
    while True:
        prime_factorization_list = factorization(i)
        if len(prime_factorization_list) == 0 :
            yield i
        i += 1



if __name__ == '__main__':
    input_str = str (input("Do you want to get next prime number?\n"))
    for i in next_prime_number():
        print(i)
        input_str = str(input("Do you want to get next prime number?\n"))
        if input_str.startswith("y") or input_str.startswith("Y") or input_str.startswith("Yes"):
            continue
        else:
            break