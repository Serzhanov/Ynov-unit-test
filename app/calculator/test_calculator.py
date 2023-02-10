import unittest
import sys

sys.path.insert(0, "../../../..")
from app.calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        self.assertEqual(result, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(6, 0)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_limit(self):
        max_int = sys.maxsize
        result = self.calculator.power(max_int, 2)
        self.assertEqual(result, max_int * max_int)

    def test_square_root(self):
        result = self.calculator.square_root(9)
        self.assertEqual(round(result), 3)

    def test_power_negative_exponent(self):
        with self.assertRaises(ValueError):
            self.calculator.power(2, -3)

    def test_square_root_negative_input(self):
        with self.assertRaises(ValueError):
            self.calculator.square_root(-9)


if __name__ == "__main__":
    unittest.main()
