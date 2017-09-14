from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.scientific_calculator import calculate_expresion
import unittest


class CalculatorTestCase(unittest.TestCase):

    @parameterized.expand([
        ('exp ( -1 / 2 * 5 )', 0.0820849986238988),
        ('exp ( -1 / 2 * 5 ) + ln ( lg ( 100 ) )', 0.7752321791838441),
        ('ln ( lg ( 100 ) )', 0.6931471805599453),
        ('ln ( cos ( sin ( 100 ) ) )', -0.1340881747847246)
    ])
    def test_calculator(self, expression, result):
        assert_equal(calculate_expresion(expression), result)
