from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Zibai(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.zibai
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=17.5028, defense=74.48835, health_points=1005.7526)
    ascn: BaseStat = BaseStat(attack=71.8707, defense=305.8965, health_points=4130.164)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.geo
    cons_name: str = "Equa Alba"
    afln: str = "Liyue Harbor"
    head: str = "White Horse's Fleeting Spring"
