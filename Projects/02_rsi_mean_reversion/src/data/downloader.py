"""Simple downloader using yfinance with caching to `data/raw/`.

Designed to be easy to read for beginners.
"""
from pathlib import Path
from typing import Optional
import pandas as pd

import yfinance as yf

from ..config import RAW_DIR


def download_data(ticker: str, start: Optional[str] = None, end: Optional[str] = None, force: bool = False) -> pd.DataFrame:
    """Download OHLCV data for `ticker` and cache to `data/raw/{ticker}.csv`.

    Parameters
    ----------
    ticker: symbol like 'BTC-USD' or 'AAPL'
    start, end: yyyy-mm-dd strings (optional)
    force: if True, re-download even if cached file exists

    Returns
    -------
    pd.DataFrame: historical data indexed by date
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(RAW_DIR) / f"{ticker}.csv"

    if path.exists() and not force:
        df = pd.read_csv(path, index_col=0, parse_dates=True)
        return df

    df = yf.download(ticker, start=start, end=end, progress=False)
    if df.empty:
        raise ValueError(f"No data downloaded for {ticker}")

    df.to_csv(path)
    return df