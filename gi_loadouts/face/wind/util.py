from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QStatusBar

from ... import conf


def show_status(status_bar: QStatusBar, text: str, orig: str = "Ready.") -> None:
    """
    Show a message in the status bar with a timeout, and reset back to a default message

    :param status_bar: Targeted QStatusBar instance
    :param text: Intended message to be shown
    :param orig: Default message to be shown
    :return:
    """
    status_bar.showMessage(text, conf.stattime)
    QTimer.singleShot(conf.stattime, lambda: status_bar.showMessage(orig))
