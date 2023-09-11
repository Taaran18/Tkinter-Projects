import tkinter as tk
from tkinter import messagebox

class ExpenseSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Splitter App")

        self.expenses = []
        self.total_expense = 0
        self.total_people = 0

        self.expense_label = tk.Label(root, text="Enter Expense:")
        self.expense_label.pack()

        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack()

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.total_label = tk.Label(root, text="Total Expense: $0")
        self.total_label.pack()

        self.people_label = tk.Label(root, text="Enter Number of People:")
        self.people_label.pack()

        self.people_entry = tk.Entry(root)
        self.people_entry.pack()

        self.split_button = tk.Button(root, text="Split Expenses", command=self.split_expenses)
        self.split_button.pack()

    def add_expense(self):
        try:
            expense = float(self.expense_entry.get())
            self.expenses.append(expense)
            self.total_expense += expense
            self.total_label.config(text=f"Total Expense: ${self.total_expense:.2f}")
            self.expense_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid expense.")

    def split_expenses(self):
        try:
            total_people = int(self.people_entry.get())
            if total_people > 0:
                per_person_share = self.total_expense / total_people
                result_text = f"Each person owes: ${per_person_share:.2f}"
                messagebox.showinfo("Expense Split Result", result_text)
            else:
                messagebox.showwarning("Warning", "Number of people must be greater than 0.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number of people.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSplitterApp(root)
    root.mainloop()
