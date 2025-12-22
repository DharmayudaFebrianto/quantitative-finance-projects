import pandas as pd
import yfinance as yf
import os
from pathlib import Path

# input syntax for yfinance download function
ticker = str(input("Enter Finances Ticker Symbol: "))
start_date = str(input("Enter Start Date (YYYY-MM-DD): "))
end_date = str(input("Enter End Date (YYYY-MM-DD): "))
interval = str(input("Enter Data Interval (e.g., '1d', '1h'): "))

df = yf.download(tickers=ticker,
                start=start_date,
                end=end_date,
                interval=interval,
                multi_level_index=False,
                auto_adjust=True,
                prepost=False,
                threads=True,
                proxy=None)
df.reset_index(inplace=True)
# save to CSV to data folder with ticker name
project_root = Path(__file__).resolve().parents[2]  # .../01_moving_average_crossover
data_dir = project_root / "data"
data_dir.mkdir(parents=True, exist_ok=True)
file_path = data_dir / f"{ticker}_historical_data.csv"
df.to_csv(file_path, index=False)
print(f"Saved: {file_path}")