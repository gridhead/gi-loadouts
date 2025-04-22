from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Albedo(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_geo_perc
    name: CharName = CharName.albedo
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=19.551, defense=68.2062, health_points=1029.5856)
    ascn: BaseStat = BaseStat(attack=80.28111, defense=280.098, health_points=4228.035)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.geo
    cons_name: str = "Princeps Cretaceus"
    afln: str = "Knights of Favonius"
    head: str = "Kreideprinz"
