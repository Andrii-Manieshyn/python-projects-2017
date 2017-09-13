from nose.tools import assert_equal
from parameterized import parameterized

from numbers_tasks.src.fibonachi_functions import fibonacci

@parameterized([
    (0, 0),
    (10, 55),
    (20, 6765),
    (99, 218922995834555169026),
])
def test_fibonacci_function(n, expected):
    assert_equal(fibonacci(n), expected)
