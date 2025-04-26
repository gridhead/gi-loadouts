from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheFirstGreatMagic(Bow):
    name: str = "The First Great Magic"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Parsifal the Great"
    refi_list: list[str] = [
            "DMG dealt by Charged Attacks increased by 16%. For every party member with the same Elemental Type as the wielder (including the wielder themselves), gain 1 Gimmick stack. For every party member with a different Elemental Type from the wielder, gain 1 Theatrics stack. When the wielder has 1/2/3 or more Gimmick stacks, ATK will be increased by 16%/32%/48%. When the wielder has 1/2/3 or more Theatrics stacks, Movement SPD will be increased by 4%/7%/10%.",
            "DMG dealt by Charged Attacks increased by 20%. For every party member with the same Elemental Type as the wielder (including the wielder themselves), gain 1 Gimmick stack. For every party member with a different Elemental Type from the wielder, gain 1 Theatrics stack. When the wielder has 1/2/3 or more Gimmick stacks, ATK will be increased by 20%/40%/60%. When the wielder has 1/2/3 or more Theatrics stacks, Movement SPD will be increased by 6%/9%/12%.",
            "DMG dealt by Charged Attacks increased by 24%. For every party member with the same Elemental Type as the wielder (including the wielder themselves), gain 1 Gimmick stack. For every party member with a different Elemental Type from the wielder, gain 1 Theatrics stack. When the wielder has 1/2/3 or more Gimmick stacks, ATK will be increased by 24%/48%/72%. When the wielder has 1/2/3 or more Theatrics stacks, Movement SPD will be increased by 8%/11%/14%.",
            "DMG dealt by Charged Attacks increased by 28%. For every party member with the same Elemental Type as the wielder (including the wielder themselves), gain 1 Gimmick stack. For every party member with a different Elemental Type from the wielder, gain 1 Theatrics stack. When the wielder has 1/2/3 or more Gimmick stacks, ATK will be increased by 28%/56%/84%. When the wielder has 1/2/3 or more Theatrics stacks, Movement SPD will be increased by 10%/13%/16%.",
            "DMG dealt by Charged Attacks increased by 32%. For every party member with the same Elemental Type as the wielder (including the wielder themselves), gain 1 Gimmick stack. For every party member with a different Elemental Type from the wielder, gain 1 Theatrics stack. When the wielder has 1/2/3 or more Gimmick stacks, ATK will be increased by 32%/64%/96%. When the wielder has 1/2/3 or more Theatrics stacks, Movement SPD will be increased by 12%/15%/18%.",
        ]
    file: str = "tfgm"
