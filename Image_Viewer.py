import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer App")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.open_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_image)
        self.prev_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_image)
        self.next_button.pack()

        self.current_image_index = 0
        self.image_paths = []

    def open_image(self):
        image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if image_paths:
            self.image_paths = image_paths
            self.current_image_index = 0
            self.show_image()

    def prev_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.show_image()

    def next_image(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.show_image()

    def show_image(self):
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((400, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()
