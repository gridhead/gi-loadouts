from os import path, remove
from pathlib import Path
from random import choice, uniform
from tempfile import NamedTemporaryFile, gettempdir
from uuid import uuid4

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot

from gi_loadouts.data.arti import __artilist__
from gi_loadouts.face.util import truncate_text
from gi_loadouts.face.wind import file
from gi_loadouts.face.wind.main import MainWindow
from gi_loadouts.type.arti import ArtiLevl, base
from gi_loadouts.type.stat import STAT
from test import json_type, yaml_type

from . import (
    actual_ccol,
    actual_fwol,
    actual_gboe,
    actual_pmod,
    actual_sdoe,
    json_ccol_sample,
    json_fwol_sample,
    json_gboe_sample,
    json_pmod_sample,
    json_sdoe_sample,
    yaml_ccol_sample,
    yaml_fwol_sample,
    yaml_gboe_sample,
    yaml_pmod_sample,
    yaml_sdoe_sample,
)


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol", id="face.wind.rule: Saving a 'None' artifact from 'Flower of Life' area"
        ),
        pytest.param(
            "pmod", id="face.wind.rule: Saving a 'None' artifact from 'Plume of Death' area"
        ),
        pytest.param(
            "sdoe", id="face.wind.rule: Saving a 'None' artifact from 'Sands of Eon' area"
        ),
        pytest.param(
            "gboe", id="face.wind.rule: Saving a 'None' artifact from 'Goblet of Eonothem' area"
        ),
        pytest.param(
            "ccol", id="face.wind.rule: Saving a 'None' artifact from 'Circlet of Logos' area"
        ),
    ],
)
def test_arti_save_none(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test saving a 'None' artifact across five areas

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(getattr(runner, f"arti_{area}_wipe"), Qt.LeftButton)

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."


@pytest.mark.parametrize(
    "area",
    [
        pytest.param("fwol", id="face.wind.rule: Saving an artifact from 'Flower of Life' area"),
        pytest.param("pmod", id="face.wind.rule: Saving an artifact from 'Plume of Death' area"),
        pytest.param("sdoe", id="face.wind.rule: Saving an artifact from 'Sands of Eon' area"),
        pytest.param(
            "gboe", id="face.wind.rule: Saving an artifact from 'Goblet of Eonothem' area"
        ),
        pytest.param("ccol", id="face.wind.rule: Saving an artifact from 'Circlet of Logos' area"),
    ],
)
def test_arti_save_name(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test saving an artifact across five areas

    :return:
    """
    conf = dict()

    """
    Set the user interface elements as intended
    """
    name = choice([item for item in __artilist__.keys() if item != "None"])
    getattr(runner, f"arti_{area}_type").setCurrentText(name)
    conf["rare"] = choice([item for item in __artilist__[name].rare])
    getattr(runner, f"arti_{area}_rare").setCurrentText(conf["rare"].value.name)
    conf["levl"] = choice([item for item in ArtiLevl if conf["rare"] in item.value.rare])
    getattr(runner, f"arti_{area}_levl").setCurrentText(conf["levl"].value.name)
    conf["stat"] = choice(
        [item for item in getattr(base, f"MainStatType_{area.upper()}") if item.value != STAT.none]
    )
    getattr(runner, f"arti_{area}_name_main").setCurrentText(conf["stat"].value.value)
    for indx in ["a", "b", "c", "d"]:
        getattr(runner, f"arti_{area}_data_{indx}").setText(str(round(uniform(0, 100), 2)))

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol", id="face.wind.rule: Failing to save an artifact from 'Flower of Life' area"
        ),
        pytest.param(
            "pmod", id="face.wind.rule: Failing to save an artifact from 'Plume of Death' area"
        ),
        pytest.param(
            "sdoe", id="face.wind.rule: Failing to save an artifact from 'Sands of Eon' area"
        ),
        pytest.param(
            "gboe", id="face.wind.rule: Failing to save an artifact from 'Goblet of Eonothem' area"
        ),
        pytest.param(
            "ccol", id="face.wind.rule: Failing to save an artifact from 'Circlet of Logos' area"
        ),
    ],
)
def test_arti_save_fail(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test failing to save an artifact across five areas due to empty data fields

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Save failed"
    assert (
        "Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact data in a location that is accessible."
        in runner.dialog.text()
    )
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area, sample, actual",
    [
        pytest.param(
            "fwol",
            yaml_fwol_sample,
            actual_fwol,
            id="face.wind.rule: Loading an artifact into 'Flower of Life' area from YAML data",
        ),
        pytest.param(
            "pmod",
            yaml_pmod_sample,
            actual_pmod,
            id="face.wind.rule: Loading an artifact into 'Plume of Death' area from YAML data",
        ),
        pytest.param(
            "sdoe",
            yaml_sdoe_sample,
            actual_sdoe,
            id="face.wind.rule: Loading an artifact into 'Sands of Eon' area from YAML data",
        ),
        pytest.param(
            "gboe",
            yaml_gboe_sample,
            actual_gboe,
            id="face.wind.rule: Loading an artifact into 'Goblet of Eonothem' area from YAML data",
        ),
        pytest.param(
            "ccol",
            yaml_ccol_sample,
            actual_ccol,
            id="face.wind.rule: Loading an artifact into 'Circlet of Logos' area from YAML data",
        ),
    ],
)
def test_arti_load_yaml(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, actual: dict
) -> None:
    """
    Test loading an artifact across five areas from YAML data

    :return:
    """

    """
    Perform the action of loading the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, yaml_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert getattr(runner, f"arti_{area}_type").currentText() == actual["type"]
    assert getattr(runner, f"arti_{area}_rare").currentText() == actual["rare"]
    assert getattr(runner, f"arti_{area}_levl").currentText() == actual["levl"]
    assert getattr(runner, f"arti_{area}_type_name").text() == truncate_text(actual["name"], 32)
    assert getattr(runner, f"arti_{area}_name_main").currentText() == actual["main"]
    for item in ["a", "b", "c", "d"]:
        assert (
            getattr(runner, f"arti_{area}_name_{item}").currentText()
            == actual["stat"][item]["name"]
        )
        assert getattr(runner, f"arti_{area}_data_{item}").text() == str(
            actual["stat"][item]["data"]
        )
    assert runner.statarea.currentMessage() == "Artifact data has been successfully loaded."


@pytest.mark.parametrize(
    "area, sample, actual",
    [
        pytest.param(
            "fwol",
            json_fwol_sample,
            actual_fwol,
            id="face.wind.rule: Loading an artifact into 'Flower of Life' area from JSON data",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample,
            actual_pmod,
            id="face.wind.rule: Loading an artifact into 'Plume of Death' area from JSON data",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample,
            actual_sdoe,
            id="face.wind.rule: Loading an artifact into 'Sands of Eon' area from JSON data",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample,
            actual_gboe,
            id="face.wind.rule: Loading an artifact into 'Goblet of Eonothem' area from JSON data",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample,
            actual_ccol,
            id="face.wind.rule: Loading an artifact into 'Circlet of Logos' area from JSON data",
        ),
    ],
)
def test_arti_load_json(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, actual: dict
) -> None:
    """
    Test loading an artifact across five areas from JSON data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, json_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert getattr(runner, f"arti_{area}_type").currentText() == actual["type"]
    assert getattr(runner, f"arti_{area}_rare").currentText() == actual["rare"]
    assert getattr(runner, f"arti_{area}_levl").currentText() == actual["levl"]
    assert getattr(runner, f"arti_{area}_type_name").text() == truncate_text(actual["name"], 32)
    assert getattr(runner, f"arti_{area}_name_main").currentText() == actual["main"]
    for item in ["a", "b", "c", "d"]:
        assert (
            getattr(runner, f"arti_{area}_name_{item}").currentText()
            == actual["stat"][item]["name"]
        )
        assert getattr(runner, f"arti_{area}_data_{item}").text() == str(
            actual["stat"][item]["data"]
        )
    assert runner.statarea.currentMessage() == "Artifact data has been successfully loaded."


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol", id="face.wind.rule: Cancelling loading an artifact into 'Flower of Life' area"
        ),
        pytest.param(
            "pmod", id="face.wind.rule: Cancelling loading an artifact into 'Plume of Death' area"
        ),
        pytest.param(
            "sdoe", id="face.wind.rule: Cancelling loading an artifact into 'Sands of Eon' area"
        ),
        pytest.param(
            "gboe",
            id="face.wind.rule: Cancelling loading an artifact into 'Goblet of Eonothem' area",
        ),
        pytest.param(
            "ccol", id="face.wind.rule: Cancelling loading an artifact into 'Circlet of Logos' area"
        ),
    ],
)
def test_arti_load_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test cancelling loading an artifact across five areas

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(False, "", ""))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert getattr(runner, f"arti_{area}_type").currentText() == "Adventurer"
    assert getattr(runner, f"arti_{area}_rare").currentText() == "Star 1"
    assert getattr(runner, f"arti_{area}_levl").currentText() == "Level 00"


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol",
            id="face.wind.rule: Loading an artifact into 'Flower of Life' area from an empty file",
        ),
        pytest.param(
            "pmod",
            id="face.wind.rule: Loading an artifact into 'Plume of Death' area from an empty file",
        ),
        pytest.param(
            "sdoe",
            id="face.wind.rule: Loading an artifact into 'Sands of Eon' area from an empty file",
        ),
        pytest.param(
            "gboe",
            id="face.wind.rule: Loading an artifact into 'Goblet of Eonothem' area from an empty file",
        ),
        pytest.param(
            "ccol",
            id="face.wind.rule: Loading an artifact into 'Circlet of Logos' area from an empty file",
        ),
    ],
)
def test_arti_load_void(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test loading an artifact across five areas from an empty file

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, "", ""))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "Selected file cannot be read." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area, sample, type",
    [
        pytest.param(
            "fwol",
            json_fwol_sample.replace("fwol", "AWRY"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Flower of Life' area from YAML data",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample.replace("pmod", "AWRY"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Plume of Death' area from YAML data",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample.replace("sdoe", "AWRY"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Sands of Eon' area from YAML data",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample.replace("gboe", "AWRY"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Goblet of Eonothem' area from YAML data",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample.replace("ccol", "AWRY"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Circlet of Logos' area from YAML data",
        ),
        pytest.param(
            "fwol",
            json_fwol_sample.replace("flower", "AWRY"),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Flower of Life' area from JSON data",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample.replace("plume", "AWRY"),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Plume of Death' area from JSON data",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample.replace("sands", "AWRY"),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Sands of Eon' area from JSON data",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample.replace("goblet", "AWRY"),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Goblet of Eonothem' area from JSON data",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample.replace("circlet", "AWRY"),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect area into 'Circlet of Logos' area from JSON data",
        ),
    ],
)
def test_arti_load_awry(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, type: str
) -> None:
    """
    Test loading an artifact with incorrect area across five areas from data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert (
        "Artifact stat cannot be identified or unit data cannot be parsed." in runner.dialog.text()
    )
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area, sample, type",
    [
        pytest.param(
            "fwol",
            yaml_pmod_sample.replace("name: HP\n", "name: Energy Recharge\n").replace(
                "name: ATK\n", "name: HP\n"
            ),
            yaml_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Flower of Life' area from YAML data",
        ),
        pytest.param(
            "pmod",
            yaml_sdoe_sample.replace("name: ATK\n", "name: HP\n").replace(
                "name: Elemental Mastery\n", "name: ATK\n"
            ),
            yaml_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Plume of Death' area from YAML data",
        ),
        pytest.param(
            "sdoe",
            yaml_gboe_sample.replace("name: Physical DMG Bonus\n", "name: ATK %\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Sands of Eon' area from YAML data",
        ),
        pytest.param(
            "gboe",
            yaml_ccol_sample.replace("name: Healing Bonus\n", "name: HP %\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Goblet of Eonothem' area from YAML data",
        ),
        pytest.param(
            "ccol",
            yaml_fwol_sample.replace("name: HP\n", "name: HP %\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Circlet of Logos' area from YAML data",
        ),
        pytest.param(
            "fwol",
            json_pmod_sample.replace('"key": "hp",\n', '"key": "enerRech_",\n').replace(
                '"mainStatKey": "atk",\n', '"mainStatKey": "hp",\n'
            ),
            json_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Flower of Life' area from JSON data",
        ),
        pytest.param(
            "pmod",
            json_sdoe_sample.replace('"key": "atk",\n', '"key": "hp",\n').replace(
                '"mainStatKey": "eleMas",\n', '"mainStatKey": "atk",\n'
            ),
            json_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Plume of Death' area from JSON data",
        ),
        pytest.param(
            "sdoe",
            json_gboe_sample.replace(
                '"mainStatKey": "physical_dmg_",\n', '"mainStatKey": "atk_",\n'
            ),
            json_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Sands of Eon' area from JSON data",
        ),
        pytest.param(
            "gboe",
            json_ccol_sample.replace('"mainStatKey": "heal_",\n', '"mainStatKey": "hp_",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect mismatched into 'Goblet of Eonothem' area from JSON data",
        ),
        pytest.param(
            "ccol",
            json_fwol_sample.replace('"mainStatKey": "hp",\n', '"mainStatKey": "hp_",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with mismatched area into 'Circlet of Logos' area from JSON data",
        ),
    ],
)
def test_arti_load_area_diff(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, type: str
) -> None:
    """
    Test loading an artifact with mismatched area from the file

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "The artifact file does not match the expected equipment slot." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area, sample, type",
    [
        pytest.param(
            "fwol",
            yaml_fwol_sample.replace("name: Crit Rate\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Flower of Life' area from YAML data",
        ),
        pytest.param(
            "pmod",
            yaml_pmod_sample.replace("name: DEF\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Plume of Death' area from YAML data",
        ),
        pytest.param(
            "sdoe",
            yaml_sdoe_sample.replace("name: ATK\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Sands of Eon' area from YAML data",
        ),
        pytest.param(
            "gboe",
            yaml_gboe_sample.replace("name: Elemental Mastery\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Goblet of Eonothem' area from YAML data",
        ),
        pytest.param(
            "ccol",
            yaml_ccol_sample.replace("name: ATK\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Circlet of Logos' area from YAML data",
        ),
        pytest.param(
            "fwol",
            json_fwol_sample.replace('"key": "critRate_",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Flower of Life' area from JSON data",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample.replace('"key": "def",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Plume of Death' area from JSON data",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample.replace('"key": "atk",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Sands of Eon' area from JSON data",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample.replace('"key": "eleMas",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Goblet of Eonothem' area from JSON data",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample.replace('"key": "atk",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats into 'Circlet of Logos' area from JSON data",
        ),
    ],
)
def test_arti_load_name(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, type: str
) -> None:
    """
    Test loading an artifact with incorrect substats across five areas from data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert (
        "Artifact stat cannot be identified or unit data cannot be parsed." in runner.dialog.text()
    )
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area, sample, type",
    [
        pytest.param(
            "fwol",
            yaml_fwol_sample.replace("name: Crit Rate\n", "name: HP\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Flower of Life' area from YAML data",
        ),
        pytest.param(
            "pmod",
            yaml_pmod_sample.replace("name: DEF\n", "name: ATK\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Plume of Death' area from YAML data",
        ),
        pytest.param(
            "sdoe",
            yaml_sdoe_sample.replace("name: ATK\n", "name: Elemental Mastery\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Sands of Eon' area from YAML data",
        ),
        pytest.param(
            "gboe",
            yaml_gboe_sample.replace("name: Elemental Mastery\n", "name: ATK %\n").replace(
                "name: Physical DMG Bonus\n", "name: ATK %\n"
            ),
            yaml_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Goblet of Eonothem' area from YAML data",
        ),
        pytest.param(
            "ccol",
            yaml_ccol_sample.replace("name: ATK\n", "name: HP\n").replace(
                "name: Healing Bonus\n", "name: HP\n"
            ),
            yaml_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Circlet of Logos' area from YAML data",
        ),
        pytest.param(
            "fwol",
            json_fwol_sample.replace('"key": "critRate_",\n', '"key": "hp",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Flower of Life' area from JSON data",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample.replace('"key": "def",\n', '"key": "atk",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Plume of Death' area from JSON data",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample.replace('"key": "atk",\n', '"key": "eleMas",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Sands of Eon' area from JSON data",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample.replace('"key": "eleMas",\n', '"key": "atk_",\n').replace(
                '"mainStatKey": "physical_dmg_",\n', '"mainStatKey": "atk_",\n'
            ),
            json_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Goblet of Eonothem' area from JSON data",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample.replace('"key": "atk",\n', '"key": "hp",\n').replace(
                '"mainStatKey": "heal_",\n', '"mainStatKey": "hp",\n'
            ),
            json_type,
            id="face.wind.rule: Loading an artifact with same substat and mainstat into 'Circlet of Logos' area from JSON data",
        ),
    ],
)
def test_arti_load_same(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str, type: str
) -> None:
    """
    Test loading an artifact with same substat and mainstat across five areas from data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "Artifact substat matches main stat." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol",
            id="face.wind.rule: Saving an artifact from 'Flower of Life' area actually as a YAML file",
        ),
        pytest.param(
            "pmod",
            id="face.wind.rule: Saving an artifact from 'Plume of Death' area actually as a YAML file",
        ),
        pytest.param(
            "sdoe",
            id="face.wind.rule: Saving an artifact from 'Sands of Eon' area actually as a YAML file",
        ),
        pytest.param(
            "gboe",
            id="face.wind.rule: Saving an artifact from 'Goblet of Eonothem' area actually as a YAML file",
        ),
        pytest.param(
            "ccol",
            id="face.wind.rule: Saving an artifact from 'Circlet of Logos' area actually as a YAML file",
        ),
    ],
)
def test_arti_save_yaml_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str
) -> None:
    """
    Test saving an artifact across five areas

    :return:
    """
    conf = dict()

    """
    Set the user interface elements as intended
    """
    name = choice([item for item in __artilist__.keys() if item != "None"])
    getattr(runner, f"arti_{area}_type").setCurrentText(name)
    conf["rare"] = choice([item for item in __artilist__[name].rare])
    getattr(runner, f"arti_{area}_rare").setCurrentText(conf["rare"].value.name)
    conf["levl"] = choice([item for item in ArtiLevl if conf["rare"] in item.value.rare])
    getattr(runner, f"arti_{area}_levl").setCurrentText(conf["levl"].value.name)
    conf["stat"] = choice(
        [item for item in getattr(base, f"MainStatType_{area.upper()}") if item.value != STAT.none]
    )
    getattr(runner, f"arti_{area}_name_main").setCurrentText(conf["stat"].value.value)
    for indx in ["a", "b", "c", "d"]:
        getattr(runner, f"arti_{area}_data_{indx}").setText(str(round(uniform(0, 100), 2)))

    """
    Perform the action of saving the artifact information
    """
    extn = ".yaml"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol",
            id="face.wind.rule: Saving an artifact from 'Flower of Life' area actually as a JSON file",
        ),
        pytest.param(
            "pmod",
            id="face.wind.rule: Saving an artifact from 'Plume of Death' area actually as a JSON file",
        ),
        pytest.param(
            "sdoe",
            id="face.wind.rule: Saving an artifact from 'Sands of Eon' area actually as a JSON file",
        ),
        pytest.param(
            "gboe",
            id="face.wind.rule: Saving an artifact from 'Goblet of Eonothem' area actually as a JSON file",
        ),
        pytest.param(
            "ccol",
            id="face.wind.rule: Saving an artifact from 'Circlet of Logos' area actually as a JSON file",
        ),
    ],
)
def test_arti_save_json_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str
) -> None:
    """
    Test saving an artifact across five areas

    :return:
    """
    conf = dict()

    """
    Set the user interface elements as intended
    """
    name = choice([item for item in __artilist__.keys() if item != "None"])
    getattr(runner, f"arti_{area}_type").setCurrentText(name)
    conf["rare"] = choice([item for item in __artilist__[name].rare])
    getattr(runner, f"arti_{area}_rare").setCurrentText(conf["rare"].value.name)
    conf["levl"] = choice([item for item in ArtiLevl if conf["rare"] in item.value.rare])
    getattr(runner, f"arti_{area}_levl").setCurrentText(conf["levl"].value.name)
    conf["stat"] = choice(
        [item for item in getattr(base, f"MainStatType_{area.upper()}") if item.value != STAT.none]
    )
    getattr(runner, f"arti_{area}_name_main").setCurrentText(conf["stat"].value.value)
    for indx in ["a", "b", "c", "d"]:
        getattr(runner, f"arti_{area}_data_{indx}").setText(str(round(uniform(0, 100), 2)))

    """
    Perform the action of saving the artifact information
    """
    extn = ".json"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully saved."


@pytest.mark.parametrize(
    "area, sample",
    [
        pytest.param(
            "fwol",
            yaml_fwol_sample,
            id="face.wind.rule: Loading an artifact from 'Flower of Life' area actually as a YAML file",
        ),
        pytest.param(
            "pmod",
            yaml_pmod_sample,
            id="face.wind.rule: Loading an artifact from 'Plume of Death' area actually as a YAML file",
        ),
        pytest.param(
            "sdoe",
            yaml_sdoe_sample,
            id="face.wind.rule: Loading an artifact from 'Sands of Eon' area actually as a YAML file",
        ),
        pytest.param(
            "gboe",
            yaml_gboe_sample,
            id="face.wind.rule: Loading an artifact from 'Goblet of Eonothem' area actually as a YAML file",
        ),
        pytest.param(
            "ccol",
            yaml_ccol_sample,
            id="face.wind.rule: Loading an artifact from 'Circlet of Logos' area actually as a YAML file",
        ),
    ],
)
def test_arti_load_yaml_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str
) -> None:
    """
    Test loading an artifact across five areas

    :return:
    """

    """
    Perform the action of loading the artifact information
    """
    extn = ".yaml"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, yaml_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)


@pytest.mark.parametrize(
    "area, sample",
    [
        pytest.param(
            "fwol",
            json_fwol_sample,
            id="face.wind.rule: Loading an artifact from 'Flower of Life' area actually as a JSON file",
        ),
        pytest.param(
            "pmod",
            json_pmod_sample,
            id="face.wind.rule: Loading an artifact from 'Plume of Death' area actually as a JSON file",
        ),
        pytest.param(
            "sdoe",
            json_sdoe_sample,
            id="face.wind.rule: Loading an artifact from 'Sands of Eon' area actually as a JSON file",
        ),
        pytest.param(
            "gboe",
            json_gboe_sample,
            id="face.wind.rule: Loading an artifact from 'Goblet of Eonothem' area actually as a JSON file",
        ),
        pytest.param(
            "ccol",
            json_ccol_sample,
            id="face.wind.rule: Loading an artifact from 'Circlet of Logos' area actually as a JSON file",
        ),
    ],
)
def test_arti_load_json_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str, sample: str
) -> None:
    """
    Test loading an artifact across five areas

    :return:
    """

    """
    Perform the action of loading the artifact information
    """
    extn = ".json"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, json_type))
    qtbot.mouseClick(getattr(runner, f"arti_{area}_load"), Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact data has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)


@pytest.mark.parametrize(
    "area",
    [
        pytest.param(
            "fwol",
            id="face.wind.rule: Cancelling the save process for an artifact from 'Flower of Life' area",
        ),
        pytest.param(
            "pmod",
            id="face.wind.rule: Cancelling the save process for an artifact from 'Plume of Death' area",
        ),
        pytest.param(
            "sdoe",
            id="face.wind.rule: Cancelling the save process for an artifact from 'Sands of Eon' area",
        ),
        pytest.param(
            "gboe",
            id="face.wind.rule: Cancelling the save process for an artifact from 'Goblet of Eonothem' area",
        ),
        pytest.param(
            "ccol",
            id="face.wind.rule: Cancelling the save process for an artifact from 'Circlet of Logos' area",
        ),
    ],
)
def test_arti_save_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, area: str) -> None:
    """
    Test cancelling the save process for an artifact in different areas

    :return:
    """

    conf = dict()

    """
    Set the user interface elements as intended
    """
    name = choice([item for item in __artilist__.keys() if item != "None"])
    getattr(runner, f"arti_{area}_type").setCurrentText(name)
    conf["rare"] = choice([item for item in __artilist__[name].rare])
    getattr(runner, f"arti_{area}_rare").setCurrentText(conf["rare"].value.name)
    conf["levl"] = choice([item for item in ArtiLevl if conf["rare"] in item.value.rare])
    getattr(runner, f"arti_{area}_levl").setCurrentText(conf["levl"].value.name)
    conf["stat"] = choice(
        [item for item in getattr(base, f"MainStatType_{area.upper()}") if item.value != STAT.none]
    )
    getattr(runner, f"arti_{area}_name_main").setCurrentText(conf["stat"].value.value)
    for indx in ["a", "b", "c", "d"]:
        getattr(runner, f"arti_{area}_data_{indx}").setText(str(round(uniform(0, 100), 2)))

    """
    Mock file.save to simulate cancellation
    """
    mocker.patch.object(file.FileHandling, "save", return_value=False)

    """
    Perform the action of saving the artifact information
    """
    qtbot.mouseClick(getattr(runner, f"arti_{area}_save"), Qt.LeftButton)

    """
    Confirm that the status message is updated correctly
    """
    assert runner.statarea.currentMessage() == "Ready."
