from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    Saves the current date in a current_date variable.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate a future date by adding specified number of days to the current date.
    
    Parameters:
    current_date (datetime): The current date
    days_to_add (int): Number of days to add
    
    Returns:
    datetime: The future date
    """
    future_date = current_date + timedelta(days=days_to_add)
    return future_date

def main():
    # Part 1: Display the Current Date and Time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a Future Date
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        future_date = calculate_future_date(current_date, days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()