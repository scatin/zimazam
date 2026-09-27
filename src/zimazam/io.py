import openpyxl
import pandas as pd
import polars as pl
from pathlib import Path
from .steps import step

def get_extension(filepath: str) -> str:
    return Path(filepath).suffix.lstrip(".")

def pd_to_polars(df: pd.DataFrame) -> pl.DataFrame:
    return pl.from_pandas(df)

@step
def input(filepath: str) -> pl.DataFrame:
    extension = get_extension(filepath)

    match extension:
        case "xlsx":
            df = pd.read_excel(filepath)
        case "csv":
            df = pd.read_csv(filepath)
        case _:
            raise ValueError(f"Unsupported file extension: {extension}")

    result = pd_to_polars(df)

    return result

def output(filepath: str) -> str:
    print("this is the output function")