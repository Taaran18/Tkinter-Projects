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
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                color = "white" if (row + col) % 2 == 0 else "black"
                self.buttons[row][col] = tk.Button(root, text=piece, bg=color, width=5, height=2,
                                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def on_button_click(self, row, col):
        piece = self.board[row][col]
        if piece:
            print(f"Selected piece: {piece}")
        else:
            print("No piece selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessGameApp(root)
    root.mainloop()
