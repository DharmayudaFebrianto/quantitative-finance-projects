from pathlib import Path
from typing import List

import pandas as pd
import yfinance as yf

from src.config import RAW_DATA_DIR, DATA_CONFIG


def ensure_data_dirs():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


def download_price_data(
    ticker: str,
    start: str = None,
    end: str = None,
    auto_save: bool = True
) -> pd.DataFrame:
    """
    Download data harga dari yfinance dan (opsional) simpan ke CSV di data/raw.

    Parameters
    ----------
    ticker : str
        Ticker, misal 'AAPL', 'SPY', atau 'BTC-USD'.
    start : str
        Tanggal mulai, format 'YYYY-MM-DD'. Default dari DATA_CONFIG.
    end : str
        Tanggal akhir. Default dari DATA_CONFIG.
    auto_save : bool
        Jika True, simpan ke file CSV.

    Returns
    -------
    df : pd.DataFrame
        Data harga dengan index Datetime.
    """
    ensure_data_dirs()

    if start is None:
        start = DATA_CONFIG["start"]
    if end is None:
        end = DATA_CONFIG["end"]

    df = yf.download(ticker, start=start, end=end)

    # Pastikan index datetime & nama kolom konsisten
    df.index.name = "date"
    df.columns = [c.lower() for c in df.columns]

    if auto_save:
        file_path = RAW_DATA_DIR / f"{ticker.replace('-', '_')}_raw.csv"
        df.to_csv(file_path)
        print(f"[INFO] Saved raw data for {ticker} to {file_path}")

    return df


def load_raw_data(ticker: str) -> pd.DataFrame:
    """
    Load data dari CSV di data/raw. Kalau belum ada, auto download.
    """
    ensure_data_dirs()
    file_path = RAW_DATA_DIR / f"{ticker.replace('-', '_')}_raw.csv"

    if not file_path.exists():
        print(f"[INFO] Raw data for {ticker} not found. Downloading...")
        return download_price_data(ticker)

    df = pd.read_csv(file_path, index_col="date", parse_dates=True)
    return df


def bulk_download(tickers: List[str] = None):
    """
    Download banyak ticker sekaligus.
    """
    if tickers is None:
        tickers = DATA_CONFIG["tickers"]

    for t in tickers:
        download_price_data(t)
