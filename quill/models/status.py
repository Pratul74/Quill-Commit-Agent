from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class GitStatus:
    staged: list[Path]
    modified: list[Path]
    untracked: list[Path]
    deleted: list[Path]
    renamed: list[Path]   