import pytest
from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot

from gi_loadouts.data.char import __charmaps__
from gi_loadouts.face.wind.main import MainWindow
from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.levl import Level


@pytest.mark.parametrize(
    "name",
    [
        pytest.param(name, id=f"face.wind.rule: Configuring character - {name}")
        for name in __charmaps__.keys()
    ],
)
def test_char_drop(runner: MainWindow, name: str) -> None:
    """
    Test configuring characters on the user interface

    :return:
    """

    char = __charmaps__[name]()
    char.levl = Level.Level_80_90_Rank_6
    char.cons = Cons.Constellation_6

    vson = char.vision.value.name
    cons = char.cons.value.name
    levl = char.levl.value.name
    rare = char.rare.value.qant
    cons_name = char.cons_name
    afln = char.afln
    weap = char.weapon.value
    attk = round(char.attack.stat_data)
    dfns = round(char.defense.stat_data)
    hlpt = round(char.health_points.stat_data)
    stat = char.seco.stat_data
    seco = char.__statname__.value

    """
    Set the user interface elements as intended
    """
    runner.head_char_elem.setCurrentText(vson.title())
    runner.head_char_name.setCurrentText(name)
    runner.head_char_levl.setCurrentText(levl)
    runner.head_char_cons.setCurrentText(cons.replace(" ", "_"))

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.head_area_line_prim.text() == name
    assert runner.char_area_rare.text() == " ".join(["STAR"] * rare)
    assert runner.head_area_line_seco.text() == cons_name
    assert runner.head_area_line_tert.text() == weap
    assert (
        runner.head_area_line_quat.text()
        == f"<i>{name} is a {weap.lower()}-wielding {vson + ' ' if vson.lower() != 'none' else ''}character of {rare}-star quality.</i>"
    )
    assert (
        runner.head_area_line_quin.text() == f"<i>{name} is affiliated with {afln}.</i>"
        if afln != ""
        else f"<i>{name} is not affiliated with any association.</i>"
    )
    assert int(runner.head_char_data_attk.text()) == attk
    assert int(runner.head_char_data_dfns.text()) == dfns
    assert int(runner.head_char_data_hlpt.text()) == hlpt
    assert float(runner.head_char_data_subs.text()) == stat
    assert runner.head_char_icon_attk.toolTip() == "ATK"
    assert runner.head_char_icon_dfns.toolTip() == "DEF"
    assert runner.head_char_icon_hlpt.toolTip() == "HP"
    assert runner.head_char_icon_subs.toolTip() == seco


@pytest.mark.parametrize(
    "name, butn",
    [
        pytest.param(name, butn, id=f"face.wind.rule: Configuring character - {name}")
        for name, butn in {"Lumine": "char_head_lumi", "Aether": "char_head_aeth"}.items()
    ],
)
def test_char_butn(runner: MainWindow, qtbot: QtBot, name: str, butn: str) -> None:
    """
    Test configuring travelers on the user interface

    :return:
    """

    char = __charmaps__[name]()
    char.levl = Level.Level_80_90_Rank_6
    char.cons = Cons.Constellation_6

    cons = char.cons.value.name
    levl = char.levl.value.name
    rare = char.rare.value.qant
    cons_name = char.cons_name
    weap = char.weapon.value
    attk = round(char.attack.stat_data)
    dfns = round(char.defense.stat_data)
    hlpt = round(char.health_points.stat_data)
    stat = char.seco.stat_data
    seco = char.__statname__.value

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(getattr(runner, butn), Qt.LeftButton)
    runner.head_char_levl.setCurrentText(levl)
    runner.head_char_cons.setCurrentText(cons.replace(" ", "_"))

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.head_area_line_prim.text() == name
    assert runner.char_area_rare.text() == " ".join(["STAR"] * rare)
    assert runner.head_area_line_seco.text() == cons_name
    assert runner.head_area_line_tert.text() == weap
    assert (
        runner.head_area_line_quat.text()
        == f"<i>{name} is a {weap.lower()}-wielding character of {rare}-star quality.</i>"
    )
    assert (
        runner.head_area_line_quin.text()
        == f"<i>{name} is not affiliated with any association.</i>"
    )
    assert int(runner.head_char_data_attk.text()) == attk
    assert int(runner.head_char_data_dfns.text()) == dfns
    assert int(runner.head_char_data_hlpt.text()) == hlpt
    assert float(runner.head_char_data_subs.text()) == stat
    assert runner.head_char_icon_attk.toolTip() == "ATK"
    assert runner.head_char_icon_dfns.toolTip() == "DEF"
    assert runner.head_char_icon_hlpt.toolTip() == "HP"
    assert runner.head_char_icon_subs.toolTip() == seco
