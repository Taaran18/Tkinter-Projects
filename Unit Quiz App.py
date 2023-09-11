import tkinter as tk
from tkinter import messagebox

class UnitQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Quiz App")

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
        if question and options:
            self.questions.append((question, options))
            self.question_entry.delete(0, tk.END)
            self.options_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both question and options.")

    def start_quiz(self):
        if self.questions:
            self.current_question = 0
            self.score = 0
            self.show_question()
        else:
            messagebox.showwarning("Warning", "Please add questions first.")

    def show_question(self):
        if self.current_question < len(self.questions):
            question, options = self.questions[self.current_question]
            options_text = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(options)])
            self.quiz_label.config(text=f"{question}\n{options_text}")
            self.answer_entry.delete(0, tk.END)
        else:
            self.quiz_label.config(text=f"Quiz Finished!\nYour Score: {self.score}/{len(self.questions)}")

    def submit_answer(self):
        if self.current_question < len(self.questions):
            selected_option = self.answer_entry.get()
            correct_option = self.questions[self.current_question][1][0]
            if selected_option == correct_option:
                self.score += 1
            self.current_question += 1
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitQuizApp(root)
    root.mainloop()
