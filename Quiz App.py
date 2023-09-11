import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = []
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var)
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.load_questions()

    def load_questions(self):
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
        ]
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]["question"]
            self.question_label.config(text=question)
            self.answer_var.set("")
        else:
            self.question_label.config(text="Quiz completed!")
            self.answer_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

    def submit_answer(self):
        if self.current_question_index < len(self.questions):
            user_answer = self.answer_var.get().strip().lower()
            correct_answer = self.questions[self.current_question_index]["answer"].lower()

            if user_answer == correct_answer:
                self.score += 1

            self.score_label.config(text=f"Score: {self.score}")
            self.current_question_index += 1
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
