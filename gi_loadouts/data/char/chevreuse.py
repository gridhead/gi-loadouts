from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Chevreuse(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.chevreuse
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.205280303955, defense=50.701351165771, health_points=1002.9700927734)
    ascn: BaseStat = BaseStat(attack=57.983562469482, defense=181.40849304199, health_points=3588.6091308594)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.pyro
    cons_name: str = "Sclopetum Ensiferum"
    afln: str = "Special Security and Surveillance Patrol"
    head: str = "Executor of Justice"
