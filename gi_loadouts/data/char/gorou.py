from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Gorou(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_geo_perc
    name: CharName = CharName.gorou
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=15.31488, defense=54.36375, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=54.797653, defense=194.5125, health_points=2870.8872)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.geo
    cons_name: str = "Canis Bellatoris"
    afln: str = "Watatsumi Island"
    head: str = "Canine Warrior"
