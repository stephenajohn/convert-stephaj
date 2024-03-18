"""
This module coordinates the fetching, processing, and visualization of interest rate data from FRED.
It provides command-line argument for specifying the FRED series ID, data range, and optional
output directory to save the processed data and plots.
"""

import os
import argparse
import matplotlib.pyplot as plt
import data_fetch
import data_processing
import visualization

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch, process, and plot interest rates data.")
    parser.add_argument("series_id", help="ID of the interest rate series from FRED.")
    parser.add_argument("start_date", help="Start date for fetching data (YYYY-MM-DD).")
    parser.add_argument("end_date", help="End date for fetching data (YYYY-MM-DD).")
    parser.add_argument("-o", "--output_dir", help="Directory to save processed data and plots.")

    args = parser.parse_args()

    # Fetch the data
    raw_data = data_fetch.fetch_fred_data(args.series_id, args.start_date, args.end_date)

    # Process the data
    processed_data = data_processing.prepare_data(raw_data.copy())

    # Calculate the log changes based on the column name
    processed_data = data_processing.calculate_log_changes(processed_data, args.series_id)

    # Save processed data
    if args.output_dir:
        processed_data.to_csv(os.path.join(args.output_dir, "processed_interest_rates.csv"))

    # Generate and save visualizations using series_id as the column name
    visualization.plot_interest_rates(processed_data.copy(), args.series_id)
    if args.output_dir:
        plt.savefig(os.path.join(args.output_dir, f"{args.series_id}_interest_rates_plot.png"))
        plt.close()

    visualization.plot_log_changes(processed_data.copy())
    if args.output_dir:
        plt.savefig(os.path.join(args.output_dir, f"{args.series_id}_log_changes_plot.png"))
        plt.close()
