import tkinter as tk
from tkinter import messagebox
import datetime

class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Reminder App")

        self.reminders = []

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()

        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.reminder_label = tk.Label(root, text="Reminder:")
        self.reminder_label.pack()

        self.reminder_entry = tk.Entry(root)
        self.reminder_entry.pack()

        self.add_reminder_button = tk.Button(root, text="Add Reminder", command=self.add_reminder)
        self.add_reminder_button.pack()

    def add_reminder(self):
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()
        reminder_text = self.reminder_entry.get()

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            time = datetime.datetime.strptime(time_str, "%H:%M").time()

            reminder_datetime = datetime.datetime.combine(date.date(), time)
            self.reminders.append((reminder_datetime, reminder_text))
            messagebox.showinfo("Reminder Added", "Reminder has been added.")
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.reminder_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter valid date and time.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()
