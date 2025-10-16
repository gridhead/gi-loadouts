import pytest
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog
from pytest_mock.plugin import MockerFixture
from pytestqt.qtbot import QtBot

from gi_loadouts import __gicompat_part__, __gicompat_vers__, __releases__, __versdata__
from gi_loadouts.face.wind.main import MainWindow


@pytest.mark.parametrize("_", [pytest.param(None, id="face.info: Clicking the info button")])
def test_info(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test clicking the info button on side of UI

    :return:
    """

    """
    Perform the action of clicking the info button
    """
    qtbot.mouseClick(runner.side_info, Qt.LeftButton)
    mock_open_url = mocker.patch.object(QDesktopServices, "openUrl")
    qtbot.mouseClick(runner.infoobjc.updt, Qt.LeftButton)
    expected_url = QUrl(__releases__)
    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.side_info.toolTip() == "Info"
    assert isinstance(runner.infoobjc, QDialog)
    assert runner.infoobjc.windowTitle() == f"Loadouts for Genshin Impact v{__versdata__}"
    assert runner.infoobjc.vers.text() == f"Version v{__versdata__}"
    assert (
        runner.infoobjc.comp.text()
        == f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}"
    )
    mock_open_url.assert_called_once_with(expected_url)
