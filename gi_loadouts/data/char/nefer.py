from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import ATTR, STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Nefer(Char):
    # Nefer has 100 Elemental Mastery in her base statistics
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.nefer
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.8128, defense=62.2232, health_points=988.9742)
    ascn: BaseStat = BaseStat(attack=110.09981, defense=255.528, health_points=4061.2627)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.dendro
    cons_name: str = "Ludus Latrunculorum"
    afln: str = "Curatorium of Secrets"
    head: str = "Owner of the Curatorium of Secrets"

    @property
    def elemental_mastery(self) -> ATTR:
        return ATTR(stat_name=STAT.elemental_mastery, stat_data=100.0)
