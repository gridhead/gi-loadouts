from collections.abc import Generator

import pytest
from PySide6.QtWidgets import QApplication

from gi_loadouts.face.scan.main import ScanDialog
from gi_loadouts.face.wind.main import MainWindow


@pytest.fixture(scope="session")
def runner(qapp: QApplication) -> Generator[MainWindow, None, None]:
    """
    Fixture for MainWindow class

    :return: Instance of MainWindow
    """
    testwind = MainWindow()
    yield testwind
    testwind.close()


@pytest.fixture(scope="session")
def scantest(qapp: QApplication) -> Generator[ScanDialog, None, None]:
    """
    Fixture for ScanDialog class

    :return: Instance of ScanDialog
    """
    testscan = ScanDialog("fwol")
    yield testscan
    testscan.close()
