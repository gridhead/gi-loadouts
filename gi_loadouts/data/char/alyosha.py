from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Alyosha(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.7, 3: 13.4, 4: 13.4, 5: 20.1, 6: 26.8}
    __statname__: STAT = STAT.energy_recharge_perc
    name: CharName = CharName.alyosha
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=22.26, defense=58.94175, health_points=1002.9701)
    ascn: BaseStat = BaseStat(attack=79.64775, defense=210.8925, health_points=3588.6091)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Canis Borzoides"
    afln: str = "Snezhnaya"
    head: str = "Swift-Striding Hound"
