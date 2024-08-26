from PySide6.QtWidgets import QFileDialog


class FileHandling:
    def __init__(self):
        super().__init__()

    def save(self, prnt, head: str, path: str, data: str) -> None:
        """
        Handle file operations involved in saving data to the storage device

        :param prnt: Parent window reference calling for the save command
        :param head: Title of the interaction dialog for file saving
        :param path: Location to begin browsing from with the filename default
        :param data: Data that is intended to be saved to the sought file
        :return:
        """
        explorer = QFileDialog()
        savefile = explorer.getSaveFileName(prnt, head, path, "YAML Files (*.yaml);;All Files (*)")[0]
        if savefile.strip() == "":
            raise FileNotFoundError("No file selected.")
        with open(savefile, "w") as fileobjc:
            fileobjc.write(data)
        return None

    def load(self, prnt, head: str) -> str:
        """
        Handle file operations involved in loading data from the storage device

        :param prnt: Parent window reference calling for the load command
        :param head: Title of the interaction dialog for file loading
        :return: Data that is intended to be loaded from the sought file
        """
        explorer = QFileDialog()
        loadfile = explorer.getOpenFileName(prnt, head, "", "YAML Files (*.yaml);;All Files (*)")[0]
        if loadfile.strip() == "":
            raise FileNotFoundError("No file selected.")
        with open(loadfile) as fileobjc:
            data = fileobjc.read()
        return data


file = FileHandling()
