import matplotlib.pyplot as plt
import pandas as pd


def plot_price_with_ma(
    df: pd.DataFrame,
    short_window: int,
    long_window: int,
    title: str = None
):
    """
    Plot harga close dengan MA short & MA long.
    """
    ma_short_col = f"ma_short_{short_window}"
    ma_long_col = f"ma_long_{long_window}"

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["close"], label="Close")
    if ma_short_col in df.columns:
        plt.plot(df.index, df[ma_short_col], label=f"MA {short_window}")
    if ma_long_col in df.columns:
        plt.plot(df.index, df[ma_long_col], label=f"MA {long_window}")

    plt.legend()
    plt.grid(True)
    plt.xlabel("Date")
    plt.ylabel("Price")
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_equity_curve(df: pd.DataFrame, title: str = "Equity Curve"):
    """
    Plot equity curve dari backtest.
    Expects 'equity' column.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["equity"], label="Equity")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
