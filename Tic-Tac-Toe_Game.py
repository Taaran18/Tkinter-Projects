import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Tic-Tac-Toe Game")

        # Initialize game state variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Create and place buttons on the game board
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                # Use lambda to pass row and column indices to make_move function
                button = tk.Button(
                    root,
                    text="",
                    width=10,
                    height=3,
                    command=lambda r=row, c=col: self.make_move(r, c),
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        # Make a move when a button is clicked
        if self.board[row][col] == "":
            # Update board state and button text
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner or draw
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "It's a draw!")
                self.reset_board()
            else:
                # Switch to the other player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check for a winner in rows, columns, and diagonals
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        # Check for a draw (all spaces filled)
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset_board(self):
        # Reset the game board and button texts
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                self.buttons[row][col].config(text="")


if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
