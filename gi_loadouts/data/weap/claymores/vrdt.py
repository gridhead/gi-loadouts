from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Verdict(Claymore):
    name: str = "Verdict"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Many Oaths of Dawn and Dusk"
    refi_list: list[str] = [
        "Increases ATK by 20%. When characters in your party obtain Elemental Shards from Crystallize reactions, the equipping character will gain 1 Seal, increasing Elemental Skill DMG by 18%. The Seal lasts for 15s, and the equipped may have up to 2 Seals at once. All of the equipper's Seals will disappear 0.2s after their Elemental Skill deals DMG.",
        "Increases ATK by 25%. When characters in your party obtain Elemental Shards from Crystallize reactions, the equipping character will gain 1 Seal, increasing Elemental Skill DMG by 22.5%. The Seal lasts for 15s, and the equipped may have up to 2 Seals at once. All of the equipper's Seals will disappear 0.2s after their Elemental Skill deals DMG.",
        "Increases ATK by 30%. When characters in your party obtain Elemental Shards from Crystallize reactions, the equipping character will gain 1 Seal, increasing Elemental Skill DMG by 27%. The Seal lasts for 15s, and the equipped may have up to 2 Seals at once. All of the equipper's Seals will disappear 0.2s after their Elemental Skill deals DMG.",
        "Increases ATK by 35%. When characters in your party obtain Elemental Shards from Crystallize reactions, the equipping character will gain 1 Seal, increasing Elemental Skill DMG by 31.5%. The Seal lasts for 15s, and the equipped may have up to 2 Seals at once. All of the equipper's Seals will disappear 0.2s after their Elemental Skill deals DMG.",
        "Increases ATK by 40%. When characters in your party obtain Elemental Shards from Crystallize reactions, the equipping character will gain 1 Seal, increasing Elemental Skill DMG by 36%. The Seal lasts for 15s, and the equipped may have up to 2 Seals at once. All of the equipper's Seals will disappear 0.2s after their Elemental Skill deals DMG.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=40.0)],
    ]
    file: str = "vrdt"
