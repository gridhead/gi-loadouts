from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WaveridingWhirl(Catalyst):
    name: str = "Waveriding Whirl"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=13.3)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Fangs Flying To and Fro"
    refi_list: list[str] = [
        "Decreases Swimming Stamina consumption by 15%. In addition, for 10s after using an Elemental Skill, Max HP is increased by 20%. For every Hydro Elemental character in the party, Max HP is increased by another 12%, and the maximum increase that can be achieved in this way is 24%. Can be triggered once every 15s.",
        "Decreases Swimming Stamina consumption by 15%. In addition, for 10s after using an Elemental Skill, Max HP is increased by 25%. For every Hydro Elemental character in the party, Max HP is increased by another 15%, and the maximum increase that can be achieved in this way is 30%. Can be triggered once every 15s.",
        "Decreases Swimming Stamina consumption by 15%. In addition, for 10s after using an Elemental Skill, Max HP is increased by 30%. For every Hydro Elemental character in the party, Max HP is increased by another 18%, and the maximum increase that can be achieved in this way is 36%. Can be triggered once every 15s.",
        "Decreases Swimming Stamina consumption by 15%. In addition, for 10s after using an Elemental Skill, Max HP is increased by 35%. For every Hydro Elemental character in the party, Max HP is increased by another 21%, and the maximum increase that can be achieved in this way is 42%. Can be triggered once every 15s.",
        "Decreases Swimming Stamina consumption by 15%. In addition, for 10s after using an Elemental Skill, Max HP is increased by 40%. For every Hydro Elemental character in the party, Max HP is increased by another 24%, and the maximum increase that can be achieved in this way is 48%. Can be triggered once every 15s."
    ]
    file: str = "wrwl"
