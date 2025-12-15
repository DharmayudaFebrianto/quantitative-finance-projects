from typing import Dict

import pandas as pd
import numpy as np

from src.config import STRATEGY_CONFIG


def run_backtest(
    df: pd.DataFrame,
    initial_capital: float = None,
    trade_cost: float = None
) -> pd.DataFrame:
    """
    Backtest long-only sederhana berdasarkan kolom 'position'.
    Position:
      1 = fully invested (all in)
      0 = cash

    Assumes df memiliki kolom:
      - 'close'
      - 'position'
    """
    if initial_capital is None:
        initial_capital = STRATEGY_CONFIG["initial_capital"]
    if trade_cost is None:
        trade_cost = STRATEGY_CONFIG["trade_cost"]

    df = df.copy()

    # daily returns
    df["return"] = df["close"].pct_change().fillna(0)

    # strategy returns = position * return
    df["strategy_return"] = df["position"] * df["return"]

    # biaya transaksi: saat ada perubahan posisi
    df["trade"] = df["position"].diff().fillna(0).abs()
    # trade_cost dikali perdagangan, dipotong dari strategy_return
    df["strategy_return_after_cost"] = df["strategy_return"] - df["trade"] * trade_cost

    # equity curve
    df["equity"] = (1 + df["strategy_return_after_cost"]).cumprod() * initial_capital

    return df


def summarize_backtest(df: pd.DataFrame) -> Dict[str, float]:
    """
    Hitung ringkasan sederhana: total return, CAGR, Sharpe, max drawdown, dll.
    Implementasi detail ada di metrics.py, ini optional wrapper.
    """
    from src.backtest.metrics import (
        total_return,
        cagr,
        sharpe_ratio,
        max_drawdown,
    )

    equity = df["equity"]
    strat_ret = df["strategy_return_after_cost"]

    summary = {
        "total_return": total_return(equity),
        "cagr": cagr(equity),
        "sharpe_ratio": sharpe_ratio(strat_ret),
        "max_drawdown": max_drawdown(equity),
    }

    return summary
