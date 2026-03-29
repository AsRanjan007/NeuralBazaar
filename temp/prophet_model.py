# prophet_model.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from datetime import timedelta


def forecast_next_7_days(ticker="META"):
    """
    Train Prophet on 1-year stock data and forecast next 7 days.

    Returns
    -------
    forecast_df : pd.DataFrame
        Columns: [Date, Predicted]
    fig_full : matplotlib.figure.Figure
        Historical + 7‑day forecast
    fig_zoom : matplotlib.figure.Figure
        7‑day forecast zoomed-in
    """
    # ── 1. Download 1-year of data ────────────────────────────────
    df = yf.download(ticker, period="1y", interval="1d")
    if df.empty:
        raise ValueError("No data found for this ticker.")
    df = df.reset_index()
    df = df[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})

    # ── 2. Train Prophet model ─────────────────────────────────────
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    # ── 3. Make future DataFrame for 7 business days ───────────────
    future = model.make_future_dataframe(periods=7, freq='B')
    forecast = model.predict(future)

    forecast_tail = forecast[["ds", "yhat"]].tail(7)
    forecast_df = forecast_tail.rename(columns={"ds": "Date", "yhat": "Predicted"})

    # ── 4. Plot full history + forecast ────────────────────────────
    fig_full, ax1 = plt.subplots(figsize=(11, 4))
    ax1.plot(df['ds'], df['y'], label="Historical", color='steelblue')
    ax1.plot(forecast["ds"], forecast["yhat"], label="Forecast", color='darkorange')
    ax1.set_title(f"{ticker} – Prophet 7‑Day Forecast")
    ax1.set_xlabel("Date"); ax1.set_ylabel("Price")
    ax1.grid(ls=":"); ax1.legend()

    # ── 5. Plot zoom-in of 7‑day forecast only ─────────────────────
    fig_zoom, ax2 = plt.subplots(figsize=(10, 3.5))
    ax2.plot(forecast_df["Date"], forecast_df["Predicted"], marker="o", color='orangered')
    ax2.set_title("🔍 7‑Day Forecast (Prophet)")
    ax2.set_xticks(forecast_df["Date"])
    ax2.set_xticklabels([d.strftime("%b %d") for d in forecast_df["Date"]], rotation=45)
    ax2.set_ylabel("Predicted Price")
    for d, v in zip(forecast_df["Date"], forecast_df["Predicted"]):
        ax2.annotate(f"{v:.2f}", (d, v), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=8)
    ax2.grid(ls="--", alpha=.4)

    return forecast_df, fig_full, fig_zoom


# Optional test run
if __name__ == "__main__":
    df_out, f1, f2 = forecast_next_7_days("META")
    print(df_out)
    plt.show()
    plt.show()
