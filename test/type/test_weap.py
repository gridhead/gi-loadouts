import pytest

from gi_loadouts.type.weap import WeaponType


@pytest.mark.parametrize(
    "type",
    [
        pytest.param(weapon.value, id=f"type.weap: {weapon.value}") for weapon in WeaponType
    ]
)
def test_weap(type: str) -> None:
    """
    Test type of weapon

    :return:
    """
    weapunit = WeaponType(type)
    assert weapunit.value == type
