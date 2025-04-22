from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CranesEchoingCall(Catalyst):
    name: str = "Crane's Echoing Call"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=3.6)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_5
    refi_name: str = "Cloudfall Axiom"
    refi_list: list[str] = [
        "After the equipping character hits an opponent with a Plunging Attack, all nearby party members' Plunging Attacks will deal 28% increased DMG for 20s. When nearby party members hit opponents with Plunging Attacks, they will restore 2.5 Energy to the equipping character. Energy can restored this way every 0.7s. This energy regain effect can be triggered even if the equipping character is not on the field.",
        "After the equipping character hits an opponent with a Plunging Attack, all nearby party members' Plunging Attacks will deal 41% increased DMG for 20s. When nearby party members hit opponents with Plunging Attacks, they will restore 2.75 Energy to the equipping character. Energy can restored this way every 0.7s. This energy regain effect can be triggered even if the equipping character is not on the field.",
        "After the equipping character hits an opponent with a Plunging Attack, all nearby party members' Plunging Attacks will deal 54% increased DMG for 20s. When nearby party members hit opponents with Plunging Attacks, they will restore 3 Energy to the equipping character. Energy can restored this way every 0.7s. This energy regain effect can be triggered even if the equipping character is not on the field.",
        "After the equipping character hits an opponent with a Plunging Attack, all nearby party members' Plunging Attacks will deal 67% increased DMG for 20s. When nearby party members hit opponents with Plunging Attacks, they will restore 3.25 Energy to the equipping character. Energy can restored this way every 0.7s. This energy regain effect can be triggered even if the equipping character is not on the field.",
        "After the equipping character hits an opponent with a Plunging Attack, all nearby party members' Plunging Attacks will deal 80% increased DMG for 20s. When nearby party members hit opponents with Plunging Attacks, they will restore 3.5 Energy to the equipping character. Energy can restored this way every 0.7s. This energy regain effect can be triggered even if the equipping character is not on the field.",
    ]
    file: str = "cegc"
