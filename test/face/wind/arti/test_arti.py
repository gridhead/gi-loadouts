from random import choice

import pytest
from PySide6.QtCore import Qt
from pytestqt.qtbot import QtBot

from gi_loadouts.data.arti import __artilist__
from gi_loadouts.face.util import truncate_text
from gi_loadouts.face.wind.main import MainWindow
from gi_loadouts.type.arti import ArtiLevl, base
from gi_loadouts.type.stat import STAT


@pytest.mark.parametrize(
    "name, rare, pair, quad, coll",
    [
        pytest.param(
            name,
            team.rare,
            team.pairtext,
            team.quadtext,
            (team.fwol, team.pmod, team.sdoe, team.gboe, team.ccol),
            id=f"face.wind.rule: Configuration artifact - {name}",
        )
        for name, team in __artilist__.items()
    ],
)
def test_arti_drop(
    runner: MainWindow, name: str, rare: list, pair: str, quad: str, coll: tuple
) -> None:
    """
    Test configuring artifacts on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    conf = dict()

    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        conf[area] = dict()
        getattr(runner, f"arti_{area}_type").setCurrentText(name)
        conf[area]["rare"] = choice([item for item in rare])
        getattr(runner, f"arti_{area}_rare").setCurrentText(conf[area]["rare"].value.name)
        conf[area]["levl"] = choice(
            [item for item in ArtiLevl if conf[area]["rare"] in item.value.rare]
        )
        getattr(runner, f"arti_{area}_levl").setCurrentText(conf[area]["levl"].value.name)
        conf[area]["stat"] = choice(
            [
                item
                for item in getattr(base, f"MainStatType_{area.upper()}")
                if item.value != STAT.none
            ]
        )
        getattr(runner, f"arti_{area}_name_main").setCurrentText(conf[area]["stat"].value.value)

    """
    Confirm if the user interface elements change accordingly
    """
    if name == "None":
        return

    for indx, area in enumerate(["fwol", "pmod", "sdoe", "gboe", "ccol"]):
        item = coll[indx]
        assert getattr(runner, f"arti_{area}_type_name").text() == truncate_text(
            coll[indx].__name__, 32
        )
        item.rare, item.levl, item.stat_name = (
            conf[area]["rare"].value.qant,
            conf[area]["levl"].value.levl,
            conf[area]["stat"],
        )
        assert getattr(runner, f"arti_{area}_data_main").text() == str(round(item.stat_data, 1))

    assert runner.pair_area_head.text() == f"<b>{truncate_text(name, 26)}</b> (2)"
    assert runner.quad_area_head.text() == f"<b>{truncate_text(name, 26)}</b> (4)"
    assert runner.pair_area_desc.toPlainText() == pair
    assert runner.quad_area_desc.toPlainText() == quad


@pytest.mark.parametrize(
    "area",
    [
        pytest.param("fwol", id="face.wind.rule: Clearing the 'Flower of Life' area"),
        pytest.param("pmod", id="face.wind.rule: Clearing the 'Plume of Death' area"),
        pytest.param("sdoe", id="face.wind.rule: Clearing the 'Sands of Eon' area"),
        pytest.param("gboe", id="face.wind.rule: Clearing the 'Goblet of Eonothem' area"),
        pytest.param("ccol", id="face.wind.rule: Clearing the 'Circlet of Logos' area"),
    ],
)
def test_arti_wipe(runner: MainWindow, qtbot: QtBot, area: str) -> None:
    """
    Test configuring characters on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(getattr(runner, f"arti_{area}_wipe"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert getattr(runner, f"arti_{area}_type").currentText() == "None"
    assert getattr(runner, f"arti_{area}_levl").currentText() == "None"
    assert getattr(runner, f"arti_{area}_rare").currentText() == "Star 0"
    assert getattr(runner, f"arti_{area}_type_name").text() == "None"
    for item in ["main", "a", "b", "c", "d"]:
        assert getattr(runner, f"arti_{area}_name_{item}").currentText() == "None"
        assert getattr(runner, f"arti_{area}_data_{item}").text() == ""
