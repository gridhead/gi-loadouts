from os import path, remove
from pathlib import Path
from random import choice
from tempfile import NamedTemporaryFile, gettempdir
from uuid import uuid4

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot

from gi_loadouts.data.weap import Family
from gi_loadouts.face.wind import file
from gi_loadouts.face.wind.main import MainWindow
from test import json_type, yaml_type

from . import (
    actual_bow,
    actual_catalyst,
    actual_claymore,
    actual_polearm,
    actual_sword,
    json_bow_sample,
    json_catalyst_sample,
    json_claymore_sample,
    json_polearm_sample,
    json_sword_sample,
    yaml_bow_sample,
    yaml_catalyst_sample,
    yaml_claymore_sample,
    yaml_polearm_sample,
    yaml_sword_sample,
)


@pytest.mark.parametrize(
    "type, char",
    [
        pytest.param("Bow", "Venti", id="face.wind.rule: Saving a random weapon of bow type"),
        pytest.param("Catalyst", "Nahida", id="face.wind.rule: Saving a random weapon of catalyst type"),
        pytest.param("Claymore", "Navia", id="face.wind.rule: Saving a random weapon of claymore type"),
        pytest.param("Polearm", "Raiden Shogun", id="face.wind.rule: Saving a random weapon of polearm type"),
        pytest.param("Sword", "Furina", id="face.wind.rule: Saving a random weapon of sword type"),
    ]
)
def test_weap_save(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, type: str, char: str) -> None:
    """
    Test saving a random weapon of a certain type

    :return:
    """

    """
    Set the user interface elements as intended
    """
    name = choice(list(Family[type].keys()))
    objc = Family[type][name]()
    levl = choice(objc.levl_bind).value.name

    runner.head_char_name.setCurrentText(char)
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText() == type
    assert runner.statarea.currentMessage() == "Weapon data has been successfully saved."


@pytest.mark.parametrize(
    "type, char",
    [
        pytest.param("Bow", "Venti", id="face.wind.rule: Failing to save a random weapon of bow type"),
        pytest.param("Catalyst", "Nahida", id="face.wind.rule: Failing to save a random weapon of catalyst type"),
        pytest.param("Claymore", "Navia", id="face.wind.rule: Failing to save a random weapon of claymore type"),
        pytest.param("Polearm", "Raiden Shogun", id="face.wind.rule: Failing to save a random weapon of polearm type"),
        pytest.param("Sword", "Furina", id="face.wind.rule: Failing to save a random weapon of sword type"),
    ]
)
def test_weap_save_fail(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, type: str, char: str) -> None:
    """
    Test failing to save a random weapon of a certain type

    :return:
    """

    """
    Set the user interface elements as intended
    """
    name = choice(list(Family[type].keys()))
    objc = Family[type][name]()
    levl = choice(objc.levl_bind).value.name

    runner.head_char_name.setCurrentText(char)
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "save", side_effect=ValueError("Mocked mismatch."))
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText() == type
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Save failed"
    assert "Please confirm that the location that is accessible before saving the weapon data." in runner.dialog.text()
    assert "Mocked mismatch." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "char, sample, data",
    [
        pytest.param("Venti", yaml_bow_sample, actual_bow, id="face.wind.rule: Loading a weapon of bow type from YAML data"),
        pytest.param("Nahida", yaml_catalyst_sample, actual_catalyst, id="face.wind.rule: Loading a weapon of catalyst type from YAML data"),
        pytest.param("Navia", yaml_claymore_sample, actual_claymore, id="face.wind.rule: Loading a weapon of claymore type from YAML data"),
        pytest.param("Raiden Shogun", yaml_polearm_sample, actual_polearm, id="face.wind.rule: Loading a weapon of polearm type from YAML data"),
        pytest.param("Furina", yaml_sword_sample, actual_sword, id="face.wind.rule: Loading a weapon of sword type from YAML data"),
    ]
)
def test_weap_load_yaml(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, data: dict) -> None:
    """
    Test loading a weapon of a certain type from YAML data

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, yaml_type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText() == data["type"]
    assert runner.weap_area_name.currentText() == data["name"]
    assert runner.weap_area_refn.currentText() == data["refn"]
    assert runner.weap_area_levl.currentText() == data["levl"]


@pytest.mark.parametrize(
    "char, sample, data",
    [
        pytest.param("Venti", json_bow_sample, actual_bow, id="face.wind.rule: Loading a weapon of bow type from JSON data"),
        pytest.param("Nahida", json_catalyst_sample, actual_catalyst, id="face.wind.rule: Loading a weapon of catalyst type from JSON data"),
        pytest.param("Navia", json_claymore_sample, actual_claymore, id="face.wind.rule: Loading a weapon of claymore type from JSON data"),
        pytest.param("Raiden Shogun", json_polearm_sample, actual_polearm, id="face.wind.rule: Loading a weapon of polearm type from JSON data"),
        pytest.param("Furina", json_sword_sample, actual_sword, id="face.wind.rule: Loading a weapon of sword type from JSON data"),
    ]
)
def test_weap_load_json(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, data: dict) -> None:
    """
    Test loading a weapon of a certain type from JSON data

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, json_type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_type.currentText() == data["type"]
    assert runner.weap_area_name.currentText() == data["name"]
    assert runner.weap_area_refn.currentText() == data["refn"]
    assert runner.weap_area_levl.currentText() == data["levl"]


