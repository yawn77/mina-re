from pathlib import Path
from mina_re.item_to_rename import ItemToRename
from mina_re.utils import get_common_prefix


def test_empty_list() -> None:
    pre = get_common_prefix([])

    assert pre == ''


def test_return_empty_string_when_list_contains_one_item() -> None:
    pre = get_common_prefix([
        ItemToRename(Path('/directory/file.txt')),
    ])

    assert pre == ''


def test_get_common_prefix() -> None:
    pre = get_common_prefix([
        ItemToRename(Path('/directory/file.txt')),
        ItemToRename(Path('/directory/fite.txt')),
    ])

    assert pre == 'fi'
