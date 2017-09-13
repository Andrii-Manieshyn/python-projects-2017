import unittest
from numbers.src.pi_for_n_digit import find_pi_to_n_digit

class TestPyForNDigit(unittest.TestCase):

    def test_10_digits(self):
        self.assertEqual(find_pi_to_n_digit(10), '3.1415926536')

    def test_20_digits(self):
        self.assertEqual(find_pi_to_n_digit(20), '3.14159265358979311600')

    def test_50_digits(self):
        self.assertEqual(find_pi_to_n_digit(48), '3.141592653589793115997963468544185161590576171875')

    def test_100_digits(self):
        self.assertEqual(find_pi_to_n_digit(100), '3.141592653589793238462643383279502884197169399375105'
                                                 '8209749445923078164062862089986280348253421170679')

if __name__ == '__main__':
    unittest.main()