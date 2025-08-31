from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Flins(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.flins
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.37, defense=62.94, health_points=972)
    ascn: BaseStat = BaseStat(attack=112.40357, defense=258.48734, health_points=3996.692)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Laterna Vigilis"
    afln: str = "Lightkeepers"
    head: str = "Shadowy Lights, Stranger Wights"
