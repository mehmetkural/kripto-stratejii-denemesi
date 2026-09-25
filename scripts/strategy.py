"""Trend İçi Geri Çekilme (TİGÇ) stratejisi — backtest motoru.

Veri: Coin Metrics açık veri seti (günlük kapanış fiyatları, USD).
Tüm sinyaller ve işlemler günlük KAPANIŞ fiyatı üzerinden hesaplanır.
"""
from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd

FEE = 0.001       # işlem başına komisyon (%0.1, alış + satış ayrı ayrı)
SLIPPAGE = 0.0005  # işlem başına kayma (%0.05)


@dataclass(frozen=True)
class Params:
    trend_sma: int = 150     # uzun vadeli trend filtresi (coin'in kendisi)
    btc_sma: int = 100       # piyasa rejimi filtresi (BTC)
    rsi_len: int = 3         # kısa vadeli RSI
    rsi_entry: float = 15.0  # RSI bu değerin altına düşünce "aşırı satım" -> al
    exit_sma: int = 5        # fiyat bu ortalamanın üstünde kapanınca kâr al
    stop_pct: float = 0.12   # kapanış bazlı zarar kes
    max_hold: int = 10       # zaman stopu (gün)


def rsi(close: pd.Series, n: int) -> pd.Series:
    """Wilder RSI."""
    delta = close.diff()
    up = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    down = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = up / down.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).fillna(100)


def load_prices(path="data/prices.csv") -> dict:
    df = pd.read_csv(path, parse_dates=["date"])
    return {c: g.set_index("date")["close"].sort_index() for c, g in df.groupby("coin")}


def indicators(close: pd.Series, btc: pd.Series, p: Params) -> pd.DataFrame:
    d = pd.DataFrame({"close": close})
    d["sma_trend"] = close.rolling(p.trend_sma).mean()
    d["sma_exit"] = close.rolling(p.exit_sma).mean()
    d["rsi"] = rsi(close, p.rsi_len)
    btc_sma = btc.rolling(p.btc_sma).mean()
    d["btc_ok"] = (btc > btc_sma).reindex(d.index).fillna(False)
    d["signal"] = (d.close > d.sma_trend) & d.btc_ok & (d.rsi < p.rsi_entry)
    return d


def backtest_coin(coin: str, close: pd.Series, btc: pd.Series, p: Params) -> list:
    d = indicators(close, btc, p)
    trades, pos = [], None
    for row in d.itertuples():
        date = row.Index
        if pos is None:
            if row.signal:
                pos = {"coin": coin, "entry_date": date, "entry": row.close,
                       "rsi": round(row.rsi, 1),
                       "trend_gap": round(row.close / row.sma_trend - 1, 4), "days": 0}
            continue
        pos["days"] += 1
        chg = row.close / pos["entry"] - 1
        reason = None
        if chg <= -p.stop_pct:
            reason = "Zarar kes"
        elif row.close > row.sma_exit and chg > 0:
            reason = "Kâr al (SMA5 üstü)"
        elif pos["days"] >= p.max_hold:
            reason = "Zaman stopu"
        if reason:
            ret = row.close / pos["entry"] * (1 - FEE - SLIPPAGE) / (1 + FEE + SLIPPAGE) - 1
            pos.update(exit_date=date, exit=row.close, reason=reason,
                       ret=ret, gross=chg, win=ret > 0)
            trades.append(pos)
            pos = None
    return trades


def run(prices: dict, p: Params, start=None, end=None) -> pd.DataFrame:
    btc = prices["BTC"]
    allt = []
    for coin, close in prices.items():
        allt += backtest_coin(coin, close, btc, p)
    t = pd.DataFrame(allt)
    if t.empty:
        return t
    if start:
        t = t[t.entry_date >= pd.Timestamp(start)]
    if end:
        t = t[t.entry_date <= pd.Timestamp(end)]
    return t.sort_values(["entry_date", "coin"]).reset_index(drop=True)


def stats(t: pd.DataFrame) -> dict:
    if t.empty:
        return {"n": 0}
    wins, losses = t[t.ret > 0].ret, t[t.ret <= 0].ret
    pf = wins.sum() / -losses.sum() if len(losses) and losses.sum() < 0 else None  # kayıp yoksa tanımsız
    return {
        "n": int(len(t)),
        "win_rate": float(t.win.mean()),
        "avg_ret": float(t.ret.mean()),
        "avg_win": float(wins.mean()) if len(wins) else 0.0,
        "avg_loss": float(losses.mean()) if len(losses) else 0.0,
        "profit_factor": float(pf) if pf is not None else None,
        "avg_days": float(t.days.mean()),
        "worst": float(t.ret.min()),
        "best": float(t.ret.max()),
    }


__all__ = ["Params", "load_prices", "run", "stats", "indicators", "asdict"]
