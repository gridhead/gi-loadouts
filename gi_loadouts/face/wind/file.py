from PySide6.QtWidgets import QFileDialog


class FileHandling:
    def __init__(self):
        super().__init__()

    def save(self, prnt, head, path, data) -> None:
        explorer = QFileDialog()
        savefile = explorer.getSaveFileName(prnt, head, path, "YAML Files (*.yaml);;All Files (*)")[0]
        if savefile.strip() == "":
            raise FileNotFoundError("No file selected.")
        with open(savefile, "w") as fileobjc:
            fileobjc.write(data)
        return None

    def load(self, prnt, head) -> str:
        explorer = QFileDialog()
        loadfile = explorer.getOpenFileName(prnt, head, "", "YAML Files (*.yaml);;All Files (*)")[0]
        if loadfile.strip() == "":
            raise FileNotFoundError("No file selected.")
        with open(loadfile) as fileobjc:
            data = fileobjc.read()
        return data


file = FileHandling()
