from platform import system
from shutil import which


def get_tessexec_path() -> str | None:
    tessexec = which("tesseract")
    if tessexec is None and system() == "Windows":
        # Fallback to default Windows installation path if not found in PATH
        return "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    return tessexec


tessexec = get_tessexec_path()

tempname = ""
temppath = ""
stattime = 5000

data_prefix = "gi-loadouts-"
data_suffix = ".traineddata"
