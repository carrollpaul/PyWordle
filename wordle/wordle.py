import random

from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from wordle.gui import update_display


class Wordle:
    def __init__(self) -> None:
        with open("wordle/words.txt", "r") as f:
            self.words = f.read().splitlines()

        self.answer = random.choice(self.words)
        self.console = Console(width=50)
        self.table = Table(box=None)

    def is_valid_guess(self, guess: str) -> bool:
        """
        Returns true if guess is five letters and exists in word list.
        """
        if len(guess) != 5:
            return False

        if not guess.isalpha():
            return False

        if guess.lower() not in self.words:
            return False

        return True

    def check_guess(self, guess: str) -> tuple[bool, dict[int, str]]:
        """
        Checks guess against puzzle answer.

        Args:
            guess: The guess to check against the puzzle answer.

        Returns:
            A tuple with two values:
                1. A boolean indicating if the guess is correct
                2. A dictionary mapping each letter's index in guess to their status
        """
        guess = guess.lower()

        if guess == self.answer:
            letters = {i: "green" for i in range(5)}
            return True, letters

        letters = {}
        for index, letter in enumerate(guess):
            if letter not in self.answer:
                letters[index] = "black"

            elif letter == self.answer[index]:
                letters[index] = "green"

            else:
                letters[index] = "yellow"

        return False, letters

    def play(self) -> None:
        guesses_remaining = 6

        # Main game loop
        while guesses_remaining:
            update_display(self.console, self.table)

            # Get guess and validate
            while True:
                guess = self.console.input(
                    f"[b] Gimme a word ([red]{guesses_remaining}[/red] remaining): "
                )
                if self.is_valid_guess(guess):
                    break

                self.console.print("[red]Invalid guess![/red] :angry:")

            # Check guess against puzzle answer
            correct_guess, letters = self.check_guess(guess)

            # Display each letter as a box with color corresponding to status
            row = [
                f"[white on {status}] {guess[index]} [/white on {status}]"
                for index, status in letters.items()
            ]
            self.table.add_row(*row)
            self.table.add_row("")
            self.console.print(self.table)

            if correct_guess:
                panel = Panel("You nailed it!", title=":victory_hand:")
                update_display(self.console, self.table, panel)
                return

            guesses_remaining -= 1

        panel = Panel(
            f"Better luck next time! Correct answer is [bold green]{self.answer}[/bold green]",
            title=":frowning_face:",
        )
        update_display(self.console, self.table, panel)
