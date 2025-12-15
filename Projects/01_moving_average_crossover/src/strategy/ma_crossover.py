import pandas as pd


def add_moving_averages(
    df: pd.DataFrame,
    short_window: int,
    long_window: int
) -> pd.DataFrame:
    """
    Tambahkan kolom moving average short & long ke DataFrame.

    Expects 'close' column.
    """
    df = df.copy()
    df[f"ma_short_{short_window}"] = df["close"].rolling(short_window).mean()
    df[f"ma_long_{long_window}"] = df["close"].rolling(long_window).mean()
    return df


def generate_ma_crossover_signals(
    df: pd.DataFrame,
    short_window: int,
    long_window: int
) -> pd.DataFrame:
    """
    Generate sinyal MA crossover:
    - signal = 1 : long
    - signal = 0 : out of market

    Crossover dilakukan pada MA short & long.
    """
    df = add_moving_averages(df, short_window, long_window)
    df = df.copy()

    ma_short_col = f"ma_short_{short_window}"
    ma_long_col = f"ma_long_{long_window}"

    df["signal"] = 0
    df.loc[df[ma_short_col] > df[ma_long_col], "signal"] = 1

    # posisi = signal yang digeser 1 bar (entry di open bar berikutnya)
    df["position"] = df["signal"].shift(1).fillna(0)

    return df
