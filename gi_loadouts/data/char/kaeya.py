from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Kaeya(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.7, 3: 13.4, 4: 13.4, 5: 20.1, 6: 26.8}
    __statname__: STAT = STAT.energy_recharge_perc
    name: CharName = CharName.kaeya
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=66.381, health_points=975.6164)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=237.51, health_points=3490.7378)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Pavo Ocellus"
    afln: str = "Knights of Favonius"
    head: str = "Frostwind Swordsman"
