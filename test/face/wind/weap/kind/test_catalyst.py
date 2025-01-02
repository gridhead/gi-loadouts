import pytest

from gi_loadouts.data.weap.catalysts import CatalystsDict
from gi_loadouts.face.wind.main import MainWindow
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap import Catalyst, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, levl, batk, seco, valu, refn",
    [
        pytest.param("Magic Guide", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.elemental_mastery, 171, 5, id="face.wind.rule: Configuring weapon - Catalyst - Magic Guide"),
        pytest.param("Dodoco Tales", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Dodoco Tales"),
        pytest.param("Eye of Perception", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Eye of Perception"),
        pytest.param("Sacrificial Fragments", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.elemental_mastery, 201, 5, id="face.wind.rule: Configuring weapon - Catalyst - Sacrificial Fragments"),
        pytest.param("Sacrificial Jade", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.critical_rate_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Catalyst - Sacrificial Jade"),
        pytest.param("Waveriding Whirl", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Waveriding Whirl"),
        pytest.param("A Thousand Floating Dreams", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.elemental_mastery, 241, 5, id="face.wind.rule: Configuring weapon - Catalyst - A Thousand Floating Dreams"),
        pytest.param("Surf's Up", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Catalyst - Surf's Up"),
        pytest.param("Tome of the Eternal Flow", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Catalyst - Tome of the Eternal Flow"),
        pytest.param("Apprentice's Notes", 1, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Catalyst - Apprentice's Notes"),
        pytest.param("Pocket Grimoire", 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Catalyst - Pocket Grimoire"),
        pytest.param("Otherworldly Story", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.energy_recharge_perc, 35.6, 5, id="face.wind.rule: Configuring weapon - Catalyst - Otherworldly Story"),
        pytest.param("Thrilling Tales of Dragon Slayers", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.health_points_perc, 32.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Thrilling Tales of Dragon Slayers"),
        pytest.param("Ash-Graven Drinking Horn", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Catalyst - Ash-Graven Drinking Horn"),
        pytest.param("Blackcliff Agate", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Blackcliff Agate"),
        pytest.param("Favonius Codex", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Favonius Codex"),
        pytest.param("Frostbearer", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Catalyst - Frostbearer"),
        pytest.param("Fruit of Fulfillment", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Fruit of Fulfillment"),
        pytest.param("Prototype Amber", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Catalyst - Prototype Amber"),
        pytest.param("Ring of Yaxche", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.health_points_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Catalyst - Ring of Yaxche"),
        pytest.param("Solar Pearl", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Solar Pearl"),
        pytest.param("The Widsith", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_damage_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - The Widsith"),
        pytest.param("Wandering Evenstar", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Catalyst - Wandering Evenstar"),
        pytest.param("Everlasting Moonglow", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.health_points_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Everlasting Moonglow"),
        pytest.param("Jadefall's Splendor", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.health_points_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Jadefall's Splendor"),
        pytest.param("Kagura's Verity", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Kagura's Verity"),
        pytest.param("Lost Prayer to the Sacred Winds", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Catalyst - Lost Prayer to the Sacred Winds"),
        pytest.param("Memory of Dust", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Catalyst - Memory of Dust"),
        pytest.param("Emerald Orb", 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.elemental_mastery, 85, 5, id="face.wind.rule: Configuring weapon - Catalyst - Emerald Orb"),
        pytest.param("Twin Nephrite", 3, "Level 80/90 (Rank 6)", 415, WeaponStatType.critical_rate_perc, 14.2, 5, id="face.wind.rule: Configuring weapon - Catalyst - Twin Nephrite"),
        pytest.param("Ballad of the Boundless Blue", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Ballad of the Boundless Blue"),
        pytest.param("Flowing Purity", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Flowing Purity"),
        pytest.param("Hakushin Ring", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Hakushin Ring"),
        pytest.param("Mappa Mare", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.elemental_mastery, 101, 5, id="face.wind.rule: Configuring weapon - Catalyst - Mappa Mare"),
        pytest.param("Oathsworn Eye", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Oathsworn Eye"),
        pytest.param("Royal Grimoire", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Royal Grimoire"),
        pytest.param("Wine and Song", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Catalyst - Wine and Song"),
        pytest.param("Cashflow Supervision", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Cashflow Supervision"),
        pytest.param("Skyward Atlas", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.attack_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Catalyst - Skyward Atlas"),
        pytest.param("Tulaytullah's Remembrance", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_damage_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Catalyst - Tulaytullah's Remembrance"),
        pytest.param("Crane's Echoing Call", 5, "Level 80/90 (Rank 6)", 679, WeaponStatType.attack_perc, 15.1, 5, id="face.wind.rule: Configuring weapon - Catalyst - Crane's Echoing Call"),
        pytest.param("Starcaller's Watch", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.elemental_mastery, 241, 5, id="face.wind.rule: Configuring weapon - Catalyst - Starcaller's Watch"),
    ]
)
def test_catalyst(runner: MainWindow, name: str, rare: int, levl: str, batk: int, seco: WeaponStatType, valu: float, refn: int | None) -> None:
    """
    Test configuring weapons of catalyst type on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText("Dendro")
    runner.head_char_name.setCurrentText("Nahida")
    unit = CatalystsDict[name]()
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    if isinstance(refn, int):
        runner.weap_area_refn.setCurrentText(f"Refinement {refn}")

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText().strip() == Catalyst().type.value
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
