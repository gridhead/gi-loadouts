from pydantic import BaseModel

from ..file import __artiarea_good_revmap__
from ..file.arti import (
    ArtiArea,
    ArtiFile,
    make_artifile_from_good,
    make_artifile_from_yaml,
)


class TeamFile(BaseModel):
    """
    Artifact collection storage primitive
    """
    fwol: ArtiFile = ArtiFile(area=ArtiArea.fwol)
    pmod: ArtiFile = ArtiFile(area=ArtiArea.pmod)
    sdoe: ArtiFile = ArtiFile(area=ArtiArea.sdoe)
    gboe: ArtiFile = ArtiFile(area=ArtiArea.gboe)
    ccol: ArtiFile = ArtiFile(area=ArtiArea.ccol)

    @property
    def to_yaml(self) -> dict:
        """
        Derive the information stored for consumption in file storage in the YAML format

        :return: Dictionary consisting of associated artifact collection statistics
        """
        data = {
            "fwol": self.fwol.to_yaml,
            "pmod": self.pmod.to_yaml,
            "sdoe": self.sdoe.to_yaml,
            "gboe": self.gboe.to_yaml,
            "ccol": self.ccol.to_yaml,
        }
        return data

    @property
    def to_good(self):
        """
        Derive the information stored for consumption in file storage in the GOOD format

        :return: Dictionary consisting of associated artifact statistics
        """
        data = {
            "flower": self.fwol.to_good,
            "plume": self.pmod.to_good,
            "sands": self.sdoe.to_good,
            "goblet": self.gboe.to_good,
            "circlet": self.ccol.to_good,
        }
        return data


def make_teamfile_from_yaml(objc: dict) -> TeamFile:
    """
    Parse the provided dictionary of artifact statistics to make a supported artifact collection object

    :param objc: Dictionary consisting of associated artifact collection statistics
    :return: Supported artifact collection object for processing
    """
    teamobjc = TeamFile()
    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        try:
            setattr(teamobjc, area, make_artifile_from_yaml(objc[area]))
        except Exception as expt:
            raise ValueError("Artifact set data cannot be parsed.") from expt
    return teamobjc


def make_teamfile_from_good(objc: dict) -> TeamFile:
    """
    Parse the provided dictionary of artifact statistics to make a supported artifact collection object

    :param objc: Dictionary consisting of associated artifact collection statistics
    :return: Supported artifact collection object for processing
    """
    teamobjc = TeamFile()
    for gdst, ydst in __artiarea_good_revmap__.items():
        try:
            setattr(teamobjc, ydst.lower(), make_artifile_from_good(objc[gdst]))
        except Exception as expt:
            raise ValueError("Artifact set data cannot be parsed.") from expt
    return teamobjc
