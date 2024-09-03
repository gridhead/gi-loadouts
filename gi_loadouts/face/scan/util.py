from os.path import realpath
from pathlib import Path, PurePath
from re import search
from tempfile import NamedTemporaryFile, gettempdir
from time import time

from PIL import Image
from PySide6.QtCore import QFile, QIODevice
from pytesseract import image_to_string, pytesseract

from gi_loadouts import conf
from gi_loadouts.data.arti import ArtiList
from gi_loadouts.face.rsrc import data  # noqa: F401
from gi_loadouts.face.scan import areaiden, levliden, mainstat, substats, teamiden
from gi_loadouts.type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from gi_loadouts.type.stat import ATTR, STAT


class ScanWorker:
    def __init__(self) -> None:
        file = QFile(":data/data/best.traineddata")
        if not file.open(QIODevice.ReadOnly):
            raise FileNotFoundError("Training data for Tesseract OCR could not be initialized")
        cont = file.readAll()
        file.close()
        self.temp = NamedTemporaryFile(delete=False, prefix="gi-loadouts-", suffix=".traineddata")
        self.temp.write(cont)
        self.name = Path(self.temp.name).name.replace(".traineddata", "")
        print(self.name)

    def scan_artifact(self, path: str = "") -> tuple:
        """
        Scan the screenshot for computing artifact information using Tesseract OCR

        :return: Collection of artifact information and duration of computation
        """
        strttime = time()
        pytesseract.tesseract_cmd = conf.tessexec
        imej = Image.open(path)
        w, h = imej.size
        l, t, r, b = w // 2, 0, w, h  # noqa: E741
        imej = imej.crop((l, t, r, b))
        location = PurePath(realpath(gettempdir())).as_posix()
        text = image_to_string(imej, lang=self.name, config=f"--tessdata-dir {location}")

        area, main, seco, team, levl, rare = None, ATTR(), list(), "", 0, "Star 0"

        # DISTRIBUTION AREA
        for ptrn, name in areaiden.items():
            mtch = search(ptrn, text)
            if mtch:
                area = name

        # TEAM IDENTITY
        teamdict = {}
        for item, coll in teamiden.items():
            teamdict[item] = 0
            for sbst in coll:
                if sbst in text:
                    teamdict[item] += 1
        sortkeys = sorted(teamdict, key=lambda item: teamdict[item], reverse=True)
        team = sortkeys[0]

        # RARITY
        if team.strip() != "":
            teamobjc = getattr(ArtiList, team.replace(" ", "_").replace("'", "").replace("-", "_"))
            rare = teamobjc.value.rare[0].value.name

        # MAINSTAT
        if area == FWOL:
            main = ATTR(stat_name=STAT.health_points, stat_data=0.0)
        elif area == PMOD:
            main = ATTR(stat_name=STAT.attack, stat_data=0.0)
        elif area in [SDOE, GBOE, CCOL]:
            for ptrn, name in mainstat[area].items():
                mtch = search(ptrn, text)
                if mtch:
                    main = ATTR(stat_name=name, stat_data=0.0)

        # SUBSTATS
        for ptrn, name in substats.items():
            mtch = search(ptrn, text)
            if mtch and len(seco) < 4:
                data = search(r"\b\d+(\.\d+)?\b", mtch.group()).group()
                seco.append(ATTR(stat_name=name, stat_data=float(data)))

        # LEVELS
        mtch = search(levliden, text)
        if mtch:
            levl = f"Level {mtch.group()}"

        stoptime = time()

        return area, main, seco, team, levl, rare, (stoptime - strttime)


scanworker = ScanWorker()
