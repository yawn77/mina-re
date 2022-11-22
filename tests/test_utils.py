from mina_re.utils import get_common_prefix


def test_default() -> None:
    pre = get_common_prefix([])
    assert pre == ""
