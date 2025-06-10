import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive results
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative results
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
        # Test identity
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
        # Test identity
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(1, 2), 0.5, places=7)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Test identity
        self.assertEqual(self.calc.divide(5, 1), 5)

if __name__ == '__main__':
    unittest.main()
