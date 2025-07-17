from shutil import which


def get_tessexec_path() -> str | None:
    return which("tesseract")

tessexec = get_tessexec_path()

tempname = ""
temppath = ""
stattime = 5000

data_prefix = "gi-loadouts-"
data_suffix = ".traineddata"
