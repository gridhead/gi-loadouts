from os import path, remove
from tempfile import NamedTemporaryFile

import pytest
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMessageBox

from gi_loadouts import __donation__, __homepage__, __issutckt__, conf
from gi_loadouts.face.rsrc import make_temp_file
from gi_loadouts.face.wind.main import MainWindow
from test.face.wind import MockQFile


@pytest.mark.parametrize(
    "button, link",
    [
        pytest.param("side_head", __homepage__, id="face.info: Clicking the home button"),
        pytest.param("side_tckt", __issutckt__, id="face.info: Clicking the report button"),
        pytest.param("side_cash", __donation__, id="face.info: Clicking the donate button")
    ]
)
def test_wind_main_buttons(runner, qtbot, mocker, button, link) -> None:
    """
    Attempt clicking the buttons on side of UI

    :return:
    """

    """
    Perform the action of clicking the button
    """
    mock_open_url = mocker.patch.object(QDesktopServices, 'openUrl')
    qtbot.mouseClick(getattr(runner, f"{button}"), Qt.LeftButton)
    expected_url = QUrl(link)

    """
    Confirm if the link is opened
    """
    mock_open_url.assert_called_once_with(expected_url)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.wind: Initialise the training data for Tesseract OCR")
    ]
)
def test_wind_main_fail(mocker, _) -> None:
    """
    Attempt failing initialisation of training data for Tesseract OCR

    :return:
    """

    """
    Mock QFile to return false when open method is called and initiate runner after the mocking
    """
    with NamedTemporaryFile(prefix="gi-loadouts-", suffix=".traineddata", delete=False) as savefile:
        savefile.write(b"")
    mocker.patch("gi_loadouts.face.rsrc.QFile", MockQFile)

    """
    This is not a proper implementation. We will change it with runner fixture
    """
    test_runner = MainWindow()

    """
    Confirm if the user interface elements change accordingly
    """
    assert isinstance(test_runner.dialog, QMessageBox)
    assert test_runner.dialog.icon() == QMessageBox.Information
    assert test_runner.dialog.windowTitle() == "Initialization failed"
    assert "Training data for Tesseract OCR could not be initialized." in test_runner.dialog.text()
    assert test_runner.dialog.isVisible()

    """
    Cleanup the temporary files from temp directory
    """
    if path.exists(savefile.name):
        remove(savefile.name)


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.wind: Remove the already existing training data for Tesseract OCR")
    ]
)
def test_wind_main_fail_continue(runner, mocker, _) -> None:
    """
    Attempt failing removing of training data for Tesseract OCR at startup

    :return:
    """

    """
    Mock remove function in rsrc.py for excepting FileNotFoundError
    """
    mocker.patch("gi_loadouts.face.rsrc.remove", side_effect=FileNotFoundError)
    make_temp_file()


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="face.wind: Manually invoke __del__")
    ]
)
def test_wind_del(runner, _) -> None:
    """
    Attempt manually invoking __del__

    :return:
    """
    """
    pytest-qt does not invoke __del__ automatically. Refer https://github.com/gridhead/gi-loadouts/issues/165
    for more details. Thus manually invoking __del__ for increasing the coverage.
    As per ChatGPT: Test runners like pytest-qt keep strong references to objects for logging,
    reporting, and debugging, which can prevent the automatic invocation of the __del__ method.
    """
    runner.__del__()

    """
    Confirm if the training data for Tesseract OCR is deleted
    """
    assert not path.exists(conf.temppath)
