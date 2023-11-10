import tkinter as tk


class ShoppingListApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Shopping List App")

        # List to store items in the shopping list
        self.shopping_list = []

        # Label and Entry for entering a new item
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        # Button to add an item to the shopping list
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        # Listbox to display the shopping list
        self.shopping_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.shopping_listbox.pack()

        # Button to remove a selected item from the shopping list
        self.remove_button = tk.Button(
            root, text="Remove Item", command=self.remove_item
        )
        self.remove_button.pack()

    def add_item(self):
        # Add a new item to the shopping list
        item = self.item_entry.get()
        if item:
            self.shopping_list.append(item)
            self.update_listbox()
            self.item_entry.delete(0, tk.END)

    def remove_item(self):
        # Remove a selected item from the shopping list
        selected_index = self.shopping_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.shopping_list[index]
            self.update_listbox()

    def update_listbox(self):
        # Update the listbox to reflect the current shopping list
        self.shopping_listbox.delete(0, tk.END)
        for item in self.shopping_list:
            self.shopping_listbox.insert(tk.END, item)


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
