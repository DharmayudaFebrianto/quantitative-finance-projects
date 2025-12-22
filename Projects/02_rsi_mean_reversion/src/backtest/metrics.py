"""Simple performance metrics for beginners."""
import numpy as np
import pandas as pd


def cumulative_return(equity: pd.Series) -> float:
    return equity.iloc[-1] / equity.iloc[0] - 1


def sharpe_ratio(returns: pd.Series, periods_per_year: int = 252) -> float:
    # using excess returns with rf=0 for simplicity
    mean = returns.mean() * periods_per_year
    std = returns.std() * (periods_per_year ** 0.5)
    return mean / (std if std != 0 else np.nan)


def max_drawdown(equity: pd.Series) -> float:
    roll_max = equity.cummax()
    drawdown = (equity - roll_max) / roll_max
    return drawdown.min()