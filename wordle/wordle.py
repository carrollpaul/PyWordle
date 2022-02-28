import random


class Wordle:
    def __init__(self) -> None:
        with open("wordle/words.txt", "r") as f:
            text = f.read()
            self.words = list(map(str, text.split()))

        self.answer = random.choice(self.words)

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
