import pytest
from pathlib import Path
from mina_re.item_to_rename import ItemToRename


@pytest.fixture
def item() -> ItemToRename:
    path = Path('/directory/prefix-file.txt')
    return ItemToRename(path)


def test_str(item: ItemToRename) -> None:
    assert str(item) == str(item.path / f'{item.name}{item.suffix}')


def test_change_prefix(item: ItemToRename) -> None:
    item.change_prefix('prefix', 'new-prefix')

    assert str(item) == f'{item.path / f"{item.name}{item.suffix}"} -> {item.new_name}{item.suffix}'


def test_value_error_if_old_prefix_does_not_match(item: ItemToRename) -> None:
    with pytest.raises(ValueError) as _:
        item.change_prefix('wrong-prefix', 'new-prefix')


def test_rename(tmp_path: Path) -> None:
    path = tmp_path / 'prefix-file.txt'
    path.write_text('')
    item = ItemToRename(path)
    item.change_prefix('prefix', 'prefix2')

    item.rename()

    new_path = tmp_path / 'prefix2-file.txt'

    assert len(list(tmp_path.iterdir())) == 1
    assert new_path.exists()


def test_raise_error_when_file_to_rename_cannot_be_found(tmp_path: Path) -> None:
    path = tmp_path / 'prefix-file.txt'
    item = ItemToRename(path)
    item.change_prefix('prefix', 'prefix2')

    with pytest.raises(FileNotFoundError) as _:
        item.rename()


def test_do_not_rename_without_new_name(tmp_path: Path) -> None:
    path = tmp_path / 'prefix-file.txt'
    path.write_text('')
    item = ItemToRename(path)

    item.rename()

    assert len(list(tmp_path.iterdir())) == 1
    assert path.exists()
