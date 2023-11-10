import tkinter as tk
from tkinter import messagebox


class CurrencyExchangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Exchange App")

        # Dictionary with approximate exchange rates
        self.rates = {
            "USD": 1.0,  # US Dollar
            "EUR": 0.85,  # Euro
            "GBP": 0.72,  # British Pound
            "JPY": 110.0,  # Japanese Yen
            "AUD": 1.35,  # Australian Dollar
            "CAD": 1.26,  # Canadian Dollar
            "INR": 74.0,  # Indian Rupee
            "CNY": 6.46,  # Chinese Yuan
        }

        # Widgets for From Currency selection
        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.pack()

        self.from_currency_var = tk.StringVar(root)
        self.from_currency_var.set("USD")
        self.from_currency_menu = tk.OptionMenu(
            root, self.from_currency_var, *self.rates.keys()
        )
        self.from_currency_menu.pack()

        # Widget for entering the amount to be converted
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # Widgets for To Currency selection
        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_var = tk.StringVar(root)
        self.to_currency_var.set("USD")
        self.to_currency_menu = tk.OptionMenu(
            root, self.to_currency_var, *self.rates.keys()
        )
        self.to_currency_menu.pack()

        # Button to trigger currency conversion
        self.convert_button = tk.Button(
            root, text="Convert", command=self.convert_currency
        )
        self.convert_button.pack()

        # Label to display the conversion result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert_currency(self):
        try:
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            amount = float(self.amount_entry.get())

            if from_currency in self.rates and to_currency in self.rates:
                converted_amount = amount * (
                    self.rates[to_currency] / self.rates[from_currency]
                )
                result_text = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
                self.result_label.config(text=result_text)
            else:
                messagebox.showwarning("Warning", "Invalid currency selected.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid amount.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyExchangeApp(root)
    root.mainloop()
