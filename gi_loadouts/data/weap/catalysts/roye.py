from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RingofYaxche(Catalyst):
    name: str = "Ring of Yaxche"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Echoes of the Plentiful Land"
    refi_list: list[str] = [
        "Using an Elemental Skill grants the Jade-Forged Crown effect: Every 1,000 Max HP will increase the Normal Attack DMG dealt by the equipping character by 0.6% for 10s. Normal Attack DMG can be increased this way by a maximum of 16%.",
        "Using an Elemental Skill grants the Jade-Forged Crown effect: Every 1,000 Max HP will increase the Normal Attack DMG dealt by the equipping character by 0.7% for 10s. Normal Attack DMG can be increased this way by a maximum of 20%.",
        "Using an Elemental Skill grants the Jade-Forged Crown effect: Every 1,000 Max HP will increase the Normal Attack DMG dealt by the equipping character by 0.8% for 10s. Normal Attack DMG can be increased this way by a maximum of 24%.",
        "Using an Elemental Skill grants the Jade-Forged Crown effect: Every 1,000 Max HP will increase the Normal Attack DMG dealt by the equipping character by 0.9% for 10s. Normal Attack DMG can be increased this way by a maximum of 28%.",
        "Using an Elemental Skill grants the Jade-Forged Crown effect: Every 1,000 Max HP will increase the Normal Attack DMG dealt by the equipping character by 1% for 10s. Normal Attack DMG can be increased this way by a maximum of 32%."
    ]
    file: str = "roye"
