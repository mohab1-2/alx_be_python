class Calculator:
    """Calculator class demonstrating static methods and class methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Static method: Returns the sum of two numbers. Use the @staticmethod decorator."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method: Returns the product of two numbers. Use the @classmethod decorator and ensure it prints a class attribute named calculation_type before performing the multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


def main():
    """Main function to test the Calculator class's static and class methods."""
    
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    
    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    main()