#!/usr/bin/env python3
import sys

# -------------------------------------------------
# 1.  BankAccount class (encapsulated balance)
# -------------------------------------------------
class BankAccount:
    def __init__(self, balance: float = 0):
        """Initialize a new account (default balance = 0)."""
        self.__balance = balance          # private attribute
    
    # Deposit --------------------------------------------------
    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        self.__balance += amount
    
    # Withdraw -------------------------------------------------
    def withdraw(self, amount: float) -> bool:
        """
        Subtract money from the account.
        Returns True on success, False if funds are insufficient.
        """
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    # Display --------------------------------------------------
    def display_balance(self) -> None:
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__balance:.2f}")

# -------------------------------------------------
# 2.  Command-line interface
# -------------------------------------------------
def parse_cli(argv):
    """
    Accepts either:
        deposit:50        (single token with a colon)
        deposit 50        (two tokens)
        display           (single token, no amount)
    Returns (command:str, amount:float|None)
    """
    if len(argv) == 1:
        token = argv[0]
        if ":" in token:                        # form: cmd:amount
            cmd, amt = token.split(":", 1)
            return cmd, float(amt)
        return token, None                     # form: display
    elif len(argv) == 2:                        # form: cmd amount
        return argv[0], float(argv[1])
    return None, None                           # invalid usage

def main() -> None:
    # Example starting balance chosen to match the screenshot (100).
    account = BankAccount(100)
    
    if len(sys.argv) < 2:
        print("Usage: python bank_app.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    
    command, amount = parse_cli(sys.argv[1:])
    
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:g}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:g}")
        else:
            print("Insufficient funds.")
    elif command == "display" and amount is None:
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
