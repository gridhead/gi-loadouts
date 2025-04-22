from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EyeofPerception(Catalyst):
    name: str = "Eye of Perception"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Echo"
    refi_list: list[str] = [
        "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 240% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 12s.",
        "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 270% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 11s.",
        "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 300% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 10s.",
        "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 330% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 9s.",
        "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 360% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 8s.",
    ]
    file: str = "eypt"
