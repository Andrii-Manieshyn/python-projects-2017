from nose.tools import assert_equal
from parameterized import parameterized

from numbers_tasks.src.prime_factorization import factorization

@parameterized([
    (525, [3, 5, 5, 7]),
    (512, [2, 2, 2, 2, 2, 2, 2, 2, 2]),
    (1566, [3, 3, 3, 2, 29]),
    (1566, [3, 3, 3, 2, 29]),
    (1, []),
    (223, []),
    (4, [2, 2])
])
def test_prime_factorization(number, expected_result):
    assert_equal(sorted(factorization(number)), sorted(expected_result))