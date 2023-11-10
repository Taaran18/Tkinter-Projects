import tkinter as tk
from tkinter import messagebox


class LanguageLearningApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Language Learning App")

        # Vocabulary dictionary containing word pairs
        self.vocabulary = {
            "apple": "manzana",
            "banana": "plátano",
            "cat": "gato",
            "dog": "perro",
        }

        # Label to display the translation question
        self.question_label = tk.Label(root, text="Translate:")
        self.question_label.pack()

        # Variable to dynamically update the question label
        self.question_var = tk.StringVar(root)
        self.question_label = tk.Label(root, textvariable=self.question_var)
        self.question_label.pack()

        # Labels and entry for user input
        self.answer_label = tk.Label(root, text="Your Answer:")
        self.answer_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        # Button to check the user's answer
        self.check_button = tk.Button(
            root, text="Check Answer", command=self.check_answer
        )
        self.check_button.pack()

    def check_answer(self):
        # Function to check the user's answer against the correct answer
        question = self.question_var.get()
        user_answer = self.answer_entry.get()
        correct_answer = self.vocabulary.get(question.lower())

        # Display a message box based on the correctness of the answer
        if correct_answer and user_answer.lower() == correct_answer:
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showerror(
                "Incorrect", f"Incorrect. The correct answer is {correct_answer}."
            )

        # Move on to the next question
        self.next_question()

    def next_question(self):
        # Function to move to the next question in the vocabulary
        question, _ = next(iter(self.vocabulary.items()))
        self.question_var.set(question)
        self.answer_entry.delete(0, tk.END)


if __name__ == "__main__":
    # Create and run the Language Learning application
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
