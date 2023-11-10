import tkinter as tk

class PaintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Painting App")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color_label = tk.Label(root, text="Color:")
        self.color_label.pack()

        self.color_var = tk.StringVar(root)
        self.color_var.set("black")
        self.color_menu = tk.OptionMenu(root, self.color_var, "black", "red", "blue", "green")
        self.color_menu.pack()

        self.size_label = tk.Label(root, text="Brush Size:")
        self.size_label.pack()

        self.size_var = tk.StringVar(root)
        self.size_var.set("2")
        self.size_menu = tk.OptionMenu(root, self.size_var, "2", "4", "6", "8")
        self.size_menu.pack()

        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

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
            color = self.color_var.get()
            size = int(self.size_var.get())
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=color, width=size)
            self.last_x = x
            self.last_y = y

    def stop_drawing(self, event):
        self.is_drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintingApp(root)
    root.mainloop()
