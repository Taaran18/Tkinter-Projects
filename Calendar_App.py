import tkinter as tk
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.year_label = tk.Label(root, text="Year:")
        self.year_label.pack()

        self.year_entry = tk.Entry(root)
        self.year_entry.pack()

        self.show_calendar_button = tk.Button(root, text="Show Calendar", command=self.show_calendar)
        self.show_calendar_button.pack()

        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack()

    def show_calendar(self):
        year = int(self.year_entry.get())
        cal_text = self.generate_calendar(year)
        self.calendar_frame.config(text=cal_text)

    def generate_calendar(self, year):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_text = cal.formatyear(year)
        return cal_text

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
