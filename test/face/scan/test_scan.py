from os import remove
from random import choice, randbytes
from tempfile import NamedTemporaryFile
from uuid import uuid4

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from pytesseract import TesseractError

from gi_loadouts import __versdata__, conf
from gi_loadouts.data.arti import __artilist__
from gi_loadouts.face.rsrc import kill_temp_file, make_temp_file
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
            name, team.rare, team.fwol, "Flower of Life", id=f"face.scan.rule: Configuring Flower of Life artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.pmod, "Plume of Death", id=f"face.scan.rule: Configuring Plume of Death artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.sdoe, "Sands of Eon", id=f"face.scan.rule: Configuring Sands of Eon artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.gboe, "Goblet of Eonothem", id=f"face.scan.rule: Configuring Goblet of Eonothem artifact - {name}"
        ) for name, team in __artilist__.items()
    ] +
    [
        pytest.param(
            name, team.rare, team.ccol, "Circlet of Logos", id=f"face.scan.rule: Configuring Circlet of Logos artifact - {name}"
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
    Create the Tesseract training data
    """
    mocker.patch("gi_loadouts.conf.data_prefix", f"{uuid4().hex.upper()[0:8]}-")
    make_temp_file()

    """
    Perform the action of loading the artifact information
    """
    tempfile = "test/static/img/gi-loadouts-ocr-test.webp"
    savefile = NamedTemporaryFile(prefix="gi-loadouts-ocr-test-", suffix=".webp", delete=False, mode="wb")
    with open(tempfile, "rb") as src_file:
        savefile.write(src_file.read())
    savefile.close()
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile.name, ""))
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
    Cleanup the temporary files from temp directory
    """
    remove(savefile.name)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Cancelling loading an artifact snapshot")
    ]
)
def test_scan_arti_load_nope(scantest, qtbot, mocker, _) -> None:
    """
    Attempt cancelling loading an artifact snapshot

    :return:
    """

    """
    Store the artifact information before trying to load
    """
    init_arti_type = scantest.arti_type.currentText()
    init_arti_levl = scantest.arti_levl.currentText()
    init_arti_rare = scantest.arti_rare.currentText()
    init_arti_type_name = scantest.arti_type_name.text()
    init_arti_name_main = scantest.arti_name_main.currentText()
    init_arti_data_main = scantest.arti_data_main.text()
    init_arti_name_a = scantest.arti_name_a.currentText()
    init_arti_data_a = scantest.arti_data_a.text()
    init_arti_name_b = scantest.arti_name_b.currentText()
    init_arti_data_b = scantest.arti_data_b.text()
    init_arti_name_c = scantest.arti_name_c.currentText()
    init_arti_data_c = scantest.arti_data_c.text()
    init_arti_name_d = scantest.arti_name_d.currentText()
    init_arti_data_d = scantest.arti_data_d.text()

    """
    Perform the action of loading the artifact information
    """
    mocker.patch.object(file.FileHandling, "load_screenshot", return_value=(False, None, None))
    qtbot.mouseClick(scantest.arti_cnvs_load, Qt.LeftButton)

    """
    Confirm if the user interface elements stayed the same
    """
    assert scantest.arti_type.currentText() == init_arti_type
    assert scantest.arti_levl.currentText() == init_arti_levl
    assert scantest.arti_rare.currentText() == init_arti_rare
    assert scantest.arti_type_name.text() == init_arti_type_name
    assert scantest.arti_name_main.currentText() == init_arti_name_main
    assert scantest.arti_data_main.text() == init_arti_data_main
    assert scantest.arti_name_a.currentText() == init_arti_name_a
    assert scantest.arti_data_a.text() == init_arti_data_a
    assert scantest.arti_name_b.currentText() == init_arti_name_b
    assert scantest.arti_data_b.text() == init_arti_data_b
    assert scantest.arti_name_c.currentText() == init_arti_name_c
    assert scantest.arti_data_c.text() == init_arti_data_c
    assert scantest.arti_name_d.currentText() == init_arti_name_d
    assert scantest.arti_data_d.text() == init_arti_data_d


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Failing to load the artifact snapshot")
    ]
)
def test_scan_arti_load_fail(scantest, qtbot, mocker, _) -> None:
    """
    Attempt failing to loading the artifact snapshot

    :return:
    """

    """
    Create a temporary file filled with random data to simulate a failure when trying to open an
    image using PIL.Image.open().
    """
    savefile = NamedTemporaryFile(prefix="gi-loadouts-", suffix=".webp", delete=False, mode="wb")
    savefile.write(randbytes(512*1024))
    savefile.close()

    """
    Perform the action of loading the artifact snapshot
    """
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile.name, ""))
    qtbot.mouseClick(scantest.arti_cnvs_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(scantest.dialog, QMessageBox)
    assert scantest.dialog.icon() == QMessageBox.Information
    assert scantest.dialog.windowTitle() == "Faulty scanning"
    assert "Please select an accurate screenshot." in scantest.dialog.text()
    assert scantest.dialog.isVisible()

    """
    Cleanup the temporary files from temp directory
    """
    remove(savefile.name)


@pytest.mark.parametrize(
    "platform, tempexec",
    [
        pytest.param("Linux", "/usr/bin/tesseract", id="face.scan.rule: Actual loading of Tesseract OCR executable in Linux"),
        pytest.param("Windows", "C:\\Program Files\\Tesseract-OCR\\tesseract.exe", id="face.scan.rule: Actual loading of Tesseract OCR executable in Windows")
    ]
)
def test_scan_tessexec_load(scantest, qtbot, mocker, platform, tempexec) -> None:
    """
    Attempt actual loading of Tesseract OCR executable

    :return:
    """

    """
    Store the initial conf.tessexec so that after this test it can be restored to the original value
    """
    temp = conf.tessexec

    """
    Mock the system environment and reload the tessexec variable to apply the mocked path
    """
    mocker.patch("gi_loadouts.conf.system", return_value=platform)
    conf.tessexec = conf.get_tessexec_path()

    """
    Perform the action of loading the actual Tesseract OCR executable
    """
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(tempexec, ""))
    qtbot.mouseClick(scantest.arti_cnvs_conf, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert conf.tessexec == tempexec

    """
    Reinstate the path for Tesseract OCR executable
    """
    conf.tessexec = temp


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Failing to load the Tesseract OCR executable")
    ]
)
def test_scan_tessexec_load_fail(scantest, qtbot, mocker, _) -> None:
    """
    Attempt failing to load the Tesseract OCR executable

    :return:
    """

    """
    Perform the action of loading the Tesseract OCR executable
    """
    mocker.patch.object(file.FileHandling, "load_tessexec", side_effect=Exception)
    qtbot.mouseClick(scantest.arti_cnvs_conf, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(scantest.dialog, QMessageBox)
    assert scantest.dialog.icon() == QMessageBox.Information
    assert scantest.dialog.windowTitle() == "Faulty scanning"
    assert "Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected." in scantest.dialog.text()
    assert scantest.dialog.isVisible()


@pytest.mark.parametrize(
    "expt",
    [
        pytest.param(OSError, id="face.scan.rule: Failing of register function with OSError"),
        pytest.param(TesseractError("abc", "xyz"), id="face.scan.rule: Failing of register function with TesseractError")
    ]
)
def test_scan_register_fail(scantest, qtbot, mocker, expt) -> None:
    """
    Attempt failing the register function with OSError and TesseractError

    :return:
    """

    """
    Create the tesseract training data
    """
    mocker.patch("gi_loadouts.conf.data_prefix", f"{uuid4().hex.upper()[0:8]}-")
    make_temp_file()

    """
    Perform the action of loading the artifact information
    """
    tempfile = "test/static/img/gi-loadouts-ocr-test.webp"
    savefile = NamedTemporaryFile(prefix="gi-loadouts-ocr-test-", suffix=".webp", delete=False, mode="wb")
    with open(tempfile, "rb") as src_file:
        savefile.write(src_file.read())
    savefile.close()
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile.name, ""))
    mocker.patch("gi_loadouts.face.scan.work.image_to_string", side_effect=expt)
    qtbot.mouseClick(scantest.arti_cnvs_load, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    def check_label():
        """
        Checking the interface elements change asynchronously
        """
        assert isinstance(scantest.dialog, QMessageBox)
        assert scantest.dialog.icon() == QMessageBox.Information
        assert scantest.dialog.windowTitle() == "Faulty scanning"
        if isinstance(expt, OSError):
            assert "Selected executable of Tesseract OCR is unfunctional." in scantest.dialog.text()
        elif isinstance(expt, TesseractError):
            assert "Processing failed as either Tesseract OCR executable ceased to function or training data was tampered with." in scantest.dialog.text()
        assert scantest.dialog.isVisible()

    qtbot.waitUntil(check_label)

    """
    Cleanup the temporary files from temp directory
    """
    kill_temp_file()
    remove(savefile.name)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Clearing Snapshot")
    ]
)
def test_scan_snapshot_wipe(scantest, qtbot, _) -> None:
    """
    Attempt clearing of the snapshot

    :return:
    """

    """
    Perform the action to clear the snapshot
    """
    qtbot.mouseClick(scantest.arti_cnvs_wipe, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    assert scantest.arti_shot.text() == "YOUR ARTIFACT SCREENSHOT WILL SHOW UP HERE"


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.scan.rule: Importing artifact information in MainWindow")
    ]
)
def test_scan_import_arti(scantest, qtbot, mocker, _) -> None:
    """
    Attempt importing artifact information in MainWindow

    :return:
    """

    """
    Create the tesseract training data
    """
    mocker.patch("gi_loadouts.conf.data_prefix", f"{uuid4().hex.upper()[0:8]}-")
    make_temp_file()

    """
    Perform the action of loading the artifact information
    """
    tempfile = "test/static/img/gi-loadouts-ocr-test.webp"
    savefile = NamedTemporaryFile(prefix="gi-loadouts-ocr-test-", suffix=".webp", delete=False, mode="wb")
    with open(tempfile, "rb") as src_file:
        savefile.write(src_file.read())
    savefile.close()
    mocker.patch.object(QFileDialog, "getOpenFileName", return_value=(savefile.name, ""))
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

    """
    Cleanup the temporary files from temp directory
    """
    kill_temp_file()
    remove(savefile.name)
