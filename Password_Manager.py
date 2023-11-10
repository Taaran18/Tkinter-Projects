import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordManagerApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Password Manager App")

        # List to store website-password pairs
        self.passwords = []

        # Label and entry for entering website
        self.site_label = tk.Label(root, text="Website:")
        self.site_label.pack()

        self.site_entry = tk.Entry(root)
        self.site_entry.pack()

        # Button to generate a random password
        self.generate_button = tk.Button(
            root, text="Generate Password", command=self.generate_password
        )
        self.generate_button.pack()

        # Label and entry for displaying and entering passwords
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root)
        self.password_entry.pack()

        # Button to save the entered password
        self.save_button = tk.Button(
            root, text="Save Password", command=self.save_password
        )
        self.save_button.pack()

        # Listbox to display the saved passwords
        self.password_listbox = tk.Listbox(root, width=40)
        self.password_listbox.pack()

    def generate_password(self):
        # Generate a random password
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        # Display the generated password in the entry field
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        # Save the website and password to the list and display in the listbox
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.passwords.append((site, password))
            self.password_listbox.insert(tk.END, f"{site}: {password}")
            self.site_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            # Show a warning if either website or password is not entered
            messagebox.showwarning("Warning", "Please enter both website and password.")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
