from os.path import commonprefix
from typing import List
from mina_re.item_to_rename import ItemToRename


def get_common_prefix(items: List[ItemToRename]) -> str:
    if len(items) == 1:
        return ''

    names = [item.name.lower() for item in items]

    return commonprefix(names)
