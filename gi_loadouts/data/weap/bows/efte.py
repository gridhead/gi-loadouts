from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ElegyfortheEnd(Bow):
    name: str = "Elegy for the End"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "The Parting Refrain"
    refi_list: list[str] = [
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 60.When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field. When you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s.\"Millennial Movement: Farewell Song\" increases Elemental Mastery by 100 and increases ATK by 20%. Once this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 75.When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field. When you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s.\"Millennial Movement: Farewell Song\" increases Elemental Mastery by 125 and increases ATK by 25%. Once this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 90.When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field. When you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s.\"Millennial Movement: Farewell Song\" increases Elemental Mastery by 150 and increases ATK by 30%. Once this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 105.When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field. When you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s.\"Millennial Movement: Farewell Song\" increases Elemental Mastery by 175 and increases ATK by 35%. Once this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
        "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 120.When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field. When you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s.\"Millennial Movement: Farewell Song\" increases Elemental Mastery by 200 and increases ATK by 40%. Once this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=60.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=75.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=90.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=105.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=120.0)],
    ]
    file: str = "efte"
