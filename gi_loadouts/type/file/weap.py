from uuid import uuid4

from pydantic import BaseModel

from ..levl import Level
from ..weap import WeaponType
from . import __ascn_bond__, __weaplist_good__, __weaplist_good_revmap__


class WeapFile(BaseModel):
    """
    Weapon storage primitive
    """
    name: str = ""
    type: WeaponType = WeaponType.none
    levl: Level = Level.Level_01_20_Rank_0
    refn: str = "Refinement 1"

    @property
    def to_yaml(self) -> dict:
        """
        Derive the information stored for consumption in file storage in the YAML format

        :return: Dictionary consisting of associated artifact collection statistics
        """
        data = {
            "name": self.name,
            "type": self.type.name,
            "levl": self.levl.value.name,
            "refn": self.refn,
        }
        return data

    @property
    def to_good(self) -> dict:
        """
        Derive the information stored for consumption in file storage in the GOOD format

        :return: Dictionary consisting of associated artifact collection statistics
        """
        data = {
            "id": uuid4().hex[0:8].upper(),
            "location": "",
            "lock": False,
            "key": __weaplist_good__[self.name],
            "level": self.levl.value.qant,
            "ascension": self.levl.value.rank.value,
            "refinement": int(self.refn.split(" ")[1]) if self.refn != "" else self.refn,
            "type": self.type.name
        }
        return data


def make_weapfile_from_yaml(objc: dict) -> WeapFile:
    """
    Parse the provided dictionary of artifact statistics read from a YAML file to make a supported weapon object

    :param objc: Dictionary consisting of associated weapon statistics
    :return: Supported weapon object for processing
    """
    try:
        weapobjc = WeapFile(
            name=objc["name"],
            type=getattr(WeaponType, objc["type"]),
            levl=getattr(Level, objc["levl"].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")),
            refn=objc["refn"],
        )
    except Exception as expt:
        raise ValueError("Weapon data cannot be parsed.") from expt
    return weapobjc


def make_weapfile_from_good(objc: dict) -> WeapFile:
    """
    Parse the provided dictionary of artifact statistics read from a GOOD file to make a supported weapon object

    :param objc: Dictionary consisting of associated weapon statistics
    :return: Supported weapon object for processing
    """
    try:
        weapobjc = WeapFile(
            name=__weaplist_good_revmap__[objc["key"]],
            type=getattr(WeaponType, objc["type"]),
            levl=getattr(Level, f"Level_0{objc["level"]}_{__ascn_bond__[objc["ascension"]]}_Rank_{objc["ascension"]}" if objc["level"] < 10 else f"Level_{objc["level"]}_{__ascn_bond__[objc["ascension"]]}_Rank_{objc["ascension"]}"),
            refn=f"Refinement {objc["refinement"]}" if objc["refinement"] != "" else objc["refinement"],
        )
    except Exception as expt:
        raise ValueError("Weapon data cannot be parsed.") from expt
    return weapobjc
