import pytest

from gi_loadouts.type.stat import ATTR, STAT, __revmap__


@pytest.mark.parametrize(
    "text, name, qant",
    [pytest.param(item, data, 0.0, id=f"type.stat: {item}") for item, data in __revmap__.items()],
)
def test_attr(text: str, name: STAT, qant: float) -> None:
    """
    Test type of stats

    :return:
    """
    prop = ATTR(stat_name=name, stat_data=qant)
    assert prop.stat_name.value == text
