import pytest

from gi_loadouts.data.weap.claymores import ClaymoresDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap import Claymore, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, levl, batk, seco, valu, refn",
    [
        pytest.param("Bloodtainted Greatsword", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.elemental_mastery, 171, 5, id="face.wind.rule: Configuring weapon - Claymore - Bloodtainted Greatsword"),
        pytest.param("Portable Power Saw", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.health_points_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Claymore - Portable Power Saw"),
        pytest.param("Luxurious Sea-Lord", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Claymore - Luxurious Sea-Lord"),
        pytest.param("Favonius Greatsword", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, 5, id="face.wind.rule: Configuring weapon - Claymore - Favonius Greatsword"),
        pytest.param("Redhorn Stonethresher", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Claymore - Redhorn Stonethresher"),
        pytest.param("Waster Greatsword", 1, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Claymore - Waster Greatsword"),
        pytest.param("Old Merc's Pal", 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Claymore - Old Merc's Pal"),
        pytest.param("White Iron Greatsword", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.defense_perc, 40.1, 5, id="face.wind.rule: Configuring weapon - Claymore - White Iron Greatsword"),
        pytest.param("Skyrider Greatsword", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.damage_bonus_physical_perc, 40.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Skyrider Greatsword"),
        pytest.param("Ferrous Shadow", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.health_points_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Ferrous Shadow"),
        pytest.param("Debate Club", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Debate Club"),
        pytest.param("Serpent Spine", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Serpent Spine"),
        pytest.param("Whiteblind", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.defense_perc, 47.2, 5, id="face.wind.rule: Configuring weapon - Claymore - Whiteblind"),
        pytest.param("Tidal Shadow", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Claymore - Tidal Shadow"),
        pytest.param("The Bell", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Claymore - The Bell"),
        pytest.param("Rainslasher", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Claymore - Rainslasher"),
        pytest.param("Makhaira Aquamarine", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Claymore - Makhaira Aquamarine"),
        pytest.param("Lithic Blade", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Claymore - Lithic Blade"),
        pytest.param("Katsuragikiri Nagamasa", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Claymore - Katsuragikiri Nagamasa"),
        pytest.param("Blackcliff Slasher", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Claymore - Blackcliff Slasher"),
        pytest.param("Akuoumaru", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Claymore - Akuoumaru"),
        pytest.param("Beacon of the Reed Sea", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Claymore - Beacon of the Reed Sea"),
        pytest.param("Wolf's Gravestone", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Claymore - Wolf's Gravestone"),
        pytest.param("The Unforged", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Claymore - The Unforged"),
        pytest.param("Talking Stick", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_rate_perc, 16.8, 5, id="face.wind.rule: Configuring weapon - Claymore - Talking Stick"),
        pytest.param("Snow-Tombed Starsilver", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, 5, id="face.wind.rule: Configuring weapon - Claymore - Snow-Tombed Starsilver"),
        pytest.param("Royal Greatsword", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Royal Greatsword"),
        pytest.param("Prototype Archaic", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Prototype Archaic"),
        pytest.param("Sacrificial Greatsword", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Claymore - Sacrificial Greatsword"),
        pytest.param("Mailed Flower", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, 5, id="face.wind.rule: Configuring weapon - Claymore - Mailed Flower"),
        pytest.param("Forest Regalia", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Claymore - Forest Regalia"),
        pytest.param("Earth Shaker", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Earth Shaker"),
        pytest.param("\"Ultimate Overlord's Mega Magic Sword\"", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Claymore - \"Ultimate Overlord's Mega Magic Sword\""),
        pytest.param("Skyward Pride", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.energy_recharge_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Claymore - Skyward Pride"),
        pytest.param("Verdict", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, 5, id="face.wind.rule: Configuring weapon - Claymore - Verdict"),
        pytest.param("Song of Broken Pines", 5, "Level 80/90 (Rank 6)", 679, WeaponStatType.damage_bonus_physical_perc, 18.9, 5, id="face.wind.rule: Configuring weapon - Claymore - Song of Broken Pines"),
    ]
)
def test_claymore(runner, name, rare, levl, batk, seco, valu, refn) -> None:
    """
    Test the configuration of weapons on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText("Geo")
    runner.head_char_name.setCurrentText("Navia")
    unit = ClaymoresDict[name]()
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    if isinstance(refn, int):
        runner.weap_area_refn.setCurrentText(f"Refinement {refn}")

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText().strip() == Claymore().type.value
    assert runner.weap_area_rare.text() == " ".join(["STAR"] * unit.rare.value.qant)
    assert runner.weap_area_batk.text().split(" ")[0] == "ATK"
    assert verify_accuracy(round(float(runner.weap_area_batk.text().split(" ")[-1])), round(unit.main_stat.stat_data), 1)
    if unit.seco_stat.stat_name == WeaponStatType.none:
        assert runner.weap_area_stat.text() == "No substats"
    else:
        assert unit.seco_stat.stat_name.value.value in runner.weap_area_stat.text()
        assert verify_accuracy(unit.seco_stat_calc.stat_data, float(runner.weap_area_stat.text().split(" ")[-1]), 1)

    if isinstance(refn, int):
        assert runner.weap_area_refn_head.text() == f"<b>{unit.refi_name}</b>"
        assert runner.weap_area_refn_body.toPlainText() == unit.refi_list[refn - 1]
