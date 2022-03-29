import pandas as pd

def parseDate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function parses date from first column

    Args:
        df (pd.DataFrame):

    Returns:
        pd.DataFrame:
    """
    df["date"] = df["system:index"].str.split("_").str[3]

    return df


def get_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function extracts year, month and date from date

    Args:
        df (pd.DataFrame):

    Returns:
        pd.DataFrame:
    """
    date_string = str(df["date"])
    df["year"] = date_string[:4]
    df["month"] = date_string[4:6]
    df["day"] = date_string[6:8]

    return df

def parseCounty(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function gets County and Province from DataFrame

    Args:
        df (pd.DataFrame):

    Returns:
        pd.DataFrame:
    """
    df["province"] = df[""][0:2]
    df["county"] = df[""][2:4]