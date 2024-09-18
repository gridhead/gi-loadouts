import pytest

from gi_loadouts.type.levl import Level, LevelType, __level__
from gi_loadouts.type.rank import Rank


@pytest.mark.parametrize(
    "text, qant, rank, name",
    [
        pytest.param(
            item.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"),
            int(item.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").split("_")[1]),
            int(item.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").split("_")[4]),
            item,
            id=f"type.levl: {item}"
        ) for item in __level__.keys()
    ]
)
def test_levl(text, qant, rank, name):
    unit = LevelType(
        qant = qant,
        rank = getattr(Rank, f"Rank_{rank}"),
        name = name
    )
    lvut = getattr(Level, text)
    assert unit == lvut.value
