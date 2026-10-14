import typer

from quill.ui.console import console

app = typer.Typer()


@app.command()
def main():
    console.print()

    console.rule("[bold cyan]Quill[/bold cyan]")

    console.print("🤖 AI Git Commit Assistant")
    console.print("Version 0.1.0", style="dim")

    console.print()

    console.print("[green]Ready![/green]")


if __name__ == "__main__":
    app()