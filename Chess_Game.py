import tkinter as tk


class ChessGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game App")

        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]

        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                color = "white" if (row + col) % 2 == 0 else "black"
                self.buttons[row][col] = tk.Button(
                    root,
                    text=piece,
                    bg=color,
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_button_click(r, c),
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.selected_piece = None

    def on_button_click(self, row, col):
        piece = self.board[row][col]

        if self.selected_piece:
            # Move the selected piece to the clicked square if it's a valid move
            if self.is_valid_move(self.selected_piece, row, col):
                self.board[row][col] = self.selected_piece
                self.board[self.selected_piece_row][self.selected_piece_col] = ""
                self.clear_highlights()
            else:
                print("Invalid move. Try again.")
        elif piece:
            # Select the piece if the square is not empty
            self.selected_piece = piece
            self.selected_piece_row, self.selected_piece_col = row, col
            self.highlight_possible_moves(row, col)
        else:
            print("No piece selected.")

    def is_valid_move(self, piece, to_row, to_col):
        # Implement basic validation for pawn and empty squares for demonstration
        # You can extend this function for other pieces and specific movement rules
        return (
            piece.lower() == "p"
            and to_row == self.selected_piece_row + 1
            and to_col == self.selected_piece_col
        )

    def highlight_possible_moves(self, row, col):
        # For demonstration, highlight the square below the selected piece
        if self.selected_piece.lower() == "p":
            target_row = row + 1
            target_col = col
            if 0 <= target_row < 8 and 0 <= target_col < 8:
                self.buttons[target_row][target_col].configure(bg="yellow")

    def clear_highlights(self):
        # Clear all highlighted squares
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.buttons[row][col].configure(bg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChessGameApp(root)
    root.mainloop()
