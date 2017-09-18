import unittest
from nose.tools import assert_equal
import classical_algorithm.src.sieve_of_eratosthenes as se
from parameterized import parameterized

class SortAlrgoTestCase(unittest.TestCase):

    @parameterized.expand([
        (100, [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
        (1, [1]),
        (200, [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]),
    ])
    def test_merge_sort(self, n, result):
        assert_equal(se.sieve_of_eratosthenes(n), result)
