import tkinter as tk

class FlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards App")

        self.flashcards = []
        self.current_flashcard_index = 0

        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack()

        self.question_entry = tk.Entry(root)
        self.question_entry.pack()

        self.answer_label = tk.Label(root, text="Answer:")
        self.answer_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.add_flashcard_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_flashcard_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.show_next_flashcard)
        self.next_button.pack()

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        if question and answer:
            self.flashcards.append((question, answer))
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)

    def show_next_flashcard(self):
        if self.flashcards:
            if self.current_flashcard_index >= len(self.flashcards):
                self.current_flashcard_index = 0

            current_flashcard = self.flashcards[self.current_flashcard_index]
            question, answer = current_flashcard

            self.question_label.config(text=f"Question: {question}")
            self.answer_label.config(text=f"Answer: {answer}")

            self.current_flashcard_index += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()
