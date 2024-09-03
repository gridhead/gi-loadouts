from platform import system

if system() == "Windows":
    tessexec = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
else:
    tessexec = "/usr/bin/tesseract"
