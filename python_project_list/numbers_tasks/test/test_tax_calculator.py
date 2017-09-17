import unittest
from nose.tools import assert_equal
import numbers_tasks.src.tax_calculator as tx
from  unittest.mock import Mock, call, MagicMock, patch
from parameterized import parameterized

class TestNameGetter(unittest.TestCase):


    @patch('builtins.input', side_effect=[2, 100, 'Germany'])
    def test_tax_calculator(self, mocket_input):
        result = tx.calculate_tax_rate()
        assert_equal(result, ('Germany', 0.1, 110))


    @patch('builtins.input', side_effect=[1, 100, 0.3])
    def test_tax_calculator(self, mocket_input):
        result = tx.calculate_tax_rate()
        assert_equal(result, ( 0.3, 130))


if __name__ == '__main__':
    unittest.main()