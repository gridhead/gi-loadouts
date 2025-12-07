from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AthameArtis(Sword):
    name: str = "Athame Artis"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Day King's Splendor Solis"
    refi_list: list[str] = [
        "CRIT DMG from Elemental Bursts is increased by 16%. When Elemental Burst hits an opponent, ATK is increased by 20%, and nearby active party members' ATK is increased by 16% for 3s. When the party possesses Hexerei: Secret Rite effects, the aforementioned effects are increased by an additional 75%. This effect can be triggered even if the equipping character is off-field.",
        "CRIT DMG from Elemental Bursts is increased by 20%. When Elemental Burst hits an opponent, ATK is increased by 25%, and nearby active party members' ATK is increased by 20% for 3s. When the party possesses Hexerei: Secret Rite effects, the aforementioned effects are increased by an additional 75%. This effect can be triggered even if the equipping character is off-field.",
        "CRIT DMG from Elemental Bursts is increased by 24%. When Elemental Burst hits an opponent, ATK is increased by 30%, and nearby active party members' ATK is increased by 24% for 3s. When the party possesses Hexerei: Secret Rite effects, the aforementioned effects are increased by an additional 75%. This effect can be triggered even if the equipping character is off-field.",
        "CRIT DMG from Elemental Bursts is increased by 28%. When Elemental Burst hits an opponent, ATK is increased by 35%, and nearby active party members' ATK is increased by 28% for 3s. When the party possesses Hexerei: Secret Rite effects, the aforementioned effects are increased by an additional 75%. This effect can be triggered even if the equipping character is off-field.",
        "CRIT DMG from Elemental Bursts is increased by 32%. When Elemental Burst hits an opponent, ATK is increased by 40%, and nearby active party members' ATK is increased by 32% for 3s. When the party possesses Hexerei: Secret Rite effects, the aforementioned effects are increased by an additional 75%. This effect can be triggered even if the equipping character is off-field.",
    ]
    file: str = "aeas"
