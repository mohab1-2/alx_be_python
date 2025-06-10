import sys

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__balance}")

def main():
    acct = BankAccount(100)  # You can change the initial balance here

    if len(sys.argv) < 2:
        print("Usage: python script_name.py [command]:[amount]")
        return

    command, *params = sys.argv[1].split(":")
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        acct.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        success = acct.withdraw(amount)
        if success:
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        acct.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
