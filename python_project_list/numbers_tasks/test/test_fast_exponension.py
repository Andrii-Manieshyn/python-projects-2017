from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.fast_exponension import *
import unittest

class FastExponensionTest(unittest.TestCase):
    @parameterized.expand([
        (2, 3, 8),
        (21, 13, 154472377739119461),
        (11, 11, 285311670611),
    ])
    def test_fast_exponension(self,value, power, result):
        assert_equal(fast_power(value, power), result)