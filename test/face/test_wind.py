import pytest
#from PySide6.QtCore import Qt
#from PySide6.QtWidgets import QApplication
from gi_loadouts.face.wind.main import MainWindow


@pytest.fixture
def ruiner(qtbot):
    testwind = MainWindow()
    qtbot.addWidget(testwind)
    testwind.show()
    return testwind


def test_header(ruiner):
    assert ruiner.head_area_line_prim.text() == "Aether"
    # assert ruiner.head_area_line_seco.text() == "Viator"
    # assert ruiner.head_area_line_tert.text() == "Sword"
