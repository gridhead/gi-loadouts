from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Beidou(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_electro_perc
    name: CharName = CharName.beidou
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.87648, defense=54.36375, health_points=1094.1492)
    ascn: BaseStat = BaseStat(attack=67.54129, defense=194.5125, health_points=3914.8462)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.electro
    cons_name: str = "Victor Mare"
    afln: str = "The Crux"
    head: str = "Uncrowned Lord of the Ocean"
