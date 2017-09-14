"""
Binary to Decimal and Back Converter

Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""

def decimal_to_binary(decimal):
    """
    Function convert decimal number to binary

    :param decimal: integer number to convert
    :return: string representation of binary result
    """
    return bin(decimal)

def binary_to_decimal(binary):
    """
    Function convert binary number to integer

    :param binary: string that present binary number
    :return: integer converted from binary number
    """
    return int(binary, 2)
