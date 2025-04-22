from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ScionoftheBlazingSun(Bow):
    name: str = "Scion of the Blazing Sun"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "The Way of Sunfire"
    refi_list: list[str] = [
            "After a Charged Attack hits an opponent, a Sunfire Arrow will descend upon the opponent hit, dealing 60% ATK as DMG, and applying the Heartsearer effect to the opponent damaged by said Arrow for 10s. Opponents affected by Heartsearer take 28% more Charged Attack DMG from the wielder. A Sunfire Arrow can be triggered once every 10s.",
            "After a Charged Attack hits an opponent, a Sunfire Arrow will descend upon the opponent hit, dealing 75% ATK as DMG, and applying the Heartsearer effect to the opponent damaged by said Arrow for 10s. Opponents affected by Heartsearer take 35% more Charged Attack DMG from the wielder. A Sunfire Arrow can be triggered once every 10s.",
            "After a Charged Attack hits an opponent, a Sunfire Arrow will descend upon the opponent hit, dealing 90% ATK as DMG, and applying the Heartsearer effect to the opponent damaged by said Arrow for 10s. Opponents affected by Heartsearer take 42% more Charged Attack DMG from the wielder. A Sunfire Arrow can be triggered once every 10s.",
            "After a Charged Attack hits an opponent, a Sunfire Arrow will descend upon the opponent hit, dealing 105% ATK as DMG, and applying the Heartsearer effect to the opponent damaged by said Arrow for 10s. Opponents affected by Heartsearer take 49% more Charged Attack DMG from the wielder. A Sunfire Arrow can be triggered once every 10s.",
            "After a Charged Attack hits an opponent, a Sunfire Arrow will descend upon the opponent hit, dealing 120% ATK as DMG, and applying the Heartsearer effect to the opponent damaged by said Arrow for 10s. Opponents affected by Heartsearer take 56% more Charged Attack DMG from the wielder. A Sunfire Arrow can be triggered once every 10s.",
        ]
    file: str = "sobs"
