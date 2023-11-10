import tkinter as tk

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter App")

        self.text_label = tk.Label(root, text="Enter Text:")
        self.text_label.pack()

        self.text_widget = tk.Text(root, height=10, width=50)
        self.text_widget.pack()

        self.count_button = tk.Button(root, text="Count Words", command=self.count_words)
        self.count_button.pack()

        self.word_count_label = tk.Label(root, text="Word Count:")
        self.word_count_label.pack()

        self.word_count_value_label = tk.Label(root, text="0")
        self.word_count_value_label.pack()

    def count_words(self):
        text = self.text_widget.get("1.0", tk.END)
        words = text.split()
        word_count = len(words)
        self.word_count_value_label.config(text=str(word_count))

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
