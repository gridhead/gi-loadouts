from typing import Tuple

from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog


class FileHandling:
    def __init__(self):
        super().__init__()

    def load_screenshot(self, prnt, head: str) -> Tuple[QPixmap, str]:
        """
        Handle file operations involved in loading data from the storage device

        :return: Image that is intended to be read from
        """
        explorer = QFileDialog()
        filepath = explorer.getOpenFileName(prnt, head, "", "All Files (*)")[0]
        if filepath.strip() == "":
            raise FileNotFoundError("No file selected.")
        data = Image.open(filepath)
        qtim = ImageQt.ImageQt(data)
        pxmp = QPixmap.fromImage(qtim)
        return pxmp, filepath

    def load_tessexec(self, prnt, head: str) -> str:
        """
        Handle file operations involved in loading executable from the storage device

        :return: Path to the Tesseract OCR executable
        """
        explorer = QFileDialog()
        filepath = explorer.getOpenFileName(prnt, head, "", "All Files (*);;Executable Files (*.exe)")[0]
        if filepath.strip() == "":
            raise FileNotFoundError("No file selected.")
        return filepath.strip()


file = FileHandling()
