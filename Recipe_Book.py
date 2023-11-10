import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class Recipe:
    def __init__(self, name, ingredients, instructions, image_path):
        # Initialize a Recipe object with name, ingredients, instructions, and image path
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_path = image_path


class RecipeBookApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Recipe Book App")

        # Initialize a list to store Recipe objects
        self.recipes = []

        # Create and configure widgets for entering recipe details
        self.recipe_name_label = tk.Label(root, text="Recipe Name:")
        self.recipe_name_label.pack()

        self.recipe_name_entry = tk.Entry(root)
        self.recipe_name_entry.pack()

        self.ingredients_label = tk.Label(root, text="Ingredients:")
        self.ingredients_label.pack()

        self.ingredients_text = tk.Text(root, height=5, width=40)
        self.ingredients_text.pack()

        self.instructions_label = tk.Label(root, text="Instructions:")
        self.instructions_label.pack()

        self.instructions_text = tk.Text(root, height=10, width=40)
        self.instructions_text.pack()

        self.image_label = tk.Label(root, text="Recipe Image:")
        self.image_label.pack()

        self.image_path = tk.StringVar()
        self.image_path_label = tk.Label(root, textvariable=self.image_path)
        self.image_path_label.pack()

        # Create buttons for loading an image, adding a recipe, and viewing recipes
        self.load_image_button = tk.Button(
            root, text="Load Image", command=self.load_image
        )
        self.load_image_button.pack()

        self.add_recipe_button = tk.Button(
            root, text="Add Recipe", command=self.add_recipe
        )
        self.add_recipe_button.pack()

        self.view_recipes_button = tk.Button(
            root, text="View Recipes", command=self.view_recipes
        )
        self.view_recipes_button.pack()

    def load_image(self):
        # Open a file dialog to select an image file and update the image path label
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
        )
        self.image_path.set(file_path)

    def add_recipe(self):
        # Get recipe details from the entry widgets, create a Recipe object, and add it to the list
        name = self.recipe_name_entry.get()
        ingredients = self.ingredients_text.get("1.0", tk.END)
        instructions = self.instructions_text.get("1.0", tk.END)
        image_path = self.image_path.get()

        recipe = Recipe(name, ingredients, instructions, image_path)
        self.recipes.append(recipe)

        # Clear the entry widgets
        self.recipe_name_entry.delete(0, tk.END)
        self.ingredients_text.delete("1.0", tk.END)
        self.instructions_text.delete("1.0", tk.END)
        self.image_path.set("")

    def view_recipes(self):
        # Open a new window to display the stored recipes with their details
        recipes_window = tk.Toplevel(self.root)
        recipes_window.title("View Recipes")

        for recipe in self.recipes:
            # Create a frame for each recipe
            recipe_frame = tk.Frame(recipes_window)
            recipe_frame.pack(padx=10, pady=10)

            # Display recipe name in a larger font
            recipe_name_label = tk.Label(
                recipe_frame, text=recipe.name, font=("Helvetica", 14, "bold")
            )
            recipe_name_label.pack()

            # Display ingredients label and text
            ingredients_label = tk.Label(
                recipe_frame, text="Ingredients:", font=("Helvetica", 12)
            )
            ingredients_label.pack()

            ingredients_text = tk.Text(recipe_frame, height=5, width=40)
            ingredients_text.insert(tk.END, recipe.ingredients)
            ingredients_text.pack()

            # Display instructions label and text
            instructions_label = tk.Label(
                recipe_frame, text="Instructions:", font=("Helvetica", 12)
            )
            instructions_label.pack()

            instructions_text = tk.Text(recipe_frame, height=10, width=40)
            instructions_text.insert(tk.END, recipe.instructions)
            instructions_text.pack()

            # Display recipe image if available
            if recipe.image_path:
                img = Image.open(recipe.image_path)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                image_label = tk.Label(recipe_frame, image=img)
                image_label.image = img
                image_label.pack()


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = RecipeBookApp(root)
    root.mainloop()
