from os import rename, walk
from os.path import commonprefix, join, split
from pathlib import Path
from typing import List
from mina_re.item_to_rename import ItemToRename


IGNORE_LIST = [
    'Thumbs.db',
    '.DS_Store',
]


def get_common_prefix(items: List[ItemToRename]) -> str:
    if len(items) == 1:
        return ''

    names = [item.name.lower() for item in items]

    return commonprefix(names)


def get_items_to_rename(path_to_folder: Path) -> List[ItemToRename]:
    items = []
    for (dirpath, _, filenames) in walk(path_to_folder):
        for filename in filenames:
            if filename in IGNORE_LIST:
                continue

            item = ItemToRename(Path(dirpath) / filename)
            items.append(item)

    return items


def set_new_prefix(items: List[ItemToRename], old_prefix: str, new_prefix: str) -> None:
    for item in items:
        item.change_prefix(old_prefix, new_prefix)
        print(item)


def rename_action() -> None:
    path_to_folder = Path(input('path to movie: ').replace("'", ''))
    title = input('title: ').replace(':', ' - ').replace('  ', ' ')
    year = input('year: ')
    new_prefix = f'{title} ({year})'

    items = get_items_to_rename(path_to_folder)
    common_prefix = get_common_prefix(items)
    print()
    set_new_prefix(items, common_prefix, new_prefix)

    if input('apply? (y/n) ') == 'y':
        print('rename')
        for item in items:
            item.rename()

        rename(path_to_folder, join(split(path_to_folder)[0], new_prefix))
