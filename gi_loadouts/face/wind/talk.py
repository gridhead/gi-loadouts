from PySide6.QtWidgets import QMessageBox


class Dialog:
    def __init__(self) -> None:
        self.dialog = QMessageBox(parent=self)

    def show_dialog(self, icon: QMessageBox.Icon, head: str, text: str) -> None:
        self.dialog.setIcon(icon)
        self.dialog.setWindowTitle(f"{head}")
        self.dialog.setText(text)
        self.dialog.setFont("IBM Plex Sans")
        self.dialog.show()
