def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Draw the pattern using nested loops
    row = 0  # Initialize row counter for while loop
    
    # Use while loop to iterate through each row
    while row < size:
        # Use for loop to print asterisks side by side without advancing to new line
        for col in range(size):
            print("*", end="")
        
        # Print newline character to move to the next row
        print()
        
        # Increment row counter
        row += 1

if __name__ == "__main__":
    main()