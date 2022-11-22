from os import rename, walk
from os.path import join, split
from pathlib import Path
from mina_re.item_to_rename import ItemToRename

from mina_re.utils import get_common_prefix


ignore = ['Thumbs.db', '.DS_Store']


def rename_action() -> None:
    path_to_folder = input('path to movie: ').replace("'", '')
    title = input('title: ').replace(':', ' - ').replace('  ', ' ')
    year = input('year: ')
    new_name = f'{title} ({year})'

    items = []
    for (dirpath, _, filenames) in walk(path_to_folder):
        for filename in filenames:
            if filename in ignore:
                continue

            item = ItemToRename(Path(dirpath) / filename)
            items.append(item)

    common_prefix = get_common_prefix(items)

    print()
    for item in items:
        item.set_new_name_by_prefix(new_name, common_prefix)
        print(item)

    if input('apply? (y/n) ') == 'y':
        print('rename')
        for item in items:
            item.rename()

        rename(path_to_folder, join(split(path_to_folder)[0], new_name))


while True:
    rename_action()
