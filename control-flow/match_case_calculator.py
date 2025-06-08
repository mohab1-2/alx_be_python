# match_case_calculator.py
# Simple Calculator using Match Case statements

def main():
    # Prompt for user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask for the type of operation
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform the calculation using Match Case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
    main()