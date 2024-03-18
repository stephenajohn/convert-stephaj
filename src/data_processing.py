"""
This module provides functions for preparing, merging, and analyzing interest rate data.

Functions:
    prepare_data: Prepares a DataFrame for analysis by setting the 'DATE' column as the
        index (if present), converting it to datetime format, sorting, and resampling monthly.

    merge_interest_rates: Merges two interest rate DataFrames and performs validation to
        ensure the specified merge column exists in both DataFrames.

    calculate_log_changes: Calculates log changes for a given column within a DataFrame
        and handles missing values (NaN) by dropping rows.
"""
import pandas as pd
import numpy as np


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Prepares a DataFrame potentially containing treasury data for further analysis.

    Args:
        df: A pandas DataFrame.

    Returns:
        A pandas DataFrame with 'DATE' column set as index (if present),
        converted to datetime format, sorted, and resampled monthly.
    """
    if "DATE" in df.columns:
        df["DATE"] = pd.to_datetime(df["DATE"])
        df.set_index("DATE", inplace=True)
    elif df.index.name == "DATE":
        df.index = pd.to_datetime(df.index)

    return df.sort_index().resample("MS").first()


def merge_interest_rates(
    df1: pd.DataFrame, df2: pd.DataFrame, on: str = "DATE", how: str = "inner"
) -> pd.DataFrame:
    """Merges two interest rate DataFrames.

    Args:
        df1: The first DataFrame.
        df2: The second DataFrame.
        on: The column name to use for joining (defaults to "DATE").
        how: The type of merge to perform (defaults to "inner").

    Returns:
        A pandas DataFrame containing the merged interest rate data.
    """
    if on not in df1.columns or on not in df2.columns:
        raise ValueError(f"Invalid 'on' columns: '{on}' not found in both DataFrames.")

    try:
        df1.merge(df2, on=on, how=how)
    except Exception as e:
        print(f"Error during merging: {e}")


def calculate_log_changes(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Calculates the log changes for a given column in a DataFrame.

    Args:
        df: The DataFrame containing the column.
        column: The name of the column for which to calculate log changes.

    Returns:
        A DataFrame with the calculated log changes (and original data).
    """
    df["log_change"] = np.log(df[column]) - np.log(df[column].shift(1))
    df.dropna(inplace=True)  # Drop rows with missing values (NaN)
    return df
