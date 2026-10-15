from dataclasses import dataclass
from quill.models.change import ChangedFile

@dataclass(frozen=True)
class GitStatus:
    staged: list[ChangedFile]
    modified: list[ChangedFile]
    untracked: list[ChangedFile]
    deleted: list[ChangedFile]
    renamed: list[ChangedFile]