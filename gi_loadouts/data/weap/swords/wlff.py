from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WhitelakeFrostfeather(Sword):
    name: str = "Whitelake Frostfeather"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Snow Swan's Finale"
    refi_list: list[str] = [
        "When the equipping character hits an opponent with their Elemental Skill, they gain \"Lake-Hued Lament\": ATK increases by 8% for 8s. This effect can trigger once every 0.1s. Max 3 stacks, and each stack's duration is independent. At 3 stacks, the CRIT DMG of any Stellar Glimmer reaction DMG caused by the equipping character is increased by 50%, and triggering Stellar Glimmer reactions or Stellar Glimmer reaction DMG will also restore 4 Elemental Energy to the character. This Energy recovery effect can trigger once every 3.5s. This effect can be triggered even when the equipping character is off-field.",
        "When the equipping character hits an opponent with their Elemental Skill, they gain \"Lake-Hued Lament\": ATK increases by 10% for 8s. This effect can trigger once every 0.1s. Max 3 stacks, and each stack's duration is independent. At 3 stacks, the CRIT DMG of any Stellar Glimmer reaction DMG caused by the equipping character is increased by 65%, and triggering Stellar Glimmer reactions or Stellar Glimmer reaction DMG will also restore 4.5 Elemental Energy to the character. This Energy recovery effect can trigger once every 3.5s. This effect can be triggered even when the equipping character is off-field.",
        "When the equipping character hits an opponent with their Elemental Skill, they gain \"Lake-Hued Lament\": ATK increases by 12% for 8s. This effect can trigger once every 0.1s. Max 3 stacks, and each stack's duration is independent. At 3 stacks, the CRIT DMG of any Stellar Glimmer reaction DMG caused by the equipping character is increased by 80%, and triggering Stellar Glimmer reactions or Stellar Glimmer reaction DMG will also restore 5 Elemental Energy to the character. This Energy recovery effect can trigger once every 3.5s. This effect can be triggered even when the equipping character is off-field.",
        "When the equipping character hits an opponent with their Elemental Skill, they gain \"Lake-Hued Lament\": ATK increases by 14% for 8s. This effect can trigger once every 0.1s. Max 3 stacks, and each stack's duration is independent. At 3 stacks, the CRIT DMG of any Stellar Glimmer reaction DMG caused by the equipping character is increased by 95%, and triggering Stellar Glimmer reactions or Stellar Glimmer reaction DMG will also restore 5.5 Elemental Energy to the character. This Energy recovery effect can trigger once every 3.5s. This effect can be triggered even when the equipping character is off-field.",
        "When the equipping character hits an opponent with their Elemental Skill, they gain \"Lake-Hued Lament\": ATK increases by 16% for 8s. This effect can trigger once every 0.1s. Max 3 stacks, and each stack's duration is independent. At 3 stacks, the CRIT DMG of any Stellar Glimmer reaction DMG caused by the equipping character is increased by 110%, and triggering Stellar Glimmer reactions or Stellar Glimmer reaction DMG will also restore 6 Elemental Energy to the character. This Energy recovery effect can trigger once every 3.5s. This effect can be triggered even when the equipping character is off-field.",
    ]
    file: str = "wlff"
