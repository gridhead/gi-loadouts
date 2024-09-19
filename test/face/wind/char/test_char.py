import pytest
from PySide6.QtCore import Qt

from gi_loadouts.data.char import Aether, Lumine, __charmaps__
from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.levl import Level


@pytest.mark.parametrize(
    "name, vson, cons, levl, rare, cons_name, afln, weap, attk, dfns, hlpt, stat, seco",
    [
        pytest.param(
            char.name,
            char.vision.value.name,
            char.cons.value.name,
            char.levl.value.name,
            char.rare.value.qant,
            char.cons_name,
            char.afln,
            char.weapon.value,
            round(char.attack.stat_data),
            round(char.defense.stat_data),
            round(char.health_points.stat_data),
            char.seco.stat_data,
            char.__statname__.value,
            id=f"face.wind.rule: Configuring character - {char.name}"
        ) for char in __charmaps__.values()
        if setattr(char, 'levl', Level.Level_80_90_Rank_6) is None and setattr(char, 'cons', Cons.Constellation_6) is None
    ]
)
def test_char_drop(runner, name, vson, cons, levl, rare, cons_name, afln, weap, attk, dfns, hlpt, stat, seco):
    """
    Test the configuration of characters on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText(vson.title())
    runner.head_char_name.setCurrentText(name)
    runner.head_char_levl.setCurrentText(levl)
    runner.head_char_cons.setCurrentText(cons.replace(" ","_"))

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.head_area_line_prim.text() == name
    assert runner.char_area_rare.text() == " ".join(["STAR"] * rare)
    assert runner.head_area_line_seco.text() == cons_name
    assert runner.head_area_line_tert.text() == weap
    assert runner.head_area_line_quat.text() == f"<i>{name} is a {weap.lower()}-wielding {vson + " " if vson.lower() != "none" else ""}character of {rare}-star quality.</i>"
    assert runner.head_area_line_quin.text() == f"<i>{name} is affiliated with {afln}.</i>" if afln != "" else f"<i>{name} is not affiliated with any association.</i>"
    assert int(runner.head_char_data_attk.text()) == attk
    assert int(runner.head_char_data_dfns.text()) == dfns
    assert int(runner.head_char_data_hlpt.text()) == hlpt
    assert float(runner.head_char_data_subs.text()) == stat
    assert runner.head_char_icon_attk.toolTip() == "ATK"
    assert runner.head_char_icon_dfns.toolTip() == "DEF"
    assert runner.head_char_icon_hlpt.toolTip() == "HP"
    assert runner.head_char_icon_subs.toolTip() == seco


@pytest.mark.parametrize(
    "name, cons, levl, rare, cons_name, weap, attk, dfns, hlpt, stat, seco, butn",
    [
        pytest.param(
            char.name,
            char.cons.value.name,
            char.levl.value.name,
            char.rare.value.qant,
            char.cons_name,
            char.weapon.value,
            round(char.attack.stat_data),
            round(char.defense.stat_data),
            round(char.health_points.stat_data),
            char.seco.stat_data,
            char.__statname__.value,
            butn,
            id=f"face.wind.rule: Configuring character - {char.name}"
        ) for butn, char in {"char_head_lumi": Lumine(), "char_head_aeth": Aether()}.items()
        if setattr(char, 'levl', Level.Level_80_90_Rank_6) is None and setattr(char, 'cons', Cons.Constellation_6) is None
    ]
)
def test_char_butn(runner, qtbot, name, cons, levl, rare, cons_name, weap, attk, dfns, hlpt, stat, seco, butn):
    """
    Test the configuration of characters on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(getattr(runner, butn), Qt.LeftButton)
    runner.head_char_levl.setCurrentText(levl)
    runner.head_char_cons.setCurrentText(cons.replace(" ","_"))

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.head_area_line_prim.text() == name
    assert runner.char_area_rare.text() == " ".join(["STAR"] * rare)
    assert runner.head_area_line_seco.text() == cons_name
    assert runner.head_area_line_tert.text() == weap
    assert runner.head_area_line_quat.text() == f"<i>{name} is a {weap.lower()}-wielding character of {rare}-star quality.</i>"
    assert runner.head_area_line_quin.text() == f"<i>{name} is not affiliated with any association.</i>"
    assert int(runner.head_char_data_attk.text()) == attk
    assert int(runner.head_char_data_dfns.text()) == dfns
    assert int(runner.head_char_data_hlpt.text()) == hlpt
    assert float(runner.head_char_data_subs.text()) == stat
    assert runner.head_char_icon_attk.toolTip() == "ATK"
    assert runner.head_char_icon_dfns.toolTip() == "DEF"
    assert runner.head_char_icon_hlpt.toolTip() == "HP"
    assert runner.head_char_icon_subs.toolTip() == seco
