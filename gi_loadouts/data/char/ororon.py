from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Ororon(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Ororon"
    rare: Rare = Rare.Star_4
    """
    TODO: Change the default values after the values are updated in Genshin Impact Wiki
    """
    base: BaseStat = BaseStat(attack=20.4792, defense=49.2135, health_points=775.02234)
    ascn: BaseStat = BaseStat(attack=73.275939, defense=176.085, health_points=2773.016)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.electro
    cons_name: str = "Vampyrum Spectrum"
    afln: str = "Masters of the Night-Wind"
    head: str = "Shadow of the Night-Wind"
