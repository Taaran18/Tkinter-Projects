import tkinter as tk
import time


class TaskTimerApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Task Timer App")

        # Label and entry for task input
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        # Button to start the timer
        self.start_button = tk.Button(
            root, text="Start Timer", command=self.start_timer
        )
        self.start_button.pack()

        # Label to display the timer
        self.timer_label = tk.Label(root, text="Time left: 00:00")
        self.timer_label.pack()

        # Variables to track timer state
        self.running = False
        self.end_time = 0

    def start_timer(self):
        # Start the timer with a default time of 5 minutes (300 seconds)
        if not self.running:
            task_time = 300  # 5 minutes in seconds
            self.end_time = time.time() + task_time
            self.running = True
            self.update_timer()

    def update_timer(self):
        # Update the timer display and check for timer completion
        if self.running:
            remaining_time = self.end_time - time.time()
            if remaining_time <= 0:
                self.timer_label.config(text="Time's up!")
                self.running = False
            else:
                minutes = int(remaining_time // 60)
                seconds = int(remaining_time % 60)
                time_format = f"{minutes:02}:{seconds:02}"
                self.timer_label.config(text=f"Time left: {time_format}")
                # Schedule the update every second
                self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = TaskTimerApp(root)
    root.mainloop()
