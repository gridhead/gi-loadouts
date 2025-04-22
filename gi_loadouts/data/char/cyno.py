from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Cyno(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.cyno
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=24.7646, defense=66.88994, health_points=972.3864)
    ascn: BaseStat = BaseStat(attack=101.68941, defense=274.6926, health_points=3993.1443)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Lupus Aureus"
    afln: str = "Temple of Silence"
    head: str = "Judicator of Secrets"
