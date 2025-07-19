import pytest

from gi_loadouts.data.weap.bows import BowsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Bow, Tier, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, tier, levl, batk, seco, valu",
    [
        pytest.param("Hunter's Bow", 1, 2, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, id="data.weap.bows: Hunter's Bow"),
        pytest.param("Seasoned Hunter's Bow", 2, 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, id="data.weap.bows: Seasoned Hunter's Bow"),
        pytest.param("Recurve Bow", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.health_points_perc, 42.7, id="data.weap.bows: Recurve Bow"),
        pytest.param("Slingshot", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.critical_rate_perc, 28.5, id="data.weap.bows: Slingshot"),
        pytest.param("Compound Bow", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.damage_bonus_physical_perc, 62.9, id="data.weap.bows: Compound Bow"),
        pytest.param("Favonius Warbow", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.bows: Favonius Warbow"),
        pytest.param("Hamayumi", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.bows: Hamayumi"),
        pytest.param("King's Squire", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.bows: King's Squire"),
        pytest.param("Aqua Simulacra", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.bows: Aqua Simulacra"),
        pytest.param("Hunter's Path", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, id="data.weap.bows: Hunter's Path"),
        pytest.param("Silvershower Heartstrings", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.health_points_perc, 60.3, id="data.weap.bows: Silvershower Heartstrings"),
        pytest.param("Sharpshooter's Oath", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_damage_perc, 42.7, id="data.weap.bows: Sharpshooter's Oath"),
        pytest.param("Cloudforged", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.bows: Cloudforged"),
        pytest.param("End of the Line", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.bows: End of the Line"),
        pytest.param("Flower-Wreathed Feathers", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Flower-Wreathed Feathers"),
        pytest.param("Mitternachts Waltz", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.damage_bonus_physical_perc, 47.2, id="data.weap.bows: Mitternachts Waltz"),
        pytest.param("Predator", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Predator"),
        pytest.param("Prototype Crescent", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Prototype Crescent"),
        pytest.param("Royal Bow", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Royal Bow"),
        pytest.param("Rust", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Rust"),
        pytest.param("Sequence of Solitude", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.bows: Sequence of Solitude"),
        pytest.param("Song of Stillness", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.bows: Song of Stillness"),
        pytest.param("The Stringless", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.bows: The Stringless"),
        pytest.param("The Viridescent Hunt", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.bows: The Viridescent Hunt"),
        pytest.param("Windblume Ode", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.bows: Windblume Ode"),
        pytest.param("Amos' Bow", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.bows: Amos' Bow"),
        pytest.param("Astral Vulture's Crimson Plumage", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, id="data.weap.bows: Astral Vulture's Crimson Plumage"),
        pytest.param("Elegy for the End", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, id="data.weap.bows: Elegy for the End"),
        pytest.param("Polar Star", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, id="data.weap.bows: Polar Star"),
        pytest.param("The First Great Magic", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, id="data.weap.bows: The First Great Magic"),
        pytest.param("Thundering Pulse", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, id="data.weap.bows: Thundering Pulse"),
        pytest.param("Alley Hunter", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.bows: Alley Hunter"),
        pytest.param("Blackcliff Warbow", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_damage_perc, 33.5, id="data.weap.bows: Blackcliff Warbow"),
        pytest.param("Chain Breaker", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.bows: Chain Breaker"),
        pytest.param("Fading Twilight", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.bows: Fading Twilight"),
        pytest.param("Ibis Piercer", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.bows: Ibis Piercer"),
        pytest.param("Mouun's Moon", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.bows: Mouun's Moon"),
        pytest.param("Range Gauge", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.bows: Range Gauge"),
        pytest.param("Sacrificial Bow", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.bows: Sacrificial Bow"),
        pytest.param("Scion of the Blazing Sun", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_rate_perc, 16.8, id="data.weap.bows: Scion of the Blazing Sun"),
        pytest.param("Skyward Harp", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.bows: Skyward Harp"),
    ]
)
def test_bow(name: str, rare: int, tier: int, levl: str, batk: int, seco: WeaponStatType, valu: float) -> None:
    """
    Test all weapons of bow type for correctness

    :return:
    """
    unit = BowsDict[name]()
    assert unit.type == Bow().type
    assert len(unit.refinement) == len(unit.refi_list)
    assert len(unit.levl_bind) == 74 if rare in {1, 2} else 96
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    assert unit.rare == getattr(Rare, f"Star_{rare}")
    assert unit.tier == getattr(Tier, f"Tier_{tier}")
    assert round(unit.main_stat.stat_data) == batk
    assert unit.seco_stat.stat_name == seco
    if unit.seco_stat.stat_name != WeaponStatType.none:
        assert verify_accuracy(unit.seco_stat_calc.stat_data, valu, 1)
