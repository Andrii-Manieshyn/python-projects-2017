from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.binary_to_decimal import *
import unittest


class ChangeReturnTestCase(unittest.TestCase):

    @parameterized.expand([
        ('0b1', 1),
        ('0b1001', 9),
        ('0b110111', 55),
        ('0b1000000000', 512)
    ])
    def test_binary_to_decimal(self, binary, decimal_result):
        assert_equal(binary_to_decimal(binary), decimal_result)

    @parameterized.expand([
        (1, '0b1'),
        (9, '0b1001'),
        (55, '0b110111'),
        (512, '0b1000000000')
    ])
    def test_decimal_to_binary(self, decimal, binary_result):
        assert_equal(decimal_to_binary(decimal), binary_result)
