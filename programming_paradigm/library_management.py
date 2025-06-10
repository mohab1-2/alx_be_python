#!/usr/bin/env python3
"""
Unit Tests for SimpleCalculator Class
Author: Assistant
Date: June 2025

This module contains comprehensive unit tests to verify the correctness of the 
SimpleCalculator class methods including edge cases and various scenarios.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator that inherits from unittest.TestCase."""
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(4, 5), 20)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(7, 1), 7)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(6, -2), -12)
        
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
    
    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        
        # Test division resulting in decimal
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(1, 4), 0.25)
        
        # Test division with zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Test division by zero (edge case)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        self.assertEqual(self.calc.divide(8, -4), -2.0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333, places=7)
    
    def test_edge_cases_comprehensive(self):
        """Test comprehensive edge cases for all methods."""
        # Test very large numbers
        large_num = 1000000
        self.assertEqual(self.calc.add(large_num, large_num), 2000000)
        self.assertEqual(self.calc.multiply(large_num, 2), 2000000)
        
        # Test very small decimal numbers
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 0.000002, places=7)
        
        # Test mixed integer and float operations
        self.assertEqual(self.calc.add(5, 2.5), 7.5)
        self.assertEqual(self.calc.subtract(10, 3.2), 6.8)
        self.assertEqual(self.calc.multiply(4, 2.5), 10.0)
        self.assertEqual(self.calc.divide(9, 2.0), 4.5)


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()