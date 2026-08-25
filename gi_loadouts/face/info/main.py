from time import time

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QMoveEvent, QPixmap, QShowEvent
from PySide6.QtWidgets import QDialog

from ... import __gicompat_part__, __gicompat_vers__, __releases__, __versdata__
from .info import Ui_info


class InfoDialog(QDialog, Ui_info):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__}")
        self.icon.setPixmap(QPixmap(f":pmon/imgs/pmon/{int(time() % 10)}.webp"))
        self.vers.setText(f"Version v{__versdata__}")
        self.comp.setText(
            f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}"
        )
        self.updt.clicked.connect(self.open_update_link)

    def showEvent(self, event: QShowEvent) -> None:
        """
        Center the dialog box over the parent window
        GNOME/Wayland does not need but Windows does

        :param event:
        :return:
        """
        if self.parent():
            self.tocenter = True
            geo = self.parent().geometry()
            self.move(
                geo.center().x() - self.width() // 2,
                geo.center().y() - self.height() // 2,
            )
            self.tocenter = False
        super().showEvent(event)

    def moveEvent(self, event: QMoveEvent) -> None:
        """
        Move the parent window along with the dialog
        GNOME/Wayland does not need but Windows does

        :param event:
        :return:
        """
        if self.parent() and not getattr(self, "tocenter", False):
            self.parent().move(self.parent().pos() + event.pos() - event.oldPos())
        super().moveEvent(event)

    def open_update_link(self):
        QDesktopServices.openUrl(QUrl(__releases__))
