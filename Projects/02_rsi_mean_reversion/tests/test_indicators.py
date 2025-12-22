import pandas as pd
from src.strategy.rsi_mean_reversion import compute_rsi


def test_compute_rsi_length_and_bounds():
    s = pd.Series(range(1, 51))
    rsi = compute_rsi(s, period=14)
    assert len(rsi) == len(s)
    # RSI values should be between 0 and 100 for non-NaN entries
    valid = rsi.dropna()
    assert ((valid >= 0) & (valid <= 100)).all()
