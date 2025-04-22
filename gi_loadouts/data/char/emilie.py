from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Emilie(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.emilie
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.068, defense=56.8385, health_points=1056.2786)
    ascn: BaseStat = BaseStat(attack=107.04148, defense=233.415, health_points=4337.651)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.dendro
    cons_name: str = "Pomum de Ambra"
    afln: str = "Court of Fontaine"
    head: str = "A Thousand Scents Traced"
