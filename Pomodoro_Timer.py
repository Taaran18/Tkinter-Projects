import tkinter as tk
from tkinter import messagebox
import time


class PomodoroTimerApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Pomodoro Timer App")

        # Set initial durations and variables
        self.work_duration = 25  # in minutes
        self.break_duration = 5  # in minutes
        self.time_left = self.work_duration * 60
        self.timer_running = False

        # Create and configure the time label
        self.time_label = tk.Label(
            root, text=f"{self.work_duration:02}:00", font=("Helvetica", 48)
        )
        self.time_label.pack()

        # Create start and stop buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

    def start_timer(self):
        # Start the timer if not already running
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.run_timer()

    def stop_timer(self):
        # Stop the timer if running
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def run_timer(self):
        # Update the timer display and check for completion
        if self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.time_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.run_timer)
        else:
            # Handle the end of a work or break session
            if self.work_duration == 0:
                self.work_duration = self.break_duration
                message = "Time for a break!"
            else:
                self.work_duration = 0
                message = "Time to work!"

            # Reset timer variables, notify the user, and bring the window to the front
            self.time_left = self.work_duration * 60
            self.time_label.config(text=f"{self.work_duration:02}:00")
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.root.lift()  # Bring the app window to the front
            messagebox.showinfo("Pomodoro Timer", message)


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = PomodoroTimerApp(root)
    root.mainloop()
