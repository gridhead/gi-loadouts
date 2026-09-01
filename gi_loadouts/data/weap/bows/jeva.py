from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class JadeVista(Bow):
    name: str = "Jade Vista"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "A Candle Woven From the Night"
    refi_list: list[str] = [
        "For every party member other than the equipping character:\nWho is of the same Elemental Type as the equipper: The equipping character's Elemental Mastery is increased by 64;\nWho is not of the same Elemental Type as the equipper: The equipping character's ATK increases by 12%. The two effects described above can stack up to 3 times in total, with Elemental Mastery buffs applied first.",
        "For every party member other than the equipping character:\nWho is of the same Elemental Type as the equipper: The equipping character's Elemental Mastery is increased by 80;\nWho is not of the same Elemental Type as the equipper: The equipping character's ATK increases by 15%. The two effects described above can stack up to 3 times in total, with Elemental Mastery buffs applied first.",
        "For every party member other than the equipping character:\nWho is of the same Elemental Type as the equipper: The equipping character's Elemental Mastery is increased by 96;\nWho is not of the same Elemental Type as the equipper: The equipping character's ATK increases by 18%. The two effects described above can stack up to 3 times in total, with Elemental Mastery buffs applied first.",
        "For every party member other than the equipping character:\nWho is of the same Elemental Type as the equipper: The equipping character's Elemental Mastery is increased by 112;\nWho is not of the same Elemental Type as the equipper: The equipping character's ATK increases by 21%. The two effects described above can stack up to 3 times in total, with Elemental Mastery buffs applied first.",
        "For every party member other than the equipping character:\nWho is of the same Elemental Type as the equipper: The equipping character's Elemental Mastery is increased by 128;\nWho is not of the same Elemental Type as the equipper: The equipping character's ATK increases by 24%. The two effects described above can stack up to 3 times in total, with Elemental Mastery buffs applied first.",
    ]
    file: str = "jeva"
