from nose.tools import assert_equals
from parameterized import parameterized
from numbers_tasks.src.factorial_finder import *
import unittest

class FactorialTest(unittest.TestCase):

    results = [
        (15, 1307674368000),
        (10, 3628800),
        (5, 120),
        (1, 1),
    ]

    @parameterized.expand(results)
    def test_factorial_finder_recursive(self, n, result):
        assert_equals(factorial_recursive(n), result)

    @parameterized.expand(results)
    def test_factorial_finder_loops(self, n, result):
        assert_equals(factorial_loops(n), result)