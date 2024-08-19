from PySide6.QtWidgets import QMessageBox

from gi_loadouts.face.wind.rule import Rule


class MainWindow(Rule):
    def __init__(self):
        super().__init__()
        self.headtext = "Loadouts for Genshin Impact"
        self.dialog = QMessageBox()
        self.setupUi(self)
        self.setWindowTitle(self.headtext)
        self.initialize_events()
        self.initialize_elements()

    def initialize_elements(self):
        self.statarea.showMessage("Ready.")
        self.populate_dropdown()
        self.handle_char_data(0)
        self.convey_weapon_type_change(0)
        self.convey_weapon_name_change(0)
        self.convey_weapon_levl_change(0)
        self.convey_refinement_change(0)
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_name_main, self.arti_fwol_data_main, "fwol", self.arti_fwol_data_main, self.arti_fwol_type_name),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_name_main, self.arti_pmod_data_main, "pmod", self.arti_pmod_data_main, self.arti_pmod_type_name),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_name_main, self.arti_sdoe_data_main, "sdoe", self.arti_sdoe_data_main, self.arti_sdoe_type_name),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_name_main, self.arti_gboe_data_main, "gboe", self.arti_gboe_data_main, self.arti_gboe_type_name),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_name_main, self.arti_ccol_data_main, "ccol", self.arti_ccol_data_main, self.arti_ccol_type_name),
        ]:
            self.change_rarity_by_changing_type(item[1], item[2], item[6], item[5])
            self.change_artifact_team_by_changing_type(item[1], item[5])
            self.change_data_by_changing_level_or_stat(item[0], item[1], item[2], item[3], item[4], item[5])
            self.change_artifact_substats_by_changing_rarity_or_mainstat(item[2], item[3], item[5])
            self.change_levels_by_changing_rarity(item[0], item[2])

    def initialize_events(self):
        self.head_scan.clicked.connect(self.show_output_window)
        self.head_char_name.currentIndexChanged.connect(self.handle_char_data)
        self.head_char_levl.currentIndexChanged.connect(self.handle_char_data)
        self.weap_area_type.currentIndexChanged.connect(self.convey_weapon_type_change)
        self.weap_area_name.currentIndexChanged.connect(self.convey_weapon_name_change)
        self.weap_area_levl.currentIndexChanged.connect(self.convey_weapon_levl_change)
        self.weap_area_refn.currentIndexChanged.connect(self.convey_refinement_change)
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_name_main, self.arti_fwol_data_main, "fwol", self.arti_fwol_type_name),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_name_main, self.arti_pmod_data_main, "pmod", self.arti_pmod_type_name),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_name_main, self.arti_sdoe_data_main, "sdoe", self.arti_sdoe_type_name),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_name_main, self.arti_gboe_data_main, "gboe", self.arti_gboe_type_name),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_name_main, self.arti_ccol_data_main, "ccol", self.arti_ccol_type_name),
        ]:
            item[1].currentIndexChanged.connect(lambda _, a_type=item[1], a_rare=item[2], a_name=item[6], a_id=item[5]: self.change_rarity_by_changing_type(a_type, a_rare, a_name, a_id))
            item[1].currentIndexChanged.connect(lambda _, a_type=item[1], a_id=item[5]: self.change_artifact_team_by_changing_type(a_type, a_id))
            item[1].currentIndexChanged.connect(lambda _, a_type=item[1], a_id=item[5]: self.remove_artifact(a_type, a_id))
            item[0].currentIndexChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
            item[3].currentIndexChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
            item[2].currentIndexChanged.connect(lambda _, a_rare=item[2], a_name=item[3], a_id=item[5]: self.change_artifact_substats_by_changing_rarity_or_mainstat(a_rare, a_name, a_id))
            item[3].currentIndexChanged.connect(lambda _, a_rare=item[2], a_name=item[3], a_id=item[5]: self.change_artifact_substats_by_changing_rarity_or_mainstat(a_rare, a_name, a_id))
            item[2].currentIndexChanged.connect(lambda _, a_levl=item[0], a_rare=item[2]: self.change_levels_by_changing_rarity(a_levl, a_rare))
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            for alfa in ["a", "b", "c", "d"]:
                drop, text = getattr(self, f"arti_{part}_name_{alfa}"), getattr(self, f"arti_{part}_data_{alfa}")
                drop.currentIndexChanged.connect(lambda _, a_drop=drop, a_text=text: self.render_lineedit_readonly_when_none(a_drop, a_text))
                text.textChanged.connect(self.validate_lineedit_userdata)
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            getattr(self, f"arti_{part}_load").clicked.connect(lambda _, a_part=part: self.open_explorer_load(a_part))
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            getattr(self, f"arti_{part}_save").clicked.connect(lambda _, a_part=part: self.open_explorer_save(a_part))
