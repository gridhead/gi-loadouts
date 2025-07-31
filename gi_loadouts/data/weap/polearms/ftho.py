from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FracturedHalo(Polearm):
    name: str = "Fractured Halo"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Purifying Crown"
    refi_list: list[str] = [
        "After an Elemental Skill or Elemental Burst is used, ATK is increased by 24% for 20s. If the equipping character creates a Shield while this effect is active, they will gain the Electrifying Edict effect for 20s: All nearby party members deal 40% more Lunar-Charged DMG.",
        "After an Elemental Skill or Elemental Burst is used, ATK is increased by 30% for 20s. If the equipping character creates a Shield while this effect is active, they will gain the Electrifying Edict effect for 20s: All nearby party members deal 50% more Lunar-Charged DMG.",
        "After an Elemental Skill or Elemental Burst is used, ATK is increased by 36% for 20s. If the equipping character creates a Shield while this effect is active, they will gain the Electrifying Edict effect for 20s: All nearby party members deal 60% more Lunar-Charged DMG.",
        "After an Elemental Skill or Elemental Burst is used, ATK is increased by 42% for 20s. If the equipping character creates a Shield while this effect is active, they will gain the Electrifying Edict effect for 20s: All nearby party members deal 70% more Lunar-Charged DMG.",
        "After an Elemental Skill or Elemental Burst is used, ATK is increased by 48% for 20s. If the equipping character creates a Shield while this effect is active, they will gain the Electrifying Edict effect for 20s: All nearby party members deal 80% more Lunar-Charged DMG.",
    ]
    file: str = "ftho"
