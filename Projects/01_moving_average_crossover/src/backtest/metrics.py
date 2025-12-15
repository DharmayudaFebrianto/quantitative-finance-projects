import numpy as np
import pandas as pd


def total_return(equity: pd.Series) -> float:
    """
    Total return dari equity curve.
    """
    if len(equity) == 0:
        return 0.0
    return equity.iloc[-1] / equity.iloc[0] - 1.0


def cagr(equity: pd.Series, periods_per_year: int = 252) -> float:
    """
    Compound Annual Growth Rate (CAGR).

    Assumes daily data (252 trading days) by default.
    """
    if len(equity) < 2:
        return 0.0

    total_ret = equity.iloc[-1] / equity.iloc[0]
    n_periods = len(equity)
    years = n_periods / periods_per_year

    if years <= 0:
        return 0.0
    return total_ret ** (1 / years) - 1


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252
) -> float:
    """
    Sharpe ratio tahunan.
    """
    if returns.std() == 0:
        return 0.0

    excess_ret = returns - risk_free_rate / periods_per_year
    mean_ret = excess_ret.mean()
    vol = excess_ret.std()

    return (mean_ret / vol) * np.sqrt(periods_per_year)


def max_drawdown(equity: pd.Series) -> float:
    """
    Max drawdown (nilai negatif, contoh -0.35 = -35%).
    """
    if len(equity) == 0:
        return 0.0

    roll_max = equity.cummax()
    drawdown = equity / roll_max - 1.0
    return drawdown.min()
