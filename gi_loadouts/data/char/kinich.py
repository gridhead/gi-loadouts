from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Kinich(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.kinich
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.8818, defense=62.40269, health_points=1000.986)
    ascn: BaseStat = BaseStat(attack=106.2769, defense=256.2651, health_points=4110.59)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.dendro
    cons_name: str = "Chimaera Alebriius"
    afln: str = "Huitztlan"
    head: str = "Turnfire Hunt"
