from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class RepositoryInfo:
    name: str
    root: Path
    current_branch: str