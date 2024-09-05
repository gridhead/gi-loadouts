from os.path import realpath
from pathlib import PurePath
from re import search
from tempfile import gettempdir
from time import time

from PIL import ImageFile
from pytesseract import TesseractError, image_to_string, pytesseract

from gi_loadouts import conf
from gi_loadouts.data.arti import ArtiList
from gi_loadouts.face.scan import areaiden, levliden, mainstat, substats, teamiden
from gi_loadouts.type.arti import CCOL, FWOL, GBOE, PMOD, SDOE, ArtiLevl
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import ATTR, STAT

__revmap__ = {
    FWOL: "Flower of Life",
    PMOD: "Plume of Death",
    SDOE: "Sands of Eon",
    GBOE: "Goblet of Eonothem",
    CCOL: "Circlet of Logos"
}


def scan_artifact(snap: ImageFile) -> tuple:
    """
    Scan the screenshot for computing artifact information using Tesseract OCR

    :return: Collection of artifact information and duration of computation
    """
    strttime = time()

    area, main, seco, team, levl, rare = "", ATTR(), {"a": ATTR(), "b": ATTR(), "c": ATTR(), "d": ATTR()}, "", "Level 00", "Star 0"
    pytesseract.tesseract_cmd = conf.tessexec

    w, h = snap.size
    l, t, r, b = w // 2, 0, w, h  # noqa: E741
    snap = snap.crop((l, t, r, b))
    location = PurePath(realpath(gettempdir())).as_posix()

    try:
        text = image_to_string(snap, lang=conf.tempname, config=f"--tessdata-dir {location}")
    except (OSError, TesseractError) as expt:
        if isinstance(expt, OSError):
            raise OSError("Selected executable of Tesseract OCR is unfunctional.") from expt
        elif isinstance(expt, TesseractError):
            raise ValueError("Processing failed as either Tesseract OCR executable ceased to function or training data was tampered with.") from expt

    # DISTRIBUTION AREA
    for ptrn, name in areaiden.items():
        mtch = search(ptrn, text)
        if mtch:
            area = __revmap__[name]

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

    for ptrn, name in calcdict.items():
        """
        As the mainstats are always shown before the level indicator of the artifact, we can safely
        assume that any matches made in between the start of the text to the first occurrence of
        the `+` sign is the mainstat of the artifact. There, of course, are pitfalls for whenever
        the `+` sign cannot be reliably read but there is only so much that we can do here.
        """
        mtch = search(ptrn, text[0:text.index("+")])
        if mtch:
            """
            It is possible for artifacts having absolute HP, DEF and ATK units as their mainstat to
            have relative HP%, DEF% and ATK% units in substats and vice versa. To ensure that the
            presence of HP, DEF, ATK, HP%, DEF% and ATK% units in the substats is accounted for
            when one of these is also in the mainstat, a localized replacement must be performed.
            """
            text = text[0:text.index("+")].replace(mtch.group(), "") + text[text.index("+"):]
            main = ATTR(stat_name=name, stat_data=0.0)
            break

    # SUBSTATS
    lict = list()
    seco = {"a": ATTR(), "b": ATTR(), "c": ATTR(), "d": ATTR()}
    for ptrn, name in substats.items():
        mtch = search(ptrn, text)
        if mtch and len(lict) < 4:
            text = text.replace(mtch.group(), "")
            data = search(r"\b\d+(\.\d+)?\b", mtch.group()).group()
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

    return area, main, seco, team, levl, rare, (stoptime - strttime)
