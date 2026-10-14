from pathlib import Path
from quill.models.status import GitStatus
from quill.git.repository import Repository

class StatusService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_status(self) -> GitStatus:
        repo = self.repository.repo

        staged = []
        modified = [] 
        renamed = []
        deleted = []
        for diff in repo.index.diff(None):
            if diff.change_type == "M":
                modified.append(Path(diff.a_path))
            elif diff.change_type == "D":
                deleted.append(Path(diff.a_path))
            elif diff.change_type == "R":
                renamed.append(
                    (
                        Path(diff.a_path),
                        Path(diff.b_path),
                    )
                )
        for diff in repo.index.diff("HEAD"):
            staged.append(Path(diff.b_path or diff.a_path))
        untracked = [
            Path(path)
            for path in repo.untracked_files
        ]

        return GitStatus(
            staged=staged,
            modified=modified,
            untracked=untracked,
            deleted=deleted,
            renamed=renamed
        )