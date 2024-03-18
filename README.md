# convert-stephaj

## Introduction
This project provides the tools for fetching, processing, and visualizing interest rate data from the Federal Reserve Economic Data (FRED) database.

## Environment Setup
### Prerequisites
- Python 3.7 or newer

### Install required packages
```bash
pip install pandas numpy pandas-datareader matplotlib
```

## Functionality
- Data Fetching (data_fetch.py)
  - Fetches interest rate data from the FRED database using a series ID and data range.
- Data Processing (data_processing.py)
  - Prepares the dataframe by handling missing values, setting the date as the index, and resamples to monthly frequency.
- Visualization (visualization.py)
  - Generates two plots: line plot for actual interest rates over time and a line plot of log changes in interest rates.
- Main Script (main.py)
  - Executes the pipeline of data fetching, processing, and visualization using the command line.
 
## Usage
To run the main script, use the following example for the command line:  
```bash
python src/main.py <series_id> <start_date> <end_date> -o <output_directory>
```
- Description of placeholders:
  - <series_id>: The FRED series ID (e.g., "FEDFUNDS")
  - <start_date> and <end_date>: Dates in YYYY-MM-DD format.
  - <output_directory>: Path to the directory for saving the processed data and plots (optional). Defaults to current directory.

### Example:
```bash
python src/main.py FEDFUNDS 2015-01-01 2023-12-31 -o ./output
```
