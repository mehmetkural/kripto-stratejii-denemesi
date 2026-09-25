"""Backtest'i çalıştırır ve siteye gömülecek sonuçları docs/results.json'a yazar.

Kullanım:  python3 scripts/build_results.py
"""
import json
from pathlib import Path

import pandas as pd

from strategy import Params, asdict, indicators, load_prices, run, stats

ROOT = Path(__file__).resolve().parent.parent
TRAIN = ("2018-01-01", "2024-12-31")   # parametreler SADECE bu aralıkta seçildi
TEST_START = "2025-01-01"              # kilitli, daha önce görülmemiş dönem
POSITION_SIZE = 0.10                   # sermaye eğrisi için işlem başına %10


def fmt_trades(t: pd.DataFrame) -> list:
    out = []
    for r in t.itertuples():
        out.append({
            "coin": r.coin, "entry_date": r.entry_date.strftime("%Y-%m-%d"),
            "exit_date": r.exit_date.strftime("%Y-%m-%d"), "entry": float(r.entry),
            "exit": float(r.exit), "rsi": float(r.rsi), "trend_gap": float(r.trend_gap),
            "days": int(r.days), "reason": r.reason, "ret": round(float(r.ret), 5),
            "gross": round(float(r.gross), 5), "win": bool(r.win),
        })
    return out


def equity(t: pd.DataFrame) -> list:
    eq, pts = 1.0, []
    for r in t.sort_values("exit_date").itertuples():
        eq *= 1 + POSITION_SIZE * r.ret
        pts.append({"date": r.exit_date.strftime("%Y-%m-%d"), "equity": round(eq, 5)})
    return pts


def blocks_of_ten(t: pd.DataFrame) -> dict:
    """Ardışık, çakışmayan 10'lu işlem bloklarında kazanan sayısı dağılımı."""
    wins = t.sort_values("entry_date").win.astype(int).tolist()
    counts = [sum(wins[i:i + 10]) for i in range(0, len(wins) - 9, 10)]
    return {str(k): counts.count(k) for k in range(11)}


def main():
    prices = load_prices(ROOT / "data/prices.csv")
    p = Params()
    train = run(prices, p, *TRAIN)
    test = run(prices, p, TEST_START)
    first10 = test.head(10)

    # Yıllık kırılım (eğitim + test)
    allt = run(prices, p, TRAIN[0])
    by_year = [{"year": int(y), **stats(g)} for y, g in allt.groupby(allt.entry_date.dt.year)]
    by_coin = [{"coin": c, **stats(g)} for c, g in test.groupby("coin")]

    # BTC fiyatı + SMA100 (test dönemi) — piyasa rejimi grafiği
    btc = prices["BTC"]
    sma = btc.rolling(p.btc_sma).mean()
    seg = btc[btc.index >= TEST_START]
    btc_series = [{"date": d.strftime("%Y-%m-%d"), "close": round(float(c), 2),
                   "sma": round(float(sma[d]), 2)} for d, c in seg.items()]

    # Verinin son gününde her coin için güncel durum
    status = []
    for coin, close in prices.items():
        d = indicators(close, btc, p).iloc[-1]
        status.append({"coin": coin, "date": d.name.strftime("%Y-%m-%d"),
                       "close": float(d.close), "trend_ok": bool(d.close > d.sma_trend),
                       "btc_ok": bool(d.btc_ok), "rsi": round(float(d.rsi), 1),
                       "signal": bool(d.signal)})

    res = {
        "params": asdict(p), "train_range": TRAIN, "test_start": TEST_START,
        "data_end": max(s.index.max() for s in prices.values()).strftime("%Y-%m-%d"),
        "coins": sorted(prices), "position_size": POSITION_SIZE,
        "train": stats(train), "test": stats(test), "first10": stats(first10),
        "first10_trades": fmt_trades(first10), "test_trades": fmt_trades(test),
        "test_equity": equity(test), "train_equity": equity(train),
        "train_blocks": blocks_of_ten(train), "by_year": by_year, "by_coin": by_coin,
        "btc_series": btc_series, "status": sorted(status, key=lambda s: s["coin"]),
    }
    out = ROOT / "docs/results.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print("yazıldı:", out)
    for k in ("train", "test", "first10"):
        print(k, {a: (round(b, 3) if b is not None else None) for a, b in res[k].items()})
    print("10'lu bloklar (eğitim):", res["train_blocks"])
    print("by_year:", [(y["year"], y["n"], round(y.get("win_rate", 0), 2)) for y in by_year])


if __name__ == "__main__":
    main()
