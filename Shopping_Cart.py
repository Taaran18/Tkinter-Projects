import tkinter as tk
from tkinter import messagebox


class ShoppingCartApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Shopping Cart App")

        # List to store items and their prices in the shopping cart
        self.items = []

        # Create and configure widgets for entering item details
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        # Button to add an item to the cart
        self.add_to_cart_button = tk.Button(
            root, text="Add to Cart", command=self.add_to_cart
        )
        self.add_to_cart_button.pack()

        # Listbox to display items in the cart
        self.cart_listbox = tk.Listbox(root, width=40)
        self.cart_listbox.pack()

        # Labels to display the total cost
        self.total_label = tk.Label(root, text="Total:")
        self.total_label.pack()

        self.total_value_label = tk.Label(root, text="0.00")
        self.total_value_label.pack()

    def add_to_cart(self):
        # Get item and price details and add to the shopping cart
        item = self.item_entry.get()
        price = self.price_entry.get()
        if item and price:
            self.items.append((item, float(price)))
            self.cart_listbox.insert(tk.END, f"{item}: ${price}")
            self.update_total()
            # Clear entry fields after adding an item
            self.item_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            # Show a warning if either item or price is missing
            messagebox.showwarning("Warning", "Please enter both item and price.")

    def update_total(self):
        # Calculate and update the total cost
        total = sum(item[1] for item in self.items)
        self.total_value_label.config(text=f"${total:.2f}")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
