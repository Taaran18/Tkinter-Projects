import tkinter as tk
from tkinter import colorchooser


class ColorPaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Palette App")

        # Label to prompt the user to select a color
        self.color_label = tk.Label(root, text="Select a Color:")
        self.color_label.pack()

        # Button to open the color chooser dialog
        self.color_button = tk.Button(
            root, text="Pick a Color", command=self.pick_color
        )
        self.color_button.pack()

        # Frame to display the selected color
        self.color_frame = tk.Frame(root, width=200, height=100)
        self.color_frame.pack()

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
    app = ColorPaletteApp(root)
    root.mainloop()
