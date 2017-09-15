from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.unit_converter import *
import unittest

class ConverterTestCase(unittest.TestCase):

    @parameterized.expand([
        (0, 32.0),
        (36.6, 97.88),
        (100, 212.00),
    ])
    def test_convert_temp_celsius_to_fahrenheit(self, value, result):
        assert_equal(convert_temp_celsius_to_fahrenheit(value)[1], result)

    @parameterized.expand([
        (0, -17.78),
        (36.6, 2.56),
        (100, 37.78),
    ])
    def test_convert_temp_fahrenheit_to_celsius(self, value, result):
        assert_equal(convert_temp_fahrenheit_to_celsius(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 30.38),
        (100, 83.00),
    ])
    def test_convert_dollar_to_euro(self, value, result):
        assert_equal(convert_dollar_to_euro(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 44.10),
        (100, 120.48),
    ])
    def test_convert_euro_to_dollar(self, value, result):
        assert_equal(convert_euro_to_dollar(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 9.67),
        (100, 26.42),
    ])
    def test_convert_liter_to_gallons(self, value, result):
        assert_equal(convert_liter_to_gallons(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 138.55),
        (100, 378.54),
    ])
    def test_convert_gallons_to_liter(self, value, result):
        assert_equal(convert_gallons_to_liter(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 80.69),
        (100, 220.46),
    ])
    def test_convert_kilos_to_pounds(self, value, result):
        assert_equal(convert_kilos_to_pounds(value)[1], result)

    @parameterized.expand([
        (0, 0.00),
        (36.6, 16.60),
        (100, 45.36),
    ])
    def test_convert_pounds_to_kilos(self, value, result):
        assert_equal(convert_pounds_to_kilos(value)[1], result)