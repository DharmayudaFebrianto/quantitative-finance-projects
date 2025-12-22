"""RSI mean reversion: compute RSI and generate simple signals.

Signals:
- Long when RSI < oversold
- Exit long when RSI > 50
- Short when RSI > overbought (optional)

This implementation uses pandas only so it's easy for beginners to read.
"""
from typing import Tuple
import pandas as pd


def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """Compute RSI using the Wilder smoothing method.

    Returns a pd.Series aligned with `close`.
    """
    delta = close.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)

    # Wilder's smoothing
    roll_up = up.ewm(alpha=1 / period, adjust=False).mean()
    roll_down = down.ewm(alpha=1 / period, adjust=False).mean()
    rs = roll_up / roll_down
    rsi = 100 - (100 / (1 + rs))
    return rsi


def generate_signals(df: pd.DataFrame, period: int = 14, oversold: int = 30, overbought: int = 70) -> pd.DataFrame:
    """Return a dataframe with RSI and a `signal` column: 1=long, 0=flat, -1=short (optional).

    This is intentionally simple to illustrate the idea to beginners.
    """
    df = df.copy()
    df["rsi"] = compute_rsi(df["Close"], period=period)
    df["signal"] = 0

    # Long entry
    df.loc[df["rsi"] < oversold, "signal"] = 1
    # Exit long when RSI > 50
    df.loc[df["rsi"] > 50, "signal"] = 0
    # Optional short entry
    df.loc[df["rsi"] > overbought, "signal"] = -1

    # Turn consecutive identical signals into positions by forward filling
    df["position"] = df["signal"].replace(to_replace=0, method="ffill").fillna(0)
    return df