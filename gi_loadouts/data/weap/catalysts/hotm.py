from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class HymnOfTheMaelstrom(Catalyst):
    name: str = "Hymn of the Maelstrom"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Rondo of Slumber"
    refi_list: list[str] = [
        "Increases Healing Bonus by 4%.\nWhen performing healing, the equipping character gains the \"Vatsamonga's Vatic Vintage\" effect, which increases Max HP by 4% as well as increases the currently active party member's ATK by 0.4% for every 1,000 Max HP the equipping character has over 40,000. A maximum of 8% ATK can be gained in this way. This effect lasts 10s, max 3 stacks.\nWhen a nearby party member triggers a Frozen or Stellar Swirl reaction, the aforementioned Max HP and ATK boosts will be further increased by 75% for the next 5s.\nThe aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Healing Bonus by 5%.\nWhen performing healing, the equipping character gains the \"Vatsamonga's Vatic Vintage\" effect, which increases Max HP by 5% as well as increases the currently active party member's ATK by 0.5% for every 1,000 Max HP the equipping character has over 40,000. A maximum of 10% ATK can be gained in this way. This effect lasts 10s, max 3 stacks.\nWhen a nearby party member triggers a Frozen or Stellar Swirl reaction, the aforementioned Max HP and ATK boosts will be further increased by 75% for the next 5s.\nThe aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Healing Bonus by 6%.\nWhen performing healing, the equipping character gains the \"Vatsamonga's Vatic Vintage\" effect, which increases Max HP by 6% as well as increases the currently active party member's ATK by 0.6% for every 1,000 Max HP the equipping character has over 40,000. A maximum of 12% ATK can be gained in this way. This effect lasts 10s, max 3 stacks.\nWhen a nearby party member triggers a Frozen or Stellar Swirl reaction, the aforementioned Max HP and ATK boosts will be further increased by 75% for the next 5s.\nThe aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Healing Bonus by 7%.\nWhen performing healing, the equipping character gains the \"Vatsamonga's Vatic Vintage\" effect, which increases Max HP by 7% as well as increases the currently active party member's ATK by 0.7% for every 1,000 Max HP the equipping character has over 40,000. A maximum of 14% ATK can be gained in this way. This effect lasts 10s, max 3 stacks.\nWhen a nearby party member triggers a Frozen or Stellar Swirl reaction, the aforementioned Max HP and ATK boosts will be further increased by 75% for the next 5s.\nThe aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Healing Bonus by 8%.\nWhen performing healing, the equipping character gains the \"Vatsamonga's Vatic Vintage\" effect, which increases Max HP by 8% as well as increases the currently active party member's ATK by 0.8% for every 1,000 Max HP the equipping character has over 40,000. A maximum of 16% ATK can be gained in this way. This effect lasts 10s, max 3 stacks.\nWhen a nearby party member triggers a Frozen or Stellar Swirl reaction, the aforementioned Max HP and ATK boosts will be further increased by 75% for the next 5s.\nThe aforementioned effects can still trigger even when the equipping character is not on the field.",
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=4.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=5.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=6.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=7.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=8.0)],
    ]
    file: str = "hotm"
