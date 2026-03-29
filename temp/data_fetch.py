import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """
    Stock data download karega aur CSV mein save karega.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f"{ticker}_data.csv")
    print(f"{ticker} ka data download ho gaya aur save ho gaya CSV mein.")
    return data

# Test ke liye, agar direct run karoge to:
if __name__ == "__main__":
    fetch_stock_data("AAPL", "2020-01-01", "2023-01-01")
