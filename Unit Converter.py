import tkinter as tk

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter App")

        self.units = {
            "Length": {"meters": 1, "feet": 3.28084, "yards": 1.09361},
            "Weight": {"kilograms": 1, "pounds": 2.20462, "ounces": 35.27396},
            "Temperature": {"Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1},
        }

        self.unit_type_label = tk.Label(root, text="Select Unit Type:")
        self.unit_type_label.pack()

        self.unit_type_var = tk.StringVar()
        self.unit_type_var.set("Length")
        self.unit_type_menu = tk.OptionMenu(root, self.unit_type_var, *self.units.keys())
        self.unit_type_menu.pack()

        self.from_unit_label = tk.Label(root, text="From Unit:")
        self.from_unit_label.pack()

        self.from_unit_var = tk.StringVar()
        self.from_unit_menu = tk.OptionMenu(root, self.from_unit_var, *self.units[self.unit_type_var.get()].keys())
        self.from_unit_menu.pack()

        self.to_unit_label = tk.Label(root, text="To Unit:")
        self.to_unit_label.pack()

        self.to_unit_var = tk.StringVar()
        self.to_unit_menu = tk.OptionMenu(root, self.to_unit_var, *self.units[self.unit_type_var.get()].keys())
        self.to_unit_menu.pack()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.unit_type_var.trace("w", self.update_unit_menus)

    def update_unit_menus(self, *args):
        selected_unit_type = self.unit_type_var.get()
        from_units = self.units[selected_unit_type].keys()
        to_units = self.units[selected_unit_type].keys()
        self.from_unit_menu['menu'].delete(0, 'end')
        self.to_unit_menu['menu'].delete(0, 'end')
        for unit in from_units:
            self.from_unit_menu['menu'].add_command(label=unit, command=tk._setit(self.from_unit_var, unit))
        for unit in to_units:
            self.to_unit_menu['menu'].add_command(label=unit, command=tk._setit(self.to_unit_var, unit))

    def convert_units(self):
        selected_unit_type = self.unit_type_var.get()
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        amount = float(self.amount_entry.get())

        conversion_factor = self.units[selected_unit_type][to_unit] / self.units[selected_unit_type][from_unit]
        converted_amount = amount * conversion_factor

        self.result_label.config(text=f"{amount} {from_unit} is {converted_amount:.2f} {to_unit}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
