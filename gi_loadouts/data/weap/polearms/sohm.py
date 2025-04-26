from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier

# Dynamic calculation has not been implemented

class StaffOfHoma(Polearm):
    name: str = "Staff of Homa"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Reckless Cinnabar"
    refi_list: list[str] = [
        "HP increased by 20%. Additionally, provides an ATK Bonus based on 0.8% of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK bonus is increased by an additional 1% of Max HP.",
        "HP increased by 25%. Additionally, provides an ATK Bonus based on 1% of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK bonus is increased by an additional 1.2% of Max HP.",
        "HP increased by 30%. Additionally, provides an ATK Bonus based on 1.2% of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK bonus is increased by an additional 1.4% of Max HP.",
        "HP increased by 35%. Additionally, provides an ATK Bonus based on 1.4% of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK bonus is increased by an additional 1.6% of Max HP.",
        "HP increased by 40%. Additionally, provides an ATK Bonus based on 1.6% of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK bonus is increased by an additional 1.8% of Max HP.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=40.0)],
    ]
    file: str = "sohm"
