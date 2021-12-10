from calc.calculation import Calculation

import pandas as pd


class csv_read:
    def write_csv_file(csv_filename: string):
        return pd.to_csv(csv_filename.absolutepath(filename))
