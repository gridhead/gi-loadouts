from time import time

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QDialog

from ... import __gicompat_part__, __gicompat_vers__, __releases__, __versdata__
from .info import Ui_info


class InfoDialog(QDialog, Ui_info):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__}")
        self.icon.setPixmap(QPixmap(f":pmon/imgs/pmon/{int(time() % 10)}.webp"))
        self.vers.setText(f"Version v{__versdata__}")
        self.comp.setText(f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}")
        self.updt.clicked.connect(self.open_update_link)

    def open_update_link(self):
        QDesktopServices.openUrl(QUrl(__releases__))
