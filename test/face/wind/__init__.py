class MockQFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def open(self, method):
        return False
