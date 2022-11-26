from os import rename
from pathlib import Path
from typing import Optional


class ItemToRename:

    def __init__(self, path: Path) -> None:
        self.name: str = path.stem
        self.suffix: str = path.suffix
        self.path: Path = path.parents[0]
        self.new_name: Optional[str] = None

    def change_prefix(self, old_prefix: str, new_prefix: str) -> None:
        if not self.name.lower().startswith(old_prefix.lower()):
            raise ValueError(f'file name "{self.name}" does not start with prefix "{old_prefix}"')

        self.new_name = f'{new_prefix}{self.name[len(old_prefix):]}'

    def rename(self) -> None:
        path = Path(self.path) / f'{self.name}{self.suffix}'

        if not path.exists():
            raise FileNotFoundError(f'cannot find "{str(path)}" to rename it')

        if self.new_name:
            rename(path, Path(self.path) / f'{self.new_name}{self.suffix}')

    def __str__(self) -> str:
        s = str(self.path / f"{self.name}{self.suffix}")

        if self.new_name:
            s = f'{s} -> {self.new_name}{self.suffix}'

        return s
