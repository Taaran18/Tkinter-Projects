import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.add_contact_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack()

        self.contact_listbox = tk.Listbox(root, width=40)
        self.contact_listbox.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact = (name, phone)
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
