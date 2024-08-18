from gi_loadouts.face.otpt.rule import Rule


class OtptWindow(Rule):
    def __init__(self, charname):
        super().__init__()
        self.headtext = f"Loadouts for Genshin Impact - {charname}"
        self.setupUi(self)
        self.setWindowTitle(self.headtext)
