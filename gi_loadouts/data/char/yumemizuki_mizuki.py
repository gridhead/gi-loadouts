from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class YumemizukiMizuki(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 28.8, 3: 57.6, 4: 57.6, 5: 86.4, 6: 115.2}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.yumemizuki_mizuki
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=16.758, defense=58.93255, health_points=991.4528)
    ascn: BaseStat = BaseStat(attack=68.81238, defense=242.0145, health_points=4071.4412)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Tapirus Somniator"
    afln: str = "Aisa Bathhouse"
    head: str = "Embrace of Enchanting Dreams"
