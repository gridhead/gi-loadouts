import pytest

from gi_loadouts.data.weap.bows import BowsDict
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap import Bow, WeaponStatType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, rare, levl, batk, seco, valu, refn",
    [
        pytest.param("Hunter's Bow", 1, "Level 60/70 (Rank 4)", 169, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Bow - Hunter's Bow"),
        pytest.param("Seasoned Hunter's Bow", 2, "Level 60/70 (Rank 4)", 220, WeaponStatType.none, 0, None, id="face.wind.rule: Configuring weapon - Bow - Seasoned Hunter's Bow"),
        pytest.param("Recurve Bow", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.health_points_perc, 42.7, 5, id="face.wind.rule: Configuring weapon - Bow - Recurve Bow"),
        pytest.param("Slingshot", 3, "Level 80/90 (Rank 6)", 334, WeaponStatType.critical_rate_perc, 28.5, 5, id="face.wind.rule: Configuring weapon - Bow - Slingshot"),
        pytest.param("Compound Bow", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.damage_bonus_physical_perc, 62.9, 5, id="face.wind.rule: Configuring weapon - Bow - Compound Bow"),
        pytest.param("Favonius Warbow", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.energy_recharge_perc, 55.9, 5, id="face.wind.rule: Configuring weapon - Bow - Favonius Warbow"),
        pytest.param("Hamayumi", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Bow - Hamayumi"),
        pytest.param("King's Squire", 4, "Level 80/90 (Rank 6)", 427, WeaponStatType.attack_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Bow - King's Squire"),
        pytest.param("Aqua Simulacra", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_damage_perc, 80.4, 5, id="face.wind.rule: Configuring weapon - Bow - Aqua Simulacra"),
        pytest.param("Hunter's Path", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.critical_rate_perc, 40.2, 5, id="face.wind.rule: Configuring weapon - Bow - Hunter's Path"),
        pytest.param("Silvershower Heartstrings", 5, "Level 80/90 (Rank 6)", 506, WeaponStatType.health_points_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Bow - Silvershower Heartstrings"),
        pytest.param("Sharpshooter's Oath", 3, "Level 80/90 (Rank 6)", 375, WeaponStatType.critical_damage_perc, 42.7, 5, id="face.wind.rule: Configuring weapon - Bow - Sharpshooter's Oath"),
        pytest.param("Cloudforged", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Bow - Cloudforged"),
        pytest.param("End of the Line", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.energy_recharge_perc, 41.9, 5, id="face.wind.rule: Configuring weapon - Bow - End of the Line"),
        pytest.param("Mitternachts Waltz", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.damage_bonus_physical_perc, 47.2, 5, id="face.wind.rule: Configuring weapon - Bow - Mitternachts Waltz"),
        pytest.param("Predator", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 1, id="face.wind.rule: Configuring weapon - Bow - Predator"),
        pytest.param("Prototype Crescent", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Bow - Prototype Crescent"),
        pytest.param("Royal Bow", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Bow - Royal Bow"),
        pytest.param("Rust", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Bow - Rust"),
        pytest.param("Song of Stillness", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.attack_perc, 37.7, 5, id="face.wind.rule: Configuring weapon - Bow - Song of Stillness"),
        pytest.param("The Stringless", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Bow - The Stringless"),
        pytest.param("The Viridescent Hunt", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.critical_rate_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - The Viridescent Hunt"),
        pytest.param("Windblume Ode", 4, "Level 80/90 (Rank 6)", 475, WeaponStatType.elemental_mastery, 151, 5, id="face.wind.rule: Configuring weapon - Bow - Windblume Ode"),
        pytest.param("Amos' Bow", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.attack_perc, 45.3, 5, id="face.wind.rule: Configuring weapon - Bow - Amos' Bow"),
        pytest.param("Elegy for the End", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.energy_recharge_perc, 50.3, 5, id="face.wind.rule: Configuring weapon - Bow - Elegy for the End"),
        pytest.param("Polar Star", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_rate_perc, 30.2, 5, id="face.wind.rule: Configuring weapon - Bow - Polar Star"),
        pytest.param("The First Great Magic", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Bow - The First Great Magic"),
        pytest.param("Thundering Pulse", 5, "Level 80/90 (Rank 6)", 563, WeaponStatType.critical_damage_perc, 60.3, 5, id="face.wind.rule: Configuring weapon - Bow - Thundering Pulse"),
        pytest.param("Alley Hunter", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - Alley Hunter"),
        pytest.param("Blackcliff Warbow", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_damage_perc, 33.5, 5, id="face.wind.rule: Configuring weapon - Bow - Blackcliff Warbow"),
        pytest.param("Chain Breaker", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - Chain Breaker"),
        pytest.param("Fading Twilight", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Bow - Fading Twilight"),
        pytest.param("Ibis Piercer", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - Ibis Piercer"),
        pytest.param("Mouun's Moon", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - Mouun's Moon"),
        pytest.param("Range Gauge", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.attack_perc, 25.1, 5, id="face.wind.rule: Configuring weapon - Bow - Range Gauge"),
        pytest.param("Sacrificial Bow", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.energy_recharge_perc, 27.9, 5, id="face.wind.rule: Configuring weapon - Bow - Sacrificial Bow"),
        pytest.param("Scion of the Blazing Sun", 4, "Level 80/90 (Rank 6)", 523, WeaponStatType.critical_rate_perc, 16.8, 5, id="face.wind.rule: Configuring weapon - Bow - Scion of the Blazing Sun"),
        pytest.param("Skyward Harp", 5, "Level 80/90 (Rank 6)", 621, WeaponStatType.critical_rate_perc, 20.1, 5, id="face.wind.rule: Configuring weapon - Bow - Skyward Harp"),
    ]
)
def test_bow(runner, name, rare, levl, batk, seco, valu, refn) -> None:
    """
    Test the configuration of weapons on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText("Anemo")
    runner.head_char_name.setCurrentText("Venti")
    unit = BowsDict[name]
    unit.levl = getattr(Level, levl.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    if isinstance(refn, int):
        runner.weap_area_refn.setCurrentText(f"Refinement {refn}")

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText().strip() == Bow().type.value
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
