from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Odette(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.odette
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.068, defense=61.26592, health_points=1010.5192)
    ascn: BaseStat = BaseStat(attack=107.04148, defense=251.5968, health_points=4149.7383)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Cygnus Olor"
    afln: str = "Korolevskiy Troupe"
    head: str = "Swirling Snow"
