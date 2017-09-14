"""
Mortgage Calculator

Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
Also figure out how long it will take the user to pay back the loan.
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
"""
from enum import Enum

class Interval(Enum):
    MONTHLY = 12.0
    WEEKLY = 52.1429
    DAILY = 365.0

term = int(input('Enter term: '))
print()
interest_rate = float(input('Enter interest rate: '))
print()
loan = float(input('Enter loan: '))
print()
interval = Interval[str(input('Enter interval: '))]
print()


monthly_rate = interest_rate / 100 / interval.value
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-term))) * loan

print ("Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (term / interval.value), interest_rate, payment))