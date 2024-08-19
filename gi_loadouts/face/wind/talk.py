from PySide6.QtWidgets import QMessageBox


class Dialog:
    def __init__(self):
        self.dialog = QMessageBox(parent=self)

    def show_dialog(self, icon, head, text):
        self.dialog.setIcon(icon)
        self.dialog.setWindowTitle(f"{head}")
        self.dialog.setText(text)
        self.dialog.setFont("IBM Plex Sans")
        self.dialog.show()
