"""
Quant Project - Moving Average Crossover

Package ini berisi:
- config          konfigurasi project
- data            modul download & load data
- strategy        logika strategi MA crossover
- backtest        engine & metrics untuk backtest
- utils           plotting dan helper lain
"""

from . import config
from .data import downloader
from .strategy import ma_crossover
from .backtest import engine, metrics
from .utils import plotting

__all__ = [
    "config",
    "downloader",
    "ma_crossover",
    "engine",
    "metrics",
    "plotting",
]
