# arima_model.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMA


def forecast_next_7_days(ticker: str = "META"):
    """
    Train an ARIMA(5,1,0) on the last year of daily closes and
    predict the next 7 business days.

    Returns
    -------
    forecast_df : pd.DataFrame
        Columns: [Date, Predicted]
    fig_full : matplotlib.figure.Figure
        Historical + 7‑day forecast figure
    fig_zoom : matplotlib.figure.Figure
        Zoom‑in figure showing just the 7 forecast points
    """
    # ── 1. Download one‑year daily data ─────────────────────────────
    df = yf.download(ticker, period="1y", interval="1d")
    if df.empty:
        raise ValueError("No data downloaded for this ticker.")
    close = df["Close"].asfreq("B")  # force business‑day frequency

    # ── 2. Fit ARIMA(5,1,0) ─────────────────────────────────────────
    model = ARIMA(close, order=(5, 1, 0))
    model_fit = model.fit()

    # ── 3. Forecast next 7 business days ────────────────────────────
    forecast_vals = model_fit.forecast(steps=7)
    last_date = close.index[-1]
    future_dates = [last_date + timedelta(days=i) for i in range(1, 8)]

    forecast_df = pd.DataFrame(
        {"Date": future_dates, "Predicted": forecast_vals.values}
    )

    # ── 4. Plot A • historical + forecast ───────────────────────────
    fig_full, ax1 = plt.subplots(figsize=(11, 4))
    ax1.plot(close.index, close, label="Historical", color="steelblue")
    ax1.plot(future_dates, forecast_vals, "o--", color="orangered",
             label="Forecast (7 days)")
    ax1.set_title(f"{ticker} – ARIMA(5,1,0) Forecast")
    ax1.set_xlabel("Date"); ax1.set_ylabel("Price")
    ax1.grid(ls=":"); ax1.legend()

    # ── 5. Plot B • zoom only forecast days ─────────────────────────
    fig_zoom, ax2 = plt.subplots(figsize=(10, 3.5))
    ax2.plot(future_dates, forecast_vals, marker="o", color="orangered")
    ax2.set_title("🔍 7‑Day Forecast (ARIMA)")
    ax2.set_xticks(future_dates)
    ax2.set_xticklabels([d.strftime("%b %d") for d in future_dates], rotation=45)
    ax2.set_ylabel("Predicted Price")
    for d, v in zip(future_dates, forecast_vals):
        ax2.annotate(f"{v:.2f}", (d, v), xytext=(0, 6),
                     textcoords="offset points", ha="center", fontsize=8)
    ax2.grid(ls="--", alpha=.4)

    return forecast_df, fig_full, fig_zoom


# Optional quick test / standalone run
if __name__ == "__main__":
    df_out, f1, f2 = forecast_next_7_days("META")
    print(df_out)
    plt.show()          # shows fig_full
    plt.show()          # shows fig_zoom
