import os
import platform
from pathlib import Path


class Writer:
    collection = None
    output_path = Path()

    def __init__(self, collection, output_path):
        self.collection = collection
        self.output_path = os.path.abspath(self.parse_path(output_path))

    def create_dir(self):
        dir_path = self.parse_path(self.output_path.split(os.sep)[0:-1])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    @staticmethod
    def parse_path(path):
        if '/' in path:
            pieces = path.split('/')
        elif '\\' in path:
            pieces = path.split('\\')
        else:
            pieces = path

        operating_system = platform.system()
        tmp_path = ""
        for item in pieces:
            if operating_system == "Linux" or operating_system == "Darvin":  # /
                tmp_path += item + "//"
            else:  # \\
                tmp_path += item + "\\"
        return tmp_path
