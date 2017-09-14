from nose.tools import assert_equal
from parameterized import parameterized
from numbers_tasks.src.change_return import return_change
import unittest


class ChangeReturnTestCase(unittest.TestCase):

    @parameterized.expand([
        (100, {'dollars': 100}),
        (75.55, {'dollars': 75, 'quarters': 2, 'nickles': 1}),
        (13.99, {'dollars': 13, 'quarters': 3, 'dimes': 2, 'pennies':4}),
        (14.94, {'dollars': 14, 'quarters': 3, 'dimes': 1, 'nickles': 1, 'pennies': 4})
    ])
    def test_simple_solution(self, cost, change):
        assert_equal(return_change(cost), change)
