"""Strateji iyileştirme araştırması.

Kural: varyantlar SADECE eğitim döneminde (2018–2024) karşılaştırılır ve seçilir.
Test dönemi (2025+) seçim bittikten sonra yalnızca raporlama için hesaplanır.

Kullanım:  python3 scripts/research.py
"""
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
import pandas as pd

from strategy import FEE, SLIPPAGE, load_prices, rsi

TRAIN = ("2018-01-01", "2024-12-31")


@dataclass(frozen=True)
class V:
    name: str = "Temel (v1)"
    trend_sma: int = 150
    btc_sma: int = 100
    rsi_entry: float = 15.0
    stop_pct: float = 0.12
    max_hold: int = 10
    # --- varyant anahtarları ---
    slope: bool = False          # SMA50 > SMA150 (trend olgun ve yükselen)
    vol_stop: float = 0.0        # >0 ise stop = k * 20g oynaklık (sınırlı %6–%20)
    btc_crash: float = 0.0       # >0 ise BTC son 3 günde bu kadar düştüyse girme
    exit_rsi: float = 0.0        # >0 ise çıkış: RSI3 > değer (SMA5 yerine)
    min_dip: float = 0.0         # >0 ise fiyat 10g zirvesinden en az bu kadar aşağıda olmalı
    max_pos: int = 0             # >0 ise aynı anda en fazla bu kadar pozisyon (düşük RSI öncelikli)


def prep(prices: dict, v: V) -> dict:
    btc = prices["BTC"]
    btc_ok = btc > btc.rolling(v.btc_sma).mean()
    btc_3d = btc.pct_change(3)
    out = {}
    for c, close in prices.items():
        d = pd.DataFrame({"close": close})
        d["sma_t"] = close.rolling(v.trend_sma).mean()
        d["sma50"] = close.rolling(50).mean()
        d["sma5"] = close.rolling(5).mean()
        d["rsi"] = rsi(close, 3)
        d["vol"] = close.pct_change().rolling(20).std()
        d["dip"] = close / close.rolling(10).max() - 1
        sig = (d.close > d.sma_t) & btc_ok.reindex(d.index).fillna(False) & (d.rsi < v.rsi_entry)
        if v.slope:
            sig &= d.sma50 > d.sma_t
        if v.btc_crash:
            sig &= btc_3d.reindex(d.index).fillna(0) > -v.btc_crash
        if v.min_dip:
            sig &= d.dip <= -v.min_dip
        d["signal"] = sig
        out[c] = d
    return out


def simulate(prices: dict, v: V) -> pd.DataFrame:
    """Gün gün, tüm coin'ler birlikte simüle edilir (max_pos için gerekli)."""
    data = prep(prices, v)
    dates = sorted(set().union(*[d.index for d in data.values()]))
    open_pos, trades = {}, []
    exited = set()  # aynı gün çıkıp tekrar girmeyi engelle (v1 ile aynı davranış)
    cost = (1 - FEE - SLIPPAGE) / (1 + FEE + SLIPPAGE)
    for date in dates:
        # çıkışlar
        exited.clear()
        for c in list(open_pos):
            d = data[c]
            if date not in d.index:
                continue
            row, pos = d.loc[date], open_pos[c]
            pos["days"] += 1
            chg = row.close / pos["entry"] - 1
            reason = None
            if chg <= -pos["stop"]:
                reason = "Zarar kes"
            elif v.exit_rsi and row.rsi > v.exit_rsi and chg > 0:
                reason = "Kâr al (RSI)"
            elif not v.exit_rsi and row.close > row.sma5 and chg > 0:
                reason = "Kâr al (SMA5 üstü)"
            elif pos["days"] >= v.max_hold:
                reason = "Zaman stopu"
            if reason:
                ret = row.close / pos["entry"] * cost - 1
                pos.update(exit_date=date, exit=row.close, reason=reason, ret=ret, win=ret > 0)
                trades.append(pos)
                del open_pos[c]
                exited.add(c)
        # girişler
        cands = []
        for c, d in data.items():
            if c in open_pos or c in exited or date not in d.index:
                continue
            row = d.loc[date]
            if row.signal:
                cands.append((row.rsi, c, row))
        cands.sort()
        for r, c, row in cands:
            if v.max_pos and len(open_pos) >= v.max_pos:
                break
            stop = v.stop_pct
            if v.vol_stop:
                stop = float(np.clip(v.vol_stop * row.vol * np.sqrt(5), 0.06, 0.20))
            open_pos[c] = {"coin": c, "entry_date": date, "entry": row.close, "rsi": round(r, 1),
                           "trend_gap": round(row.close / row.sma_t - 1, 4), "stop": stop, "days": 0}
    t = pd.DataFrame(trades)
    return t.sort_values(["entry_date", "coin"]).reset_index(drop=True)


def summarize(t: pd.DataFrame) -> dict:
    if t.empty:
        return {"n": 0}
    w, l = t[t.ret > 0].ret, t[t.ret <= 0].ret
    yr = t.groupby(t.entry_date.dt.year).ret.mean()
    # portföy: her işlem sermayenin %10'u, çıkış sırasına göre bileşik
    eq = (1 + 0.10 * t.sort_values("exit_date").ret).cumprod()
    dd = (eq / eq.cummax() - 1).min()
    return {
        "n": len(t), "win": t.win.mean(), "avg": t.ret.mean(),
        "avg_win": w.mean(), "avg_loss": l.mean() if len(l) else 0.0,
        "pf": w.sum() / -l.sum() if l.sum() < 0 else np.nan,
        "worst": t.ret.min(), "neg_years": int((yr <= 0).sum()), "min_year": yr.min(),
        "total": eq.iloc[-1] - 1, "max_dd": dd,
    }


def split(t, a, b=None):
    t = t[t.entry_date >= pd.Timestamp(a)]
    return t[t.entry_date <= pd.Timestamp(b)] if b else t


VARIANTS = [
    V(),
    V(name="+ Trend eğimi (SMA50>SMA150)", slope=True),
    V(name="+ BTC çöküş filtresi (3g > -%8)", btc_crash=0.08),
    V(name="+ Oynaklığa göre stop (2.5σ)", vol_stop=2.5),
    V(name="+ Min. %8 geri çekilme", min_dip=0.08),
    V(name="RSI>50 çıkışı", exit_rsi=50),
    V(name="+ Maks. 4 pozisyon", max_pos=4),
]


def main(variants=VARIANTS, show_test=False):
    prices = load_prices(Path(__file__).resolve().parent.parent / "data/prices.csv")
    rows = []
    for v in variants:
        t = simulate(prices, v)
        s = summarize(split(t, *TRAIN))
        row = {"varyant": v.name, **s}
        if show_test:
            st = summarize(split(t, "2025-01-01"))
            row.update({"T_n": st["n"], "T_win": st["win"], "T_pf": st["pf"],
                        "T_ilk10": int(split(t, "2025-01-01").head(10).win.sum())})
        rows.append(row)
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    print(pd.DataFrame(rows).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
