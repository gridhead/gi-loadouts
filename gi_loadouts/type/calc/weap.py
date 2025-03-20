from pydantic import BaseModel

from gi_loadouts.type.stat import ATTR
from gi_loadouts.type.weap import WeaponStat, WeaponStatType


class WEAP(BaseModel):
    """
    Weapon primitive for computational purposes
    """
    base: ATTR = ATTR(stat_name=WeaponStatType.attack.value, stat_data=0.0)
    seco: ATTR = ATTR(stat_name=WeaponStatType.none.value, stat_data=0.0)
    refn: list[WeaponStat] = []
