import typer

from quill.ui.console import console
from quill.git.repository import Repository
from quill.ui.status import render_status
from quill.git.status import StatusService

app = typer.Typer()


@app.command()
def main():
    console.print()

    console.rule("[bold cyan]Quill[/bold cyan]")

    console.print("🤖 AI Git Commit Assistant")
    console.print("Version 0.1.0", style="dim")

    console.print()

    console.print("[green]Ready![/green]")
    repo = Repository()
    if not repo.exists():
        console.print("[red]✗ Not inside a Git repository[/red]")
        raise typer.Exit(1)
    info = repo.info()

    console.print(f"[green]✓ Repository:[/green] {info.name}")
    console.print(f"[green]✓ Branch:[/green] {info.current_branch}")
    console.print(f"[green]✓ Root:[/green] {info.root}")

    status = StatusService(repo).get_status()
    console.print()
    render_status(status)


if __name__ == "__main__":
    app()