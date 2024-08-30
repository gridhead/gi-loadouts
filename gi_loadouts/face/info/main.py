from time import time

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from gi_loadouts.face.info.info import Ui_info


class InfoDialog(QDialog, Ui_info):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Loadouts for Genshin Impact")
        self.icon.setPixmap(QPixmap(f":pmon/imgs/pmon/{int(time() % 10)}.png"))
