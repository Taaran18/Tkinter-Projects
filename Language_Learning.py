import tkinter as tk
from tkinter import messagebox

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")

        self.vocabulary = {
            "apple": "manzana",
            "banana": "plátano",
            "cat": "gato",
            "dog": "perro"
        }

        self.question_label = tk.Label(root, text="Translate:")
        self.question_label.pack()

        self.question_var = tk.StringVar(root)
        self.question_label = tk.Label(root, textvariable=self.question_var)
        self.question_label.pack()

        self.answer_label = tk.Label(root, text="Your Answer:")
        self.answer_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.check_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

    def check_answer(self):
        question = self.question_var.get()
        user_answer = self.answer_entry.get()
        correct_answer = self.vocabulary.get(question.lower())

        if correct_answer and user_answer.lower() == correct_answer:
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showerror("Incorrect", f"Incorrect. The correct answer is {correct_answer}.")

        self.next_question()

    def next_question(self):
        question, _ = next(iter(self.vocabulary.items()))
        self.question_var.set(question)
        self.answer_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
