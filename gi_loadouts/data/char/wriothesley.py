from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Wriothesley(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.wriothesley
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=24.206, defense=59.41119, health_points=1058.18518)
    ascn: BaseStat = BaseStat(attack=99.39566, defense=243.9801, health_points=4345.48)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.cryo
    cons_name: str = "Cerberus"
    afln: str = "Fortress of Meropide"
    head: str = "Emissary of Solitary Iniquity"
