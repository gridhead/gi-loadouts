import pytest

from gi_loadouts.data.weap.polearms import PolearmsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap import Polearm, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, levl, batk, seco, valu, refn",
    [
        pytest.param("Beginner's Protector", 1, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Polearm - Beginner's Protector"),
        pytest.param("Iron Point", 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Polearm - Iron Point"),
        pytest.param("Black Tassel", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.health_points_perc, 42.7, 5, id="face.wind.rule: Configuring weapon - Polearm - Black Tassel"),
        pytest.param("Deathmatch", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.critical_rate_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Polearm - Deathmatch"),
        pytest.param("Dragon's Bane", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.elemental_mastery, 201, 5, id="face.wind.rule: Configuring weapon - Polearm - Dragon's Bane"),
        pytest.param("Dragonspine Spear", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.damage_bonus_physical_perc, 62.9, 5, id="face.wind.rule: Configuring weapon - Polearm - Dragonspine Spear"),
        pytest.param("Staff of the Scarlet Sands", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Polearm - Staff of the Scarlet Sands"),
        pytest.param("White Tassel", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_rate_perc, 21.4, 5, id="face.wind.rule: Configuring weapon - Polearm - White Tassel"),
        pytest.param("\"The Catch\"", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Polearm - \"The Catch\""),
        pytest.param("Ballad of the Fjords", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Ballad of the Fjords"),
        pytest.param("Blackcliff Pole", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Polearm - Blackcliff Pole"),
        pytest.param("Dialogues of the Desert Sages", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Polearm - Dialogues of the Desert Sages"),
        pytest.param("Footprint of the Rainbow", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.defense_perc, 47.2, 5, id="face.wind.rule: Configuring weapon - Polearm - Footprint of the Rainbow"),
        pytest.param("Missive Windspear", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Polearm - Missive Windspear"),
        pytest.param("Prototype Starglitter", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Polearm - Prototype Starglitter"),
        pytest.param("Engulfing Lightning", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Polearm - Engulfing Lightning"),
        pytest.param("Lumidouce Elegy", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Polearm - Lumidouce Elegy"),
        pytest.param("Staff of Homa", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Polearm - Staff of Homa"),
        pytest.param("Vortex Vanquisher", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Polearm - Vortex Vanquisher"),
        pytest.param("Halberd", 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.attack_perc, 21.4, 5, id="face.wind.rule: Configuring weapon - Polearm - Halberd"),
        pytest.param("Crescent Pike", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, 5, id="face.wind.rule: Configuring weapon - Polearm - Crescent Pike"),
        pytest.param("Favonius Lance", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Polearm - Favonius Lance"),
        pytest.param("Kitain Cross Spear", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, 5, id="face.wind.rule: Configuring weapon - Polearm - Kitain Cross Spear"),
        pytest.param("Lithic Spear", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Lithic Spear"),
        pytest.param("Moonpiercer", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, 5, id="face.wind.rule: Configuring weapon - Polearm - Moonpiercer"),
        pytest.param("Prospector's Drill", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Prospector's Drill"),
        pytest.param("Rightful Reward", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.health_points_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Rightful Reward"),
        pytest.param("Royal Spear", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Royal Spear"),
        pytest.param("Crimson Moon's Semblance", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Crimson Moon's Semblance"),
        pytest.param("Primordial Jade Winged-Spear", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Primordial Jade Winged-Spear"),
        pytest.param("Skyward Spine", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.energy_recharge_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Polearm - Skyward Spine"),
        pytest.param("Wavebreaker's Fin", 4, "Level 80/90 (Rank 6)", 571, WeaponStatType.attack_perc, 12.5, 5, id="face.wind.rule: Configuring weapon - Polearm - Wavebreaker's Fin"),
        pytest.param("Calamity Queller", 5, "Level 80/90 (Rank 6)", 679, WeaponStatType.attack_perc, 15.1, 5, id="face.wind.rule: Configuring weapon - Polearm - Calamity Queller"),
    ]
)
def test_polearm(runner, name, rare, levl, batk, seco, valu, refn) -> None:
    """
    Test the configuration of weapons on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText("Electro")
    runner.head_char_name.setCurrentText("Raiden Shogun")
    unit = PolearmsDict[name]
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    if isinstance(refn, int):
        runner.weap_area_refn.setCurrentText(f"Refinement {refn}")

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText().strip() == Polearm().type.value
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
