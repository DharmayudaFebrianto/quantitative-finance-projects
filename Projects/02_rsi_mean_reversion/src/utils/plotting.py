"""Beginner-friendly plotting helpers."""
import matplotlib.pyplot as plt


def plot_signals(df, price_col="Close", rsi_col="rsi", position_col="position"):
    fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    ax[0].plot(df.index, df[price_col], label="Price")
    ax[0].set_ylabel("Price")

    # highlight long positions
    longs = df[df[position_col] == 1]
    ax[0].scatter(longs.index, longs[price_col], marker="^", color="g", label="Long", zorder=5)

    ax[1].plot(df.index, df[rsi_col], label="RSI")
    ax[1].axhline(30, color="gray", linestyle="--", label="Oversold")
    ax[1].axhline(70, color="gray", linestyle="--", label="Overbought")
    ax[1].set_ylabel("RSI")

    ax[0].legend()
    ax[1].legend()
    plt.tight_layout()
    return fig, ax