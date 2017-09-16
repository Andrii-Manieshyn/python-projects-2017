def fast_power(value, pow):
    result = 1
    while (pow > 0):
        print(pow)
        if pow % 2 == 1:
            result *= value
        value *= value
        pow //= 2
        print(pow)
    return result
