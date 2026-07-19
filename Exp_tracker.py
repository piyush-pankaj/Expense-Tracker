from abc import ABC, abstractmethod
import csv


# ---------------- Abstract Class ----------------
class Record(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def display(self):
        pass


# ---------------- Income Class ----------------
class Income(Record):
    def __init__(self, amount, category, month):
        super().__init__(amount)
        self.__category = category
        self.__month = month

    @property
    def category(self):
        return self.__category

    @property
    def month(self):
        return self.__month

    def display(self):
        return ["Income", self.amount, self.category, self.month]


# ---------------- Expense Class ----------------
class Expense(Record):
    def __init__(self, amount, category, month):
        super().__init__(amount)
        self.__category = category
        self.__month = month

    @property
    def category(self):
        return self.__category

    @property
    def month(self):
        return self.__month

    def display(self):
        return ["Expense", self.amount, self.category, self.month]


# ---------------- Expense Tracker ----------------
class ExpenseTracker:

    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def show_records(self):
        if not self.records:
            print("No records found.")
            return

        for r in self.records:
            print(r.display())

    def search_category(self, category):
        found = False

        for r in self.records:
            if r.category.lower() == category.lower():
                print(r.display())
                found = True

        if not found:
            print("No record found.")

    def monthly_summary(self, month):
        income = 0
        expense = 0

        for r in self.records:
            if r.month.lower() == month.lower():
                if isinstance(r, Income):
                    income += r.amount
                else:
                    expense += r.amount

        print("Income :", income)
        print("Expense:", expense)
        print("Balance:", income - expense)

    def save_file(self):
        try:
            with open("expenses.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Type", "Amount", "Category", "Month"])

                for r in self.records:
                    writer.writerow(r.display())

            print("Records saved.")

        except Exception:
            print("Error saving file.")

    def load_file(self):
        try:
            with open("expenses.csv", "r") as f:
                reader = csv.DictReader(f)

                self.records.clear()

                for row in reader:

                    amount = float(row["Amount"])
                    category = row["Category"]
                    month = row["Month"]

                    if row["Type"] == "Income":
                        self.records.append(
                            Income(amount, category, month)
                        )

                    else:
                        self.records.append(
                            Expense(amount, category, month)
                        )

            print("Records loaded.")

        except FileNotFoundError:
            print("No saved file found.")


# ---------------- Main Program ----------------

tracker = ExpenseTracker()

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Display Records")
    print("4. Search Category")
    print("5. Monthly Summary")
    print("6. Save")
    print("7. Load")
    print("8. Exit")

    try:

        choice = int(input("Enter choice: "))

        if choice == 1:

            amount = float(input("Amount: "))
            category = input("Category: ")
            month = input("Month: ")

            tracker.add_record(
                Income(amount, category, month)
            )

            print("Income added.")

        elif choice == 2:

            amount = float(input("Amount: "))
            category = input("Category: ")
            month = input("Month: ")

            tracker.add_record(
                Expense(amount, category, month)
            )

            print("Expense added.")

        elif choice == 3:

            tracker.show_records()

        elif choice == 4:

            category = input("Category: ")
            tracker.search_category(category)

        elif choice == 5:

            month = input("Month: ")
            tracker.monthly_summary(month)

        elif choice == 6:

            tracker.save_file()

        elif choice == 7:

            tracker.load_file()

        elif choice == 8:

            print("Thank You")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")