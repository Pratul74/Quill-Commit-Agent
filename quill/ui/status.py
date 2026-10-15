from rich.console import Console
from rich.table import Table
from quill.git.services.status import GitStatus

console = Console()

def render_status(status: GitStatus):
    table = Table(title="Git Status")

    table.add_column("Type")
    table.add_column("Files")

    table.add_row(
        "Staged",
        str(len(status.staged)),
    )

    table.add_row(
        "Modified",
        str(len(status.modified)),
    )

    table.add_row(
        "Deleted",
        str(len(status.deleted)),
    )

    table.add_row(
        "Untracked",
        str(len(status.untracked)),
    )
    console.print(table)