from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingAccount(BankAccount):
    def __init__(self, balance=5000):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
saving_account = SavingAccount()
saving_account.deposit(2000)
saving_account.withdraw(1000)