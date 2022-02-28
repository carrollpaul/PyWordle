import os

from wordle.wordle import Wordle
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


def clear_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def update_display(console: Console, table: Table, msg: Panel = None) -> None:
    clear_terminal()
    console.rule("PyWordle")
    console.print(table)
    if msg:
        console.print(msg)


def main() -> None:
    puzzle = Wordle()
    console = Console(width=50)
    table = Table(box=None)

    guesses_remaining = 6

    # Main game loop
    while guesses_remaining:
        update_display(console, table)

        # Get guess and validate
        while True:
            guess = console.input(f"[b] Gimme a word ([red]{guesses_remaining}[/red] remaining): ")
            if puzzle.is_valid_guess(guess):
                break

            console.print("[red]Invalid guess![/red] :angry:")

        # Check guess against puzzle answer
        correct_guess, letters = puzzle.check_guess(guess)

        # Display each letter as a box with color corresponding to status
        row = [
            f"[white on {status}] {guess[index]} [/white on {status}]"
            for index, status in letters.items()
        ]
        table.add_row(*row)
        table.add_row("")
        console.print(table)

        if correct_guess:
            panel = Panel("You nailed it!", title=":victory_hand:")
            update_display(console, table, panel)
            return

        guesses_remaining -= 1

    panel = Panel(
        f"Better luck next time! Correct answer is [bold green]{puzzle.answer}[/bold green]",
        title=":frowning_face:",
    )
    update_display(console, table, panel)


if __name__ == "__main__":
    main()
