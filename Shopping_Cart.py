import tkinter as tk
from tkinter import messagebox

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart App")

        self.items = []

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()

        self.cart_listbox = tk.Listbox(root, width=40)
        self.cart_listbox.pack()

        self.total_label = tk.Label(root, text="Total:")
        self.total_label.pack()

        self.total_value_label = tk.Label(root, text="0.00")
        self.total_value_label.pack()

    def add_to_cart(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        if item and price:
            self.items.append((item, float(price)))
            self.cart_listbox.insert(tk.END, f"{item}: ${price}")
            self.update_total()
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both item and price.")

    def update_total(self):
        total = sum(item[1] for item in self.items)
        self.total_value_label.config(text=f"${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
