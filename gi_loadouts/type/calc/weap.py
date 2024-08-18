from typing import List

from pydantic import BaseModel

from gi_loadouts.type.levl import Level
from gi_loadouts.type.stat import ATTR
from gi_loadouts.type.weap import WeaponStat, WeaponStatType


class WEAP(BaseModel):
    name: str = ""
    levl: Level = Level.Level_01_20_Rank_0
    base: ATTR = ATTR(stat_name=WeaponStatType.attack.value, stat_data=0.0)
    seco: WeaponStat = WeaponStat(stat_name=WeaponStatType.none.value, stat_data=0.0)
    refn: List[WeaponStat] = []
