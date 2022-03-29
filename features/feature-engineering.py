import pandas as pd
import datetime
import geopandas


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


def getMongoliaShpFile(filepath: str="soum_aimag.shp") -> pd.DataFrame:
    """
    Function reads Shp File from

    Args:
        filepath (str, optional): Defaults to "soum_aimag.shp".

    Returns:
        pd.DataFrame:
    """
    gdf = geopandas.read_file("soum_aimag.shp")
    df = pd.DataFrame(gdf)
    return df


def joinShpData(df1: pd.DataFrame, df2: pd.DataFrame, partition: str="asid"):
    """
    Outer Join 2 Dataframe based on partition

    Args:
        df1 - pd.DataFrame:
        df2 - pd.DataFrame:
        partition str: Defaults to "asid".

    Returns:
        pd.DataFrame:
    """
    df2["asid"] = df2["asid"].astype("int")
    df1["asid"] = df1["asid"].astype("int")
    df = pd.merge(df1, df2, on=partition, how="outer")
    return df