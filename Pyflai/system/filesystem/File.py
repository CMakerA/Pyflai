import os.path
from Pyflai.system.filesystem.Directory import *


class File:
    def __init__(self, directory: Directory, filename: str):
        self.directory = directory
        self.filename = filename
        self.extension = filename.split(".")[len(filename.split(".")) - 1]
        self.path = directory.path + self.filename

    def exists(self) -> bool:
        return os.path.isfile(self.directory.path + self.filename)
