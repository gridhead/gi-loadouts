from pydantic import BaseModel

from gi_loadouts.type.file.arti import ArtiArea, ArtiFile, make_artifile


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
    def easydict(self) -> dict:
        """
        Derive the information stored for consumption in file storage

        :return: Dictionary consisting of associated artifact collection statistics
        """
        data = {
            "fwol": self.fwol.easydict,
            "pmod": self.pmod.easydict,
            "sdoe": self.sdoe.easydict,
            "gboe": self.gboe.easydict,
            "ccol": self.ccol.easydict,
        }
        return data


def make_teamfile(objc: dict) -> TeamFile:
    """
    Parse the provided dictionary of artifact statistics to make a supported artifact collection object

    :param objc: Dictionary consisting of associated artifact collection statistics
    :return: Supported artifact collection object for processing
    """
    teamobjc = TeamFile()
    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        try:
            setattr(teamobjc, area, make_artifile(objc[area]))
        except Exception as expt:
            raise ValueError("Artifact set data cannot be parsed.") from expt
    return teamobjc
