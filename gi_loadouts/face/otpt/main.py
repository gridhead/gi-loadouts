from PySide6.QtCore import Qt

from gi_loadouts import __versdata__
from gi_loadouts.face.otpt.rule import Rule
from gi_loadouts.type.calc.char import CHAR


class OtptWindow(Rule):
    def __init__(self, char: dict, weap: dict, arti: dict, tyvt: CHAR) -> None:
        super().__init__()
        self.arti = arti
        self.char = char
        self.weap = weap
        self.tyvt = tyvt
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__} - {self.char["char"].name.value}")
        self.setWindowModality(Qt.ApplicationModal)
        self.manage_assets()
        self.populate_header()
        self.populate_blanks()
