from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Chiori(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.chiori
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.137, defense=74.19, health_points=890.4)
    ascn: BaseStat = BaseStat(attack=103.21856689453, defense=304.66799926758, health_points=3656.4672851562)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.geo
    cons_name: str = "Cisoria"
    afln: str = "Court of Fontaine"
    head: str = "The Thundering Seamstress"
