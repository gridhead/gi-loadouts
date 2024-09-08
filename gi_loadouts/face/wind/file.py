import json

import yaml
from PySide6.QtWidgets import QFileDialog

from gi_loadouts.type.file.arti import ArtiFile


class FileHandling:
    def __init__(self):
        super().__init__()

    def save(self, prnt, head: str, path: str, data: ArtiFile) -> None:
        """
        Handle file operations involved in saving data to the storage device

        :param prnt: Parent window reference calling for the save command
        :param head: Title of the interaction dialog for file saving
        :param path: Location to begin browsing from with the filename default
        :param data: Data that is intended to be saved to the sought file
        :return:
        """
        explorer = QFileDialog()
        savefile, filetype = explorer.getSaveFileName(prnt, head, path, "YAML Files (*.yaml);;GOOD Files (*.json)")

        if savefile.strip() == "":
            raise FileNotFoundError("No file selected.")

        if filetype == "YAML Files (*.yaml)":
            text = yaml.dump(data.easydict)
        else:
            text = json.dumps(data.to_good, indent=2)

        with open(savefile, "w") as fileobjc:
            fileobjc.write(text)

        return None

    def load(self, prnt, head: str) -> tuple:
        """
        Handle file operations involved in loading data from the storage device

        :param prnt: Parent window reference calling for the load command
        :param head: Title of the interaction dialog for file loading
        :return: Data that is intended to be loaded from the sought file
        """
        explorer = QFileDialog()
        loadfile, filetype = explorer.getOpenFileName(prnt, head, "", "YAML Files (*.yaml);;GOOD Files (*.json)")

        if loadfile.strip() == "":
            raise FileNotFoundError("No file selected.")

        with open(loadfile) as fileobjc:
            data = fileobjc.read()

        return data, filetype


file = FileHandling()
