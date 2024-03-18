"""
This module provides functions for visualizing interest rate data.

Functions:
    plot_interest_rates: Plots the interest rates over time for a specified column.

    plot_log_changes: Plots the log changes of interest rates over time. Assumes the
        DataFrame contains a 'log_change' column and raises a ValueError if missing.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_interest_rates(df: pd.DataFrame, column: str) -> None:
    """
    Plots the interest rate over time for a specified column.

    Args:
        df: The DataFrame containing the interest rate data.
        column: The name of the column containing the interest rates.
    """
    # Plot the interest rates over time
    fig, ax = plt.subplots()
    ax.plot(df.index, df[column], label="Interest Rate", color="tab:blue")
    ax.xaxis.set_major_locator(mdates.YearLocator(base=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlim(df.index[0], df.index[-1])
    ax.set_title(f"{column}")
    ax.set_ylabel("Interest Rate (%)")
    ax.legend()
    plt.show()


def plot_log_changes(df: pd.DataFrame) -> None:
    """
    Plots the log changes of interest rates over time.

    Args:
        df: The DataFrame containing the interest rate data
            (assumes a 'log_change' column is present).
    """
    if "log_change" not in df.columns:
        raise ValueError(
            f"The column 'log_change' is not present in the DataFrame. Run calculate_log_changes first."
        )
    # Plot the log changes
    fig, ax = plt.subplots()
    ax.plot(df.index, df["log_change"], label="Log Change", color="tab:orange")
    ax.xaxis.set_major_locator(mdates.YearLocator(base=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_xlim(df.index[0], df.index[-1])
    ax.set_title("Log Change")
    ax.set_ylabel("Log Change")
    ax.legend()
    plt.show()
