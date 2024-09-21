import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from gi_loadouts import __gicompat_part__, __gicompat_vers__, __versdata__


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(
            None,
            id="face.lcns: Clicking the help button"
        )
    ]
)
def test_lcns(runner, qtbot, _) -> None:
    """
    Attempt clicking the help button on side of UI

    :return:
    """

    """
    Perform the action of clicking the help button
    """
    qtbot.mouseClick(runner.side_lcns, Qt.LeftButton)
    """
    Confirm if the user interface elements change accordingly
    """
    assert runner.side_lcns.toolTip() == "Help"
    assert isinstance(runner.lcnsobjc, QDialog)
    assert runner.lcnsobjc.windowTitle() == f"Loadouts for Genshin Impact v{__versdata__}"
    assert runner.lcnsobjc.vers.text() == f"Version v{__versdata__}"
    assert runner.lcnsobjc.comp.text() == f"This version is compatible with Genshin Impact {__gicompat_vers__} Phase {__gicompat_part__}"
