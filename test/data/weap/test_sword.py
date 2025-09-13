import pytest

from gi_loadouts.data.weap.swords import SwordsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Sword, Tier, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, tier, levl, batk, seco, valu",
    [
        pytest.param("Skyrider Sword", 3, 1, "Level 80/90 (Rank 6)", 334, WeaponStatType.energy_recharge_perc, 47.2, id="data.weap.swords: Skyrider Sword"),
        pytest.param("Amenoma Kageuchi", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, id="data.weap.swords: Amenoma Kageuchi"),
        pytest.param("Cinnabar Spindle", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.defense_perc, 62.9, id="data.weap.swords: Cinnabar Spindle"),
        pytest.param("Favonius Sword", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.swords: Favonius Sword"),
        pytest.param("Flute of Ezpitzal", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.defense_perc, 62.9, id="data.weap.swords: Flute of Ezpitzal"),
        pytest.param("Sacrificial Sword", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.swords: Sacrificial Sword"),
        pytest.param("Serenity's Call", 4, 1, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, id="data.weap.swords: Serenity's Call"),
        pytest.param("Key of Khaj-Nisut", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.health_points_perc, 60.3, id="data.weap.swords: Key of Khaj-Nisut"),
        pytest.param("Light of Foliar Incision", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.swords: Light of Foliar Incision"),
        pytest.param("Peak Patrol Song", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.defense_perc, 75.4, id="data.weap.swords: Peak Patrol Song"),
        pytest.param("Primordial Jade Cutter", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, id="data.weap.swords: Primordial Jade Cutter"),
        pytest.param("Splendor of Tranquil Waters", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.swords: Splendor of Tranquil Waters"),
        pytest.param("Uraku Misugiri", 5, 1, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, id="data.weap.swords: Uraku Misugiri"),
        pytest.param("Dull Blade", 1, 2, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, id="data.weap.swords: Dull Blade"),
        pytest.param("Silver Sword", 2, 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, id="data.weap.swords: Silver Sword"),
        pytest.param("Cool Steel", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, id="data.weap.swords: Cool Steel"),
        pytest.param("Dark Iron Sword", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.elemental_mastery, 128, id="data.weap.swords: Dark Iron Sword"),
        pytest.param("Fillet Blade", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, id="data.weap.swords: Fillet Blade"),
        pytest.param("Harbinger of Dawn", 3, 2, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_damage_perc, 42.7, id="data.weap.swords: Harbinger of Dawn"),
        pytest.param("Festering Desire", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.swords: Festering Desire"),
        pytest.param("Fleuve Cendre Ferryman", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, id="data.weap.swords: Fleuve Cendre Ferryman"),
        pytest.param("Iron Sting", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.swords: Iron Sting"),
        pytest.param("Kagotsurube Isshin", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.swords: Kagotsurube Isshin"),
        pytest.param("Lion's Roar", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.swords: Lion's Roar"),
        pytest.param("Royal Longsword", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.swords: Royal Longsword"),
        pytest.param("Sword of Narzissenkreuz", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.swords: Sword of Narzissenkreuz"),
        pytest.param("The Black Sword", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.swords: The Black Sword"),
        pytest.param("The Dockhand's Assistant", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, id="data.weap.swords: The Dockhand's Assistant"),
        pytest.param("The Flute", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, id="data.weap.swords: The Flute"),
        pytest.param("Toukabou Shigure", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.swords: Toukabou Shigure"),
        pytest.param("Wolf-Fang", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, id="data.weap.swords: Wolf-Fang"),
        pytest.param("Xiphos' Moonlight", 4, 2, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, id="data.weap.swords: Xiphos' Moonlight"),
        pytest.param("Freedom-Sworn", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.elemental_mastery, 181, id="data.weap.swords: Freedom-Sworn"),
        pytest.param("Haran Geppaku Futsu", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, id="data.weap.swords: Haran Geppaku Futsu"),
        pytest.param("Skyward Blade", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, id="data.weap.swords: Skyward Blade"),
        pytest.param("Summit Shaper", 5, 2, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, id="data.weap.swords: Summit Shaper"),
        pytest.param("Traveler's Handy Sword", 3, 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.defense_perc, 26.7, id="data.weap.swords: Traveler's Handy Sword"),
        pytest.param("Blackcliff Longsword", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_damage_perc, 33.5, id="data.weap.swords: Blackcliff Longsword"),
        pytest.param("Calamity of Eshu", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.swords: Calamity of Eshu"),
        pytest.param("Finale of the Deep", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.swords: Finale of the Deep"),
        pytest.param("Prototype Rancour", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, id="data.weap.swords: Prototype Rancour"),
        pytest.param("Sapwood Blade", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, id="data.weap.swords: Sapwood Blade"),
        pytest.param("Sturdy Bone", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.swords: Sturdy Bone"),
        pytest.param("Absolution", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, id="data.weap.swords: Absolution"),
        pytest.param("Aquila Favonia", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.damage_bonus_physical_perc, 37.7, id="data.weap.swords: Aquila Favonia"),
        pytest.param("Azurelight", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, id="data.weap.swords: Azurelight"),
        pytest.param("Mistsplitter Reforged", 5, 3, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, id="data.weap.swords: Mistsplitter Reforged"),
        pytest.param("Moonweaver's Dawn", 4, 3, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, id="data.weap.swords: Moonweaver's Dawn"),
        pytest.param("The Alley Flash", 4, 4, "Level 80/90 (Rank 6)", 571, WeaponStatType.elemental_mastery, 50, id="data.weap.swords: The Alley Flash"),
        pytest.param("Sword of Descension", 4, 2, "Level 80/90 (Rank 6)", 414, WeaponStatType.attack_perc, 32.1, id="data.weap.swords: Sword of Descension")
    ]
)
def test_sword(name: str, rare: int, tier: int, levl: str, batk: int, seco: WeaponStatType, valu: float) -> None:
    """
    Test all weapons of sword type for correctness

    :return:
    """
    unit = SwordsDict[name]()
    assert unit.type == Sword().type
    assert len(unit.refinement) == len(unit.refi_list)
    assert len(unit.levl_bind) == 74 if rare in {1, 2} else 96
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    assert unit.rare == getattr(Rare, f"Star_{rare}")
    assert unit.tier == getattr(Tier, f"Tier_{tier}")
    assert round(unit.main_stat.stat_data) == batk
    assert unit.seco_stat.stat_name == seco
    if unit.seco_stat.stat_name != WeaponStatType.none:
        assert verify_accuracy(unit.seco_stat_calc.stat_data, valu, 1.5)
