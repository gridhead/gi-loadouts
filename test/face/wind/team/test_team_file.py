from os import path, remove
from pathlib import Path
from tempfile import NamedTemporaryFile, gettempdir
from uuid import uuid4

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox
from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot

from gi_loadouts.face.wind import file
from gi_loadouts.face.wind.main import MainWindow
from test import json_type, yaml_type

from . import actual, json_sample, yaml_sample


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Saving a 'None' artifact collection")]
)
def test_team_save_none(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test saving a 'None' artifact collection

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(runner.head_wipe, Qt.LeftButton)

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Saving an artifact collection")]
)
def test_team_save_name(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test saving an artifact across five areas

    :return:
    """

    """
    Set the user interface elements as intended
    """
    for area, data in actual.items():
        getattr(runner, f"arti_{area}_type").setCurrentText(data["type"])
        getattr(runner, f"arti_{area}_rare").setCurrentText(data["rare"])
        getattr(runner, f"arti_{area}_levl").setCurrentText(data["levl"])
        getattr(runner, f"arti_{area}_name_main").setCurrentText(data["main"])
        for item, stat in data["stat"].items():
            getattr(runner, f"arti_{area}_name_{item}").setCurrentText(stat["name"])
            getattr(runner, f"arti_{area}_data_{item}").setText(str(stat["data"]))

    """
    Perform the action of saving the artifact collection information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Failing to save the artifact collection")]
)
def test_team_save_fail(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test failing to save an artifact collection due to empty data fields

    :return:
    """

    """
    Perform the action of saving the artifact collection information
    """
    mocker.patch.object(file.FileHandling, "save", return_value=True)
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Save failed"
    assert (
        "Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact set in a location that is accessible."
        in runner.dialog.text()
    )
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Loading the artifact collection from YAML data")]
)
def test_team_load_yaml(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test loading an artifact collection from YAML data

    :return:
    """

    """
    Perform the action of loading the artifact collection information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, yaml_sample, yaml_type))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area, data in actual.items():
        assert getattr(runner, f"arti_{area}_type").currentText() == data["type"]
        assert getattr(runner, f"arti_{area}_rare").currentText() == data["rare"]
        assert getattr(runner, f"arti_{area}_levl").currentText() == data["levl"]
        assert getattr(runner, f"arti_{area}_name_main").currentText() == data["main"]
        for item, stat in data["stat"].items():
            assert getattr(runner, f"arti_{area}_name_{item}").currentText() == stat["name"]
            assert getattr(runner, f"arti_{area}_data_{item}").text() == str(stat["data"])

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully loaded."


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Loading the artifact collection from JSON data")]
)
def test_team_load_json(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test loading an artifact collection from JSON data

    :return:
    """

    """
    Perform the action of loading the artifact collection information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, json_sample, json_type))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area, data in actual.items():
        assert getattr(runner, f"arti_{area}_type").currentText() == data["type"]
        assert getattr(runner, f"arti_{area}_rare").currentText() == data["rare"]
        assert getattr(runner, f"arti_{area}_levl").currentText() == data["levl"]
        assert getattr(runner, f"arti_{area}_name_main").currentText() == data["main"]
        for item, stat in data["stat"].items():
            assert getattr(runner, f"arti_{area}_name_{item}").currentText() == stat["name"]
            assert getattr(runner, f"arti_{area}_data_{item}").text() == str(stat["data"])

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully loaded."


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Cancelling loading the artifact collection")]
)
def test_team_load_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test cancelling loading an artifact collection

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(False, "", ""))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area in actual.keys():
        assert (
            getattr(runner, f"arti_{area}_type").currentText() == "A Day Carved From Rising Winds"
        )
        assert getattr(runner, f"arti_{area}_rare").currentText() == "Star 4"
        assert getattr(runner, f"arti_{area}_levl").currentText() == "Level 00"


@pytest.mark.parametrize(
    "_",
    [pytest.param(None, id="face.wind.rule: Loading the artifact collection from an empty file")],
)
def test_team_load_void(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test loading an artifact collection from an empty file

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, "", ""))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact set follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "Selected file cannot be read." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "sample, type",
    [
        pytest.param(
            yaml_sample.replace("fwol", "AWRY")
            .replace("pmod", "AWRY")
            .replace("sdoe", "AWRY")
            .replace("gboe", "AWRY")
            .replace("ccol", "AWRY"),
            "YAML Files (*.yaml)",
            id="face.wind.rule: Loading the artifact collection with incorrect areas from YAML data",
        ),
        pytest.param(
            json_sample.replace("flower", "AWRY")
            .replace("plume", "AWRY")
            .replace("sands", "AWRY")
            .replace("goblet", "AWRY")
            .replace("circlet", "AWRY"),
            "GOOD Files (*.json)",
            id="face.wind.rule: Loading the artifact collection with incorrect areas from JSON data",
        ),
    ],
)
def test_team_load_awry(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, sample: str, type: str
) -> None:
    """
    Test loading an artifact collection with incorrect areas from data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact set follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "Artifact set data cannot be parsed." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "sample, type",
    [
        pytest.param(
            yaml_sample.replace("name: Crit Rate\n", "name: Foo Bar\n")
            .replace("name: DEF\n", "name: Foo Bar\n")
            .replace("name: ATK\n", "name: Foo Bar\n")
            .replace("name: Elemental Mastery\n", "name: Foo Bar\n")
            .replace("name: ATK\n", "name: Foo Bar\n"),
            yaml_type,
            id="face.wind.rule: Loading an artifact with incorrect substats from YAML data",
        ),
        pytest.param(
            json_sample.replace('"key": "critRate_",\n', '"key": "foobar",\n')
            .replace('"key": "def",\n', '"key": "foobar",\n')
            .replace('"key": "atk",\n', '"key": "foobar",\n')
            .replace('"key": "eleMas",\n', '"key": "foobar",\n')
            .replace('"key": "atk",\n', '"key": "foobar",\n'),
            json_type,
            id="face.wind.rule: Loading an artifact with incorrect substats from JSON data",
        ),
    ],
)
def test_team_load_name(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, sample: str, type: str
) -> None:
    """
    Test loading an artifact collection with incorrect substats from data

    :return:
    """

    """
    Perform the action of saving the artifact information
    """
    mocker.patch.object(file.FileHandling, "load", return_value=(True, sample, type))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(runner.dialog, QMessageBox)
    assert runner.dialog.icon() == QMessageBox.Information
    assert runner.dialog.windowTitle() == "Load failed"
    assert (
        "Please confirm that the artifact set follows the valid format before loading it from a location that is accessible."
        in runner.dialog.text()
    )
    assert "Artifact set data cannot be parsed." in runner.dialog.text()
    assert runner.dialog.isVisible()


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Saving an artifact collection as a YAML file")]
)
def test_team_save_yaml_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None
) -> None:
    """
    Test saving an artifact across five areas as a YAML file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    for area, data in actual.items():
        getattr(runner, f"arti_{area}_type").setCurrentText(data["type"])
        getattr(runner, f"arti_{area}_rare").setCurrentText(data["rare"])
        getattr(runner, f"arti_{area}_levl").setCurrentText(data["levl"])
        getattr(runner, f"arti_{area}_name_main").setCurrentText(data["main"])
        for item, stat in data["stat"].items():
            getattr(runner, f"arti_{area}_name_{item}").setCurrentText(stat["name"])
            getattr(runner, f"arti_{area}_data_{item}").setText(str(stat["data"]))

    """
    Perform the action of saving the artifact information
    """
    extn = ".yaml"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, yaml_type))
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."


@pytest.mark.parametrize(
    "_", [pytest.param(None, id="face.wind.rule: Saving an artifact collection as a JSON file")]
)
def test_team_save_json_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None
) -> None:
    """
    Test saving an artifact across five areas as a JSON file

    :return:
    """

    """
    Set the user interface elements as intended
    """
    for area, data in actual.items():
        getattr(runner, f"arti_{area}_type").setCurrentText(data["type"])
        getattr(runner, f"arti_{area}_rare").setCurrentText(data["rare"])
        getattr(runner, f"arti_{area}_levl").setCurrentText(data["levl"])
        getattr(runner, f"arti_{area}_name_main").setCurrentText(data["main"])
        for item, stat in data["stat"].items():
            getattr(runner, f"arti_{area}_name_{item}").setCurrentText(stat["name"])
            getattr(runner, f"arti_{area}_data_{item}").setText(str(stat["data"]))

    """
    Perform the action of saving the artifact information
    """
    extn = ".json"

    """
    Without extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper())
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)
    if path.exists(temp + extn):
        remove(temp + extn)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."

    """
    With extension
    """
    temp = str(Path(gettempdir()) / uuid4().hex[0:8].upper()) + extn
    mocker.patch.object(QFileDialog, "getSaveFileName", return_value=(temp, json_type))
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)
    if path.exists(temp):
        remove(temp)

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully saved."


