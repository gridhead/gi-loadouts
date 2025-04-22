from os.path import realpath
from pathlib import PurePath
from re import search
from tempfile import gettempdir
from time import time

from PIL import ImageFile
from PySide6.QtCore import QObject, Signal
from pytesseract import TesseractError, image_to_string, pytesseract

from ... import conf
from ...data.arti import ArtiList
from ...type.arti import ArtiLevl
from ...type.rare import Rare
from ...type.stat import ATTR
from . import areaiden, levliden, mainstat, substats, teamiden


class ScanWorker(QObject):
    result = Signal(tuple)

    def __init__(self, snap: ImageFile):
        super().__init__()
        self.snap = snap

    def scan_artifact(self) -> None:  # pragma: no cover
        """
        Scan the screenshot for computing artifact information using Tesseract OCR

        Offload a long running task to a thread to keep the user interface from becoming unresponsive

        :return: Collection of artifact information and duration of computation
        """
        """
        coverage.py does not seem to correctly work with the QThread.
        Even though this part is tested but the coverage remains unchanged. https://github.com/nedbat/coveragepy/issues/686
        """

        strttime = time()

        area, main, seco, team, levl, rare = "", ATTR(), {"a": ATTR(), "b": ATTR(), "c": ATTR(), "d": ATTR()}, "", "Level 00", "Star 0"
        pytesseract.tesseract_cmd = conf.tessexec

        w, h = self.snap.size
        l, t, r, b = w // 2, 0, w, h  # noqa: E741
        self.snap = self.snap.crop((l, t, r, b))
        location = PurePath(realpath(gettempdir())).as_posix()

        try:
            text = image_to_string(self.snap, lang=conf.tempname, config=f"--tessdata-dir {location}")
        except (OSError, TesseractError) as expt:
            if isinstance(expt, OSError):
                expt = "Selected executable of Tesseract OCR is unfunctional."
            else:
                expt = "Processing failed as either Tesseract OCR executable ceased to function or training data was tampered with."
            stoptime = time()
            rslt = area, main, seco, team, levl, rare, (stoptime - strttime), expt
            self.result.emit(rslt)
            return

        # DISTRIBUTION AREA
        areadict = {}
        for item, coll in areaiden.items():
            areadict[item] = 0
            for sbst in coll.split(" "):
                if sbst in text:
                    areadict[item] += 1

        sortkeys = sorted(areadict, key=lambda item: areadict[item], reverse=True)
        area = areaiden[sortkeys[0]]

        # TEAM IDENTITY
        teamdict = {}
        for item, coll in teamiden.items():
            teamdict[item] = 0

            """
            This provides a set of words to check for to confirm which artifact set the current
            artifact belongs to. It has to be a SET and not a LIST to ensure that the repetition of
            certain words do not end up causing problems.

            For eg. "Scrolls of the Hero of Cinder City"
            """
            calclist = {*coll["name"], *coll["dist"][area]} if area != "" else {*coll["name"], *[item for data in coll["dist"].values() for item in data]}

            for sbst in calclist:
                if sbst in text:
                    teamdict[item] += 1

        sortkeys = sorted(teamdict, key=lambda item: teamdict[item], reverse=True)
        team = sortkeys[0]

        # MAINSTAT
        if area in mainstat.keys():
            calcdict = mainstat[area]
        else:
            calcdict = {item: data for dinx in mainstat.values() for item, data in dinx.items()}

        if "+" in text:
            plus_indx = text.index("+")
        else:
            plus_indx = len(text)

        for ptrn, name in calcdict.items():
            """
            As the mainstats are always shown before the level indicator of the artifact, we can safely
            assume that any matches made in between the start of the text to the first occurrence of
            the `+` sign is the mainstat of the artifact. There, of course, are pitfalls for whenever
            the `+` sign cannot be reliably read but there is only so much that we can do here.
            """
            mtch = search(ptrn, text[0:plus_indx])
            if mtch:
                """
                It is possible for artifacts having absolute HP, DEF and ATK units as their mainstat to
                have relative HP%, DEF% and ATK% units in substats and vice versa. To ensure that the
                presence of HP, DEF, ATK, HP%, DEF% and ATK% units in the substats is accounted for
                when one of these is also in the mainstat, a localized replacement must be performed.
                """
                text = text[0:plus_indx].replace(mtch.group(), "") + text[plus_indx:]
                main = ATTR(stat_name=name, stat_data=0.0)
                break

        # SUBSTATS
        lict = list()
        seco = {"a": ATTR(), "b": ATTR(), "c": ATTR(), "d": ATTR()}
        for ptrn, name in substats.items():
            mtch = search(ptrn, text)
            if mtch and len(lict) < 4:
                text = text.replace(mtch.group(), "")
                qant = search(r"\b\d+(\.\d+)?\b", mtch.group())
                data = qant.group() if qant else "0.0"
                lict.append(ATTR(stat_name=name, stat_data=float(data)))
        for indx in range(len(lict)):
            seco[list(seco.keys())[indx]] = lict[indx]

        # LEVELS
        mtch = search(levliden, text)
        if mtch:
            data = int(search(r"\b\d+\b", mtch.group()).group())
            levl = f"Level {f"0{data}" if data < 10 else data}"

        rare_from_team, rare_from_levl = Rare.Star_0, Rare.Star_0

        # RARITY (from TEAM IDENTITY)
        if team.strip() != "":
            teamobjc = getattr(ArtiList, team.replace(" ", "_").replace("'", "").replace("-", "_"))
            rare_from_team = teamobjc.value.rare[0]

        # RARITY (from LEVELS)
        rare_from_levl = getattr(ArtiLevl, levl.replace(" ", "_")).value.rare[0]

        # RARITY (accurate)
        if rare_from_levl.value.qant > rare_from_team.value.qant:
            rare = rare_from_levl.value.name
        else:
            rare = rare_from_team.value.name

        stoptime = time()

        rslt = area, main, seco, team, levl, rare, (stoptime - strttime), None

        self.result.emit(rslt)
