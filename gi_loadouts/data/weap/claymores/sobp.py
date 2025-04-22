from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SongofBrokenPines(Claymore):
    name: str = "Song of Broken Pines"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=4.5)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_5
    refi_name: str = "Rebel's Banner-Hymn"
    refi_list: list[str] = [
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by 16%, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s. When you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by 12% and increases ATK by 20%. Once this effect is triggered, you will not gain Sigils of Whispers for 20s.Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by 20%, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s. When you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by 15% and increases ATK by 25%. Once this effect is triggered, you will not gain Sigils of Whispers for 20s.Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by 24%, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s. When you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by 18% and increases ATK by 30%. Once this effect is triggered, you will not gain Sigils of Whispers for 20s.Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by 28%, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s. When you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by 21% and increases ATK by 35%. Once this effect is triggered, you will not gain Sigils of Whispers for 20s.Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by 32%, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s. When you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by 24% and increases ATK by 40%. Once this effect is triggered, you will not gain Sigils of Whispers for 20s.Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=32.0)],
    ]
    file: str = "sobp"
