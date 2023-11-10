import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager App")

        self.passwords = []

        self.site_label = tk.Label(root, text="Website:")
        self.site_label.pack()

        self.site_entry = tk.Entry(root)
        self.site_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root)
        self.password_entry.pack()

        self.save_button = tk.Button(root, text="Save Password", command=self.save_password)
        self.save_button.pack()

        self.password_listbox = tk.Listbox(root, width=40)
        self.password_listbox.pack()

    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.passwords.append((site, password))
            self.password_listbox.insert(tk.END, f"{site}: {password}")
            self.site_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both website and password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
