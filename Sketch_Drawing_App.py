import tkinter as tk


class SketchDrawingApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Sketch Drawing App")

        # Canvas for drawing
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to canvas drawing functions
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Variables to track drawing state
        self.is_drawing = False
        self.last_x = 0
        self.last_y = 0

    def start_drawing(self, event):
        # Start drawing when the left mouse button is pressed
        self.is_drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        # Draw lines while the left mouse button is held down and moving
        if self.is_drawing:
            x = event.x
            y = event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=2)
            self.last_x = x
            self.last_y = y

    def stop_drawing(self, event):
        # Stop drawing when the left mouse button is released
        self.is_drawing = False


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = SketchDrawingApp(root)
    root.mainloop()
