# Problem 1: Bank Account Create a class representing a bank account with attributes like account number,
# account holder name, and balance. Implement methods to deposit and withdraw money from the account.

class Account:
    def __init__(self, name, acNumber, balance):
        self.name = name
        self.acNumber = acNumber
        self.balance = balance
    def checkBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

a1 = Account('Dev', 1, 6800)

print(a1.checkBalance())
a1.deposit(1000)
print(a1.checkBalance())
a1.withdraw(4800)
print(a1.checkBalance())

        
    