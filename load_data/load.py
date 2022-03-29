import pandas as pd

def load_data(filepath: str = "../data/daily_vi_soum_2020.csv"):
    df = pd.read_csv(filepath)

    return df