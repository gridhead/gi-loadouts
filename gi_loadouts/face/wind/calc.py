from gi_loadouts.data.arti import ArtiList
from gi_loadouts.data.char import __charmaps__
from gi_loadouts.data.weap import Family
from gi_loadouts.type.arti import Collection
from gi_loadouts.type.calc import CHAR, TEAM, WEAP
from gi_loadouts.type.levl import Level
from gi_loadouts.type.stat import ATTR, STAT, __revmap__
from gi_loadouts.type.weap import WeaponStatType


class Assess:
    def __init__(self):
        self.collection = Collection()
        self.c_team = None
        self.c_weap = None
        self.c_tyvt = None
        self.c_char = None

    def char_keep(self):
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            # MAIN
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))

            # BASE
            self.c_char.attack = ATTR(stat_name=STAT.attack, stat_data=char.attack)
            self.c_char.defense = ATTR(stat_name=STAT.defense, stat_data=char.defense)
            self.c_char.health_points = ATTR(stat_name=STAT.health_points, stat_data=char.health_points)

            # SUBSTATS
            prev_stat_data = getattr(self.c_char, self.c_char.revmap[char.seco.stat_name]).stat_data
            curt_stat_data = char.seco.stat_data
            setattr(
                self.c_char,
                self.c_char.revmap[char.seco.stat_name],
                ATTR(
                    stat_name=char.seco.stat_name,
                    stat_data=prev_stat_data + curt_stat_data
                )
            )

    def char_stat(self):
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            # SUBSTATS
            """
            The SUBSTATS need to be calculated before the BASE due to implications of changes in BASE attributes
            on characters that scale on ATK %, DEF % and HP %.

            ATK % scaling = Aether, Amber, Charlotte, Chongyun, Collei, Faruzan, Fischl, Freminet, Gaming, Kujou Sara, Lumine, Rosaria, Shenhe, Thoma, Xianyun, Xingqiu, Xinyan,
            DEF % scaling = Noelle,
            HP  % scaling = Baizhu, Barbara, Candace, Chevreuse, Dehya, Dori, Kirara, Kuki Shinobu, Mika, Nilou, Yaoyao
            """
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            char_substats_prev_data = getattr(self.c_tyvt, self.c_tyvt.revmap[char.seco.stat_name]).stat_data
            char_substats_curt_data = getattr(self.c_char, self.c_char.revmap[char.seco.stat_name]).stat_data
            setattr(
                self.c_tyvt,
                self.c_tyvt.revmap[char.seco.stat_name],
                ATTR(
                    stat_name=char.seco.stat_name,
                    stat_data=char_substats_prev_data + char_substats_curt_data
                )
            )

            # BASE
            self.c_tyvt.attack = ATTR(
                stat_name=STAT.attack,
                stat_data=(self.c_char.attack.stat_data + self.c_weap.base.stat_data) * (100 + self.c_tyvt.attack_perc.stat_data) / 100.0 + self.c_tyvt.attack.stat_data
            )
            self.c_tyvt.health_points = ATTR(
                stat_name=STAT.health_points,
                stat_data=self.c_char.health_points.stat_data * (100 + self.c_tyvt.health_points_perc.stat_data) / 100.0 + self.c_tyvt.health_points.stat_data
            )
            self.c_tyvt.defense = ATTR(
                stat_name=STAT.defense,
                stat_data=self.c_char.defense.stat_data * (100 + self.c_tyvt.defense_perc.stat_data) / 100.0 + self.c_tyvt.defense.stat_data
            )

            # ADDENDUM
            self.c_tyvt.addendum_base_attack = ATTR(stat_name=STAT.attack, stat_data=self.c_char.attack.stat_data + self.c_weap.base.stat_data)
            self.c_tyvt.addendum_plus_attack = ATTR(stat_name=STAT.attack, stat_data=self.c_tyvt.attack.stat_data - self.c_tyvt.addendum_base_attack.stat_data)
            self.c_tyvt.addendum_base_health_points = ATTR(stat_name=STAT.health_points, stat_data=self.c_char.health_points.stat_data)
            self.c_tyvt.addendum_plus_health_points = ATTR(stat_name=STAT.health_points, stat_data=self.c_tyvt.health_points.stat_data - self.c_tyvt.addendum_base_health_points.stat_data)
            self.c_tyvt.addendum_base_defense = ATTR(stat_name=STAT.defense, stat_data=self.c_char.defense.stat_data)
            self.c_tyvt.addendum_plus_defense = ATTR(stat_name=STAT.defense, stat_data=self.c_tyvt.defense.stat_data - self.c_tyvt.addendum_base_defense.stat_data)

    def weap_keep(self):
        if (self.weap_area_type.currentText().strip() != "" and
            self.weap_area_name.currentText().strip() != "" and
            self.weap_area_refn.currentText().strip() != "" and
            self.weap_area_levl.currentText().strip() != ""):
            # MAIN
            kind = self.weap_area_type.currentText().strip()
            name = self.weap_area_name.currentText()
            weap = Family[kind][name]
            refn = self.weap_area_refn.currentIndex()
            weap.levl = getattr(Level, self.weap_area_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.c_weap.base = ATTR(stat_name=WeaponStatType.attack.value, stat_data=weap.main_stat.stat_data)
            if weap.seco_stat.stat_name != WeaponStatType.none:
                self.c_weap.seco = ATTR(
                    stat_name=weap.seco_stat_calc.stat_name.value,
                    stat_data=weap.seco_stat_calc.stat_data
                )
            if len(weap.refi_stat) != 0:
                self.c_weap.refn = weap.refi_stat[refn]

    def weap_stat(self):
        # BASE
        # Base attack is calculated in self.char_stat()

        # SUBSTATS
        prev = getattr(self.c_tyvt, self.c_tyvt.revmap[self.c_weap.seco.stat_name]).stat_data
        curt = self.c_weap.seco.stat_data
        setattr(
            self.c_tyvt,
            self.c_tyvt.revmap[self.c_weap.seco.stat_name],
            ATTR(stat_name=self.c_weap.seco.stat_name, stat_data=prev + curt)
        )

        # REFINEMENT
        for item in self.c_tyvt.revmap:
            for indx in self.c_weap.refn:
                if item == indx.stat_name.value:
                    prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                    curt = indx.stat_data
                    setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev + curt))

    def arti_keep(self):
        # ARTIUNIT
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            if getattr(self, f"arti_{part}_type").currentText().strip() != "":
                for indx in ["main", "a", "b", "c", "d"]:
                    if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() != "":
                        if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() == "None":
                            setattr(
                                self.c_team,
                                f"{part}_{indx}",
                                ATTR(
                                    stat_name=STAT.none,
                                    stat_data=0.0
                                )
                            )
                        else:
                            setattr(
                                self.c_team,
                                f"{part}_{indx}",
                                ATTR(
                                    stat_name=__revmap__[getattr(self, f"arti_{part}_name_{indx}").currentText().strip()],
                                    stat_data=float(getattr(self, f"arti_{part}_data_{indx}").text().strip())
                                )
                            )

        # SETBONUS
        if self.collection.quad != "":
            pack = getattr(ArtiList, self.collection.quad.replace(" ", "_").replace("'", "").replace("-", "_"))
            self.c_team.pairdata_a = pack.value.pairdata
            self.c_team.quaddata = pack.value.quaddata
        elif self.collection.pair != []:
            if len(self.collection.pair) == 1:
                pack_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_a = pack_a.value.pairdata
            elif len(self.collection.pair) == 2:
                pack_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_a = pack_a.value.pairdata
                pack_b = getattr(ArtiList, self.collection.pair[1].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_b = pack_b.value.pairdata

    def arti_stat(self):
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            # ARTIUNIT
            for item in self.c_tyvt.revmap:
                for kind in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
                    for indx in ["main", "a", "b", "c", "d"]:
                        if getattr(self.c_team, f"{kind}_{indx}").stat_name == item:
                            prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                            curt = getattr(self.c_team, f"{kind}_{indx}").stat_data
                            setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev+curt))

            # SETBONUS
            for item in self.c_tyvt.revmap:
                for indx in ["pairdata_a", "pairdata_b", "quaddata"]:
                    lict = getattr(self.c_team, indx)
                    if len(indx) != 0:
                        for advn in lict:
                            if advn.stat_name == item:
                                prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                                curt = advn.stat_data
                                setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev + curt))

    def calc_stat(self):
        self.c_weap = WEAP()
        self.c_team = TEAM()
        self.c_tyvt = CHAR()
        # CR 5%, CD 50%, ER 100% are accounts in self.c_tyvt
        self.c_char = CHAR(
            critical_rate_perc=ATTR(stat_name=STAT.critical_rate_perc, stat_data=0.0),
            critical_damage_perc=ATTR(stat_name=STAT.critical_damage_perc, stat_data=0.0),
            energy_recharge_perc=ATTR(stat_name=STAT.energy_recharge_perc, stat_data=0.0),
        )
        self.char_keep()
        self.weap_keep()
        self.arti_keep()
        self.arti_stat()
        self.weap_stat()
        self.char_stat()
