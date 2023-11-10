import tkinter as tk
from tkinter import messagebox


class TimerApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Timer App")

        # Initialize timer variables
        self.time_left = 0
        self.timer_running = False

        # Create and place widgets in the window
        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.set_button = tk.Button(root, text="Set Timer", command=self.set_timer)
        self.set_button.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

    def set_timer(self):
        # Set the timer duration (you can replace this with an Entry widget for user input)
        self.time_left = int(input("Enter the duration in seconds: "))
        self.update_time_label()

    def start_timer(self):
        # Start the timer if not already running and there is time left
        if not self.timer_running and self.time_left > 0:
            self.timer_running = True
            self.set_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.run_timer()

    def stop_timer(self):
        # Stop the timer if running
        if self.timer_running:
            self.timer_running = False
            self.set_button.config(state=tk.NORMAL)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def run_timer(self):
        # Run the timer countdown and update the UI
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.update_time_label()
            self.root.after(1000, self.run_timer)
        elif self.timer_running and self.time_left == 0:
            # Timer has reached zero, stop the timer and show a message
            self.timer_running = False
            self.set_button.config(state=tk.NORMAL)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.update_time_label()
            messagebox.showinfo("Timer", "Time's up!")

    def update_time_label(self):
        # Update the displayed time on the label
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_label.config(text=f"{minutes:02}:{seconds:02}")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
