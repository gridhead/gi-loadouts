from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AquilaFavonia(Sword):
    name: str = "Aquila Favonia"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Falcon's Defiance"
    refi_list: list[str] = [
        "ATK is increased by 20%. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to 100% of ATK and dealing 200% of ATK as DMG to surrounding opponents. This effect can only occur once every 15s.",
        "ATK is increased by 25%. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to 115% of ATK and dealing 230% of ATK as DMG to surrounding opponents. This effect can only occur once every 15s.",
        "ATK is increased by 30%. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to 130% of ATK and dealing 260% of ATK as DMG to surrounding opponents. This effect can only occur once every 15s.",
        "ATK is increased by 35%. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to 145% of ATK and dealing 290% of ATK as DMG to surrounding opponents. This effect can only occur once every 15s.",
        "ATK is increased by 40%. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to 160% of ATK and dealing 320% of ATK as DMG to surrounding opponents. This effect can only occur once every 15s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=20)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=25)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=30)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=35)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=40)],
    ]
    file: str = "aqfv"
