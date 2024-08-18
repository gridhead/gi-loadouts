from gi_loadouts.face.wind.rule import Rule


class MainWindow(Rule):
    def __init__(self):
        super().__init__()
        self.headtext = "Loadouts for Genshin Impact"
        self.setupUi(self)
        self.setWindowTitle(self.headtext)
        self.initialize_elements()
        self.initialize_events()

    def initialize_elements(self):
        self.populate_dropdown()
        self.handle_char_data(0)
        self.convey_weapon_type_change(0)
        self.convey_weapon_name_change(0)
        self.convey_weapon_levl_change(0)
        self.convey_refinement_change(0)
        for quad in [
            (self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_type_name, "fwol"),
            (self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_type_name, "pmod"),
            (self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_type_name, "sdoe"),
            (self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_type_name, "gboe"),
            (self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_type_name, "ccol"),
        ]:
            self.change_rarity_by_changing_type(quad[0], quad[1], quad[2], quad[3])
            self.change_artifact_team_by_changing_type(quad[0], quad[3])
        for pair in [
            (self.arti_fwol_rare, self.arti_fwol_levl),
            (self.arti_pmod_rare, self.arti_pmod_levl),
            (self.arti_sdoe_rare, self.arti_sdoe_levl),
            (self.arti_gboe_rare, self.arti_gboe_levl),
            (self.arti_ccol_rare, self.arti_ccol_levl),
        ]:
            self.change_levels_by_changing_rarity(pair[0], pair[1])
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_main_name, self.arti_fwol_main_data, "fwol"),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_main_name, self.arti_pmod_main_data, "pmod"),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_main_name, self.arti_sdoe_main_data, "sdoe"),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_main_name, self.arti_gboe_main_data, "gboe"),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_main_name, self.arti_ccol_main_data, "ccol"),
        ]:
            self.change_data_by_changing_level_or_stat(item[0], item[1], item[2], item[3], item[4], item[5])

    def initialize_events(self):
        self.head_scan.clicked.connect(self.show_output_window)
        self.head_char_name.currentIndexChanged.connect(self.handle_char_data)
        self.head_char_levl.currentIndexChanged.connect(self.handle_char_data)
        self.weap_area_type.currentIndexChanged.connect(self.convey_weapon_type_change)
        self.weap_area_name.currentIndexChanged.connect(self.convey_weapon_name_change)
        self.weap_area_levl.currentIndexChanged.connect(self.convey_weapon_levl_change)
        self.weap_area_refn.currentIndexChanged.connect(self.convey_refinement_change)
        for quad in [
            (self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_type_name, "fwol"),
            (self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_type_name, "pmod"),
            (self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_type_name, "sdoe"),
            (self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_type_name, "gboe"),
            (self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_type_name, "ccol"),
        ]:
            quad[0].currentIndexChanged.connect(lambda _, a_type=quad[0], a_rare=quad[1], a_name=quad[2], a_id=quad[3]: self.change_rarity_by_changing_type(a_type, a_rare, a_name, a_id))
            quad[0].currentIndexChanged.connect(lambda _, a_type=quad[0], a_rare=quad[1], a_id=quad[3]: self.change_artifact_team_by_changing_type(a_type, a_id))
        for pair in [
            (self.arti_fwol_rare, self.arti_fwol_levl),
            (self.arti_pmod_rare, self.arti_pmod_levl),
            (self.arti_sdoe_rare, self.arti_sdoe_levl),
            (self.arti_gboe_rare, self.arti_gboe_levl),
            (self.arti_ccol_rare, self.arti_ccol_levl),
        ]:
            pair[0].currentIndexChanged.connect(lambda _, a_rare=pair[0], a_levl=pair[1]: self.change_levels_by_changing_rarity(a_rare, a_levl))
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_main_name, self.arti_fwol_main_data, "fwol"),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_main_name, self.arti_pmod_main_data, "pmod"),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_main_name, self.arti_sdoe_main_data, "sdoe"),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_main_name, self.arti_gboe_main_data, "gboe"),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_main_name, self.arti_ccol_main_data, "ccol"),
        ]:
            item[0].currentIndexChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
            item[3].currentIndexChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
