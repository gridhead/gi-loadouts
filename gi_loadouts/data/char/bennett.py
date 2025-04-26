from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Bennett(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.7, 3: 13.4, 4: 13.4, 5: 20.1, 6: 26.8}
    __statname__: STAT = STAT.energy_recharge_perc
    name: CharName = CharName.bennett
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.0272, defense=64.66425, health_points=1039.4418)
    ascn: BaseStat = BaseStat(attack=57.34638, defense=231.3675, health_points=3719.104)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.pyro
    cons_name: str = "Rota Calamitas"
    afln: str = "Adventurers' Guild"
    head: str = "Trial by Fire"
