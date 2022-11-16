import os
import pandas as pd


class FileInfo:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.mtime = os.path.getmtime(path)


class ExcelFileInfo(FileInfo):

    excel_file: pd.ExcelFile = None

    def __init__(self, path):
        super().__init__(path)
        self.excel_file = pd.ExcelFile(path)

    def get_sheet_names(self):
        return self.excel_file.sheet_names


class ChronicityFileInfo(ExcelFileInfo):

    age_range: str = None
    sex: str = "A"

    def __init__(self, path):
        super().__init__(path)
        self.catalogue()

    def catalogue(self):
        bad_words = ['tmp\\', ' - Femmine', ' - Maschi', ' - All', '.xlsx']
        self.age_range = self.path
        for word in bad_words:
            self.age_range = self.age_range.replace(word, '')

        if "Femmine" in self.path:
            self.sex = "F"
        elif "Maschi" in self.path:
            self.sex = "M"

    def list(directory: str) -> list['ChronicityFileInfo']:
        files = (f for f in os.listdir(directory) if f.endswith('.xlsx'))
        files = (os.path.join(directory, f) for f in files)
        return [ChronicityFileInfo(f) for f in files]
