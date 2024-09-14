import pytest

from gi_loadouts.type.rank import Rank, __rank__


@pytest.mark.parametrize(
    "text, data",
    [
        pytest.param(item, unit, id=f"type.rank: {item}") for item, unit in __rank__.items()
    ]
)
def test_rank(text, data):
    rkut = getattr(Rank, text.replace(" ", "_"))
    assert rkut.value == data
