import unittest
from numbers_tasks.src.pi_for_n_digit import find_pi_to_n_digit

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
    def test_200_digits(self):
        self.assertEqual(find_pi_to_n_digit(200), '3.141592653589793238462643383279502884197169399375105'
                                                  '82097494459230781640628620899862803482534211706798214'
                                                  '80865132823066470938446095505822317253594081284811174'
                                                  '5028410270193852110555964462294895493038196')
    def test_1000_digits(self):
        self.assertEqual(find_pi_to_n_digit(1000), '3.141592653589793238462643383279502884197169399375105'
                                                   '82097494459230781640628620899862803482534211706798214'
                                                   '80865132823066470938446095505822317253594081284811174'
                                                   '50284102701938521105559644622948954930381964428810975'
                                                   '66593344612847564823378678316527120190914564856692346'
                                                   '03486104543266482133936072602491412737245870066063155'
                                                   '88174881520920962829254091715364367892590360011330530'
                                                   '54882046652138414695194151160943305727036575959195309'
                                                   '21861173819326117931051185480744623799627495673518857'
                                                   '52724891227938183011949129833673362440656643086021394'
                                                   '94639522473719070217986094370277053921717629317675238'
                                                   '46748184676694051320005681271452635608277857713427577'
                                                   '89609173637178721468440901224953430146549585371050792'
                                                   '27968925892354201995611212902196086403441815981362977'
                                                   '47713099605187072113499999983729780499510597317328160'
                                                   '96318595024459455346908302642522308253344685035261931'
                                                   '18817101000313783875288658753320838142061717766914730'
                                                   '35982534904287554687311595628638823537875937519577818'
                                                   '577805321712268066130019278766111959092164201989')

if __name__ == '__main__':
    unittest.main()