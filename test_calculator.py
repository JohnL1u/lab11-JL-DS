# https://github.com/JohnL1u/lab11-JL-DS.git
# Partner 1: John Liu
# Partner 2: Daniel Su Liu
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(3, 2), 1)
        self.assertEqual(sub(5, 0), 5)
        self.assertEqual(sub(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        from calculator import mul
        self.assertEqual(mul(3, 4), 12)  # integers
        self.assertAlmostEqual(mul(2.5, 4), 10.0)  # floats
        self.assertEqual(mul(-3, 5), -15)  # sign

    def test_divide(self):  # 3 assertions
        from calculator import div
        # NOTE: div(a, b) returns b / a per your implementation
        self.assertEqual(div(2, 10), 5)  # 10 / 2
        self.assertAlmostEqual(div(4, 1), 0.25)  # 1 / 4
        with self.assertRaises(ZeroDivisionError):  # a == 0 -> error
            div(0, 123)
    # ##########################

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 16), 4.0)
        self.assertEqual(log(3, 9), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 10)
            log(-2, 4)
            log(10, 0)
            log(7, -4)
            log(8, 1)
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # base == 1 should raise ValueError
        from calculator import log
        with self.assertRaises(ValueError):
            log(1, 10)

    def test_hypotenuse(self):  # 3 assertions
        # hypotenuse(a, b) = sqrt(a^2 + b^2)
        from calculator import hypotenuse
        self.assertEqual(hypotenuse(3, 4), 5)  # 3-4-5 triangle
        self.assertAlmostEqual(hypotenuse(5.0, 12.0), 13.0)  # float inputs
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)  # zeros

    def test_sqrt(self):  # 3 assertions
        from calculator import square_root
        # invalid: negative -> ValueError
        with self.assertRaises(ValueError):
            square_root(-1)
        # basic cases
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(9.0), 3.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()