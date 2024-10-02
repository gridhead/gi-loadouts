import os
from pathlib import Path
from random import choice
from tempfile import gettempdir

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog

from gi_loadouts import __versdata__, conf
from gi_loadouts.data.arti import __artilist__
from gi_loadouts.face.rsrc import make_temp_file
from gi_loadouts.face.scan import file
from gi_loadouts.face.util import truncate_text
from gi_loadouts.type.arti import ArtiLevl, base
from gi_loadouts.type.stat import STAT
from test.face.scan import __dist__, __rtrn__


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan: Testing ScanWindow")
    ]
)
def test_scan_window(scantest, _) -> None:
    """
    Testing ScanWindow

    :return:
    """

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(scantest, QDialog)
    assert scantest.windowTitle() == f"Loadouts for Genshin Impact v{__versdata__}"


@pytest.mark.parametrize(
    "name, rare, part, part_type",
    [
        pytest.param(
            name, team.rare, team.fwol, "Flower of Life", id=f"face.scan.rule: Configuration Flower of Life artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.pmod, "Plume of Death", id=f"face.scan.rule: Configuration Plume of Death artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.sdoe, "Sands of Eon", id=f"face.scan.rule: Configuration Sands of Eon artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.gboe, "Goblet of Eonothem", id=f"face.scan.rule: Configuration Goblet of Eonothem artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.ccol, "Circlet of Logos", id=f"face.scan.rule: Configuration Circlet of Logos artifact - {name}"
        ) for name, team in __artilist__.items()
    ]
)
def test_scan_arti_drop(scantest, name, rare, part, part_type) -> None:
    """
    Test the configuration of artifact on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    conf = dict()

    conf["dist"] = part_type
    scantest.arti_dist.setCurrentText(conf["dist"])
    conf["name"] = name
    scantest.arti_type.setCurrentText(conf["name"])
    conf["rare"] = choice([item for item in rare])
    scantest.arti_rare.setCurrentText(conf["rare"].value.name)
    conf["levl"] = choice([item for item in ArtiLevl if conf["rare"] in item.value.rare])
    scantest.arti_levl.setCurrentText(conf["levl"].value.name)
    conf["stat"] = choice([item for item in getattr(base, __dist__[conf["dist"]]["list"].__name__) if item.value != STAT.none])
    scantest.arti_name_main.setCurrentText(conf["stat"].value.value)
    """
    Confirm if the user interface elements change accordingly
    """
    if name == "None":
        return

    assert scantest.arti_type_name.text() == truncate_text(part.__name__, 34)
    assert scantest.arti_data_main.text() == str(round(part.stat_data, 1))


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Clearing artifact")
    ]
)
def test_scan_arti_wipe(scantest, qtbot, _) -> None:
    """
    Test the clearing of the artifact

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(scantest.arti_back_wipe, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert scantest.arti_type.currentText() == "None"
    assert scantest.arti_levl.currentText() == "None"
    assert scantest.arti_rare.currentText() == "Star 0"
    assert scantest.arti_type_name.text() == "None"
    for item in ["main", "a", "b", "c", "d"]:
        assert getattr(scantest, f"arti_name_{item}").currentText() == "None"
        assert getattr(scantest, f"arti_data_{item}").text() == ""


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Test OCR functionality")
    ]
)
def test_scan_arti_load(scantest, qtbot, mocker, _) -> None:
    """
    Test OCR functionality

    :return:
    """

    """
    Create the tesseract training data
    """
    make_temp_file()

    """
    Perform the action of loading the artifact information
    """
    temp_prm = ""
    tempfile = "test/static/img/gi-loadouts-ocr-test.webp"
    savefile = str(Path(gettempdir()) / "gi-loadouts-ocr-test.webp")
    with open(tempfile, "rb") as src_file:
        with open(savefile, "wb") as dest_file:
            dest_file.write(src_file.read())
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile, temp_prm))
    qtbot.mouseClick(scantest.arti_cnvs_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    def check_label():
        """
        Checking the interface elements change asynchronously
        """
        assert scantest.arti_text.text() == "Browse your local storage to load a high quality screenshot of your artifact and the statistics will automatically be computed from there."
        assert scantest.arti_type.currentText() == "Shimenawa's Reminiscence"
        assert scantest.arti_levl.currentText() == "Level 20"
        assert scantest.arti_rare.currentText() == "Star 5"
        assert scantest.arti_type_name.text() == "Morning Dew's Moment"
        assert scantest.arti_name_main.currentText() == "Energy Recharge"
        assert scantest.arti_data_main.text() == "51.8"
        assert scantest.arti_name_a.currentText() == "Elemental Mastery"
        assert scantest.arti_data_a.text() == "23.0"
        assert scantest.arti_name_b.currentText() == "Crit Rate"
        assert scantest.arti_data_b.text() == "6.6"
        assert scantest.arti_name_c.currentText() == "Crit DMG"
        assert scantest.arti_data_c.text() == "21.0"
        assert scantest.arti_name_d.currentText() == "HP %"
        assert scantest.arti_data_d.text() == "13.4"
    qtbot.waitUntil(check_label)

    """
    Clear the copied file from temp directory
    """
    if os.path.exists(savefile):
        os.remove(savefile)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Test Loading Tesseract OCR executable")
    ]
)
def test_scan_tessexec_load(scantest, qtbot, mocker, _) -> None:
    """
    Test Loading Tesseract OCR executable

    :return:
    """

    """
    Perform the action of loading the Tesseract OCR executable
    """
    tempexec = "tesseract"
    mocker.patch.object(file.FileHandling, "load_tessexec", return_value=(True, tempexec))
    qtbot.mouseClick(scantest.arti_cnvs_conf, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert conf.tessexec == tempexec


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Test importing artifact info in MainWindow")
    ]
)
def test_scan_import_arti(scantest, qtbot, mocker, _) -> None:
    """
    Test importing artifact info in MainWindow

    :return:
    """

    """
    Create the tesseract training data
    """
    make_temp_file()

    """
    Perform the action of loading the artifact information
    """
    temp_prm = ""
    tempfile = "test/static/img/gi-loadouts-ocr-test.webp"
    savefile = str(Path(gettempdir()) / "gi-loadouts-ocr-test.webp")
    with open(tempfile, "rb") as src_file:
        with open(savefile, "wb") as dest_file:
            dest_file.write(src_file.read())
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile, temp_prm))
    qtbot.mouseClick(scantest.arti_cnvs_load, Qt.LeftButton)

    init = scantest.arti_type.currentText()
    qtbot.waitUntil(lambda: scantest.arti_type.currentText() != init)

    """
    Perform the action of importing artifact info in MainWindow
    """
    qtbot.mouseClick(scantest.arti_back_done, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert scantest.keep_info() == __rtrn__
