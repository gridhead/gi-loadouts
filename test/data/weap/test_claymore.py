import pytest

from gi_loadouts.data.weap.claymores import ClaymoresDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Claymore, Tier, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, tier, levl, batk, seco, valu",
    [
        pytest.param("Bloodtainted Greatsword", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.elemental_mastery, 171, id="data.weap.claymores: Bloodtainted Greatsword"),
        pytest.param("Portable Power Saw", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.health_points_perc, 50.3, id="data.weap.claymores: Portable Power Saw"),
        pytest.param("Luxurious Sea-Lord", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.claymores: Luxurious Sea-Lord"),
        pytest.param("Favonius Greatsword", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.claymores: Favonius Greatsword"),
        pytest.param("Redhorn Stonethresher", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.claymores: Redhorn Stonethresher"),
        pytest.param("Waster Greatsword", 1, 2, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, id="data.weap.claymores: Waster Greatsword"),
        pytest.param("Old Merc's Pal", 2, 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, id="data.weap.claymores: Old Merc's Pal"),
        pytest.param("White Iron Greatsword", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.defense_perc, 40.1, id="data.weap.claymores: White Iron Greatsword"),
        pytest.param("Skyrider Greatsword", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.damage_bonus_physical_perc, 40.1, id="data.weap.claymores: Skyrider Greatsword"),
        pytest.param("Ferrous Shadow", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.health_points_perc, 32.1, id="data.weap.claymores: Ferrous Shadow"),
        pytest.param("Debate Club", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, id="data.weap.claymores: Debate Club"),
        pytest.param("Serpent Spine", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.claymores: Serpent Spine"),
        pytest.param("Whiteblind", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.defense_perc, 47.2, id="data.weap.claymores: Whiteblind"),
        pytest.param("Tidal Shadow", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.claymores: Tidal Shadow"),
        pytest.param("The Bell", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.claymores: The Bell"),
        pytest.param("Rainslasher", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.claymores: Rainslasher"),
        pytest.param("Makhaira Aquamarine", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.claymores: Makhaira Aquamarine"),
        pytest.param("Lithic Blade", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.claymores: Lithic Blade"),
        pytest.param("Katsuragikiri Nagamasa", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.claymores: Katsuragikiri Nagamasa"),
        pytest.param("Blackcliff Slasher", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, id="data.weap.claymores: Blackcliff Slasher"),
        pytest.param("Akuoumaru", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.claymores: Akuoumaru"),
        pytest.param("Beacon of the Reed Sea", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, id="data.weap.claymores: Beacon of the Reed Sea"),
        pytest.param("Wolf's Gravestone", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.claymores: Wolf's Gravestone"),
        pytest.param("The Unforged", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.claymores: The Unforged"),
        pytest.param("Talking Stick", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_rate_perc, 16.8, id="data.weap.claymores: Talking Stick"),
        pytest.param("Snow-Tombed Starsilver", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, id="data.weap.claymores: Snow-Tombed Starsilver"),
        pytest.param("Royal Greatsword", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.claymores: Royal Greatsword"),
        pytest.param("Prototype Archaic", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.claymores: Prototype Archaic"),
        pytest.param("Sacrificial Greatsword", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.claymores: Sacrificial Greatsword"),
        pytest.param("Mailed Flower", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, id="data.weap.claymores: Mailed Flower"),
        pytest.param("Forest Regalia", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.claymores: Forest Regalia"),
        pytest.param("Earth Shaker", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.claymores: Earth Shaker"),
        pytest.param("\"Ultimate Overlord's Mega Magic Sword\"", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.claymores: \"Ultimate Overlord's Mega Magic Sword\""),
        pytest.param("Skyward Pride", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.energy_recharge_perc, 33.5, id="data.weap.claymores: Skyward Pride"),
        pytest.param("Verdict", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.claymores: Verdict"),
        pytest.param("Song of Broken Pines", 5, 4, "Level 80/90 (Rank 6)", 679, WeaponStatType.damage_bonus_physical_perc, 18.9, id="data.weap.claymores: Song of Broken Pines"),
    ]
)
def test_claymore(name, rare, tier, levl, batk, seco, valu):
    unit = ClaymoresDict[name]
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    assert unit.rare == getattr(Rare, f"Star_{rare}")
    assert unit.tier == getattr(Tier, f"Tier_{tier}")
    assert round(unit.main_stat.stat_data) == batk
    assert unit.seco_stat.stat_name == seco
    assert unit.type == Claymore().type
    if unit.seco_stat.stat_name != WeaponStatType.none:
        assert verify_accuracy(unit.seco_stat_calc.stat_data, valu, 1)
