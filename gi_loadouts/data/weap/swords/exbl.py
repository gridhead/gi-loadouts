from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ExaiphanesBlade(Sword):
    name: str = "Exaiphanes Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Traveler's Path"
    refi_list: list[str] = [
        "When the Traveler equips this, their ATK will increase by 16% for 8s after they hit an opponent. At the same time, they will also regenerate 3 Elemental Energy. This effect can trigger once every 5s. This can be triggered even when the character is not on the field.",
        "When the Traveler equips this, their CRIT DMG increases by 6% for every Element they have resonated with. Additionally, the Traveler's ATK will also increase by 20% for 8s, and regenerate 3 Elemental Energy, after they attack and hit an opponent. This effect can trigger once every 5s. This can be triggered even when the character is not on the field.",
        "When the Traveler equips this, their CRIT DMG increases by 6% for every Element they have resonated with. Additionally, the Traveler's ATK will also increase by 24% for 8s, and regenerate 5 Elemental Energy, after they attack and hit an opponent. This effect can trigger once every 5s. This can be triggered even when the character is not on the field.",
        "When the Traveler equips this, their CRIT DMG increases by 6% for every Element they have resonated with. Additionally, the Traveler's ATK will also increase by 32% for 8s, and regenerate 5 Elemental Energy, after they attack and hit an opponent. This effect can trigger once every 5s. This can be triggered even when the character is not on the field.",
        "When the Traveler equips this, their CRIT DMG increases by 6% for every Element they have resonated with. Additionally, the Traveler's ATK will also increase by 40% for 8s, and regenerate 5 Elemental Energy, after they attack and hit an opponent. This effect can trigger once every 5s. This can be triggered even when the character is not on the field.",
    ]
    file: str = "exbl"
