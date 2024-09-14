import pytest

from gi_loadouts.type.rare import Rare


@pytest.mark.parametrize(
    "indx, name, qant, back",
    [
        pytest.param("Star_0", "Star 0", 0, ":rare/imgs/rare/star_1.webp", id="type.rare: Star 0"),
        pytest.param("Star_1", "Star 1", 1, ":rare/imgs/rare/star_1.webp", id="type.rare: Star 1"),
        pytest.param("Star_2", "Star 2", 2, ":rare/imgs/rare/star_2.webp", id="type.rare: Star 2"),
        pytest.param("Star_3", "Star 3", 3, ":rare/imgs/rare/star_3.webp", id="type.rare: Star 3"),
        pytest.param("Star_4", "Star 4", 4, ":rare/imgs/rare/star_4.webp", id="type.rare: Star 4"),
        pytest.param("Star_5", "Star 5", 5, ":rare/imgs/rare/star_5.webp", id="type.rare: Star 5"),
    ]
)
def test_rare(indx, name, qant, back):
    item = getattr(Rare, indx)
    assert item.name == indx
    assert item.value.name == name
    assert item.value.qant == qant
    assert item.value.back == back
