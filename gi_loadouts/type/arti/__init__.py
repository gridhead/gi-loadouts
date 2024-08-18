from gi_loadouts.type.arti.ccol import CCOL, __revmap__ as revmap_ccol  # noqa : F401
from gi_loadouts.type.arti.fwol import FWOL, __revmap__ as revmap_fwol  # noqa : F401
from gi_loadouts.type.arti.gboe import GBOE, __revmap__ as revmap_gboe  # noqa : F401
from gi_loadouts.type.arti.pmod import PMOD, __revmap__ as revmap_pmod  # noqa : F401
from gi_loadouts.type.arti.sdoe import SDOE, __revmap__ as revmap_sdoe  # noqa : F401

from pydantic import BaseModel
from gi_loadouts.type.rare import Rare
from typing import List
from enum import Enum


class ArtifactTeam(BaseModel):
    name: str
    fwol: FWOL = FWOL()
    pmod: PMOD = PMOD()
    sdoe: SDOE = SDOE()
    gboe: GBOE = GBOE()
    ccol: CCOL = CCOL()
    pairdata: list = []
    quaddata: list = []
    pairtext: str
    quadtext: str
    rare: List[Rare] = []


class ArtiLevl(BaseModel):
    levl: int = 0
    name: str = "Level 00"
    rare: List[Rare] = [Rare.Star_1]


__artilevl__ = {
    "Level 00": ArtiLevl(levl=0, name="Level 00", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 01": ArtiLevl(levl=1, name="Level 01", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 02": ArtiLevl(levl=2, name="Level 02", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 03": ArtiLevl(levl=3, name="Level 03", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 04": ArtiLevl(levl=4, name="Level 04", rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 05": ArtiLevl(levl=5, name="Level 05", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 06": ArtiLevl(levl=6, name="Level 06", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 07": ArtiLevl(levl=7, name="Level 07", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 08": ArtiLevl(levl=8, name="Level 08", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 09": ArtiLevl(levl=9, name="Level 09", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 10": ArtiLevl(levl=10, name="Level 10", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 11": ArtiLevl(levl=11, name="Level 11", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 12": ArtiLevl(levl=12, name="Level 12", rare=[Rare.Star_3, Rare.Star_4, Rare.Star_5]),
    "Level 13": ArtiLevl(levl=13, name="Level 13", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 14": ArtiLevl(levl=14, name="Level 14", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 15": ArtiLevl(levl=15, name="Level 15", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 16": ArtiLevl(levl=16, name="Level 16", rare=[Rare.Star_4, Rare.Star_5]),
    "Level 17": ArtiLevl(levl=17, name="Level 17", rare=[Rare.Star_5]),
    "Level 18": ArtiLevl(levl=18, name="Level 18", rare=[Rare.Star_5]),
    "Level 19": ArtiLevl(levl=19, name="Level 19", rare=[Rare.Star_5]),
    "Level 20": ArtiLevl(levl=20, name="Level 20", rare=[Rare.Star_5])
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
    def team_list(self):
        return [
            self.fwol.__teamname__,
            self.pmod.__teamname__,
            self.sdoe.__teamname__,
            self.gboe.__teamname__,
            self.ccol.__teamname__,
        ]

    @property
    def pair(self):
        pair_list, seen_list = set(), set()
        for item in self.team_list:
            if item.strip() != "":
                if item in seen_list:
                    pair_list.add(item)
                else:
                    seen_list.add(item)
        pair_list = list(pair_list)
        pair_list.sort()
        return pair_list

    @property
    def quad(self):
        occurrence, team = dict(), ""
        for item in self.team_list:
            if item in occurrence:
                occurrence[item] += 1
            else:
                occurrence[item] = 1
        for item, qant in occurrence.items():
            if qant >= 4:
                team = item
        return team


__artistat__ = {
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
