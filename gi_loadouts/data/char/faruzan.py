from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Faruzan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.faruzan
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.4724, defense=52.647, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=58.939335, defense=188.37, health_points=2870.8872)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.anemo
    cons_name: str = "Flosculi Implexi"
    afln: str = "Haravatat"
    head: str = "Enigmatic Machinist"
