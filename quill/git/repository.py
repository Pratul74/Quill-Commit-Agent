from pathlib import Path
from git import InvalidGitRepositoryError
from git import NoSuchPathError
from git import Repo

from quill.models.repository import RepositoryInfo

class Repository:
    def __init__(self, path: Path | None = None):
        self.path = path

    @property
    def repo(self) -> Repo:
        return Repo(self.path, search_parent_directories=True)

    def exists(self) -> bool:
        try:
            Repo(self.path, search_parent_directories=True)
            return True
        except (InvalidGitRepositoryError, NoSuchPathError):
            return False

    def info(self) -> RepositoryInfo:
        repo = self.repo
        root = Path(repo.working_tree_dir)
        return RepositoryInfo(
            name=root.name,
            root=root,
            current_branch=repo.active_branch.name,
        )

    
