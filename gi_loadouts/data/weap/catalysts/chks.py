from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ClashOfKings(Catalyst):
    name: str = "Clash of Kings"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Without Heed for Day nor Night"
    refi_list: list[str] = [
        'Using an Elemental Skill grants the equipping character "Laws of the Board," which increases their ATK by 20% and their Elemental Mastery by 100. This effect lasts 6s and can trigger once every 12s. Does not stack. The duration of this effect will also be extended by 6s if the equipping character hits an opponent with a Charged Attack while it is active. The effect can be extended for max 6s in this way.',
        'Using an Elemental Skill grants the equipping character "Laws of the Board," which increases their ATK by 25% and their Elemental Mastery by 125. This effect lasts 6s and can trigger once every 12s. Does not stack. The duration of this effect will also be extended by 6s if the equipping character hits an opponent with a Charged Attack while it is active. The effect can be extended for max 6s in this way.',
        'Using an Elemental Skill grants the equipping character "Laws of the Board," which increases their ATK by 30% and their Elemental Mastery by 150. This effect lasts 6s and can trigger once every 12s. Does not stack. The duration of this effect will also be extended by 6s if the equipping character hits an opponent with a Charged Attack while it is active. The effect can be extended for max 6s in this way.',
        'Using an Elemental Skill grants the equipping character "Laws of the Board," which increases their ATK by 25% and their Elemental Mastery by 175. This effect lasts 6s and can trigger once every 12s. Does not stack. The duration of this effect will also be extended by 6s if the equipping character hits an opponent with a Charged Attack while it is active. The effect can be extended for max 6s in this way.',
        'Using an Elemental Skill grants the equipping character "Laws of the Board," which increases their ATK by 40% and their Elemental Mastery by 200. This effect lasts 6s and can trigger once every 12s. Does not stack. The duration of this effect will also be extended by 6s if the equipping character hits an opponent with a Charged Attack while it is active. The effect can be extended for max 6s in this way.',
    ]
    file: str = "chks"
