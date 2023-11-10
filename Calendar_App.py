import tkinter as tk
from tkinter import ttk, scrolledtext
import calendar


class CalendarApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Calendar App")

        # Label and entry for year input
        self.year_label = tk.Label(root, text="Year:")
        self.year_label.pack()

        self.year_entry = tk.Entry(root)
        self.year_entry.pack()

        # Label and dropdown for month input
        self.month_label = tk.Label(root, text="Month:")
        self.month_label.pack()

        # Use StringVar to store the selected month
        self.month_var = tk.StringVar()

        # Create a dropdown menu with month names
        self.month_dropdown = ttk.Combobox(
            root, textvariable=self.month_var, values=list(calendar.month_name)[1:]
        )
        self.month_dropdown.pack()

        # Button to show the calendar
        self.show_calendar_button = tk.Button(
            root, text="Show Calendar", command=self.show_calendar
        )
        self.show_calendar_button.pack()

        # Frame to display the calendar
        self.calendar_text = scrolledtext.ScrolledText(root, width=40, height=10)
        self.calendar_text.pack()

    def show_calendar(self):
        # Display the calendar for the given month and year
        try:
            year = int(self.year_entry.get())
            month_name = self.month_var.get()
            month = list(calendar.month_name).index(month_name)
            cal_text = self.generate_calendar(year, month)
            self.calendar_text.delete(1.0, tk.END)  # Clear previous text
            self.calendar_text.insert(tk.END, cal_text)  # Insert new calendar text
        except ValueError:
            # Handle invalid input
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, "Invalid input")

    def generate_calendar(self, year, month):
        # Generate and return the calendar as text
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_text = cal.formatmonth(year, month)
        return cal_text


if __name__ == "__main__":
    # Create and run the Calendar application
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
