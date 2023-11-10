import tkinter as tk
from tkinter import messagebox
import json


class PasswordVaultApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Password Vault App")

        # Dictionary to store website-password pairs with username
        self.passwords = {}

        # Labels and entries for entering website, username, and password
        self.website_label = tk.Label(root, text="Website:")
        self.website_label.pack()

        self.website_entry = tk.Entry(root)
        self.website_entry.pack()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Button to save the entered password
        self.save_button = tk.Button(
            root, text="Save Password", command=self.save_password
        )
        self.save_button.pack()

        # Button to view saved passwords
        self.view_button = tk.Button(
            root, text="View Passwords", command=self.view_passwords
        )
        self.view_button.pack()

    def save_password(self):
        # Save the website, username, and password to the dictionary
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            self.passwords[website] = {"username": username, "password": password}
            self.website_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Password saved successfully.")
        else:
            # Show an error if any field is empty
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_passwords(self):
        # Display a new window to view saved passwords
        passwords_window = tk.Toplevel(self.root)
        passwords_window.title("View Passwords")

        for website, data in self.passwords.items():
            # Create a frame for each saved password
            password_frame = tk.Frame(passwords_window)
            password_frame.pack(padx=10, pady=10)

            # Labels to display website, username, and password
            website_label = tk.Label(password_frame, text=f"Website: {website}")
            website_label.pack()

            username_label = tk.Label(
                password_frame, text=f"Username: {data['username']}"
            )
            username_label.pack()

            password_label = tk.Label(
                password_frame, text=f"Password: {data['password']}"
            )
            password_label.pack()


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = PasswordVaultApp(root)
    root.mainloop()
