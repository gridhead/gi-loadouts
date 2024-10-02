import pytest

from gi_loadouts.face.scan.main import ScanDialog
from gi_loadouts.face.wind.main import MainWindow


@pytest.fixture
def runner(qtbot):
    testwind = MainWindow()
    qtbot.addWidget(testwind)
    return testwind


@pytest.fixture
def scantest(qtbot):
    """
    The codebase will automatically detect the part
    once the artifact is changed manually in the window
    or changed by the after the scan
    """
    testscan = ScanDialog("fwol")
    qtbot.addWidget(testscan)
    return testscan
