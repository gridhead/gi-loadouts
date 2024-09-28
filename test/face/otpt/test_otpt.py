from random import choice

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from gi_loadouts import __versdata__
from gi_loadouts.data.char import __charmaps__
from gi_loadouts.data.weap import Family
from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.levl import Level

from . import __test_arti__


@pytest.mark.parametrize(
    "type, cond",
    [
        pytest.param("Bow", "pair", id="face.otpt.rule: Generate final calculation based on character, bow and 2 piece artifact set"),
        pytest.param("Catalyst", "pair", id="face.otpt.rule: Generate final calculation based on character, catalyst and 2 piece artifact set"),
        pytest.param("Claymore", "pair", id="face.otpt.rule: Generate final calculation based on character, claymore and 2 piece artifact set"),
        pytest.param("Polearm", "pair", id="face.otpt.rule: Generate final calculation based on character, polearm and 2 piece artifact set"),
        pytest.param("Sword", "pair", id="face.otpt.rule: Generate final calculation based on character, sword and 2 piece artifact set"),
        pytest.param("Bow", "quad", id="face.otpt.rule: Generate final calculation based on character, bow and 4 piece artifact set"),
        pytest.param("Catalyst", "quad", id="face.otpt.rule: Generate final calculation based on character, catalyst and 4 piece artifact set"),
        pytest.param("Claymore", "quad", id="face.otpt.rule: Generate final calculation based on character, claymore and 4 piece artifact set"),
        pytest.param("Polearm", "quad", id="face.otpt.rule: Generate final calculation based on character, polearm and 4 piece artifact set"),
        pytest.param("Sword", "quad", id="face.otpt.rule: Generate final calculation based on character, sword and 4 piece artifact set"),
        pytest.param("Bow", "unique", id="face.otpt.rule: Generate final calculation based on character, bow and unique artifacts"),
        pytest.param("Catalyst", "unique", id="face.otpt.rule: Generate final calculation based on character, catalyst and unique artifacts"),
        pytest.param("Claymore", "unique", id="face.otpt.rule: Generate final calculation based on character, claymore and unique artifacts"),
        pytest.param("Polearm", "unique", id="face.otpt.rule: Generate final calculation based on character, polearm and unique artifacts"),
        pytest.param("Sword", "unique", id="face.otpt.rule: Generate final calculation based on character, sword and unique artifacts"),
        pytest.param("Bow", "none", id="face.otpt.rule: Generate final calculation based on character, bow and no artifacts"),
        pytest.param("Catalyst", "none", id="face.otpt.rule: Generate final calculation based on character, catalyst and no artifacts"),
        pytest.param("Claymore", "none", id="face.otpt.rule: Generate final calculation based on character, claymore and no artifacts"),
        pytest.param("Polearm", "none", id="face.otpt.rule: Generate final calculation based on character, polearm and no artifacts"),
        pytest.param("Sword", "none", id="face.otpt.rule: Generate final calculation based on character, sword and no artifacts"),
    ]
)
def test_otpt(runner, qtbot, type, cond) -> None:
    """
    Attempt to generate final calculation based on character, weapon and artifacts

    :return:
    """

    """
    Set the user interface elements as intended
    """
    if cond == "quad":
        """
        Modify variable __test_arti__ to store 4 piece artifact set
        """
        __test_arti__["sdoe"]["type"] = "Emblem of Severed Fate"
        __test_arti__["sdoe"]["name"] = "Storm Cage"
        __test_arti__["ccol"]["type"] = "Emblem of Severed Fate"
        __test_arti__["ccol"]["name"] = "Ornate Kabuto"
    elif cond == "unique":
        """
        Modify variable __test_arti__ to store unique artifacts
        """
        __test_arti__["pmod"]["type"] = "Marechaussee Hunter"
        __test_arti__["pmod"]["name"] = "Masterpiece's Overture"
        __test_arti__["gboe"]["type"] = "Retracing Bolide"
        __test_arti__["gboe"]["name"] = "Summer Night's Waterballoon"
    elif cond == "none":
        """
        Modify variable __test_arti__ to store no artifacts
        """
        __test_arti__["fwol"]["type"] = "None"
        __test_arti__["pmod"]["type"] = "None"
        __test_arti__["sdoe"]["type"] = "None"
        __test_arti__["gboe"]["type"] = "None"
        __test_arti__["ccol"]["type"] = "None"

    """
    Setting the character statistics
    """
    c_name = choice([name for name, data in __charmaps__.items() if data().weapon.value == type])
    c_levl = choice(list(item.value.name for item in Level))
    c_cons = choice(list(item.value.name for item in Cons))
    runner.head_char_name.setCurrentText(c_name)
    runner.head_char_levl.setCurrentText(c_levl)
    runner.head_char_cons.setCurrentText(c_cons)

    """
    Setting the weapon statistics
    """
    w_name = choice(list(Family[type].keys()))
    w_objc = Family[type][w_name]()
    w_levl = choice(w_objc.levl_bind).value.name
    w_refn = f"({choice(list(w_objc.refinement.keys()))})" if w_objc.refinement.keys() else ""
    runner.weap_area_name.setCurrentText(w_name)
    runner.weap_area_levl.setCurrentText(w_levl)
    runner.weap_area_refn.setCurrentText(w_refn.replace("(","").replace(")","")) if w_refn != "" else None

    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        getattr(runner, f"arti_{area}_type").setCurrentText(__test_arti__[area]["type"])

    if cond != "none":
        for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            getattr(runner, f"arti_{area}_rare").setCurrentText(__test_arti__[area]["rare"])
            getattr(runner, f"arti_{area}_levl").setCurrentText(__test_arti__[area]["levl"])
            getattr(runner, f"arti_{area}_name_main").setCurrentText(__test_arti__[area]["main"])
            for alfa in ["a", "b", "c", "d"]:
                getattr(runner, f"arti_{area}_name_{alfa}").setCurrentText(__test_arti__[area]["stat"][alfa]["name"])
                getattr(runner, f"arti_{area}_data_{alfa}").setText(str(__test_arti__[area]["stat"][alfa]["data"]))

    if runner.collection.quad != "":
        artiline = f"4 x <b>{runner.collection.quad}</b>"
    elif len(runner.collection.pair) >= 1:
        artiline = ", ".join([f"2 x <b>{item}</b>" for item in runner.collection.pair])
    else:
        artiline = "No artifact set bonus."

    """
    Perform the action of clicking the help button
    """
    qtbot.mouseClick(runner.head_scan, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.head_scan.toolTip() == "Generate"
    assert isinstance(runner.otptobjc, QMainWindow)
    assert runner.otptobjc.windowTitle() == f"Loadouts for Genshin Impact v{__versdata__} - {runner.head_char_name.currentText()}"
    assert runner.otptobjc.windowModality() == Qt.ApplicationModal
    assert runner.otptobjc.head_area_line_prim.text() == f"<b>{c_name}</b> - {c_levl} ({c_cons})"
    assert runner.otptobjc.head_area_line_seco.text() == f"<b>{w_name}</b> - {w_levl} {w_refn}" + "<br/>" + f"{artiline}"
    assert runner.otptobjc.area_hlpt_data.text() == str(round(runner.otptobjc.tyvt.health_points.stat_data, 1))
    assert runner.otptobjc.area_hlpt_calc.text() == f"{round(runner.otptobjc.tyvt.addendum_base_health_points.stat_data, 1)} + {round(runner.otptobjc.tyvt.addendum_plus_health_points.stat_data, 1)}"
    assert runner.otptobjc.area_attk_data.text() == str(round(runner.otptobjc.tyvt.attack.stat_data, 1))
    assert runner.otptobjc.area_attk_calc.text() == f"{round(runner.otptobjc.tyvt.addendum_base_attack.stat_data, 1)} + {round(runner.otptobjc.tyvt.addendum_plus_attack.stat_data, 1)}"
    assert runner.otptobjc.area_dfns_data.text() == str(round(runner.otptobjc.tyvt.defense.stat_data, 1))
    assert runner.otptobjc.area_dfns_calc.text() == f"{round(runner.otptobjc.tyvt.addendum_base_defense.stat_data, 1)} + {round(runner.otptobjc.tyvt.addendum_plus_defense.stat_data, 1)}"
    assert runner.otptobjc.area_elma_data.text() == str(round(runner.otptobjc.tyvt.elemental_mastery.stat_data, 1))
    assert runner.otptobjc.area_crit_rate_data.text() == f"{str(round(runner.otptobjc.tyvt.critical_rate_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_crit_dmge_data.text() == f"{str(round(runner.otptobjc.tyvt.critical_damage_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_heal_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.healing_bonus_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_heal_incm_data.text() == f"{str(round(runner.otptobjc.tyvt.incoming_healing_bonus_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_enrc_data.text() == f"{str(round(runner.otptobjc.tyvt.energy_recharge_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_cldn_data.text() == f"{str(round(runner.otptobjc.tyvt.cooldown_reduction_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_sdsh_data.text() == f"{str(round(runner.otptobjc.tyvt.shield_strength_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_pyro_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_pyro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_pyro_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_pyro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_hydo_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_hydro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_hydo_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_hydro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_dend_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_dendro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_dend_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_dendro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_elec_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_electro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_elec_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_electro_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_anem_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_anemo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_anem_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_anemo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_cryo_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_cryo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_cryo_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_cryo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_geox_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_geo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_geox_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_geo_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_phys_perc_data.text() == f"{str(round(runner.otptobjc.tyvt.damage_bonus_physical_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_phys_resi_data.text() == f"{str(round(runner.otptobjc.tyvt.resistance_physical_perc.stat_data, 1))}%"
    assert runner.otptobjc.area_crvl_data.text() == f"{str(round(runner.otptobjc.tyvt.critical_damage_perc.stat_data + 2*(runner.otptobjc.tyvt.critical_rate_perc.stat_data), 1))}"
