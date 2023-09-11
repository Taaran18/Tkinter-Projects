import tkinter as tk

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator App")

        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Height (cm):")
        self.height_label.pack()

        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get()) / 100  # Convert cm to meters

        if weight > 0 and height > 0:
            bmi = weight / (height * height)
            category = self.get_bmi_category(bmi)
            self.result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
        else:
            self.result_label.config(text="Please enter valid weight and height.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
