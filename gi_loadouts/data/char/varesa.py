from gi_loadouts.type.char import BaseStat, Char, CharName
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Varesa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.varesa
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=0.00, defense=0.00, health_points=0.00)
    ascn: BaseStat = BaseStat(attack=0.00, defense=0.00, health_points=0.00)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Mascara Luctatori"
    afln: str = "Teteocan"
    head: str = "Strength in Serenity"
