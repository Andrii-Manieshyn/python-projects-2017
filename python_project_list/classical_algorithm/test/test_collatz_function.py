import unittest
from nose.tools import assert_equal
import classical_algorithm.src.collatz_conjecture as cc
from parameterized import parameterized

class CollatzConjectureTestCase(unittest.TestCase):

    @parameterized.expand([
        (3, 7),
        (19, 20),
        (27, 111),
    ])
    def test_collatz_congecture(self, n, result):
        assert_equal(cc.collatz_function(n), result)