from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FinaleoftheDeep(Sword):
    name: str = "Finale of the Deep"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "An End Sublime"
    refi_list: list[str] = [
        "When using an Elemental Skill, ATK will be increased by 12% for 15s, and a Bond of Life worth 25% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond of Life is cleared, a maximum of 150 ATK will be gained based on 2.4% of the total amount of the Life Bond cleared, lasting for 15s.",
        "When using an Elemental Skill, ATK will be increased by 15% for 15s, and a Bond of Life worth 25% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond of Life is cleared, a maximum of 187.5 ATK will be gained based on 3% of the total amount of the Life Bond cleared, lasting for 15s.",
        "When using an Elemental Skill, ATK will be increased by 18% for 15s, and a Bond of Life worth 25% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond of Life is cleared, a maximum of 225 ATK will be gained based on 3.6% of the total amount of the Life Bond cleared, lasting for 15s.",
        "When using an Elemental Skill, ATK will be increased by 21% for 15s, and a Bond of Life worth 25% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond of Life is cleared, a maximum of 262.5 ATK will be gained based on 4.2% of the total amount of the Life Bond cleared, lasting for 15s.",
        "When using an Elemental Skill, ATK will be increased by 24% for 15s, and a Bond of Life worth 25% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond of Life is cleared, a maximum of 300 ATK will be gained based on 4.8% of the total amount of the Life Bond cleared, lasting for 15s.",
    ]
    file: str = "fotd"
