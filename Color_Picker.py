import tkinter as tk
from tkinter import colorchooser


class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker App")

        # Label to display the selected color
        self.color_label = tk.Label(root, text="Selected Color:")
        self.color_label.pack()

        # Frame to show the selected color
        self.color_frame = tk.Frame(root, width=100, height=50)
        self.color_frame.pack()

        # Button to trigger the color picker dialog
        self.color_button = tk.Button(root, text="Pick Color", command=self.pick_color)
        self.color_button.pack()

        # Labels to display the RGB and Hex values of the selected color
        self.rgb_label = tk.Label(root, text="RGB:")
        self.rgb_label.pack()

        self.hex_label = tk.Label(root, text="Hex:")
        self.hex_label.pack()

    def pick_color(self):
        # Open the color chooser dialog and get the selected color
        color = colorchooser.askcolor()[1]  # Returns a tuple (RGB, Hex)

        if color:
            # Update the color frame with the selected color
            self.color_frame.config(bg=color)

            # Update the RGB and Hex labels with the selected color values
            self.rgb_label.config(text=f"RGB: {color}")
            self.hex_label.config(text=f"Hex: {color.upper()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
