import tkinter as tk

class SketchDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sketch Drawing App")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.is_drawing = False
        self.last_x = 0
        self.last_y = 0

    def start_drawing(self, event):
        self.is_drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.is_drawing:
            x = event.x
            y = event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=2)
            self.last_x = x
            self.last_y = y

    def stop_drawing(self, event):
        self.is_drawing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = SketchDrawingApp(root)
    root.mainloop()
