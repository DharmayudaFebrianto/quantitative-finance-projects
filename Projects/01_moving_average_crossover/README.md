# Moving Average Crossover Backtest (Stocks & Crypto)

Project ini mengevaluasi strategi **Moving Average Crossover** (contoh: MA 20/50)
pada beberapa aset saham dan crypto menggunakan Python.

## 🎯 Tujuan

- Menguji apakah strategi MA Crossover mampu mengalahkan strategi buy & hold.
- Mengukur metrik kinerja: CAGR, Sharpe ratio, Max Drawdown, Win Rate.
- Menjadi contoh project quantitative finance level pemula–menengah.

## 🧱 Struktur Project

- `data/` — menyimpan data harga (raw & processed)
- `notebooks/` — eksplorasi data dan analisis interaktif
- `src/` — kode utama:
  - `data/` — download & load data
  - `strategy/` — fungsi pembentukan sinyal MA crossover
  - `backtest/` — engine backtest & perhitungan metrics
  - `utils/` — plotting
- `reports/` — hasil dalam bentuk gambar dan ringkasan

## 🚀 Cara Menjalankan

1. Buat environment dan install dependency:

   ```bash
   pip install -r requirements.txt
