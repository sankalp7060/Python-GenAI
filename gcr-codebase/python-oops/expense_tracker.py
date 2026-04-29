class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount):
        self.expenses.append(amount)

    def total_expense(self):
        return sum(self.expenses)


e = ExpenseTracker()
e.add_expense(200)
e.add_expense(300)

print(e.total_expense())