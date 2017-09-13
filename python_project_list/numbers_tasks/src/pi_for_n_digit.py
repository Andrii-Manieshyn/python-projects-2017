'''
Find PI to the Nth Digit

Enter a number and have the program generate PI up to that
many decimal places. Keep a limit to how far the program will go.
'''

from decimal import *

def find_pi_to_n_digit(i):
    getcontext().prec = i + 10
    calculated_pi = Decimal(0)
    n = 0
    while n < i:
        calculated_pi += (Decimal(1) / (16 ** n)) * ((Decimal(4) / (8 * n + 1)) -
                                                     (Decimal(2) / (8 * n + 4)) -
                                                     (Decimal(1) / (8 * n + 5)) -
                                                     (Decimal(1) / (8 * n + 6)))
        n += 1
    return format(str(calculated_pi)[:len(str(calculated_pi)) - 9])

'''
No explanation for magic numbers "10" and "9" :(
Something about rounding in formula calculation
'''