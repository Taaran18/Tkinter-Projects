import tkinter as tk
from tkinter import messagebox


class BudgetPlannerApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Budget Planner App")

        # Initialize income and expenses
        self.income = 0
        self.expenses = []

        # Labels and entry for income input
        self.income_label = tk.Label(root, text="Income:")
        self.income_label.pack()

        self.income_entry = tk.Entry(root)
        self.income_entry.pack()

        # Button to add income
        self.add_income_button = tk.Button(
            root, text="Add Income", command=self.add_income
        )
        self.add_income_button.pack()

        # Labels and entries for expense input
        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.pack()

        self.expense_name_label = tk.Label(root, text="Name:")
        self.expense_name_label.pack()

        self.expense_name_entry = tk.Entry(root)
        self.expense_name_entry.pack()

        self.expense_amount_label = tk.Label(root, text="Amount:")
        self.expense_amount_label.pack()

        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.pack()

        # Button to add expense
        self.add_expense_button = tk.Button(
            root, text="Add Expense", command=self.add_expense
        )
        self.add_expense_button.pack()

        # Button to show budget summary
        self.summary_button = tk.Button(
            root, text="Show Summary", command=self.show_summary
        )
        self.summary_button.pack()

    def add_income(self):
        # Add income to the total income
        income = float(self.income_entry.get())
        self.income += income
        self.income_entry.delete(0, tk.END)  # Clear the income entry field

    def add_expense(self):
        # Add expense to the list of expenses
        name = self.expense_name_entry.get()
        amount = float(self.expense_amount_entry.get())
        self.expenses.append({"name": name, "amount": amount})
        self.expense_name_entry.delete(0, tk.END)  # Clear the expense name entry field
        self.expense_amount_entry.delete(
            0, tk.END
        )  # Clear the expense amount entry field

    def show_summary(self):
        # Calculate total expenses and balance, then display a summary message box
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        balance = self.income - total_expenses
        summary = f"Income: ${self.income:.2f}\nTotal Expenses: ${total_expenses:.2f}\nBalance: ${balance:.2f}"
        messagebox.showinfo("Budget Summary", summary)


if __name__ == "__main__":
    # Create and run the Budget Planner application
    root = tk.Tk()
    app = BudgetPlannerApp(root)
    root.mainloop()
