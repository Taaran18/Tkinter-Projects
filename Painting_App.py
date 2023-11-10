import tkinter as tk


class PaintingApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Painting App")

        # Create a canvas for drawing
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create labels for color and brush size
        self.color_label = tk.Label(root, text="Color:")
        self.color_label.pack()

        # Set the default color to black
        self.color_var = tk.StringVar(root)
        self.color_var.set("black")

        # Dropdown menu for selecting color
        self.color_menu = tk.OptionMenu(
            root, self.color_var, "black", "red", "blue", "green"
        )
        self.color_menu.pack()

        # Create labels for brush size
        self.size_label = tk.Label(root, text="Brush Size:")
        self.size_label.pack()

        # Set the default size to 2
        self.size_var = tk.StringVar(root)
        self.size_var.set("2")

        # Dropdown menu for selecting brush size
        self.size_menu = tk.OptionMenu(root, self.size_var, "2", "4", "6", "8")
        self.size_menu.pack()

        # Button to clear the canvas
        self.clear_button = tk.Button(
            root, text="Clear Canvas", command=self.clear_canvas
        )
        self.clear_button.pack()

        # Bind mouse events to canvas
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Initialize drawing variables
        self.is_drawing = False
        self.last_x = 0
        self.last_y = 0

    def start_drawing(self, event):
        # Start drawing when the left mouse button is pressed
        self.is_drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        # Draw lines while the left mouse button is held down
        if self.is_drawing:
            x = event.x
            y = event.y
            color = self.color_var.get()
            size = int(self.size_var.get())
            self.canvas.create_line(
                self.last_x, self.last_y, x, y, fill=color, width=size
            )
            self.last_x = x
            self.last_y = y

    def stop_drawing(self, event):
        # Stop drawing when the left mouse button is released
        self.is_drawing = False

    def clear_canvas(self):
        # Clear the entire canvas
        self.canvas.delete("all")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = PaintingApp(root)
    root.mainloop()
