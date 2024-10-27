from platform import system


def get_tessexec_path():
    if system() == "Windows":
        return "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    else:
        return "/usr/bin/tesseract"

tessexec = get_tessexec_path()

tempname = ""
temppath = ""
stattime = 5000

data_prefix = "gi-loadouts-"
data_suffix = ".traineddata"
