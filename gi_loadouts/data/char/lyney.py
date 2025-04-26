from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Lyney(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.lyney
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=24.7646, defense=41.881, health_points=857.987976)
    ascn: BaseStat = BaseStat(attack=101.6894, defense=171.99, health_points=3523.3625488281)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.pyro
    cons_name: str = "Felis Fuscus"
    afln: str = "Hotel Bouffes d'ete"
    head: str = "Spectacle of Phantasmagoria"
