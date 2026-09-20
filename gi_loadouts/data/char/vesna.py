from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Vesna(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.vesna
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.5576, defense=56.8385, health_points=1032.4456)
    ascn: BaseStat = BaseStat(attack=113.158134, defense=233.415, health_points=4239.78)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.anemo
    cons_name: str = "Amentum Vernum"
    afln: str = "Druzhna"
    head: str = "Snowy Banquet's Sharp Blade"
