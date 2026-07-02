from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Sandrone(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.sandrone
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.6266, defense=58.57357, health_points=1029.5856)
    ascn: BaseStat = BaseStat(attack=109.33523, defense=240.5403, health_points=4228.035)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.cryo
    cons_name: str = "Narcissorolegium"
    afln: str = "Fatui"
    head: str = "Mirrored Analysis"
