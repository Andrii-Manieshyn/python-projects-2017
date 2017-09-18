import unittest
from nose.tools import assert_equal
import classical_algorithm.src.closest_pair as cp
from parameterized import parameterized

class ClosestPairTestCase(unittest.TestCase):

    @parameterized.expand([
        ([(2.0, 1.0), (8.0, 3.0), (3.0, 6.0), (5.0, 8.0), (3, 2)], [(3.0, 2.0), (2.0, 1.0)]),
        ([(2.0, 1.0), (8.0, 3.0), (3.0, 6.0), (5.0, 8.0), (6.0, 8.0)], [(6.0, 8.0), (5.0, 8.0)]),
        ([(2.0, 1.0), (8.0, 3.0), (3.0, 6.0), (5.0, 8.0)], [(3.0, 6.0), (5.0, 8.0)]),
    ])
    def test_closes_pair(self, points, result):
        real_result = sorted(cp.closest_pair_brute_force_algorithm(points), key=lambda x: x[0])
        expected_result = sorted(result, key=lambda x: x[0])
        assert_equal(real_result, expected_result)


