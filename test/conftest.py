import pytest

try:
    from pytestqt.qtbot import QtBot

    from gi_loadouts.face.scan.main import ScanDialog
    from gi_loadouts.face.wind.main import MainWindow
    GUI_AVAILABLE = True
except ImportError:
    # GUI components not available in headless environment
    GUI_AVAILABLE = False
    QtBot = None
    ScanDialog = None
    MainWindow = None


@pytest.fixture
def runner(qtbot: QtBot) -> MainWindow:
    """
    Fixture for MainWindow class

    :return: Instance of MainWindow
    """
    if not GUI_AVAILABLE:
        pytest.skip("GUI components not available")
    testwind = MainWindow()
    qtbot.addWidget(testwind)
    return testwind


@pytest.fixture
def scantest(qtbot: QtBot) -> ScanDialog:
    """
    Fixture for ScanDialog class

    :return: Instance of ScanDialog
    """
    if not GUI_AVAILABLE:
        pytest.skip("GUI components not available")
    testscan = ScanDialog("fwol")
    qtbot.addWidget(testscan)
    return testscan
