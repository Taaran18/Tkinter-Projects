import tkinter as tk
from tkinter import messagebox


class Recipe:
    def __init__(self, name, ingredients, instructions):
        # Constructor for the Recipe class to initialize its attributes
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


class RecipeManagerApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Recipe Manager App")

        # List to store Recipe objects
        self.recipes = []

        # Create and configure widgets for entering recipe details
        self.name_label = tk.Label(root, text="Recipe Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.ingredients_label = tk.Label(root, text="Ingredients:")
        self.ingredients_label.pack()

        self.ingredients_text = tk.Text(root, height=5, width=40)
        self.ingredients_text.pack()

        self.instructions_label = tk.Label(root, text="Instructions:")
        self.instructions_label.pack()

        self.instructions_text = tk.Text(root, height=10, width=40)
        self.instructions_text.pack()

        # Button to add a recipe
        self.add_button = tk.Button(root, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack()

        # Button to view recipes
        self.view_button = tk.Button(
            root, text="View Recipes", command=self.view_recipes
        )
        self.view_button.pack()

    def add_recipe(self):
        # Get recipe details and create a Recipe object
        name = self.name_entry.get()
        ingredients = self.ingredients_text.get("1.0", tk.END)
        instructions = self.instructions_text.get("1.0", tk.END)

        if name and ingredients and instructions:
            # If all fields are filled, create a Recipe object and add it to the list
            recipe = Recipe(name, ingredients, instructions)
            self.recipes.append(recipe)

            # Clear entry fields after adding a recipe
            self.name_entry.delete(0, tk.END)
            self.ingredients_text.delete("1.0", tk.END)
            self.instructions_text.delete("1.0", tk.END)

            # Show a success message
            messagebox.showinfo("Success", "Recipe added successfully.")
        else:
            # Show an error message if any field is missing
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_recipes(self):
        # Open a new window to display the list of recipes
        recipes_window = tk.Toplevel(self.root)
        recipes_window.title("View Recipes")

        for recipe in self.recipes:
            # Create a frame for each recipe
            recipe_frame = tk.Frame(recipes_window)
            recipe_frame.pack(padx=10, pady=10)

            # Display the recipe name in a larger font
            recipe_name_label = tk.Label(
                recipe_frame, text=recipe.name, font=("Helvetica", 14, "bold")
            )
            recipe_name_label.pack()

            # Display ingredients label and text box
            ingredients_label = tk.Label(
                recipe_frame, text="Ingredients:", font=("Helvetica", 12)
            )
            ingredients_label.pack()

            ingredients_text = tk.Text(recipe_frame, height=5, width=40)
            ingredients_text.insert(tk.END, recipe.ingredients)
            ingredients_text.pack()

            # Display instructions label and text box
            instructions_label = tk.Label(
                recipe_frame, text="Instructions:", font=("Helvetica", 12)
            )
            instructions_label.pack()

            instructions_text = tk.Text(recipe_frame, height=10, width=40)
            instructions_text.insert(tk.END, recipe.instructions)
            instructions_text.pack()


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = RecipeManagerApp(root)
    root.mainloop()
