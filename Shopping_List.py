import tkinter as tk

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List App")

        self.shopping_list = []

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.shopping_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.shopping_listbox.pack()

        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        if item:
            self.shopping_list.append(item)
            self.update_listbox()
            self.item_entry.delete(0, tk.END)

    def remove_item(self):
        selected_index = self.shopping_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.shopping_list[index]
            self.update_listbox()

    def update_listbox(self):
        self.shopping_listbox.delete(0, tk.END)
        for item in self.shopping_list:
            self.shopping_listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
