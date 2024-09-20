import pytest
from PySide6.QtCore import Qt


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(
            None,
            id="face.wind.rule: Wiping the artifact collection"
        )
    ]
)
def test_team_wipe(runner, qtbot, _) -> None:
    """
    Test the configuration of characters on the user interface

    :return:
    """

    """
    Set the user interface elements as intended
    """
    qtbot.mouseClick(runner.head_wipe, Qt.LeftButton)

    """
    Confirm if the user interface elements change accordingly
    """
    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        assert getattr(runner, f"arti_{area}_type").currentText() == "None"
        assert getattr(runner, f"arti_{area}_levl").currentText() == "None"
        assert getattr(runner, f"arti_{area}_rare").currentText() == "Star 0"
        assert getattr(runner, f"arti_{area}_type_name").text() == "None"
        for item in ["main", "a", "b", "c", "d"]:
            assert getattr(runner, f"arti_{area}_name_{item}").currentText() == "None"
            assert getattr(runner, f"arti_{area}_data_{item}").text() == ""
