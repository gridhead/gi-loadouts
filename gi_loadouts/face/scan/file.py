from PIL import Image, ImageFile, ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog


class FileHandling:
    def __init__(self):
        super().__init__()

    def load_mask_from_file(self, path: str) -> tuple[QPixmap, ImageFile]:
        """
        Handle file operations involved in loading data from the storage device
        Backend

        :return: Image that is intended to be read from
        """
        pxmp, data = None, None
        if path.strip() != "":
            data = Image.open(path)
            qtim = ImageQt.ImageQt(data)
            pxmp = QPixmap.fromImage(qtim)
        return pxmp, data

    def load_screenshot_with_picker(self, prnt, head: str) -> tuple[bool, QPixmap, ImageFile]:
        """
        Handle file operations involved in loading data from the storage device
        Frontend

        :return: Image that is intended to be read from
        """
        explorer = QFileDialog()
        filepath = explorer.getOpenFileName(prnt, head, "", "All Files (*)")[0]
        if filepath.strip() == "":
            return False, None, None
        return True, *self.load_mask_from_file(filepath)

    def load_tessexec_with_picker(self, prnt, head: str) -> tuple[bool, str]:
        """
        Handle file operations involved in loading executable from the storage device

        :return: Path to the Tesseract OCR executable
        """
        explorer, status = QFileDialog(), False
        filepath = explorer.getOpenFileName(prnt, head, "", "All Files (*);;Executable Files (*.exe)")[0]
        if filepath.strip() != "":
            status = True
        return status, filepath.strip()


file = FileHandling()
