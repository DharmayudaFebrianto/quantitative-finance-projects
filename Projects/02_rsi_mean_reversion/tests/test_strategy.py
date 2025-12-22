import pandas as pd
from src.strategy.rsi_mean_reversion import generate_signals


def test_generate_signals_columns():
    # Create a simple synthetic df with Close price
    df = pd.DataFrame({'Close': [1,2,3,4,3,2,1,2,3,4,5,6,7,8,9]})
    res = generate_signals(df, period=3, oversold=30, overbought=70)
    assert 'rsi' in res.columns
    assert 'signal' in res.columns
    assert 'position' in res.columns
    # position should be numeric
    assert pd.api.types.is_numeric_dtype(res['position'])
