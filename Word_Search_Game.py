import tkinter as tk
from tkinter import messagebox


class WordSearchGameApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Word Search Game")

        # List of words to find in the game
        self.words_to_find = ["PYTHON", "JAVA", "C", "RUBY"]

        # Create and place widgets in the window
        self.word_label = tk.Label(root, text="Word:")
        self.word_label.pack()

        self.word_entry = tk.Entry(root)
        self.word_entry.pack()

        self.check_button = tk.Button(root, text="Check Word", command=self.check_word)
        self.check_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def check_word(self):
        # Get the word entered by the user
        word = self.word_entry.get()

        # Check if the entered word is in the list of words to find
        if word in self.words_to_find:
            self.result_label.config(
                text=f"Congratulations! You found the word: {word}"
            )
        else:
            self.result_label.config(
                text=f"Sorry, {word} is not in the list of words to find."
            )


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = WordSearchGameApp(root)
    root.mainloop()
