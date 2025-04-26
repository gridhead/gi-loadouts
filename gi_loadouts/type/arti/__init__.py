from enum import Enum

from pydantic import BaseModel

from ..rare import Rare
from .ccol import CCOL  # noqa : F401
from .ccol import __revmap__ as revmap_ccol  # noqa : F401
from .fwol import FWOL  # noqa : F401
from .fwol import __revmap__ as revmap_fwol  # noqa : F401
from .gboe import GBOE  # noqa : F401
from .gboe import __revmap__ as revmap_gboe  # noqa : F401
from .pmod import PMOD  # noqa : F401
from .pmod import __revmap__ as revmap_pmod  # noqa : F401
from .sdoe import SDOE  # noqa : F401
from .sdoe import __revmap__ as revmap_sdoe  # noqa : F401


class ArtifactTeam(BaseModel):
    name: str = "None"
    fwol: FWOL = FWOL()
    pmod: PMOD = PMOD()
    sdoe: SDOE = SDOE()
    gboe: GBOE = GBOE()
    ccol: CCOL = CCOL()
    pairdata: list = []
    quaddata: list = []
    pairtext: str = ""
    quadtext: str = ""
    rare: list[Rare] = []
    file: str = ""


class ArtiLevlType(BaseModel):
    levl: int = 0
    name: str = "Level 00"
    rare: list[Rare] = [Rare.Star_1]


__artilevl__ = {
    "None": ArtiLevlType(levl=-1, name="None", rare=[Rare.Star_0]),
    "Level 00": ArtiLevlType(levl=0, name="Level 00", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 01": ArtiLevlType(levl=1, name="Level 01", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 02": ArtiLevlType(levl=2, name="Level 02", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 03": ArtiLevlType(levl=3, name="Level 03", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 04": ArtiLevlType(levl=4, name="Level 04", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 05": ArtiLevlType(levl=5, name="Level 05", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 06": ArtiLevlType(levl=6, name="Level 06", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 07": ArtiLevlType(levl=7, name="Level 07", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 08": ArtiLevlType(levl=8, name="Level 08", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 09": ArtiLevlType(levl=9, name="Level 09", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 10": ArtiLevlType(levl=10, name="Level 10", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 11": ArtiLevlType(levl=11, name="Level 11", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 12": ArtiLevlType(levl=12, name="Level 12", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 13": ArtiLevlType(levl=13, name="Level 13", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 14": ArtiLevlType(levl=14, name="Level 14", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 15": ArtiLevlType(levl=15, name="Level 15", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 16": ArtiLevlType(levl=16, name="Level 16", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 17": ArtiLevlType(levl=17, name="Level 17", rare=[Rare.Star_5]),
    "Level 18": ArtiLevlType(levl=18, name="Level 18", rare=[Rare.Star_5]),
    "Level 19": ArtiLevlType(levl=19, name="Level 19", rare=[Rare.Star_5]),
    "Level 20": ArtiLevlType(levl=20, name="Level 20", rare=[Rare.Star_5])
}


ArtiLevl = Enum(
    "ArtiLevl",
    {
        item.replace(" ", "_"): data for item, data in __artilevl__.items()
    }
)


class Collection(BaseModel):
    fwol: FWOL = FWOL()
    pmod: PMOD = PMOD()
    sdoe: SDOE = SDOE()
    gboe: GBOE = GBOE()
    ccol: CCOL = CCOL()

    @property
    def team_list(self) -> list:
        return [
            self.fwol.__teamname__,
            self.pmod.__teamname__,
            self.sdoe.__teamname__,
            self.gboe.__teamname__,
            self.ccol.__teamname__,
        ]

    @property
    def pair(self) -> list:
        pair_list, seen_list = set(), set()
        for item in self.team_list:
            if item.strip() != "" and item.strip() != "None":
                if item in seen_list:
                    pair_list.add(item)
                else:
                    seen_list.add(item)
        pair_list = list(pair_list)
        pair_list.sort()
        return pair_list

    @property
    def quad(self) -> str:
        occurrence, team = dict(), ""
        for item in self.team_list:
            if item.strip() != "" and item.strip() != "None":
                if item in occurrence:
                    occurrence[item] += 1
                else:
                    occurrence[item] = 1
        for item, qant in occurrence.items():
            if qant >= 4:
                team = item
        return team


__artistat__ = {
    0: {
        "active": [],
        "inactive": ["a", "b", "c", "d"]
    },
    1: {
        "active": ["a"],
        "inactive": ["b", "c", "d"]
    },
    2: {
        "active": ["a", "b"],
        "inactive": ["c", "d"]
    },
    3: {
        "active": ["a", "b", "c", "d"],
        "inactive": []
    },
    4: {
        "active": ["a", "b", "c", "d"],
        "inactive": []
    },
    5: {
        "active": ["a", "b", "c", "d"],
        "inactive": []
    }
}
