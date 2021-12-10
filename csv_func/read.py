import pandas as pd

class csv_read():
    def read_csv_file(csv_filename: string):
        return pd.read_csv(file_utilities.absolutepath(filename))

class file_utlilities:

@staticmethod

    def absolutepath(filepath):
        relative = Path(filepath)
        return relative.absolute()
