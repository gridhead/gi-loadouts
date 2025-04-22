from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EarthShaker(Claymore):
    name: str = "Earth Shaker"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Oath of Qhapaq Nan"
    refi_list: list[str] = [
        "After a party member triggers a Pyro-related reaction, the equipping character's Elemental Skill DMG is increased by 16% for 8s. This effect can be triggered even when the triggering party member is not on the field.",
        "After a party member triggers a Pyro-related reaction, the equipping character's Elemental Skill DMG is increased by 20% for 8s. This effect can be triggered even when the triggering party member is not on the field.",
        "After a party member triggers a Pyro-related reaction, the equipping character's Elemental Skill DMG is increased by 24% for 8s. This effect can be triggered even when the triggering party member is not on the field.",
        "After a party member triggers a Pyro-related reaction, the equipping character's Elemental Skill DMG is increased by 28% for 8s. This effect can be triggered even when the triggering party member is not on the field.",
        "After a party member triggers a Pyro-related reaction, the equipping character's Elemental Skill DMG is increased by 32% for 8s. This effect can be triggered even when the triggering party member is not on the field.",
    ]
    file: str = "ehsr"
