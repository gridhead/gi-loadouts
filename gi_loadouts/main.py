import os
import sys

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

from gi_loadouts.face import rsrc  # noqa: F401
from gi_loadouts.face.wind.main import MainWindow

"""
Uses absolute imports for PyInstaller compability
"""


def load_custom_font() -> None:
    """
    Register the collection of fonts from the available resources in the user interface

    :return:
    """
    fontlist = [
        ":text/font/text/sans-bold.ttf",
        ":text/font/text/sans-rlar.ttf",
        ":text/font/text/sans-bdit.ttf",
        ":text/font/text/sans-rlit.ttf",
        ":icon/font/icon/icon-bold.ttf",
    ]
    for indx in fontlist:
        QFontDatabase.addApplicationFont(indx)


def main() -> None:  # pragma: no cover
    """
    Initialize the user interface before starting up

    :return:
    """
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    load_custom_font()
    mainobjc = MainWindow()
    mainobjc.show()
    sys.exit(app.exec())


if __name__ == "__main__":  # pragma: no cover
    main()
