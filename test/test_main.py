import pytest

from gi_loadouts import main


@pytest.mark.parametrize(
    "_",
    [
        pytest.param(None, id="main: Attempt loading the custom fonts")
    ]
)
def test_load_custom_font(runner, mocker, _):
    """
    Test loading of custom fonts

    :return:
    """

    """
    Mock the loading of custom font in the user interface
    """
    mocker.patch("gi_loadouts.main.QFontDatabase.addApplicationFont", return_value=1)
    main.load_custom_font()

    """
    Confirm if the user interface elements change accordingly
    """
    assert main.QFontDatabase.addApplicationFont.call_count == 5
