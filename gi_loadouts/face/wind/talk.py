from PySide6.QtWidgets import QMessageBox


class Dialog:
    def __init__(self) -> None:  # pragma: no cover
        self.dialog = QMessageBox(parent=self)

    def show_dialog(self, icon: QMessageBox.Icon, head: str, text: str) -> None:
        """
        Modify the dialog with the passed severity, title and content before exhibiting on the user interface

        :param icon:
        :param head:
        :param text:
        :return:
        """
        self.dialog.setIcon(icon)
        self.dialog.setWindowTitle(f"{head}")
        self.dialog.setText(text)
        self.dialog.setFont("IBM Plex Sans")
        self.dialog.show()
