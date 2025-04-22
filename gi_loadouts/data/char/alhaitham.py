from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Alhaitham(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_dendro_perc
    name: CharName = CharName.alhaitham
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=24.3922, defense=60.84711, health_points=1039.1188)
    ascn: BaseStat = BaseStat(attack=100.16024, defense=249.8769, health_points=4267.1836)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.dendro
    cons_name: str = "Vultur Volans"
    afln: str = "Sumeru Akademiya"
    head: str = "Admonishing Instruction"
