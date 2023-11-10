import tkinter as tk
from tkinter import messagebox


class ExpenseSplitterApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Expense Splitter App")

        # Lists to store individual expenses
        self.expenses = []

        # Variables to store total expense and total number of people
        self.total_expense = 0
        self.total_people = 0

        # Label and entry for entering an expense
        self.expense_label = tk.Label(root, text="Enter Expense:")
        self.expense_label.pack()

        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack()

        # Button to add an expense
        self.add_expense_button = tk.Button(
            root, text="Add Expense", command=self.add_expense
        )
        self.add_expense_button.pack()

        # Label to display the total expense
        self.total_label = tk.Label(root, text="Total Expense: $0")
        self.total_label.pack()

        # Label and entry for entering the number of people
        self.people_label = tk.Label(root, text="Enter Number of People:")
        self.people_label.pack()

        self.people_entry = tk.Entry(root)
        self.people_entry.pack()

        # Button to split expenses
        self.split_button = tk.Button(
            root, text="Split Expenses", command=self.split_expenses
        )
        self.split_button.pack()

    def add_expense(self):
        # Function to add an expense to the list
        try:
            expense = float(self.expense_entry.get())
            self.expenses.append(expense)
            self.total_expense += expense
            self.total_label.config(text=f"Total Expense: ${self.total_expense:.2f}")
            self.expense_entry.delete(0, tk.END)
        except ValueError:
            # Show a warning if the entered value is not a valid expense
            messagebox.showwarning("Warning", "Please enter a valid expense.")

    def split_expenses(self):
        # Function to calculate and display the split expense per person
        try:
            total_people = int(self.people_entry.get())
            if total_people > 0:
                per_person_share = self.total_expense / total_people
                result_text = f"Each person owes: ${per_person_share:.2f}"
                messagebox.showinfo("Expense Split Result", result_text)
            else:
                # Show a warning if the entered number of people is not valid
                messagebox.showwarning(
                    "Warning", "Number of people must be greater than 0."
                )
        except ValueError:
            # Show a warning if the entered value for the number of people is not valid
            messagebox.showwarning("Warning", "Please enter a valid number of people.")


if __name__ == "__main__":
    # Create and run the Expense Splitter application
    root = tk.Tk()
    app = ExpenseSplitterApp(root)
    root.mainloop()
