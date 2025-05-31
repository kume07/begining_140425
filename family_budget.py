# family_budget.py


class Salary:
    def __init__(self):
        self.records = []

    def add(self, amount):
        self.records.append(amount)

    def total(self):
        return sum(self.records)


class Pension:
    def __init__(self):
        self.records = []

    def add(self, amount):
        self.records.append(amount)

    def total(self):
        return sum(self.records)


class Family:
    def __init__(self, name):
        self.name = name
        self.salary = Salary()
        self.pension = Pension()

    def balance(self):
        return self.salary.total() + self.pension.total()
