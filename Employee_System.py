import tkinter as tk
from tkinter import messagebox


class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary


class EmployeeSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System App")

        # List to store employee objects
        self.employees = []

        # Widgets for adding an employee
        self.id_label = tk.Label(root, text="Employee ID:")
        self.id_label.pack()

        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.position_label = tk.Label(root, text="Position:")
        self.position_label.pack()

        self.position_entry = tk.Entry(root)
        self.position_entry.pack()

        self.salary_label = tk.Label(root, text="Salary:")
        self.salary_label.pack()

        self.salary_entry = tk.Entry(root)
        self.salary_entry.pack()

        # Buttons for adding, viewing, and searching employees
        self.add_button = tk.Button(
            root, text="Add Employee", command=self.add_employee
        )
        self.add_button.pack()

        self.view_button = tk.Button(
            root, text="View Employees", command=self.view_employees
        )
        self.view_button.pack()

        # Widgets for searching an employee
        self.search_label = tk.Label(root, text="Search by ID:")
        self.search_label.pack()

        self.search_id_entry = tk.Entry(root)
        self.search_id_entry.pack()

        self.search_button = tk.Button(
            root, text="Search", command=self.search_employee
        )
        self.search_button.pack()

    def add_employee(self):
        # Function to add an employee to the list
        id = self.id_entry.get()
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()

        if id and name and position and salary:
            employee = Employee(id, name, position, salary)
            self.employees.append(employee)

            # Clear entry fields after adding an employee
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Employee added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_employees(self):
        # Function to display a separate window with a list of employees
        employees_window = tk.Toplevel(self.root)
        employees_window.title("View Employees")

        for employee in self.employees:
            # Display employee information in a frame
            employee_frame = tk.Frame(employees_window, borderwidth=2, relief="solid")
            employee_frame.pack(padx=10, pady=10, fill=tk.X)

            employee_id_label = tk.Label(employee_frame, text=f"ID: {employee.id}")
            employee_id_label.pack()

            employee_name_label = tk.Label(
                employee_frame, text=f"Name: {employee.name}"
            )
            employee_name_label.pack()

            employee_position_label = tk.Label(
                employee_frame, text=f"Position: {employee.position}"
            )
            employee_position_label.pack()

            employee_salary_label = tk.Label(
                employee_frame, text=f"Salary: {employee.salary}"
            )
            employee_salary_label.pack()

    def search_employee(self):
        # Function to search for an employee by ID
        search_id = self.search_id_entry.get()

        for employee in self.employees:
            if employee.id == search_id:
                # Display a message box with the employee's information
                messagebox.showinfo(
                    "Employee Found",
                    f"ID: {employee.id}\nName: {employee.name}\nPosition: {employee.position}\nSalary: {employee.salary}",
                )
                return

        # Display a message box if no employee is found with the given ID
        messagebox.showinfo(
            "Employee Not Found", f"No employee found with ID: {search_id}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeSystemApp(root)
    root.mainloop()
