"""
5. Create a bank account class that has attributes `owner`, `balance` 
and two methods `deposit` and `withdraw`.
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals,
and test to make sure the account can't be overdrawn.
class Account:
    pass
"""

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited. The new balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("The withdrawal cannot be made due to insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn. The new balance is {self.balance}.")

account = Account("John Doe", 1000)
account.deposit(200)
account.deposit(500)
account.deposit(100)
account.withdraw(500)
account.withdraw(300)
account.withdraw(200)
account.withdraw(1500)