import unittest
from nose.tools import assert_equal
import classical_algorithm.src.sorting_algorithms as sa
from parameterized import parameterized

class SortAlrgoTestCase(unittest.TestCase):

    @parameterized.expand([
        ([5, 6, 7, 1, 2, 3, 16, 0, 10], [0, 1, 2, 3, 5, 6, 7, 10 , 16]),
        ([1], [1]),
        ([10, 9, 8, 7, 6, 5, 3, 2, 1, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ])
    def test_merge_sort(self, array, result):
        assert_equal(sa.merge_sort(array), result)

    @parameterized.expand([
        ([5, 6, 7, 1, 2, 3, 16, 0, 10], [0, 1, 2, 3, 5, 6, 7, 10 , 16]),
        ([1], [1]),
        ([10, 9, 8, 7, 6, 5, 3, 2, 1, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ])
    def test_qsort(self, array, result):
        assert_equal(sa.qsort(array), result)