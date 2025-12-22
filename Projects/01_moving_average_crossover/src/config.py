from pathlib import Path

# Root path project ini (kalau dipanggil dari notebook di folder atasnya)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Konfigurasi data
DATA_CONFIG = {
    "tickers": ["BTC-USD"],  # bisa kamu ubah
    "start": "2025-10-01",
    "end": "2025-12-21",
}

# Konfigurasi strategi default
STRATEGY_CONFIG = {
    "short_window": 20,
    "long_window": 50,
    "initial_capital": 10000.0,
    "trade_cost": 0.0005,  # 0.05% per transaksi (optional, bisa 0)
}