import pytest

from gi_loadouts.data.weap.swords import SwordsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap import Sword, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, levl, batk, seco, valu, refn",
    [
        pytest.param("Skyrider Sword", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.energy_recharge_perc, 47.2, 5, id="face.wind.rule: Configuring weapon - Sword - Skyrider Sword"),
        pytest.param("Amenoma Kageuchi", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Sword - Amenoma Kageuchi"),
        pytest.param("Cinnabar Spindle", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.defense_perc, 62.9, 5, id="face.wind.rule: Configuring weapon - Sword - Cinnabar Spindle"),
        pytest.param("Favonius Sword", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, 5, id="face.wind.rule: Configuring weapon - Sword - Favonius Sword"),
        pytest.param("Flute of Ezpitzal", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.defense_perc, 62.9, 5, id="face.wind.rule: Configuring weapon - Sword - Flute of Ezpitzal"),
        pytest.param("Sacrificial Sword", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, 5, id="face.wind.rule: Configuring weapon - Sword - Sacrificial Sword"),
        pytest.param("Key of Khaj-Nisut", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.health_points_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Sword - Key of Khaj-Nisut"),
        pytest.param("Light of Foliar Incision", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Sword - Light of Foliar Incision"),
        pytest.param("Primordial Jade Cutter", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Sword - Primordial Jade Cutter"),
        pytest.param("Splendor of Tranquil Waters", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Sword - Splendor of Tranquil Waters"),
        pytest.param("Uraku Misugiri", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Sword - Uraku Misugiri"),
        pytest.param("Dull Blade", 1, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Sword - Dull Blade"),
        pytest.param("Silver Sword", 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Sword - Silver Sword"),
        pytest.param("Cool Steel", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Sword - Cool Steel"),
        pytest.param("Dark Iron Sword", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.elemental_mastery, 128, 5, id="face.wind.rule: Configuring weapon - Sword - Dark Iron Sword"),
        pytest.param("Fillet Blade", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.attack_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Sword - Fillet Blade"),
        pytest.param("Harbinger of Dawn", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_damage_perc, 42.7, 5, id="face.wind.rule: Configuring weapon - Sword - Harbinger of Dawn"),
        pytest.param("Festering Desire", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Sword - Festering Desire"),
        pytest.param("Fleuve Cendre Ferryman", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Sword - Fleuve Cendre Ferryman"),
        pytest.param("Iron Sting", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Sword - Iron Sting"),
        pytest.param("Kagotsurube Isshin", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 1, id="face.wind.rule: Configuring weapon - Sword - Kagotsurube Isshin"),
        pytest.param("Lion's Roar", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - Lion's Roar"),
        pytest.param("Royal Longsword", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - Royal Longsword"),
        pytest.param("Sword of Narzissenkreuz", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - Sword of Narzissenkreuz"),
        pytest.param("The Black Sword", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Sword - The Black Sword"),
        pytest.param("The Dockhand's Assistant", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - The Dockhand's Assistant"),
        pytest.param("The Flute", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - The Flute"),
        pytest.param("Toukabou Shigure", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Sword - Toukabou Shigure"),
        pytest.param("Wolf-Fang", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Sword - Wolf-Fang"),
        pytest.param("Xiphos' Moonlight", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Sword - Xiphos' Moonlight"),
        pytest.param("Freedom-Sworn", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.elemental_mastery, 181, 5, id="face.wind.rule: Configuring weapon - Sword - Freedom-Sworn"),
        pytest.param("Haran Geppaku Futsu", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Sword - Haran Geppaku Futsu"),
        pytest.param("Skyward Blade", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Sword - Skyward Blade"),
        pytest.param("Summit Shaper", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Sword - Summit Shaper"),
        pytest.param("Traveler's Handy Sword", 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.defense_perc, 26.7, 5, id="face.wind.rule: Configuring weapon - Sword - Traveler's Handy Sword"),
        pytest.param("Blackcliff Longsword", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_damage_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Sword - Blackcliff Longsword"),
        pytest.param("Finale of the Deep", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Sword - Finale of the Deep"),
        pytest.param("Prototype Rancour", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.damage_bonus_physical_perc, 31.5, 5, id="face.wind.rule: Configuring weapon - Sword - Prototype Rancour"),
        pytest.param("Sapwood Blade", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Sword - Sapwood Blade"),
        pytest.param("Absolution", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Sword - Absolution"),
        pytest.param("Aquila Favonia", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.damage_bonus_physical_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Sword - Aquila Favonia"),
        pytest.param("Mistsplitter Reforged", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Sword - Mistsplitter Reforged"),
        pytest.param("The Alley Flash", 4, "Level 80/90 (Rank 6)", 571, WeaponStatType.elemental_mastery, 50, 5, id="face.wind.rule: Configuring weapon - Sword - The Alley Flash"),
        #TODO pytest.param("Sword of Descension", 0, "Level 80/90 (Rank 6)", 414, WeaponStatType.attack_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Sword - Sword of Descension"),
    ]
)
def test_sword(runner, name, rare, levl, batk, seco, valu, refn) -> None:
    """
    Test the configuration of weapons on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText("Hydro")
    runner.head_char_name.setCurrentText("Furina")
    unit = SwordsDict[name]
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    if isinstance(refn, int):
        runner.weap_area_refn.setCurrentText(f"Refinement {refn}")

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText().strip() == Sword().type.value
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
