from os import path, remove
from pathlib import Path
from re import match
from tempfile import NamedTemporaryFile, gettempdir

from PySide6.QtCore import QFile, QIODevice

from gi_loadouts import conf
from gi_loadouts.face.rsrc import arti, data, pmon, rare, vson, weap  # noqa: F401
from gi_loadouts.face.rsrc.char import back, face, name, wish  # noqa: F401
from gi_loadouts.face.rsrc.font import icon, text  # noqa: F401


def make_temp_file() -> None:
    """
    Create temporary file with the Tesseract OCR training data during application initialization

    :return:
    """

    """
    Remove the residual cache data from the temporary directory left over during previous sessions
    due to unsuccessful termination before instantiating the same for this session.
    """
    ptrn = fr"{conf.data_prefix}[a-z0-9_]+\{conf.data_suffix}"
    temp = Path(gettempdir())
    resi = [temp / file.name for file in temp.iterdir() if file.is_file() if match(ptrn, file.name)]

    for file in resi:
        if file.exists():
            try:
                remove(file)
            except FileNotFoundError:
                continue

    file = QFile(":data/data/best.traineddata")
    if not file.open(QIODevice.ReadOnly):
        raise FileNotFoundError("Training data for Tesseract OCR could not be initialized.")
    cont = file.readAll()
    file.close()

    """
    When a file is marked for deletion on Windows, the file cannot be reliably opened. Therefore,
    the context manager protocol for `NamedTemporaryFile` cannot be used here. The temporary file
    have to be created and deleted manually. On UNIX based operating systems like GNU/Linux or
    MacOS, files can be reliably opened even when they have been marked for deletion.
    """
    temp = NamedTemporaryFile(prefix=conf.data_prefix, suffix=conf.data_suffix, delete=False, mode="w+b")
    temp.write(cont)
    temp.close()
    conf.tempname = Path(temp.name).name.replace(conf.data_suffix, "")
    conf.temppath = temp.name


def kill_temp_file() -> None:
    """
    Cleanup the temporary file created by the application when the process is decontextualized

    :return:
    """
    if path.exists(conf.temppath):
        remove(conf.temppath)
