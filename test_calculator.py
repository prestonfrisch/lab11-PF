import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        # normal division
        self.assertAlmostEqual(calculator.divide(10, 2), 5)

        # dividing by zero should raise error
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_log_invalid_argument(self):
        # log base <= 0 -> bad
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 5)

        # log number <= 0 -> bad
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -1)

        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

    def test_hypotenuse(self):
        # hypot(a, b) = sqrt(a^2 + b^2)
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(0, 7), 7)

    def test_sqrt(self):
        # normal sqrt
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(2), math.sqrt(2))

        # negative numbers should raise ValueError
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
