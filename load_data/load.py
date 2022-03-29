import pandas as pd
import glob

def load_data(filepath: str = "../data/daily_vi_soum_2020.csv"):
    df = pd.read_csv(filepath)

    return df


def load_all_data(filepath: str = "../data"):
    all_files = glob.glob(filepath + "/*.csv")
    df_files = (pd.read_csv(f) for f in all_files)
    df   = pd.concat(df_files, ignore_index=True)
    return df