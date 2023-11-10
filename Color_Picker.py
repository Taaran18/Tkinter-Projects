import tkinter as tk
from tkinter import colorchooser

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker App")

        self.color_label = tk.Label(root, text="Selected Color:")
        self.color_label.pack()

        self.color_frame = tk.Frame(root, width=100, height=50)
        self.color_frame.pack()

        self.color_button = tk.Button(root, text="Pick Color", command=self.pick_color)
        self.color_button.pack()

        self.rgb_label = tk.Label(root, text="RGB:")
        self.rgb_label.pack()

        self.hex_label = tk.Label(root, text="Hex:")
        self.hex_label.pack()

    def pick_color(self):
        color = colorchooser.askcolor()[1]  # Returns a tuple (RGB, Hex)
        if color:
            self.color_frame.config(bg=color)
            self.rgb_label.config(text=f"RGB: {color}")
            self.hex_label.config(text=f"Hex: {color.upper()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
