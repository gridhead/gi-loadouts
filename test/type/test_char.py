import pytest

from gi_loadouts.type.char.cons import Cons, ConsType, __cons__


@pytest.mark.parametrize(
    "text, name, data",
    [
        pytest.param(
            item.replace(" ", "_"), item, int(item.split(" ")[1]), id=f"type.char.cons: {item}"
        )
        for item in __cons__
    ],
)
def test_char(text: str, name: str, data: int) -> None:
    """
    Test type of constellation

    :return:
    """
    unit = ConsType(name=name, data=data)
    csut = getattr(Cons, text)
    assert unit == csut.value
