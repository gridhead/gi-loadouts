import pytest
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog
from pytest_mock.plugin import MockerFixture
from pytestqt.qtbot import QtBot

from gi_loadouts import __gicompat_part__, __gicompat_vers__, __releases__, __versdata__
from gi_loadouts.face.wind.main import MainWindow


@pytest.mark.parametrize("_", [pytest.param(None, id="face.info: Clicking the help button")])
def test_info(runner: MainWindow, qtbot: QtBot, mocker: MockerFixture, _: None) -> None:
    """
    Test clicking the help button on side of UI

    :return:
    """

    """
    Perform the action of clicking the help button
    """

    def handle_dialog() -> None:
        qtbot.mouseClick(runner.infoobjc.updt, Qt.LeftButton)
        runner.infoobjc.close()

    mock_open_link = mocker.patch.object(QDesktopServices, "openUrl")
    QTimer.singleShot(0, handle_dialog)
    qtbot.mouseClick(runner.side_info, Qt.LeftButton)
    expected_link = QUrl(__releases__)
    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.side_info.toolTip() == "Help"
    assert isinstance(runner.infoobjc, QDialog)
    assert runner.infoobjc.windowTitle() == f"Loadouts for Genshin Impact v{__versdata__}"
    assert runner.infoobjc.vers.text() == f"Version v{__versdata__}"
    assert (
        runner.infoobjc.comp.text()
        == f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}"
    )
    mock_open_link.assert_called_once_with(expected_link)
