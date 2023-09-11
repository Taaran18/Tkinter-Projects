import tkinter as tk
import time

class TaskTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Timer App")

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()

        self.timer_label = tk.Label(root, text="Time left: 00:00")
        self.timer_label.pack()

        self.running = False
        self.end_time = 0

    def start_timer(self):
        if not self.running:
            task_time = 300  # 5 minutes in seconds
            self.end_time = time.time() + task_time
            self.running = True
            self.update_timer()

    def update_timer(self):
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
                self.root.after(1000, self.update_timer)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTimerApp(root)
    root.mainloop()
