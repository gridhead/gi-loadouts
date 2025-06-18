from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Azurelight(Sword):
    name: str = "Azurelight"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "White Mountain's Bounty"
    refi_list: list[str] = [
        "Within 12s after an Elemental Skill is used, ATK is increased by 24%. During this time, when the equipping character has 0 Energy, ATK will be further increased by 24%, and CRIT DMG will be increased by 40%.",
        "Within 12s after an Elemental Skill is used, ATK is increased by 30%. During this time, when the equipping character has 0 Energy, ATK will be further increased by 30%, and CRIT DMG will be increased by 50%.",
        "Within 12s after an Elemental Skill is used, ATK is increased by 36%. During this time, when the equipping character has 0 Energy, ATK will be further increased by 36%, and CRIT DMG will be increased by 60%.",
        "Within 12s after an Elemental Skill is used, ATK is increased by 42%. During this time, when the equipping character has 0 Energy, ATK will be further increased by 42%, and CRIT DMG will be increased by 70%.",
        "Within 12s after an Elemental Skill is used, ATK is increased by 48%. During this time, when the equipping character has 0 Energy, ATK will be further increased by 48%, and CRIT DMG will be increased by 80%."
    ]
    file: str = "azlt"
