from os.path import commonprefix
from typing import List

from rename_mina.item_to_rename import ItemToRename


def get_common_prefix(items: List[ItemToRename]) -> str:
    names = [item.name.lower() for item in items]

    return commonprefix(names)
