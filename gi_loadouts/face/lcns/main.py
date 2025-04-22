from time import time

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

from ... import __gicompat_part__, __gicompat_vers__, __versdata__
from .lcns import Ui_lcns


class LcnsDialog(QDialog, Ui_lcns):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__}")
        self.icon.setPixmap(QPixmap(f":pmon/imgs/pmon/{int(time() % 10)}.webp"))
        self.vers.setText(f"Version v{__versdata__}")
        self.comp.setText(f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}")
