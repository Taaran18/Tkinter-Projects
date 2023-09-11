import tkinter as tk
from tkinter import messagebox

class FlashcardQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = []
        self.current_flashcard = 0
        self.score = 0

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

        self.start_quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_quiz_button.pack()

        self.quiz_label = tk.Label(root, text="")
        self.quiz_label.pack()

        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_flashcard)
        self.next_button.pack()

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append((question, answer))
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both question and answer.")

    def start_quiz(self):
        if self.flashcards:
            self.current_flashcard = 0
            self.score = 0
            self.show_flashcard()
        else:
            messagebox.showwarning("Warning", "Please add flashcards first.")

    def show_flashcard(self):
        if self.current_flashcard < len(self.flashcards):
            question = self.flashcards[self.current_flashcard][0]
            self.quiz_label.config(text=question)
            self.show_answer_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.quiz_label.config(text=f"Quiz Finished!\nYour Score: {self.score}/{len(self.flashcards)}")
            self.show_answer_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

    def show_answer(self):
        answer = self.flashcards[self.current_flashcard][1]
        self.quiz_label.config(text=f"Answer: {answer}")
        self.show_answer_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_flashcard(self):
        self.current_flashcard += 1
        self.score += 1
        self.show_flashcard()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardQuizApp(root)
    root.mainloop()
