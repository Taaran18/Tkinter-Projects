import tkinter as tk
from tkinter import messagebox

class RecipeConversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Conversion App")

        self.conversions = {
            "teaspoon": 1,
            "tablespoon": 3,
            "cup": 48,
            "ounce": 6,
            "gram": 0.2,
        }

        self.ingredient_label = tk.Label(root, text="Ingredient:")
        self.ingredient_label.pack()

        self.ingredient_entry = tk.Entry(root)
        self.ingredient_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.from_unit_label = tk.Label(root, text="From Unit:")
        self.from_unit_label.pack()

        self.from_unit_var = tk.StringVar(root)
        self.from_unit_var.set("teaspoon")
        self.from_unit_menu = tk.OptionMenu(root, self.from_unit_var, *self.conversions.keys())
        self.from_unit_menu.pack()

        self.to_unit_label = tk.Label(root, text="To Unit:")
        self.to_unit_label.pack()

        self.to_unit_var = tk.StringVar(root)
        self.to_unit_var.set("tablespoon")
        self.to_unit_menu = tk.OptionMenu(root, self.to_unit_var, *self.conversions.keys())
        self.to_unit_menu.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_quantity)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert_quantity(self):
        ingredient = self.ingredient_entry.get()
        quantity = float(self.quantity_entry.get())
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        if from_unit in self.conversions and to_unit in self.conversions:
            converted_quantity = quantity * (self.conversions[to_unit] / self.conversions[from_unit])
            self.result_label.config(text=f"{quantity:.2f} {from_unit} of {ingredient} is {converted_quantity:.2f} {to_unit}")
        else:
            messagebox.showwarning("Warning", "Please select valid units.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeConversionApp(root)
    root.mainloop()
