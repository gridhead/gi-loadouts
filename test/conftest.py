import pytest
from pytestqt.qtbot import QtBot

from gi_loadouts.face.scan.main import ScanDialog
from gi_loadouts.face.wind.main import MainWindow


@pytest.fixture
def runner(qtbot: QtBot) -> MainWindow:
    """
    Fixture for MainWindow class

    :return: Instance of MainWindow
    """
    testwind = MainWindow()
    qtbot.addWidget(testwind)
    return testwind


@pytest.fixture
def scantest(qtbot: QtBot) -> ScanDialog:
    """
    Fixture for ScanDialog class

    :return: Instance of ScanDialog
    """
    testscan = ScanDialog("fwol")
    qtbot.addWidget(testscan)
    return testscan
