from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BreezeborneRefrain(Bow):
    name: str = "Breezeborne Refrain"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Viper's Ballad"
    refi_list: list[str] = [
        "Increases Energy Recharge by 20%. When the equipping character hits the opponent with their Elemental Skill or Elemental Burst, they gain a stack of \"Hymn of the Pure.\" This effect can trigger once every 0.03s, max 3 stacks, and at 3 stacks, all instances of \"Hymn of the Pure\" are cleared to give the equipping character \"Thus Lied the Viper\" instead. This grants nearby party members a 24% Stellar Glimmer reaction DMG boost for 12s, during which no stacks of \"Hymn of the Pure\" can be obtained. The aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Energy Recharge by 25%. When the equipping character hits the opponent with their Elemental Skill or Elemental Burst, they gain a stack of \"Hymn of the Pure.\" This effect can trigger once every 0.03s, max 3 stacks, and at 3 stacks, all instances of \"Hymn of the Pure\" are cleared to give the equipping character \"Thus Lied the Viper\" instead. This grants nearby party members a 30% Stellar Glimmer reaction DMG boost for 12s, during which no stacks of \"Hymn of the Pure\" can be obtained. The aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Energy Recharge by 30%. When the equipping character hits the opponent with their Elemental Skill or Elemental Burst, they gain a stack of \"Hymn of the Pure.\" This effect can trigger once every 0.03s, max 3 stacks, and at 3 stacks, all instances of \"Hymn of the Pure\" are cleared to give the equipping character \"Thus Lied the Viper\" instead. This grants nearby party members a 36% Stellar Glimmer reaction DMG boost for 12s, during which no stacks of \"Hymn of the Pure\" can be obtained. The aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Energy Recharge by 35%. When the equipping character hits the opponent with their Elemental Skill or Elemental Burst, they gain a stack of \"Hymn of the Pure.\" This effect can trigger once every 0.03s, max 3 stacks, and at 3 stacks, all instances of \"Hymn of the Pure\" are cleared to give the equipping character \"Thus Lied the Viper\" instead. This grants nearby party members a 42% Stellar Glimmer reaction DMG boost for 12s, during which no stacks of \"Hymn of the Pure\" can be obtained. The aforementioned effects can still trigger even when the equipping character is not on the field.",
        "Increases Energy Recharge by 40%. When the equipping character hits the opponent with their Elemental Skill or Elemental Burst, they gain a stack of \"Hymn of the Pure.\" This effect can trigger once every 0.03s, max 3 stacks, and at 3 stacks, all instances of \"Hymn of the Pure\" are cleared to give the equipping character \"Thus Lied the Viper\" instead. This grants nearby party members a 48% Stellar Glimmer reaction DMG boost for 12s, during which no stacks of \"Hymn of the Pure\" can be obtained. The aforementioned effects can still trigger even when the equipping character is not on the field.",
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=40.0)],
    ]
    file: str = "bbrn"
