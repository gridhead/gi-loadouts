from enum import Enum
from uuid import uuid4

from pydantic import BaseModel

from ...data.arti import ArtiList
from ..arti import ArtiLevl
from ..file import (
    __artiarea_good__,
    __artiarea_good_revmap__,
    __artilevl_good__,
    __artilist_good__,
    __artilist_good_revmap__,
    __stat_good__,
    __stat_good_revmap__,
)
from ..rare import Rare
from ..stat import ATTR, __revmap__


class ArtiArea(str, Enum):
    """
    Set of possible artifact areas
    """
    fwol = "FWOL"
    pmod = "PMOD"
    sdoe = "SDOE"
    gboe = "GBOE"
    ccol = "CCOL"


class ArtiFile(BaseModel):
    """
    Artifact storage primitive
    """
    name: str = ""
    type: ArtiList = getattr(ArtiList, "None")
    area: Enum = ArtiArea.fwol
    rare: Rare = Rare.Star_1
    levl: ArtiLevl = ArtiLevl.Level_00
    stat_main: ATTR = ATTR()
    stat_a: ATTR = ATTR()
    stat_b: ATTR = ATTR()
    stat_c: ATTR = ATTR()
    stat_d: ATTR = ATTR()

    @property
    def to_yaml(self) -> dict:
        """
        Derive the information stored for consumption in file storage in the YAML format

        :return: Dictionary consisting of associated artifact statistics
        """
        data = {
            "name": self.name,
            "type": self.type.value.name,
            "area": self.area.value,
            "rare": self.rare.value.qant,
            "levl": self.levl.value.name,
            "stat": {
                "main": {
                    "name": self.stat_main.stat_name.value,
                    "data": self.stat_main.stat_data,
                },
                "a": {
                    "name": self.stat_a.stat_name.value,
                    "data": self.stat_a.stat_data,
                },
                "b": {
                    "name": self.stat_b.stat_name.value,
                    "data": self.stat_b.stat_data,
                },
                "c": {
                    "name": self.stat_c.stat_name.value,
                    "data": self.stat_c.stat_data,
                },
                "d": {
                    "name": self.stat_d.stat_name.value,
                    "data": self.stat_d.stat_data,
                },
            }
        }
        return data

    @property
    def to_good(self) -> dict:
        """
        Derive the information stored for consumption in file storage in the GOOD format

        :return: Dictionary consisting of associated artifact statistics
        """
        data = {
            "id": uuid4().hex[0:8].upper(),
            "location": "",
            "lock": False,
            "setKey": __artilist_good__[self.type.value.name],
            "rarity": self.rare.value.qant,
            "level": 0 if self.levl.value.levl == -1 else self.levl.value.levl,
            "slotKey": __artiarea_good__[self.area.value],
            "mainStatKey": __stat_good__[self.stat_main.stat_name],
            "substats": [
                {
                    "key": __stat_good__[getattr(self, f"stat_{alfa}").stat_name],
                    "value": getattr(self, f"stat_{alfa}").stat_data,
                } for alfa in ["a", "b", "c", "d"] if getattr(self, f"stat_{alfa}") != ATTR()
            ]
        }
        return data


def make_artifile_from_yaml(objc: dict) -> ArtiFile:
    """
    Parse the provided dictionary of artifact statistics read from a YAML file to make a supported artifact object

    :param objc: Dictionary consisting of associated artifact statistics
    :return: Supported artifact object for processing
    """
    try:
        artiobjc = ArtiFile(
            name=objc["name"],
            type=getattr(ArtiList, objc["type"].replace(" ", "_").replace("'", "").replace("-", "_")),
            area=getattr(ArtiArea, objc["area"].lower()),
            rare=getattr(Rare, f"Star_{objc["rare"]}"),
            levl=getattr(ArtiLevl, objc["levl"].replace(" ", "_")),
            stat_main=ATTR(stat_name=__revmap__[objc["stat"]["main"]["name"]], stat_data=objc["stat"]["main"]["data"]),
            stat_a=ATTR(stat_name=__revmap__[objc["stat"]["a"]["name"]], stat_data=objc["stat"]["a"]["data"]),
            stat_b=ATTR(stat_name=__revmap__[objc["stat"]["b"]["name"]], stat_data=objc["stat"]["b"]["data"]),
            stat_c=ATTR(stat_name=__revmap__[objc["stat"]["c"]["name"]], stat_data=objc["stat"]["c"]["data"]),
            stat_d=ATTR(stat_name=__revmap__[objc["stat"]["d"]["name"]], stat_data=objc["stat"]["d"]["data"]),
        )
    except Exception as expt:
        raise ValueError("Artifact stat cannot be identified or unit data cannot be parsed.") from expt

    for indx in ["a", "b", "c", "d"]:
        if artiobjc.stat_main.stat_name == getattr(artiobjc, f"stat_{indx}").stat_name:
            raise ValueError("Artifact substat matches main stat.")
    return artiobjc


def make_artifile_from_good(objc: dict) -> ArtiFile:
    """
    Parse the provided dictionary of artifact statistics read from a GOOD file to make a supported artifact object

    :param objc: Dictionary consisting of associated artifact statistics
    :return: Supported artifact object for processing
    """
    try:
        """
        As `NoneType` is not supported as a datatype for level in the GOOD format, we use the
        rarity of 0 (i.e. `Rare.Star_0`) to confirm the level. As artifacts belonging to `Star 0`,
        can only have level `None` - the check satisfies and the contents is loaded.
        """
        artiobjc = ArtiFile(
            name="",
            type=getattr(ArtiList, __artilist_good_revmap__[objc["setKey"]].replace(" ", "_").replace("'", "").replace("-", "_")),
            area=getattr(ArtiArea, __artiarea_good_revmap__[objc["slotKey"]].lower()),
            rare=getattr(Rare, f"Star_{objc["rarity"]}"),
            levl=getattr(ArtiLevl, "None") if objc["rarity"] == 0 else __artilevl_good__[objc["level"]],
            stat_main=ATTR(stat_name=__stat_good_revmap__[objc["mainStatKey"]], stat_data=0.0),
            stat_a=ATTR(), stat_b=ATTR(), stat_c=ATTR(), stat_d=ATTR()
        )
        alfalist = ["a", "b", "c", "d"]
        for item in objc["substats"]:
            setattr(artiobjc, f"stat_{alfalist[0]}", ATTR(stat_name=__stat_good_revmap__[item["key"]], stat_data=item["value"]))
            alfalist.pop(0)
    except Exception as expt:
        raise ValueError("Artifact stat cannot be identified or unit data cannot be parsed.") from expt

    for indx in ["a", "b", "c", "d"]:
        if artiobjc.stat_main.stat_name == getattr(artiobjc, f"stat_{indx}").stat_name:
            raise ValueError("Artifact substat matches main stat.")
    return artiobjc
