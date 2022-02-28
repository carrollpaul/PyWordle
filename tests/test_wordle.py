import unittest
from wordle.wordle import Wordle


class TestWordle(unittest.TestCase):
    def setUp(self) -> None:
        self.puzzle = Wordle()
        self.puzzle.answer = "check"

    def test_is_valid_guess(self) -> None:
        self.assertFalse(self.puzzle.is_valid_guess(""))
        self.assertFalse(self.puzzle.is_valid_guess("12345"))
        self.assertFalse(self.puzzle.is_valid_guess("abcd1"))
        self.assertFalse(self.puzzle.is_valid_guess("cat"))
        self.assertFalse(self.puzzle.is_valid_guess("abcde"))

        self.assertTrue(self.puzzle.is_valid_guess("check"))

    def test_check_guess(self) -> None:
        letters = {0: "black", 1: "black", 2: "black", 3: "black", 4: "black"}
        self.assertEqual(self.puzzle.check_guess("swill"), (False, letters))

        letters = {0: "green", 1: "green", 2: "green", 3: "green", 4: "green"}
        self.assertEqual(self.puzzle.check_guess("check"), (True, letters))


if __name__ == "__main__":
    unittest.main()
