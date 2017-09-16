from nose.tools import assert_equals
from parameterized import parameterized
from numbers_tasks.src.credit_card_validation import *
import unittest

class CredirCardTest(unittest.TestCase):
    @parameterized.expand([
        ("4556737586899855", True),
        ("4716537222222112", False),
        ("5020843942608959", True),
    ])
    def test_luhn_validation_algorithm(self, card, result):
        assert_equals(luhn_validation_algorithm(card), result)