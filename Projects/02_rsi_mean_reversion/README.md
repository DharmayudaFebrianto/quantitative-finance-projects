# RSI Mean Reversion (Beginner-friendly)

Proyek sederhana untuk mengeksplorasi strategi mean reversion berdasarkan RSI (Relative Strength Index).

## Ringkasan singkat ✅
- Cari peluang long saat RSI berada di bawah level *oversold* (default 30).
- Tutup posisi saat RSI mencapai nilai netral (mis. > 50).
- Ini dimaksudkan sebagai proyek pembelajaran — bukan rekomendasi trading.

## Langkah-langkah setup (untuk pemula) 🔧
1. Pastikan Python 3.9+ terpasang (rekomendasi: gunakan environment seperti `venv` atau `conda`).

2. Buat environment baru (contoh dengan venv):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
```

3. Install dependency:

```bash
pip install -r requirements.txt
```

4. Download data contoh (script akan menyimpan ke `data/raw/`):

```python
from src.data.downloader import download_data

df = download_data("BTC-USD", start="2021-01-01")
```

5. Gunakan notebook `notebooks/` untuk menjalankan pipeline contoh: download data → generate signals → backtest → plot.

## Struktur folder 🔎
- `src/` : paket python utama (data, strategy, backtest, utils)
- `data/` : tempat menyimpan data `raw/` dan `processed/`
- `notebooks/` : contoh notebook dengan alur kerja

## Cara menggunakan modul (contoh singkat) 💡
```python
from src.data.downloader import download_data
from src.strategy.rsi_mean_reversion import generate_signals
from src.backtest.engine import run_backtest

# download
df = download_data("BTC-USD", start="2021-01-01")

# generate signals
sig_df = generate_signals(df)

# backtest
res = run_backtest(sig_df)
print(res[["strategy_equity", "market_equity"]].tail())
```

## Hal selanjutnya yang disarankan ✨
- Tambahkan notebook tutorial step-by-step (termasuk visualisasi dan penjelasan trade-by-trade)
- Tulis unit test untuk fungsi RSI dan backtest
- Eksplorasi parameter (periode RSI, threshold) dan lakukan grid search

---
Jika ingin, saya bisa: menambahkan notebook tutorial, membuat unit tests, atau menambahkan CI (GitHub Actions) untuk otomatis menjalankan test. Beri tahu mana yang mau dikerjakan selanjutnya.