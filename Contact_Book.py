import tkinter as tk
from tkinter import messagebox


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")

        # List to store contacts (each contact is a tuple of name and phone)
        self.contacts = []

        # Label and Entry for entering contact name
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # Label and Entry for entering contact phone number
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Button to add a new contact
        self.add_contact_button = tk.Button(
            root, text="Add Contact", command=self.add_contact
        )
        self.add_contact_button.pack()

        # Listbox to display the list of contacts
        self.contact_listbox = tk.Listbox(root, width=40)
        self.contact_listbox.pack()

    def add_contact(self):
        # Retrieve the name and phone entries
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            # If both name and phone are provided, add the contact to the list
            contact = (name, phone)
            self.contacts.append(contact)

            # Update the Listbox to display the new contact
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")

            # Clear the name and phone entries
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            # Show a warning if either name or phone is missing
            messagebox.showwarning("Warning", "Please enter both name and phone.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
