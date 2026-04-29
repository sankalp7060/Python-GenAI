class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def add_interest(self):
        self.balance *= 1.05


s = SavingsAccount("Alex", 10000)
s.deposit(5000)
s.add_interest()
print(s.balance)