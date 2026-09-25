# Kripto Strateji: Trend İçi Geri Çekilme (TİGÇ)

Yükselen trenddeki kripto paralarda kısa süreli aşırı satımları alıp hızlı toparlanmada satan bir strateji,
backtest kodu ve sonuçları anlatan GitHub Pages sitesi.

- **Site:** `docs/index.html` (GitHub Pages → *Deploy from a branch* → klasör: `/docs`)
- **Strateji kuralları:** `scripts/strategy.py`
- **Sonuçları yeniden üret:** `pip install pandas numpy && python3 scripts/build_results.py`
- **Veri:** `data/prices.csv` — [Coin Metrics Community Data](https://github.com/coinmetrics/data) günlük kapanışlar (CC BY-NC 4.0)

## Kurallar (özet)
Giriş: kapanış > SMA150 **ve** BTC > BTC SMA100 **ve** RSI(3) < 15.
Çıkış: kapanış > SMA5 ve kârda → kâr al; -%12 → zarar kes; 10 gün → zaman stopu.
Maliyet: işlem başına %0,1 komisyon + %0,05 kayma (alış ve satış).

## Sonuçlar
| Dönem | İşlem | Başarı |
|---|---|---|
| Eğitim 2018–2024 (parametreler burada seçildi) | 212 | 167 (%79) |
| Test 2025 – Mayıs 2026, **ilk 10 işlem** | 10 | **10** |
| Test dönemi tamamı | 34 | 30 (%88) |

Yatırım tavsiyesi değildir; tüm işlemler geçmiş veride simülasyondur.
