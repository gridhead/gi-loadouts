from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Varesa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.varesa
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.7438, defense=60.84711, health_points=988.59283)
    ascn: BaseStat = BaseStat(attack=113.922714, defense=249.8769, health_points=4059.6965)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Mascara Luctatori"
    afln: str = "Teteocan"
    head: str = "Strength in Serenity"
