from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Layla(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.layla
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.16416, defense=54.936, health_points=930.0268)
    ascn: BaseStat = BaseStat(attack=64.99256, defense=196.56, health_points=3327.6194)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Luscinia"
    afln: str = "Rtawahist"
    head: str = "Fantastical Evening Star"
