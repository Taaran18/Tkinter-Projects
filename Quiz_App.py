import tkinter as tk


class QuizApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Quiz App")

        # Initialize variables for questions, current question index, and score
        self.questions = []
        self.current_question_index = 0
        self.score = 0

        # Create and configure widgets for question display
        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        # Create and configure entry widget for user answers
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var)
        self.answer_entry.pack()

        # Create and configure button for submitting answers
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        # Create and configure label for displaying the score
        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        # Load quiz questions
        self.load_questions()

    def load_questions(self):
        # Load quiz questions with corresponding answers
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {
                "question": "What is the largest planet in our solar system?",
                "answer": "Jupiter",
            },
        ]
        # Display the first question
        self.show_question()

    def show_question(self):
        # Display the current question or end of the quiz message
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]["question"]
            self.question_label.config(text=question)
            self.answer_var.set("")  # Clear the answer entry
        else:
            self.question_label.config(text="Quiz completed!")
            self.answer_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

    def submit_answer(self):
        # Check user's answer, update the score, and display the next question
        if self.current_question_index < len(self.questions):
            user_answer = self.answer_var.get().strip().lower()
            correct_answer = self.questions[self.current_question_index][
                "answer"
            ].lower()

            if user_answer == correct_answer:
                self.score += 1

            # Update the score label
            self.score_label.config(text=f"Score: {self.score}")

            # Move to the next question
            self.current_question_index += 1
            self.show_question()


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
