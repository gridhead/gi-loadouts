from PySide6.QtWidgets import QMainWindow

from gi_loadouts.face.otpt.otpt import Ui_otptwind


class Rule(QMainWindow, Ui_otptwind):
    def __init__(self) -> None:
        super().__init__()
