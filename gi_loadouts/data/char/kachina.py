from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Kachina(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_geo_perc
    name: CharName = CharName.kachina
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.16416, defense=66.438225, health_points=989.2932)
    ascn: BaseStat = BaseStat(attack=64.99256, defense=237.71475, health_points=3539.6733)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.geo
    cons_name: str = "Ochotona Princeps"
    afln: str = "Nanatzcayan"
    head: str = "Mottled Gold Yet Unsmelted"
