import tkinter as tk
import random
from tkinter import messagebox


class MemoryGameApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Memory Game App")

        # Define the cards with pairs of letters (total of 16 cards)
        self.cards = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
        ]
        random.shuffle(self.cards)  # Shuffle the cards randomly
        self.flipped_cards = []  # List to store the indices of flipped cards
        self.num_matches = 0  # Counter for the number of matched pairs

        # Create a 4x4 grid of buttons for the game board
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        for row in range(4):
            for col in range(4):
                # Create a button for each card and assign the flip_card function as the command
                button = tk.Button(
                    root,
                    text="",
                    width=10,
                    height=4,
                    command=lambda r=row, c=col: self.flip_card(r, c),
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def flip_card(self, row, col):
        # Function to handle flipping a card when a button is clicked
        button = self.buttons[row][col]
        card_index = row * 4 + col
        card_value = self.cards[card_index]

        if card_index not in self.flipped_cards and len(self.flipped_cards) < 2:
            button.config(text=card_value)
            self.flipped_cards.append(card_index)

            if len(self.flipped_cards) == 2:
                # After a short delay, check if the two flipped cards match
                self.root.after(1000, self.check_match)

    def check_match(self):
        # Function to check if the two flipped cards match
        card1_index, card2_index = self.flipped_cards
        card1_value = self.cards[card1_index]
        card2_value = self.cards[card2_index]

        if card1_value == card2_value:
            # If the cards match, update the match counter
            self.num_matches += 1
            if self.num_matches == 8:
                messagebox.showinfo(
                    "Memory Game", "Congratulations! You've matched all the cards."
                )
            else:
                self.flipped_cards = (
                    []
                )  # Clear the flipped cards list for the next turn
        else:
            # If the cards don't match, flip them back after a short delay
            for index in self.flipped_cards:
                self.buttons[index // 4][index % 4].config(text="")
            self.flipped_cards = []  # Clear the flipped cards list for the next turn


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGameApp(root)
    root.mainloop()
