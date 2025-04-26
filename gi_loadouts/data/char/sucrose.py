from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Sucrose(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_anemo_perc
    name: CharName = CharName.sucrose
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=14.2464, defense=58.94175, health_points=775.02234)
    ascn: BaseStat = BaseStat(attack=50.97456, defense=210.8925, health_points=2773.016)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Ampulla"
    afln: str = "Knights of Favonius"
    head: str = "Harmless Sweetie"
