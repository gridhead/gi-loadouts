from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Sayu(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.sayu
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.4792, defense=62.432476, health_points=993.8522)
    ascn: BaseStat = BaseStat(attack=73.27593, defense=223.38225, health_points=3555.9854)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.anemo
    cons_name: str = "Nyctereutes Minor"
    afln: str = "Shuumatsuban"
    head: str = "Mujina Ninja"
