# Dad_income.py

from datetime import datetime
from collections import defaultdict


class Family:
    def __init__(self, name):
        self.card_balance = 0
        self.name = name
        self.salary = Salary()
        self.pension = Pension()

    def balance(self):
        return self.salary.total() + self.pension.total()

    def accrue_to_card(self, month=None):
        salary_on_card = self.salary.total_to_card(month)
        pension_total = 0
        if month:
            pension_total = self.pension.get_monthly_totals().get(month, 0)
        else:
            pension_total = self.pension.total()

        total = salary_on_card + pension_total
        self.card_balance += total

        if month:
            print(
                f"Нараховано за {month}: зарплата на картку = {salary_on_card}, пенсія = {pension_total}."
            )
        else:
            print(
                f"Нараховано загально: зарплата на картку = {salary_on_card}, пенсія = {pension_total}."
            )
        print(f"Баланс картки: {self.card_balance} грн.")

    def __str__(self):
        return (
            f"{self.name}: Salary({self.salary.total()}), Pension({self.pension.total()}), "
            f"Total: {self.balance()}, Card: {self.card_balance}"
        )

    def monthly_report(self):
        all_months = defaultdict(lambda: {"salary": 0, "pension": 0})
        for month, amount in self.salary.get_monthly_totals().items():
            all_months[month]["salary"] = amount
        for month, amount in self.pension.get_monthly_totals().items():
            all_months[month]["pension"] = amount
        for month in sorted(all_months):
            s = all_months[month]["salary"]
            p = all_months[month]["pension"]
            print(f"{month}: Salary = {s}, Pension = {p}, Total = {s + p}")

    def show_income_for_month(self, month):
        s = self.salary.get_monthly_totals().get(month, 0)
        p = self.pension.get_monthly_totals().get(month, 0)
        print(f"Доходи за {month}:\n  Зарплата: {s}\n  Пенсія: {p}\n  Всього: {s + p}")

    def show_total_income(self):
        s = self.salary.total()
        p = self.pension.total()
        print(f"Сумарний дохід:\n  Зарплата: {s}\n  Пенсія: {p}\n  Всього: {s + p}")


class User:
    def __init__(self, name, surname, status):
        self.name = name
        self.surname = surname
        self.status = status

    def __str__(self):
        return f"{self.name} {self.surname}, Status: {self.status}"


class Salary:
    def __init__(self):
        self.records = []

    def add(self, amount, date_str, to_card=False):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        self.records.append((date, amount, to_card))

    def get_monthly_totals(self):
        monthly = defaultdict(float)
        for date, amount, _ in self.records:
            month = date.strftime("%Y-%m")
            monthly[month] += amount
        return monthly

    def total(self):
        return sum(amount for _, amount, _ in self.records)

    def total_to_card(self, month=None):
        return sum(
            amount
            for date, amount, to_card in self.records
            if to_card and (month is None or date.strftime("%Y-%m") == month)
        )


class Pension:
    def __init__(self):
        self.records = []

    def add(self, amount, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        self.records.append((date, amount))

    def get_monthly_totals(self):
        monthly = defaultdict(float)
        for date, amount in self.records:
            month = date.strftime("%Y-%m")
            monthly[month] += amount
        return monthly

    def total(self):
        return sum(amount for _, amount in self.records)


def family_menu(family):
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати зарплату")
        print("2. Додати пенсію")
        print("3. Показати дохід за місяць")
        print("4. Показати сумарний дохід")
        print("5. Нарахувати на картку")
        print("6. Показати баланс")
        print("7. Показати звіт по місяцях")
        print("0. Вихід")

        choice = input("Оберіть опцію: ").strip()
        if choice == "1":
            amount = float(input("Сума зарплати: "))
            date = input("Дата (YYYY-MM-DD): ")
            to_card = input("Нарахувати на картку? (y/n): ").lower() == "y"
            family.salary.add(amount, date, to_card)
        elif choice == "2":
            amount = float(input("Сума пенсії: "))
            date = input("Дата (YYYY-MM-DD): ")
            family.pension.add(amount, date)
        elif choice == "3":
            month = input("Введіть місяць (YYYY-MM): ")
            family.show_income_for_month(month)
        elif choice == "4":
            family.show_total_income()
        elif choice == "5":
            month = input("Введіть місяць (YYYY-MM) або Enter для всього періоду: ")
            family.accrue_to_card(month or None)
        elif choice == "6":
            print(family)
        elif choice == "7":
            family.monthly_report()
        elif choice == "0":
            print("Завершення програми.")
            break
        else:
            print("Невідома команда.")
