class MockQFile:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def open(self, method) -> bool:
        return False
