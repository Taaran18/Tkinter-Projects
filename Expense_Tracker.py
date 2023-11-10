import tkinter as tk


class ExpenseTrackerApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Expense Tracker App")

        # List to store expenses as tuples (expense, amount)
        self.expenses = []

        # Label and entry for entering an expense
        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.pack()

        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack()

        # Label and entry for entering the amount
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # Button to add an expense
        self.add_expense_button = tk.Button(
            root, text="Add Expense", command=self.add_expense
        )
        self.add_expense_button.pack()

        # Button to show expense summary
        self.summary_button = tk.Button(
            root, text="Show Summary", command=self.show_summary
        )
        self.summary_button.pack()

        # Label to display the summary
        self.summary_label = tk.Label(root, text="")
        self.summary_label.pack()

    def add_expense(self):
        # Function to add an expense to the list
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()

        if expense and amount:
            # Append the expense as a tuple to the expenses list
            self.expenses.append((expense, float(amount)))
            self.expense_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

    def show_summary(self):
        # Function to calculate and display the expense summary
        total_amount = sum(amount for _, amount in self.expenses)
        summary = (
            f"Total Expenses: {len(self.expenses)}\nTotal Amount: ${total_amount:.2f}"
        )
        self.summary_label.config(text=summary)


if __name__ == "__main__":
    # Create and run the Expense Tracker application
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
