from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Lynette(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_anemo_perc
    name: CharName = CharName.lynette
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=19.41072, defense=59.6856765747, health_points=1039.44177246)
    ascn: BaseStat = BaseStat(attack=69.452835083, defense=213.554245, health_points=3719.104)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.anemo
    cons_name: str = "Felis Alba"
    afln: str = "Hotel Bouffes d'ete"
    head: str = "Elegance in the Shadows"
