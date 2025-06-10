#!/usr/bin/env python3
"""
Simple Bank Account Class Implementation
Author: Assistant
Date: June 2025

This module implements a BankAccount class that encapsulates basic banking operations.
"""

class BankAccount:
    """
    A simple bank account class that manages account holder information and balance.
    
    Attributes:
        account_holder (str): The name of the account holder
        balance (float): The current account balance (defaults to 0.0)
    """
    
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_holder (str): Name of the account holder
            initial_balance (float, optional): Starting balance. Defaults to 0.0.
        """
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit (must be positive)
            
        Returns:
            bool: True if deposit successful, False otherwise
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw (must be positive and <= balance)
            
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    """
    Main function to demonstrate the BankAccount class functionality.
    """
    print("=== Bank Account Demo ===")
    
    # Create a new bank account
    account = BankAccount("John Doe", 100.0)
    print(f"Created account for {account.account_holder}")
    
    # Display initial balance
    account.display_balance()
    
    # Test deposit
    print("\n--- Testing Deposit ---")
    account.deposit(50.0)
    
    # Test withdrawal with sufficient funds
    print("\n--- Testing Withdrawal (Sufficient Funds) ---")
    account.withdraw(30.0)
    
    # Test withdrawal with insufficient funds
    print("\n--- Testing Withdrawal (Insufficient Funds) ---")
    account.withdraw(200.0)
    
    # Test invalid operations
    print("\n--- Testing Invalid Operations ---")
    account.deposit(-10.0)  # Negative deposit
    account.withdraw(-5.0)  # Negative withdrawal
    
    # Final balance
    print("\n--- Final Balance ---")
    account.display_balance()


if __name__ == "__main__":
    main()