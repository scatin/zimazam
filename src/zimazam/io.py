import openpyxl
import pandas as pd
import polars as pl
from pathlib import Path

def get_extension(filepath: str) -> str:
    return Path(filepath).suffix.lstrip(".")

def pd_to_polars(df: pd.DataFrame) -> pl.DataFrame:
    return pl.from_pandas(df)

def input(filepath: str) -> pl.DataFrame:
    extension = get_extension(filepath)

    match extension:
        case "xlsx":
            df = pd.read_excel(filepath)
            return pd_to_polars(df)
        case "csv":
            df = pd.read_csv(filepath)
            return pd_to_polars(df)
        case _:
            raise ValueError(f"Unsupported file extension: {extension}")

def output(filepath: str) -> str:
    print("this is the output function")