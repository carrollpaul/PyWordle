import os
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
