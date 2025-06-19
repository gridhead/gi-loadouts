from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Skirk(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.skirk
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.93, defense=62.76167, health_points=966.6665)
    ascn: BaseStat = BaseStat(attack=114.6873, defense=257.7393, health_points=3969.6553)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Crystallina"
    afln: str = "Cosmic Calamity"
    head: str = "Void Star"
