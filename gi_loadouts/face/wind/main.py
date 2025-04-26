from PySide6.QtWidgets import QMessageBox

from ... import __donation__, __homepage__, __issutckt__, __versdata__
from ...type.char import CharName
from ..rsrc import kill_temp_file, make_temp_file
from ..wind.rule import Rule


class MainWindow(Rule):
    def __init__(self) -> None:
        super().__init__()
        self.dialog = QMessageBox(parent=self)
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__}")
        self.initialize_events()
        self.initialize_elements()
        try:
            make_temp_file()
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Initialization failed",
                f"{expt}",
            )

    def __del__(self) -> None:
        kill_temp_file()

    def initialize_elements(self) -> None:
        """
        Initialize elements on the user interface

        :return:
        """
        self.populate_dropdown()
        self.handle_elem_data()
        self.handle_char_data()
        self.format_weapon_by_char_change()
        self.convey_weapon_type_change()
        self.convey_weapon_name_change()
        self.convey_weapon_levl_change()
        self.convey_refinement_change()
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_name_main, self.arti_fwol_data_main, "fwol", self.arti_fwol_data_main, self.arti_fwol_type_name, self.arti_fwol_head_area, self.arti_fwol_head_icon),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_name_main, self.arti_pmod_data_main, "pmod", self.arti_pmod_data_main, self.arti_pmod_type_name, self.arti_pmod_head_area, self.arti_pmod_head_icon),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_name_main, self.arti_sdoe_data_main, "sdoe", self.arti_sdoe_data_main, self.arti_sdoe_type_name, self.arti_sdoe_head_area, self.arti_sdoe_head_icon),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_name_main, self.arti_gboe_data_main, "gboe", self.arti_gboe_data_main, self.arti_gboe_type_name, self.arti_gboe_head_area, self.arti_gboe_head_icon),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_name_main, self.arti_ccol_data_main, "ccol", self.arti_ccol_data_main, self.arti_ccol_type_name, self.arti_ccol_head_area, self.arti_ccol_head_icon),
        ]:
            self.change_rarity_backdrop_by_changing_type(item[1], item[2], item[6], item[9], item[5])
            self.change_artifact_team_by_changing_type(item[1], item[5])
            self.change_data_by_changing_level_or_stat(item[0], item[1], item[2], item[3], item[4], item[5])
            self.change_artifact_substats_by_changing_rarity_or_mainstat(item[2], item[3], item[5])
            self.change_levels_backdrop_by_changing_rarity(item[0], item[8], item[2])
        self.regulate_taborder()
        self.statarea.showMessage("Ready.")

    def initialize_events(self) -> None:
        """
        Initialize events on the user interface

        :return:
        """
        self.head_scan.clicked.connect(self.show_output_window)
        self.head_char_elem.currentTextChanged.connect(self.handle_elem_data)
        self.head_char_name.currentTextChanged.connect(self.handle_char_data)
        self.head_char_levl.currentTextChanged.connect(self.handle_char_data)
        self.head_char_name.currentTextChanged.connect(self.format_weapon_by_char_change)
        self.weap_area_type.currentTextChanged.connect(self.convey_weapon_type_change)
        self.weap_area_name.currentTextChanged.connect(self.convey_weapon_name_change)
        self.weap_area_levl.currentTextChanged.connect(self.convey_weapon_levl_change)
        self.weap_area_refn.currentTextChanged.connect(self.convey_refinement_change)
        for item in [
            (self.arti_fwol_levl, self.arti_fwol_type, self.arti_fwol_rare, self.arti_fwol_name_main, self.arti_fwol_data_main, "fwol", self.arti_fwol_type_name, self.arti_fwol_head_area, self.arti_fwol_head_icon),
            (self.arti_pmod_levl, self.arti_pmod_type, self.arti_pmod_rare, self.arti_pmod_name_main, self.arti_pmod_data_main, "pmod", self.arti_pmod_type_name, self.arti_pmod_head_area, self.arti_pmod_head_icon),
            (self.arti_sdoe_levl, self.arti_sdoe_type, self.arti_sdoe_rare, self.arti_sdoe_name_main, self.arti_sdoe_data_main, "sdoe", self.arti_sdoe_type_name, self.arti_sdoe_head_area, self.arti_sdoe_head_icon),
            (self.arti_gboe_levl, self.arti_gboe_type, self.arti_gboe_rare, self.arti_gboe_name_main, self.arti_gboe_data_main, "gboe", self.arti_gboe_type_name, self.arti_gboe_head_area, self.arti_gboe_head_icon),
            (self.arti_ccol_levl, self.arti_ccol_type, self.arti_ccol_rare, self.arti_ccol_name_main, self.arti_ccol_data_main, "ccol", self.arti_ccol_type_name, self.arti_ccol_head_area, self.arti_ccol_head_icon),
        ]:
            item[1].currentTextChanged.connect(lambda _, a_type=item[1], a_rare=item[2], a_name=item[6], a_back=item[8], a_id=item[5]: self.change_rarity_backdrop_by_changing_type(a_type, a_rare, a_name, a_back, a_id))
            item[1].currentTextChanged.connect(lambda _, a_type=item[1], a_id=item[5]: self.change_artifact_team_by_changing_type(a_type, a_id))
            item[1].currentTextChanged.connect(lambda _, a_type=item[1], a_id=item[5]: self.remove_artifact(a_type, a_id))
            item[0].currentTextChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
            item[3].currentTextChanged.connect(lambda _, a_levl=item[0], a_type=item[1], a_rare=item[2], a_name=item[3], a_data=item[4], a_id=item[5]: self.change_data_by_changing_level_or_stat(a_levl, a_type, a_rare, a_name, a_data, a_id))
            item[2].currentTextChanged.connect(lambda _, a_rare=item[2], a_name=item[3], a_id=item[5]: self.change_artifact_substats_by_changing_rarity_or_mainstat(a_rare, a_name, a_id))
            item[3].currentTextChanged.connect(lambda _, a_rare=item[2], a_name=item[3], a_id=item[5]: self.change_artifact_substats_by_changing_rarity_or_mainstat(a_rare, a_name, a_id))
            item[2].currentTextChanged.connect(lambda _, a_levl=item[0], a_back=item[7], a_rare=item[2]: self.change_levels_backdrop_by_changing_rarity(a_levl, a_back, a_rare))
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            for alfa in ["a", "b", "c", "d"]:
                drop, text = getattr(self, f"arti_{part}_name_{alfa}"), getattr(self, f"arti_{part}_data_{alfa}")
                drop.currentTextChanged.connect(lambda _, a_drop=drop, a_text=text: self.render_lineedit_readonly_when_none(a_drop, a_text))
                text.textChanged.connect(self.validate_lineedit_userdata)
            getattr(self, f"arti_{part}_scan").clicked.connect(lambda _, a_part=part: self.show_scan_dialog(a_part))
            getattr(self, f"arti_{part}_load").clicked.connect(lambda _, a_part=part: self.arti_load(a_part))
            getattr(self, f"arti_{part}_save").clicked.connect(lambda _, a_part=part: self.arti_save(a_part))
            getattr(self, f"arti_{part}_wipe").clicked.connect(lambda _, a_part=part: self.wipe_artifact(a_part))
        self.head_load.clicked.connect(self.team_load)
        self.head_save.clicked.connect(self.team_save)
        self.head_wipe.clicked.connect(self.wipe_team)
        self.weap_head_load.clicked.connect(self.weap_load)
        self.weap_head_save.clicked.connect(self.weap_save)
        self.char_head_lumi.clicked.connect(lambda _, a_char=CharName.lumine: self.select_char_from_dropdown(a_char))
        self.char_head_aeth.clicked.connect(lambda _, a_char=CharName.aether: self.select_char_from_dropdown(a_char))
        self.side_head.clicked.connect(lambda _, a_link=__homepage__: self.open_link(a_link))
        self.side_tckt.clicked.connect(lambda _, a_link=__issutckt__: self.open_link(a_link))
        self.side_cash.clicked.connect(lambda _, a_link=__donation__: self.open_link(a_link))
        self.side_info.clicked.connect(self.show_info_dialog)
        self.side_lcns.clicked.connect(self.show_lcns_dialog)
