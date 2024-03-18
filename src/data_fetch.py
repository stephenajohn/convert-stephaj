"""
This module enables users to access and retrieve interest rate data from the Federal Reserve Economic Data (FRED)
database using the pandas_datareader library.

Example:
    from data_fetch import fetch_fred_data
    df = fetch_fred_data("FEDFUNDS", "2020-01-01", "2020-12-31")
    print(df.head())
"""
import pandas as pd
import pandas_datareader as pdr

def fetch_fred_data(series_id: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """Fetches interest rate data from FRED.
    Args:
        series_id: The ID of the interest rate series.
        start_date: The start date of the interest rate series
        end_date: The end date of the interest rate

    Returns:
        pandas.DataFrame: A DataFrame containing the interest rate data.
    """
    if not series_id:
        raise ValueError("Series ID is required.")
    try:
        df = pdr.fred.FredReader(
            series_id, start=start_date, end=end_date
        ).read()
        return df
    except Exception as e:
        print(f"Error fetching data from FRED: {e}")
        return None