@pytest.mark.parametrize(
    "sample",
    [
        pytest.param(
            yaml_sample, id="face.wind.rule: Loading the actual artifact collection from YAML data"
        )
    ],
)
def test_team_load_yaml_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, sample: str
) -> None:
    """
    Test loading an artifact collection from YAML data

    :return:
    """

    """
    Perform the action of loading the artifact collection information
    """
    extn = ".yaml"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, yaml_type))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area, data in actual.items():
        assert getattr(runner, f"arti_{area}_type").currentText() == data["type"]
        assert getattr(runner, f"arti_{area}_rare").currentText() == data["rare"]
        assert getattr(runner, f"arti_{area}_levl").currentText() == data["levl"]
        assert getattr(runner, f"arti_{area}_name_main").currentText() == data["main"]
        for item, stat in data["stat"].items():
            assert getattr(runner, f"arti_{area}_name_{item}").currentText() == stat["name"]
            assert getattr(runner, f"arti_{area}_data_{item}").text() == str(stat["data"])

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)


@pytest.mark.parametrize(
    "sample",
    [
        pytest.param(
            json_sample, id="face.wind.rule: Loading the actual artifact collection from JSON data"
        )
    ],
)
def test_team_load_json_actual(
    runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, sample: str
) -> None:
    """
    Test loading an artifact collection from JSON data

    :return:
    """

    """
    Perform the action of loading the artifact collection information
    """
    extn = ".json"
    temp = NamedTemporaryFile(prefix="gi-loadouts-", suffix=extn, delete=False, mode="w")
    temp.write(sample)
    temp.close()

    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(temp.name, json_sample))
    qtbot.mouseClick(runner.head_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area, data in actual.items():
        assert getattr(runner, f"arti_{area}_type").currentText() == data["type"]
        assert getattr(runner, f"arti_{area}_rare").currentText() == data["rare"]
        assert getattr(runner, f"arti_{area}_levl").currentText() == data["levl"]
        assert getattr(runner, f"arti_{area}_name_main").currentText() == data["main"]
        for item, stat in data["stat"].items():
            assert getattr(runner, f"arti_{area}_name_{item}").currentText() == stat["name"]
            assert getattr(runner, f"arti_{area}_data_{item}").text() == str(stat["data"])

    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.statarea.currentMessage() == "Artifact set has been successfully loaded."

    """
    Cleanup the temporary files
    """
    remove(temp.name)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(
            None, id="face.wind.rule: Cancelling the save process for an artifact collection"
        )
    ],
)
def test_team_save_nope(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test cancelling the save process for an artifact collection

    :return:
    """

    """
    Set the user interface elements as intended
    """
    for area, data in actual.items():
        getattr(runner, f"arti_{area}_type").setCurrentText(data["type"])
        getattr(runner, f"arti_{area}_rare").setCurrentText(data["rare"])
        getattr(runner, f"arti_{area}_levl").setCurrentText(data["levl"])
        getattr(runner, f"arti_{area}_name_main").setCurrentText(data["main"])
        for item, stat in data["stat"].items():
            getattr(runner, f"arti_{area}_name_{item}").setCurrentText(stat["name"])
            getattr(runner, f"arti_{area}_data_{item}").setText(str(stat["data"]))

    """
    Mock file.save to simulate cancellation
    """
    mocker.patch.object(file.FileHandling, "save", return_value=False)

    """
    Perform the action of saving the artifact collection information
    """
    qtbot.mouseClick(runner.head_save, Qt.LeftButton)

    """
    Confirm that the status message remains unchanged
    """
    assert runner.statarea.currentMessage() == "Ready."
