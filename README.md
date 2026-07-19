# 💰 Expense Tracker (Python OOP Project)

A simple **Command Line Expense Tracker** built using **Python** and **Object-Oriented Programming (OOP)** concepts. This application allows users to record incomes and expenses, search transactions by category, generate monthly summaries, and save/load records using CSV files.

---

## 📌 Features

- ➕ Add Income records
- ➖ Add Expense records
- 📋 Display all financial records
- 🔍 Search records by category
- 📊 Generate monthly income, expense, and balance summary
- 💾 Save records to a CSV file
- 📂 Load records from a CSV file
- ✅ Input validation using Exception Handling

---

## 🛠️ Technologies Used

- Python 3.x
- CSV Module
- Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Implemented

### 1. Abstraction
- Implemented using the `ABC` module.
- `Record` is an abstract class with the abstract method `display()`.

### 2. Inheritance
- `Income` and `Expense` classes inherit from the `Record` class.

### 3. Encapsulation
- Category and Month attributes are declared as private using double underscores (`__category`, `__month`).
- Access is provided using property decorators.

### 4. Polymorphism
- Both `Income` and `Expense` implement their own version of the `display()` method.

---

## 📂 Project Structure

```
ExpenseTracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

---

## ⚙️ How It Works

When the program starts, users are presented with the following menu:

```
===== Expense Tracker =====

1. Add Income
2. Add Expense
3. Display Records
4. Search Category
5. Monthly Summary
6. Save
7. Load
8. Exit
```

Users can perform different operations until they choose to exit the application.

---

## 📊 Sample Output

### Adding Income

```
Amount: 50000
Category: Salary
Month: January

Income added.
```

### Adding Expense

```
Amount: 1200
Category: Food
Month: January

Expense added.
```

### Monthly Summary

```
Income : 50000
Expense: 1200
Balance: 48800
```

---

## 💾 CSV Storage

The application stores all records in a file named:

```
expenses.csv
```

Example:

| Type | Amount | Category | Month |
|------|---------|----------|-------|
| Income | 50000 | Salary | January |
| Expense | 1200 | Food | January |

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### Navigate to the project folder

```bash
cd expense-tracker
```

### Run the program

```bash
python expense_tracker.py
```

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Python Classes and Objects
- Abstract Classes
- Inheritance
- Encapsulation
- Polymorphism
- File Handling
- CSV Operations
- Exception Handling
- Menu-driven Applications

---

## 🔮 Future Enhancements

- Add date-wise transaction history
- Edit existing records
- Delete records
- Expense analytics with charts
- Budget tracking
- Export reports to Excel
- SQLite database integration
- Graphical User Interface (Tkinter or Streamlit)

---

## 👨‍💻 Author

**Piyush Pankaj**

Data Science Consultant | Python Trainer | AI & Machine Learning Enthusiast

---

## 📜 License

This project is open-source and available under the **MIT License**
