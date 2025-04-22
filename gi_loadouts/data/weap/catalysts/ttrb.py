from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TulaytullahsRemembrance(Catalyst):
    name: str = "Tulaytullah's Remembrance"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Bygone Azure Teardrop"
    refi_list: list[str] = [
        "Normal Attack SPD is increased by 10%. After the wielder unleashes an Elemental Skill, Normal Attack DMG will increase by 4.8% every second for 14s. After this character hits an opponent with a Normal Attack during this duration, Normal Attack DMG will be increased by 9.6%. This increase can be triggered once every 0.3s. The maximum Normal Attack DMG increase per single duration of the overall effect is 48%. The effect will be removed when the wielder leaves the field, and using the Elemental Skill again will reset all DMG buffs.",
        "Normal Attack SPD is increased by 12.5%. After the wielder unleashes an Elemental Skill, Normal Attack DMG will increase by 6% every second for 14s. After this character hits an opponent with a Normal Attack during this duration, Normal Attack DMG will be increased by 12%. This increase can be triggered once every 0.3s. The maximum Normal Attack DMG increase per single duration of the overall effect is 60%. The effect will be removed when the wielder leaves the field, and using the Elemental Skill again will reset all DMG buffs.",
        "Normal Attack SPD is increased by 15%. After the wielder unleashes an Elemental Skill, Normal Attack DMG will increase by 7.2% every second for 14s. After this character hits an opponent with a Normal Attack during this duration, Normal Attack DMG will be increased by 14.4%. This increase can be triggered once every 0.3s. The maximum Normal Attack DMG increase per single duration of the overall effect is 72%. The effect will be removed when the wielder leaves the field, and using the Elemental Skill again will reset all DMG buffs.",
        "Normal Attack SPD is increased by 17.5%. After the wielder unleashes an Elemental Skill, Normal Attack DMG will increase by 8.4% every second for 14s. After this character hits an opponent with a Normal Attack during this duration, Normal Attack DMG will be increased by 16.8%. This increase can be triggered once every 0.3s. The maximum Normal Attack DMG increase per single duration of the overall effect is 84%. The effect will be removed when the wielder leaves the field, and using the Elemental Skill again will reset all DMG buffs.",
        "Normal Attack SPD is increased by 20%. After the wielder unleashes an Elemental Skill, Normal Attack DMG will increase by 9.6% every second for 14s. After this character hits an opponent with a Normal Attack during this duration, Normal Attack DMG will be increased by 19.2%. This increase can be triggered once every 0.3s. The maximum Normal Attack DMG increase per single duration of the overall effect is 96%. The effect will be removed when the wielder leaves the field, and using the Elemental Skill again will reset all DMG buffs.",
    ]
    file: str = "ttrb"
