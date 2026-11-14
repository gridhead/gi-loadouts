from ...type.char import BaseStat, Char
from ...type.rare import Rare
from ...type.stat import ATTR, STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Mitya(Char):
    # Mitya has 100 Elemental Mastery in her base statistics
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Mitya"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=20.482, defense=61.6249, health_points=905.654)
    ascn: BaseStat = BaseStat(attack=84.10402, defense=253.071, health_points=3719.105)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Nodus Gordianus"
    afln: str = "Royal Energy Commission of Snezhnaya"
    head: str = "Rules Set at Naught"

    @property
    def elemental_mastery(self) -> ATTR:
        return ATTR(stat_name=STAT.elemental_mastery, stat_data=100.0)
