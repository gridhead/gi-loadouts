import json

import yaml
from PySide6.QtWidgets import QFileDialog

from ...type.file.arti import ArtiFile
from ...type.file.team import TeamFile
from ...type.file.weap import WeapFile


class FileHandling:
    def __init__(self):
        super().__init__()

    def save(self, prnt, head: str, path: str, data: ArtiFile | TeamFile | WeapFile) -> bool:
        """
        Handle file operations involved in saving data to the storage device

        :param prnt: Parent window reference calling for the save command
        :param head: Title of the interaction dialog for file saving
        :param path: Location to begin browsing from with the filename default
        :param data: Data that is intended to be saved to the sought file
        :return:
        """
        explorer, status = QFileDialog(), False
        savefile, filetype = explorer.getSaveFileName(prnt, head, path, "YAML Files (*.yaml);;GOOD Files (*.json)")

        if savefile.strip() != "":
            if filetype == "YAML Files (*.yaml)":
                extn, text = ".yaml", yaml.dump(data.to_yaml)
            else:
                extn, text = ".json", json.dumps(data.to_good, indent=2)
            if not savefile.endswith(extn):
                savefile += extn
            with open(savefile, "w") as fileobjc:
                fileobjc.write(text)
            status = True

        return status


    def load(self, prnt, head: str) -> tuple:
        """
        Handle file operations involved in loading data from the storage device

        :param prnt: Parent window reference calling for the load command
        :param head: Title of the interaction dialog for file loading
        :return: Data that is intended to be loaded from the sought file
        """
        explorer, status, data = QFileDialog(), False, ""
        loadfile, filetype = explorer.getOpenFileName(prnt, head, "", "YAML Files (*.yaml);;GOOD Files (*.json)")

        if loadfile.strip() != "":
            with open(loadfile) as fileobjc:
                data = fileobjc.read()
            status = True

        return status, data, filetype


file = FileHandling()
