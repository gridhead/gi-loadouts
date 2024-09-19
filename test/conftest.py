import pytest

from gi_loadouts.face.wind.main import MainWindow


@pytest.fixture
def runner(qtbot):
    testwind = MainWindow()
    qtbot.addWidget(testwind)
    return testwind
