import unittest
from app.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_addition(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_string_error(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_string_error_x_arg(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_string_error_y_arg(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
