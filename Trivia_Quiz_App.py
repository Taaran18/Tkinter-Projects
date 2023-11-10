import tkinter as tk
from tkinter import messagebox

class TriviaQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz App")

        self.questions = []
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack()

        self.question_entry = tk.Entry(root)
        self.question_entry.pack()

        self.options_label = tk.Label(root, text="Options (comma-separated):")
        self.options_label.pack()

        self.options_entry = tk.Entry(root)
        self.options_entry.pack()

        self.correct_option_label = tk.Label(root, text="Correct Option (1-indexed):")
        self.correct_option_label.pack()

        self.correct_option_entry = tk.Entry(root)
        self.correct_option_entry.pack()

        self.add_question_button = tk.Button(root, text="Add Question", command=self.add_question)
        self.add_question_button.pack()

        self.start_quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_quiz_button.pack()

        self.quiz_label = tk.Label(root, text="")
        self.quiz_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack()

    def add_question(self):
        question = self.question_entry.get()
        options = [option.strip() for option in self.options_entry.get().split(",")]
        correct_option = int(self.correct_option_entry.get())
        if question and options and 1 <= correct_option <= len(options):
            self.questions.append((question, options, correct_option))
            self.question_entry.delete(0, tk.END)
            self.options_entry.delete(0, tk.END)
            self.correct_option_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter valid question, options, and correct option.")

    def start_quiz(self):
        if self.questions:
            self.current_question = 0
            self.score = 0
            self.show_question()
        else:
            messagebox.showwarning("Warning", "Please add questions first.")

    def show_question(self):
        if self.current_question < len(self.questions):
            question, options, _ = self.questions[self.current_question]
            options_text = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(options)])
            self.quiz_label.config(text=f"{question}\n{options_text}")
            self.answer_entry.delete(0, tk.END)
        else:
            self.quiz_label.config(text=f"Quiz Finished!\nYour Score: {self.score}/{len(self.questions)}")

    def submit_answer(self):
        if self.current_question < len(self.questions):
            _, _, correct_option = self.questions[self.current_question]
            selected_option = int(self.answer_entry.get())
            if selected_option == correct_option:
                self.score += 1
            self.current_question += 1
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaQuizApp(root)
    root.mainloop()
