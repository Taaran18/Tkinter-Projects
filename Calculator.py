import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Calculator App")

        # Create a StringVar to store and update the result display
        self.result_var = tk.StringVar()

        # Label to display the result
        self.result_label = tk.Label(root, textvariable=self.result_var)
        self.result_label.pack()

        # Frame to hold the calculator buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Define the labels for calculator buttons
        button_labels = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
            "C",  # Added clear button
        ]

        row = 0
        col = 0

        # Create buttons based on the button_labels list
        for label in button_labels:
            # Use lambda to pass the button label to the on_button_click method
            tk.Button(
                self.button_frame,
                text=label,
                command=lambda lbl=label: self.on_button_click(lbl),
            ).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button_text):
        # Handle button clicks
        if button_text == "=":
            try:
                # Evaluate the expression and update the result display
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                # Handle errors in the expression
                self.result_var.set("Error")
        elif button_text == "C":
            # Clear the result display
            self.result_var.set("")
        else:
            # Concatenate button_text to the current expression
            current_text = self.result_var.get()
            new_text = current_text + button_text
            self.result_var.set(new_text)


if __name__ == "__main__":
    # Create and run the Calculator application
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
