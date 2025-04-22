from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AstralVulturesCrimsonPlumage(Bow):
    name: str = "Astral Vulture's Crimson Plumage"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "The Moonring Sighted"
    refi_list: list[str] = [
        "For 12s after triggering a Swirl reaction, ATK increases by 24%. In addition, when 1/2 or more characters in the party are of a different Elemental Type from the equipping character, the DMG dealt by the equipping character's Charged Attacks is increased by 20%/48% and Elemental Burst DMG dealt is increased by 10%/24%.",
        "For 12s after triggering a Swirl reaction, ATK increases by 30%. In addition, when 1/2 or more characters in the party are of a different Elemental Type from the equipping character, the DMG dealt by the equipping character's Charged Attacks is increased by 25%/60% and Elemental Burst DMG dealt is increased by 12.5%/30%.",
        "For 12s after triggering a Swirl reaction, ATK increases by 36%. In addition, when 1/2 or more characters in the party are of a different Elemental Type from the equipping character, the DMG dealt by the equipping character's Charged Attacks is increased by 30%/72% and Elemental Burst DMG dealt is increased by 15%/36%.",
        "For 12s after triggering a Swirl reaction, ATK increases by 42%. In addition, when 1/2 or more characters in the party are of a different Elemental Type from the equipping character, the DMG dealt by the equipping character's Charged Attacks is increased by 35%/84% and Elemental Burst DMG dealt is increased by 17.5%/42%.",
        "For 12s after triggering a Swirl reaction, ATK increases by 48%. In addition, when 1/2 or more characters in the party are of a different Elemental Type from the equipping character, the DMG dealt by the equipping character's Charged Attacks is increased by 40%/96% and Elemental Burst DMG dealt is increased by 20%/48%.",
    ]
    file: str = "avcp"
