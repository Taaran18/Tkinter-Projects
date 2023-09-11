import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")

        self.result_var = tk.StringVar()

        self.result_label = tk.Label(root, textvariable=self.result_var)
        self.result_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        for label in button_labels:
            tk.Button(self.button_frame, text=label, command=lambda lbl=label: self.on_button_click(lbl)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + button_text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
