import pytest

from gi_loadouts.type.rank import Rank, __rank__


@pytest.mark.parametrize(
    "text, data",
    [
        pytest.param(item, unit, id=f"type.rank: {item}") for item, unit in __rank__.items()
    ]
)
def test_rank(text: str, data: int) -> None:
    """
    Test type of rank

    :return:
    """
    rkut = getattr(Rank, text.replace(" ", "_"))
    assert rkut.value == data
