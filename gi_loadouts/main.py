import os
import sys

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

from gi_loadouts.wind import rsrc  # noqa
from gi_loadouts.wind.main import MainWindow


def load_custom_font():
    fontlist = [
        ":font/font/text/sans-bold.ttf",
        ":font/font/text/sans-rlar.ttf",
        ":font/font/text/sans-bdit.ttf",
        ":font/font/text/sans-rlit.ttf",
        ":icon/font/icon/icon-bold.ttf",
        ":icon/font/icon/icon-rlar.ttf",
    ]
    for indx in fontlist:
        QFontDatabase.addApplicationFont(indx)


def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    load_custom_font()
    mainobjc = MainWindow()
    mainobjc.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
