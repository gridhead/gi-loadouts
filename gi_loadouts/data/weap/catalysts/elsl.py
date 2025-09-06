from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EtherlightSpindlelute(Catalyst):
    name: str = "Etherlight Spindlelute"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "The Final Voice"
    refi_list: list[str] = [
        "For 20s after using an Elemental Skill, the equipping character's Elemental Mastery is increased by 100.",
        "For 20s after using an Elemental Skill, the equipping character's Elemental Mastery is increased by 125.",
        "For 20s after using an Elemental Skill, the equipping character's Elemental Mastery is increased by 150.",
        "For 20s after using an Elemental Skill, the equipping character's Elemental Mastery is increased by 175.",
        "For 20s after using an Elemental Skill, the equipping character's Elemental Mastery is increased by 200.",
    ]
    file: str = "elsl"
