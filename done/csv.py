# Load pandas
import pandas as pd


class read:

    df = 0

    def read_csv(self):
        # Read CSV file into DataFrame df
        df = pd.read_csv('done/tests.csv')
        for row in df:
            df += row
            print(df)
        # Show dataframe
        return self.df
