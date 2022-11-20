from os import rename
from os.path import join
from pathlib import Path
from typing import Optional


class ItemToRename:

    def __init__(self, path: Path) -> None:
        self.name: str = path.stem
        self.ext: str = path.suffix
        self.path: Path = path.parents[0]
        self.new_name: Optional[str] = None

    def set_new_name_by_prefix(self, new_name: str, prefix: str) -> None:
        self.new_name = f'{new_name}{self.name[len(prefix):]}{self.ext}'

    def rename(self) -> None:
        rename(Path(self.path) / f'{self.name}{self.ext}', Path(self.path) / f'{self.new_name}')

    def __str__(self) -> str:
        return f'{join(self.path, self.name)}{self.ext} -> {self.new_name}'
