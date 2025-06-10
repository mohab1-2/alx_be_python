#!/usr/bin/env python3
"""
Main script for Command Line Division Calculator
Author: Assistant
Date: June 2025

This script interfaces with the user through command line arguments to perform
division operations using the robust_division_calculator module.
"""

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments and perform division.
    """
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)
    
    # Get numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform division using safe_divide function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()