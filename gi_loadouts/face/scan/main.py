from gi_loadouts import __versdata__
from gi_loadouts.face.scan.rule import Rule


class ScanDialog(Rule):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Loadouts for Genshin Impact v{__versdata__}")
        self.initialize_events()
        self.initialize_elements()

    def initialize_elements(self) -> None:
        """
        Initialize elements on the user interface

        :return:
        """
        self.populate_dropdown()

    def initialize_events(self) -> None:
        """
        Initialize events on the user interface

        :return:
        """
        self.arti_dist.currentTextChanged.connect(self.change_mainstat_by_changing_artifact_area)
        self.arti_dist.currentTextChanged.connect(self.change_artifact_name_by_changing_artifact_area_or_type)
        self.arti_type.currentTextChanged.connect(self.change_artifact_name_by_changing_artifact_area_or_type)
        self.arti_type.currentTextChanged.connect(self.remove_artifact)
        self.arti_rare.currentTextChanged.connect(self.change_levels_backdrop_by_changing_rarity)
        self.arti_rare.currentTextChanged.connect(self.change_artifact_substats_by_changing_rarity_or_mainstat)
        self.arti_name_main.currentTextChanged.connect(self.change_artifact_substats_by_changing_rarity_or_mainstat)
        self.arti_levl.currentTextChanged.connect(self.change_data_by_changing_level_or_stat)
        self.arti_name_main.currentTextChanged.connect(self.change_data_by_changing_level_or_stat)
        for alfa in ["a", "b", "c", "d"]:
            drop, text = getattr(self, f"arti_name_{alfa}"), getattr(self, f"arti_data_{alfa}")
            drop.currentTextChanged.connect(lambda _, a_drop=drop, a_text=text: self.render_lineedit_readonly_when_none(a_drop, a_text))
        self.arti_back_wipe.clicked.connect(self.wipe_artifact)
        self.arti_cnvs_load.clicked.connect(self.load_reader)
        self.arti_cnvs_conf.clicked.connect(self.load_tessexec)
