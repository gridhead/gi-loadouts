from pydantic import BaseModel

from gi_loadouts.type.file.arti import ArtiArea, ArtiFile, make_artifile


class TeamFile(BaseModel):
    fwol: ArtiFile = ArtiFile(area=ArtiArea.fwol)
    pmod: ArtiFile = ArtiFile(area=ArtiArea.pmod)
    sdoe: ArtiFile = ArtiFile(area=ArtiArea.sdoe)
    gboe: ArtiFile = ArtiFile(area=ArtiArea.gboe)
    ccol: ArtiFile = ArtiFile(area=ArtiArea.ccol)

    @property
    def easydict(self) -> dict:
        data = {
            "fwol": self.fwol.easydict,
            "pmod": self.pmod.easydict,
            "sdoe": self.sdoe.easydict,
            "gboe": self.gboe.easydict,
            "ccol": self.ccol.easydict,
        }
        return data


def make_teamfile(objc: dict) -> TeamFile:
    teamobjc = TeamFile()
    for area in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
        try:
            setattr(teamobjc, area, make_artifile(objc[area]))
        except Exception:
            raise
    return teamobjc
