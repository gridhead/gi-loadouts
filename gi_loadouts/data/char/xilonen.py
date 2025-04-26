from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Xilonen(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.0, 3: 18.0, 4: 18.0, 5: 27.0, 6: 36.0}
    __statname__: STAT = STAT.defense_perc
    name: CharName = CharName.xilonen
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=21.413, defense=72.3943, health_points=965.71313)
    ascn: BaseStat = BaseStat(attack=87.92693, defense=297.297, health_points=3965.7402)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.geo
    cons_name: str = "Panthera Ocelota"
    afln: str = "Nanatzcayan"
    head: str = "Ardent Flames Forge the Soul"
