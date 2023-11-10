import tkinter as tk


class ToDoListApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("ToDo List App")

        # Initialize the list to store tasks
        self.tasks = []

        # Create and place widgets in the window
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack()

        self.delete_task_button = tk.Button(
            root, text="Delete Task", command=self.delete_task
        )
        self.delete_task_button.pack()

    def add_task(self):
        # Add a task to the list when the "Add Task" button is clicked
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        # Delete the selected task when the "Delete Task" button is clicked
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.update_task_list()

    def update_task_list(self):
        # Update the task list displayed in the Listbox
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
