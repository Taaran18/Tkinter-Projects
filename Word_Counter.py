import tkinter as tk


class WordCounterApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Word Counter App")

        # Create and place widgets in the window
        self.text_label = tk.Label(root, text="Enter Text:")
        self.text_label.pack()

        self.text_widget = tk.Text(root, height=10, width=50)
        self.text_widget.pack()

        self.count_button = tk.Button(
            root, text="Count Words", command=self.count_words
        )
        self.count_button.pack()

        self.word_count_label = tk.Label(root, text="Word Count:")
        self.word_count_label.pack()

        self.word_count_value_label = tk.Label(root, text="0")
        self.word_count_value_label.pack()

    def count_words(self):
        # Get the text from the Text widget
        text = self.text_widget.get("1.0", tk.END)

        # Split the text into words using whitespace as the separator
        words = text.split()

        # Count the number of words
        word_count = len(words)

        # Update the word count label with the result
        self.word_count_value_label.config(text=str(word_count))


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
