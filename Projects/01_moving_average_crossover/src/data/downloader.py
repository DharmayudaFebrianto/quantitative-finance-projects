import pandas as pd
import yfinance as yf
from pathlib import Path

from src.config import RAW_DATA_DIR, DATA_CONFIG


def ensure_data_dirs():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalisasi nama kolom:
    - Jika MultiIndex → flatten jadi string
    - Jika ada tuple di kolom → join jadi string
    - Semua dibuat lowercase
    """
    cols = df.columns

    # Kalau MultiIndex → flatten
    if isinstance(cols, pd.MultiIndex):
        new_cols = []
        for col in cols:
            # col bisa tuple seperti ('Close', 'AAPL')
            if isinstance(col, tuple):
                # gabung level yang tidak kosong
                col_str = "_".join([str(c) for c in col if c is not None and c != ""])
            else:
                col_str = str(col)
            new_cols.append(col_str.lower())
        df.columns = new_cols
    else:
        # Bukan MultiIndex, tapi bisa jadi ada tuple juga
        new_cols = []
        for c in cols:
            if isinstance(c, tuple):
                col_str = "_".join([str(x) for x in c if x is not None and x != ""])
            else:
                col_str = str(c)
            new_cols.append(col_str.lower())
        df.columns = new_cols

    return df


def download_price_data(
    ticker: str,
    start: str = None,
    end: str = None,
    auto: bool = True
) -> pd.DataFrame:
    """
    Download price data from yfinance and save to CSV.
    """
    ensure_data_dirs()
    file_path = RAW_DATA_DIR / f"{ticker.replace('-', '_')}_raw.csv"
    
    df = yf.download(ticker, start=start, end=end)
    df.index.name = "date"
    df = _normalize_columns(df)
    df.to_csv(file_path)
    
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

    # Normalisasi lagi kalau perlu (jaga-jaga)
    df = _normalize_columns(df)

    return df