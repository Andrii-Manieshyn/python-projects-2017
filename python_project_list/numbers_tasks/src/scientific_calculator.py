"""
Calculator

A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

1) Realization already exists in python interpreter in terminal, only custom scrip required to import math package
2) same with eval function
3) Current realization will contain reverse polish notation
"""
from math import *

functions = ['exp', 'sin', 'cos', 'ln', 'lg']
function_mapping={
    'exp': lambda x : exp(x),
    'sin': lambda x : sin(x),
    'cos': lambda x : cos(x),
    'ln': lambda x : log(x, e),
    'lg': lambda x : log(x, 10),
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
}

def reverse_polish_notation(expression):
    """
    Return reverse polish notation. Input has rules to make algorithm easier
    Rules for correct program flow
        1) Everything should be passed with space separation
        2) Please keep in mind available functions
        3) Unknown parameters are forbidden
        4) Functions parameters should be put in brackets
        5) Available functions: exp, sin, cos, ln, lg, ^, *, /, +, -, () -- priority order from higher to lower
    Example of valid expression: 'exp ( -1 / 2 * 5 )'

    :param expression: string that will be converted to stack with reverse polish notation
    :return: stack
    """
    array_of_exp = expression.split(' ')
    reverse_polish_stack = []
    symbol_stack = []
    for symbol in array_of_exp:
        if symbol.lstrip('-+').isdigit():
            reverse_polish_stack.append(symbol)
        elif symbol in functions:
            symbol_stack.append(symbol)
        elif symbol == '(':
            symbol_stack.append(symbol)
        elif symbol == ')':
            stack_s = symbol_stack.pop()
            while stack_s != '(':
                reverse_polish_stack.append(stack_s)
                stack_s = symbol_stack.pop()

            stack_s = symbol_stack.pop()
            if stack_s in functions :
                reverse_polish_stack.append(stack_s)
            else :
                symbol_stack.append(stack_s)
        else :
            priority_current_symbol = get_priority(symbol)
            if (len(symbol_stack) != 0) :
                stack_symbol = symbol_stack.pop()
                priority_stack_symbol = get_priority(stack_symbol)

                while priority_current_symbol <= priority_stack_symbol:
                    reverse_polish_stack.append(stack_symbol)
                    stack_symbol = symbol_stack.pop()
                    priority_stack_symbol = get_priority(stack_symbol)

                symbol_stack.append(stack_symbol)
            symbol_stack.append(symbol)

    while len(symbol_stack) != 0:
        stack_s = symbol_stack.pop()
        reverse_polish_stack.append(stack_s)
    print(reverse_polish_stack)
    return reverse_polish_stack

def get_priority(symbol):
    if symbol == '^': return 4
    if symbol == '*' or symbol == '/': return 3
    if symbol == '+' or symbol == '-': return 2
    if symbol == '(' or symbol == ')': return 1


def calculate_reverse_polish_notation(notation):
    i = 0
    while len(notation)!=1:
        symbol = notation[i]
        if (symbol in functions) or (not symbol.replace('.','',1).lstrip('+-').isdigit()):
            if symbol in functions:
                res = 0
                j = i - 1
                digit = float(notation[j])
                res = function_mapping[symbol](digit)
                del (notation[j])
                del (notation[j])
                notation.insert(j, str(res))
                i = 0
            else :
                res = 0
                j = i - 1
                second_digit = float(notation[j])
                first_digit = float(notation[j-1])
                res = function_mapping[symbol](first_digit, second_digit)
                del (notation[j - 1])
                del (notation[j - 1])
                del (notation[j - 1])
                notation.insert(j - 1, str(res))
                i = 0
        i += 1
    return float(notation[0])

def calculate_expresion(exp):
    notation = reverse_polish_notation(exp)
    return calculate_reverse_polish_notation(notation)
