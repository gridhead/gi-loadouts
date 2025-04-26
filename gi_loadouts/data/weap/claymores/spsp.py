from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SerpentSpine(Claymore):
    name: str = "Serpent Spine"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Wavesplitter"
    refi_list: list[str] = [
        "Every 4s a character is on the field, they will deal 6% more DMG and take 3%  more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG.",
        "Every 4s a character is on the field, they will deal 7% more DMG and take 2.7%  more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG.",
        "Every 4s a character is on the field, they will deal 8% more DMG and take 2.4%  more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG.",
        "Every 4s a character is on the field, they will deal 9% more DMG and take 2.2%  more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG.",
        "Every 4s a character is on the field, they will deal 10% more DMG and take 2%  more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG.",
    ]
    file: str = "spsp"
