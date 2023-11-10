import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Reminder App")

        # List to store reminders as tuples of (datetime, reminder_text)
        self.reminders = []

        # Label and entry for date input
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)

        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and entry for time input
        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)

        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label and entry for reminder input
        self.reminder_label = tk.Label(root, text="Reminder:")
        self.reminder_label.grid(row=2, column=0, padx=5, pady=5)

        self.reminder_entry = tk.Entry(root)
        self.reminder_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to add a reminder
        self.add_reminder_button = tk.Button(
            root, text="Add Reminder", command=self.add_reminder
        )
        self.add_reminder_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Treeview to display the list of reminders
        self.reminder_tree = ttk.Treeview(
            root,
            columns=("Date", "Time", "Reminder"),
            show="headings",
            selectmode="extended",
        )
        self.reminder_tree.heading("Date", text="Date")
        self.reminder_tree.heading("Time", text="Time")
        self.reminder_tree.heading("Reminder", text="Reminder")
        self.reminder_tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Button to remove selected reminders
        self.remove_reminder_button = tk.Button(
            root, text="Remove Reminder", command=self.remove_reminder
        )
        self.remove_reminder_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_reminder(self):
        # Add a reminder to the list
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()
        reminder_text = self.reminder_entry.get()

        try:
            # Parse date and time strings
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            time = datetime.datetime.strptime(time_str, "%H:%M").time()

            # Combine date and time to create a datetime object
            reminder_datetime = datetime.datetime.combine(date.date(), time)

            # Add reminder to the list
            self.reminders.append((reminder_datetime, reminder_text))

            # Show a message box indicating successful addition
            messagebox.showinfo("Reminder Added", "Reminder has been added.")

            # Clear entry fields
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.reminder_entry.delete(0, tk.END)

            # Update the Treeview with the new data
            self.update_reminder_tree()
        except ValueError:
            # Show a warning if there's an error in date or time input
            messagebox.showwarning("Warning", "Please enter valid date and time.")

    def remove_reminder(self):
        # Remove selected reminders from the list
        selected_items = self.reminder_tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a reminder to remove.")
            return

        for item in selected_items:
            reminder_index = int(self.reminder_tree.item(item, "text")) - 1
            del self.reminders[reminder_index]

        # Show a message box indicating successful removal
        messagebox.showinfo("Reminder Removed", "Selected reminders have been removed.")

        # Update the Treeview after removal
        self.update_reminder_tree()

    def update_reminder_tree(self):
        # Update the Treeview with the current list of reminders
        self.reminder_tree.delete(*self.reminder_tree.get_children())
        for i, (reminder_datetime, reminder_text) in enumerate(self.reminders, start=1):
            date_str = reminder_datetime.strftime("%Y-%m-%d")
            time_str = reminder_datetime.strftime("%H:%M")
            self.reminder_tree.insert(
                "", "end", text=str(i), values=(date_str, time_str, reminder_text)
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()
