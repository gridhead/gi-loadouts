import pytest

from gi_loadouts.type.vson import Vision


@pytest.mark.parametrize(
    "indx, name, colour",
    [
        pytest.param("anemo", "Anemo", "rgba(126, 212, 184, 254)", id="type.vson: Anemo"),
        pytest.param("cryo", "Cryo", "rgba(164, 226, 240, 254)", id="type.vson: Cryo"),
        pytest.param("dendro", "Dendro", "rgba(166, 202, 56, 254)", id="type.vson: Dendro"),
        pytest.param("electro", "Electro", "rgba(180, 139, 202, 254)", id="type.vson: Electro"),
        pytest.param("geo", "Geo", "rgba(222, 188, 108, 254)", id="type.vson: Geo"),
        pytest.param("hydro", "Hydro", "rgba(0, 190, 254, 254)", id="type.vson: Hydro"),
        pytest.param("pyro", "Pyro", "rgba(240, 122, 52, 254)", id="type.vson: Pyro"),
        pytest.param("none", "None", "rgba(128, 128, 128, 254)", id="type.vson: None"),
    ]
)
def test_vson(indx: str, name: str, colour: str) -> None:
    """
    Test type of vision

    :return:
    """
    item = getattr(Vision, indx)
    assert item.name == indx
    assert item.value.name == name
    assert item.value.colour == colour
