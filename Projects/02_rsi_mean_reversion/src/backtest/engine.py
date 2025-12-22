"""Very simple backtest engine for educational purposes.

Assumes `df` contains `Close` and `position` (1/0/-1) columns.
"""
import pandas as pd


def run_backtest(df: pd.DataFrame, initial_cash: float = 10000.0) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["Close", "position"])  # ensure required columns

    # Calculate returns and strategy returns
    df["market_return"] = df["Close"].pct_change().fillna(0)
    df["strategy_return"] = df["market_return"] * df["position"].shift(1).fillna(0)

    df["strategy_equity"] = (1 + df["strategy_return"]).cumprod() * initial_cash
    df["market_equity"] = (1 + df["market_return"]).cumprod() * initial_cash

    return df