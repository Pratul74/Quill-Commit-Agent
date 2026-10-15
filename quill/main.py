import typer

from quill.analyzer.engine import AnalyzerEngine
from quill.git.repository import Repository
from quill.git.services.diff import DiffService  # assumed: produces patches
from quill.git.services.status import StatusService
from quill.models.snapshot import RepositorySnapshot
from quill.ui.analysis import render_analysis  # new, see below
from quill.ui.console import console
from quill.ui.status import render_status

app = typer.Typer(add_completion=False)

VERSION = "0.1.0"


def print_banner() -> None:
    console.print()
    console.rule("[bold cyan]Quill[/bold cyan]")
    console.print("🤖 AI Git Commit Assistant")
    console.print(f"Version {VERSION}", style="dim")
    console.print()


@app.command()
def main(
    staged: bool = typer.Option(
        True, "--staged/--all", help="Analyze staged changes only, or everything."
    ),
) -> None:
    print_banner()

    repo = Repository()
    if not repo.exists():
        console.print("[red]✗ Not inside a Git repository[/red]")
        raise typer.Exit(1)

    info = repo.info()
    console.print(f"[green]✓ Repository:[/green] {info.name}")
    console.print(f"[green]✓ Branch:[/green] {info.current_branch}")
    console.print(f"[green]✓ Root:[/green] {info.root}")
    console.print()

    status = StatusService(repo).get_status()
    render_status(status)

    patches = DiffService(repo).staged_patches()
    if not patches:
        console.print(
            "[yellow]Nothing to analyze.[/yellow] "
            "Stage some changes with [bold]git add[/bold] first."
        )
        raise typer.Exit(0)

    snapshot = RepositorySnapshot(status=status, patches=patches)
    report = AnalyzerEngine().analyze(snapshot)

    console.print()
    render_analysis(report)


if __name__ == "__main__":
    app()