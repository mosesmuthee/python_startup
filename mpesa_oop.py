from abc import ABC, abstractmethod

# Encapsulation
class Account:
    def __init__(self, account_id, holdser_name, balance):
        self.account_id = account_id
        self.holdser_name = holdser_name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount} New Balance {self.balance}")
    def withdraw(self,amount):
        print("Withdrawing {amount} New Balance {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
    def get_balance(self):
        return self.balance