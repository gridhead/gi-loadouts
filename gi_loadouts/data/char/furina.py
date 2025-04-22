from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Furina(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.furina
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=18.9924, defense=54.146148681641, health_points=1191.65)
    ascn: BaseStat = BaseStat(attack=77.987365722656, defense=222.35850524902, health_points=4893.5590820312)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.hydro
    cons_name: str = "Animula Choragi"
    afln: str = "Court of Fontaine"
    head: str = "Endless Solo of Solitude"
