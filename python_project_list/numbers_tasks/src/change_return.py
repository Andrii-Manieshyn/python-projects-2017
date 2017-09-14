"""
Change Return Program

The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""

from enum import Enum

class Currency(Enum):
    DOLLAR = 100
    QUARTER = 25
    DIMES = 10
    NICKLE = 5
    PENNY = 1

def return_change(cost):

    change_dict = {}

    cost_in_coins = cost * 100

    dollars = int(cost_in_coins // Currency.DOLLAR.value)
    if (dollars != 0) and (cost_in_coins // Currency.DOLLAR.value != 0): change_dict['dollars'] = dollars
    cost_in_coins %= Currency.DOLLAR.value

    quarters = int(cost_in_coins // Currency.QUARTER.value)
    if quarters != 0 and (cost_in_coins // Currency.QUARTER.value != 0): change_dict['quarters'] = quarters
    cost_in_coins %= Currency.QUARTER.value

    dimes = int(cost_in_coins // Currency.DIMES.value)
    if dimes != 0 and (cost_in_coins // Currency.DIMES.value != 0): change_dict['dimes'] = dimes
    cost_in_coins %= Currency.DIMES.value

    nickles = int(cost_in_coins // Currency.NICKLE.value)
    if nickles != 0 and (cost_in_coins // Currency.NICKLE.value != 0): change_dict['nickles'] = nickles
    cost_in_coins %= Currency.NICKLE.value

    penny = int(cost_in_coins // Currency.PENNY.value)
    if penny != 0 and (cost_in_coins // Currency.PENNY.value != 0): change_dict['pennies'] = penny

    return change_dict