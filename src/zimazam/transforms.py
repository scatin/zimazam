import openpyxl
import pandas as pd
import polars as pl
from pathlib import Path
from .steps import step

@step
def select(columns: list[str], previous_result: pl.DataFrame = None) -> pl.DataFrame:

    if previous_result is None:
        previous_result = result

    result = previous_result.select(columns)

    return result

