import tkinter as tk

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker App")

        self.expenses = []

        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.pack()

        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.pack()

        self.summary_label = tk.Label(root, text="")
        self.summary_label.pack()

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()

        if expense and amount:
            self.expenses.append((expense, float(amount)))
            self.expense_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

    def show_summary(self):
        total_amount = sum(amount for _, amount in self.expenses)
        summary = f"Total Expenses: {len(self.expenses)}\nTotal Amount: ${total_amount:.2f}"
        self.summary_label.config(text=summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
