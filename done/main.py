import pandas as pd


def read_csv():
    with open("done/tests.csv", mode='r') as csv_file:
        df = pd.csv_read(csv_file)
        line_count = 0
        for row in df:
            print(', '.join(row))