@pytest.mark.parametrize(
    "char, name",
    [
        pytest.param("Venti", "Alley Hunter", id="face.wind.rule: Cancelling loading a weapon of bow type from YAML data"),
        pytest.param("Nahida", "Apprentice's Notes", id="face.wind.rule: Cancelling loading a weapon of catalyst type from YAML data"),
        pytest.param("Navia", "Akuoumaru", id="face.wind.rule: Cancelling loading a weapon of claymore type from YAML data"),
        pytest.param("Raiden Shogun", "Ballad of the Fjords", id="face.wind.rule: Cancelling loading a weapon of polearm type from YAML data"),
        pytest.param("Furina", "Absolution", id="face.wind.rule: Cancelling loading a weapon of sword type from YAML data"),
    ]
)
def test_weap_load_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, name: str) -> None:
    """
    Test cancelling loading a weapon of a certain type

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(False, "", ""))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.weap_area_name.currentText() == name


@pytest.mark.parametrize(
    "char",
    [
        pytest.param("Venti", id="face.wind.rule: Loading a weapon of bow type from an empty file"),
        pytest.param("Nahida", id="face.wind.rule: Loading a weapon of catalyst type from an empty file"),
        pytest.param("Navia", id="face.wind.rule: Loading a weapon of claymore type from an empty file"),
        pytest.param("Raiden Shogun", id="face.wind.rule: Loading a weapon of polearm type from an empty file"),
        pytest.param("Furina", id="face.wind.rule: Loading a weapon of sword type from an empty file"),
    ]
)
def test_team_load_void(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str) -> None:
    """
    Test loading a weapon of a certain type from an empty file

    :return:
    """

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, "", ""))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert "Please confirm that the location that is accessible before loading the weapon data." in runner.dialog.text()
    assert "Selected file cannot be read." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "char, sample, type",
    [
        pytest.param("Nahida", yaml_bow_sample, yaml_type, id="face.wind.rule: Failing to load a weapon of bow type from YAML data due to type mismatch"),
        pytest.param("Navia", yaml_catalyst_sample, yaml_type, id="face.wind.rule: Failing to load a weapon of catalyst type from YAML data due to type mismatch"),
        pytest.param("Raiden Shogun", yaml_claymore_sample, yaml_type, id="face.wind.rule: Failing to load a weapon of claymore type from YAML data due to type mismatch"),
        pytest.param("Furina", yaml_polearm_sample, yaml_type, id="face.wind.rule: Failing to load a weapon of polearm type from YAML data due to type mismatch"),
        pytest.param("Venti", yaml_sword_sample, yaml_type, id="face.wind.rule: Failing to load a weapon of sword type from YAML data due to type mismatch"),
        pytest.param("Nahida", json_bow_sample, json_type, id="face.wind.rule: Failing to load a weapon of bow type from JSON data due to type mismatch"),
        pytest.param("Navia", json_catalyst_sample, json_type, id="face.wind.rule: Failing to load a weapon of catalyst type from JSON data due to type mismatch"),
        pytest.param("Raiden Shogun", json_claymore_sample, json_type, id="face.wind.rule: Failing to load a weapon of claymore type from JSON data due to type mismatch"),
        pytest.param("Furina", json_polearm_sample, json_type, id="face.wind.rule: Failing to load a weapon of polearm type from JSON data due to type mismatch"),
        pytest.param("Venti", json_sword_sample, json_type, id="face.wind.rule: Failing to load a weapon of sword type from JSON data due to type mismatch"),
    ]
)
def test_weap_load_fail_type(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, type: str) -> None:
    """
    Test failing to load a weapon of a certain type from data due to type mismatch

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert "Please confirm that the location that is accessible before loading the weapon data." in runner.dialog.text()
    assert "Weapon type cannot be identified." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "char, sample, type, data",
    [
        pytest.param("Venti", yaml_bow_sample, yaml_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from YAML data due to incorrect name"),
        pytest.param("Nahida", yaml_catalyst_sample, yaml_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from YAML data due to incorrect name"),
        pytest.param("Navia", yaml_claymore_sample, yaml_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from YAML data due to incorrect name"),
        pytest.param("Raiden Shogun", yaml_polearm_sample, yaml_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from YAML data due to incorrect name"),
        pytest.param("Furina", yaml_sword_sample, yaml_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from YAML data due to incorrect name"),
        pytest.param("Venti", json_bow_sample, json_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from JSON data due to incorrect name"),
        pytest.param("Nahida", json_catalyst_sample, json_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from JSON data due to incorrect name"),
        pytest.param("Navia", json_claymore_sample, json_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from JSON data due to incorrect name"),
        pytest.param("Raiden Shogun", json_polearm_sample, json_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from JSON data due to incorrect name"),
        pytest.param("Furina", json_sword_sample, json_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from JSON data due to incorrect name"),
    ]
)
def test_weap_load_fail_name(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, type: str, data: dict) -> None:
    """
    Test failing to load a weapon of a certain type from data due to incorrect name

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    if type == yaml_type:
        name = data["name"]
    else:
        name = "".join([word.title() for word in data["name"].replace("'", "").replace("\"", "").replace("-", " ").split(" ")])

    sample = sample.replace(name, "AWRY")
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert "Please confirm that the location that is accessible before loading the weapon data." in runner.dialog.text()
    assert runner.dialog.isVisible()
    if type == yaml_type:
        assert "Weapon name cannot be identified." in runner.dialog.text()
    else:
        assert "Weapon data cannot be parsed." in runner.dialog.text()


@pytest.mark.parametrize(
    "char, sample, type, data",
    [
        pytest.param("Venti", yaml_bow_sample, yaml_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from YAML data due to incorrect level"),
        pytest.param("Nahida", yaml_catalyst_sample, yaml_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from YAML data due to incorrect level"),
        pytest.param("Navia", yaml_claymore_sample, yaml_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from YAML data due to incorrect level"),
        pytest.param("Raiden Shogun", yaml_polearm_sample, yaml_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from YAML data due to incorrect level"),
        pytest.param("Furina", yaml_sword_sample, yaml_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from YAML data due to incorrect level"),
        pytest.param("Venti", json_bow_sample, json_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from JSON data due to incorrect level"),
        pytest.param("Nahida", json_catalyst_sample, json_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from JSON data due to incorrect level"),
        pytest.param("Navia", json_claymore_sample, json_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from JSON data due to incorrect level"),
        pytest.param("Raiden Shogun", json_polearm_sample, json_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from JSON data due to incorrect level"),
        pytest.param("Furina", json_sword_sample, json_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from JSON data due to incorrect level"),
    ]
)
def test_weap_load_fail_levl(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, type: str, data: dict) -> None:
    """
    Test failing to load a weapon of a certain type from data due to incorrect level

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    sample = sample.replace("80", "100")
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert "Please confirm that the location that is accessible before loading the weapon data." in runner.dialog.text()
    assert "Weapon data cannot be parsed." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "char, sample, type, data",
    [
        pytest.param("Venti", yaml_bow_sample, yaml_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from YAML data due to incorrect refinement"),
        pytest.param("Nahida", yaml_catalyst_sample, yaml_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from YAML data due to incorrect refinement"),
        pytest.param("Navia", yaml_claymore_sample, yaml_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from YAML data due to incorrect refinement"),
        pytest.param("Raiden Shogun", yaml_polearm_sample, yaml_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from YAML data due to incorrect refinement"),
        pytest.param("Furina", yaml_sword_sample, yaml_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from YAML data due to incorrect refinement"),
        pytest.param("Venti", json_bow_sample, json_type, actual_bow, id="face.wind.rule: Failing to load a weapon of bow type from JSON data due to incorrect refinement"),
        pytest.param("Nahida", json_catalyst_sample, json_type, actual_catalyst, id="face.wind.rule: Failing to load a weapon of catalyst type from JSON data due to incorrect refinement"),
        pytest.param("Navia", json_claymore_sample, json_type, actual_claymore, id="face.wind.rule: Failing to load a weapon of claymore type from JSON data due to incorrect refinement"),
        pytest.param("Raiden Shogun", json_polearm_sample, json_type, actual_polearm, id="face.wind.rule: Failing to load a weapon of polearm type from JSON data due to incorrect refinement"),
        pytest.param("Furina", json_sword_sample, json_type, actual_sword, id="face.wind.rule: Failing to load a weapon of sword type from JSON data due to incorrect refinement"),
    ]
)
def test_weap_load_fail_refn(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str, type: str, data: dict) -> None:
    """
    Test failing to load a weapon of a certain type from data due to incorrect refinement

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of saving the weapon information
    """
    if type == yaml_type:
        sample = sample.replace("refn: Refinement 5", "refn: Refinement 0")
    else:
        sample = sample.replace("\"refinement\": 5,", "\"refinement\": 0,")
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert "Please confirm that the location that is accessible before loading the weapon data." in runner.dialog.text()
    assert "Weapon refinement cannot be parsed." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "type, char",
    [
        pytest.param("Bow", "Venti", id="face.wind.rule: Saving a random weapon of bow type actually as a YAML file"),
        pytest.param("Catalyst", "Nahida", id="face.wind.rule: Saving a random weapon of catalyst type actually as a YAML file"),
        pytest.param("Claymore", "Navia", id="face.wind.rule: Saving a random weapon of claymore type actually as a YAML file"),
        pytest.param("Polearm", "Raiden Shogun", id="face.wind.rule: Saving a random weapon of polearm type actually as a YAML file"),
        pytest.param("Sword", "Furina", id="face.wind.rule: Saving a random weapon of sword type actually as a YAML file"),
    ]
)
def test_weap_save_yaml_actual(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, type: str, char: str) -> None:
    """
    Test saving a random weapon of a certain type as a YAML file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    name = choice(list(Family[type].keys()))
    objc = Family[type][name]()
    levl = choice(objc.levl_bind).value.name

    runner.head_char_name.setCurrentText(char)
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)

    """
    Perform the action of saving the weapon information
    """
    extn = ".yaml"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully saved."


@pytest.mark.parametrize(
    "type, char",
    [
        pytest.param("Bow", "Venti", id="face.wind.rule: Saving a random weapon of bow type actually as a JSON file"),
        pytest.param("Catalyst", "Nahida", id="face.wind.rule: Saving a random weapon of catalyst type actually as a JSON file"),
        pytest.param("Claymore", "Navia", id="face.wind.rule: Saving a random weapon of claymore type actually as a JSON file"),
        pytest.param("Polearm", "Raiden Shogun", id="face.wind.rule: Saving a random weapon of polearm type actually as a JSON file"),
        pytest.param("Sword", "Furina", id="face.wind.rule: Saving a random weapon of sword type actually as a JSON file"),
    ]
)
def test_weap_save_json_actual(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, type: str, char: str) -> None:
    """
    Test saving a random weapon of a certain type as a JSON file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    name = choice(list(Family[type].keys()))
    objc = Family[type][name]()
    levl = choice(objc.levl_bind).value.name

    runner.head_char_name.setCurrentText(char)
    runner.weap_area_name.setCurrentText(name)
    runner.weap_area_levl.setCurrentText(levl)
    """
    Perform the action of saving the weapon information
    """
    extn = ".json"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully saved."


@pytest.mark.parametrize(
    "char",
    [
        pytest.param("Venti", id="face.wind.rule: Cancelling saving a weapon of bow type"),
        pytest.param("Nahida", id="face.wind.rule: Cancelling saving a weapon of catalyst type"),
        pytest.param("Navia", id="face.wind.rule: Cancelling saving a weapon of claymore type"),
        pytest.param("Raiden Shogun", id="face.wind.rule: Cancelling saving a weapon of polearm type"),
        pytest.param("Furina", id="face.wind.rule: Cancelling saving a weapon of sword type"),
    ]
)
def test_weap_save_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str) -> None:
    """
    Test cancelling the save process for a weapon of a certain type

    :return:
    """

    """
    Set the user interface elements as intended
    """

    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of cancellation of saving the weapon information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=False)
    qtbot.mouseClick(runner.weap_head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Ready."


@pytest.mark.parametrize(
    "char, sample",
    [
        pytest.param("Venti", yaml_bow_sample, id="face.wind.rule: Loading a weapon of bow type actually from YAML file"),
        pytest.param("Nahida", yaml_catalyst_sample, id="face.wind.rule: Loading a weapon of catalyst type actually from YAML file"),
        pytest.param("Navia", yaml_claymore_sample, id="face.wind.rule: Loading a weapon of claymore type actually from YAML file"),
        pytest.param("Raiden Shogun", yaml_polearm_sample, id="face.wind.rule: Loading a weapon of polearm type actually from YAML file"),
        pytest.param("Furina", yaml_sword_sample, id="face.wind.rule: Loading a weapon of sword type actually from YAML file"),
    ]
)
def test_weap_load_yaml_actual(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str) -> None:
    """
    Test loading a weapon of a certain type from YAML file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of loading the weapon information
    """
    extn = ".yaml"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, yaml_type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)


@pytest.mark.parametrize(
    "char, sample",
    [
        pytest.param("Venti", json_bow_sample, id="face.wind.rule: Loading a weapon of bow type actually from JSON file"),
        pytest.param("Nahida", json_catalyst_sample, id="face.wind.rule: Loading a weapon of catalyst type actually from JSON file"),
        pytest.param("Navia", json_claymore_sample, id="face.wind.rule: Loading a weapon of claymore type actually from JSON file"),
        pytest.param("Raiden Shogun", json_polearm_sample, id="face.wind.rule: Loading a weapon of polearm type actually from JSON file"),
        pytest.param("Furina", json_sword_sample, id="face.wind.rule: Loading a weapon of sword type actually from JSON file"),
    ]
)
def test_weap_load_json_actual(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, char: str, sample: str) -> None:
    """
    Test loading a weapon of a certain type from JSON file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    runner.head_char_name.setCurrentText(char)

    """
    Perform the action of loading the weapon information
    """
    extn = ".json"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, json_type))
    qtbot.mouseClick(runner.weap_head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Weapon data has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)
