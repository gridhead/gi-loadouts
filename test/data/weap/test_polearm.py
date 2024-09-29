import pytest

from gi_loadouts.data.weap.polearms import PolearmsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Polearm, Tier, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, tier, levl, batk, seco, valu",
    [
        pytest.param("Beginner's Protector", 1, 2, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, id="data.weap.polearms: Beginner's Protector"),
        pytest.param("Iron Point", 2, 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, id="data.weap.polearms: Iron Point"),
        pytest.param("Black Tassel", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.health_points_perc, 42.7, id="data.weap.polearms: Black Tassel"),
        pytest.param("Deathmatch", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.critical_rate_perc, 33.5, id="data.weap.polearms: Deathmatch"),
        pytest.param("Dragon's Bane", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.elemental_mastery, 201, id="data.weap.polearms: Dragon's Bane"),
        pytest.param("Dragonspine Spear", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.damage_bonus_physical_perc, 62.9, id="data.weap.polearms: Dragonspine Spear"),
        pytest.param("Staff of the Scarlet Sands", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, id="data.weap.polearms: Staff of the Scarlet Sands"),
        pytest.param("White Tassel", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_rate_perc, 21.4, id="data.weap.polearms: White Tassel"),
        pytest.param("\"The Catch\"", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.polearms: \"The Catch\""),
        pytest.param("Ballad of the Fjords", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.polearms: Ballad of the Fjords"),
        pytest.param("Blackcliff Pole", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, id="data.weap.polearms: Blackcliff Pole"),
        pytest.param("Dialogues of the Desert Sages", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.polearms: Dialogues of the Desert Sages"),
        pytest.param("Footprint of the Rainbow", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.defense_perc, 47.2, id="data.weap.polearms: Footprint of the Rainbow"),
        pytest.param("Missive Windspear", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.polearms: Missive Windspear"),
        pytest.param("Prototype Starglitter", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.polearms: Prototype Starglitter"),
        pytest.param("Engulfing Lightning", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, id="data.weap.polearms: Engulfing Lightning"),
        pytest.param("Lumidouce Elegy", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, id="data.weap.polearms: Lumidouce Elegy"),
        pytest.param("Staff of Homa", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, id="data.weap.polearms: Staff of Homa"),
        pytest.param("Vortex Vanquisher", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.polearms: Vortex Vanquisher"),
        pytest.param("Halberd", 3, 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.attack_perc, 21.4, id="data.weap.polearms: Halberd"),
        pytest.param("Crescent Pike", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, id="data.weap.polearms: Crescent Pike"),
        pytest.param("Favonius Lance", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.polearms: Favonius Lance"),
        pytest.param("Kitain Cross Spear", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, id="data.weap.polearms: Kitain Cross Spear"),
        pytest.param("Lithic Spear", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.polearms: Lithic Spear"),
        pytest.param("Moonpiercer", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, id="data.weap.polearms: Moonpiercer"),
        pytest.param("Prospector's Drill", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.polearms: Prospector's Drill"),
        pytest.param("Rightful Reward", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.health_points_perc, 25.1, id="data.weap.polearms: Rightful Reward"),
        pytest.param("Royal Spear", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.polearms: Royal Spear"),
        pytest.param("Crimson Moon's Semblance", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.polearms: Crimson Moon's Semblance"),
        pytest.param("Primordial Jade Winged-Spear", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.polearms: Primordial Jade Winged-Spear"),
        pytest.param("Skyward Spine", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.energy_recharge_perc, 33.5, id="data.weap.polearms: Skyward Spine"),
        pytest.param("Wavebreaker's Fin", 4, 4, "Level 80/90 (Rank 6)", 571, WeaponStatType.attack_perc, 12.5, id="data.weap.polearms: Wavebreaker's Fin"),
        pytest.param("Calamity Queller", 5, 4, "Level 80/90 (Rank 6)", 679, WeaponStatType.attack_perc, 15.1, id="data.weap.polearms: Calamity Queller"),
    ]
)
def test_polearm(name, rare, tier, levl, batk, seco, valu):
    unit = PolearmsDict[name]()
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    assert unit.rare == getattr(Rare, f"Star_{rare}")
    assert unit.tier == getattr(Tier, f"Tier_{tier}")
    assert round(unit.main_stat.stat_data) == batk
    assert unit.seco_stat.stat_name == seco
    assert unit.type == Polearm().type
    if unit.seco_stat.stat_name != WeaponStatType.none:
        assert verify_accuracy(unit.seco_stat_calc.stat_data, valu, 1)
