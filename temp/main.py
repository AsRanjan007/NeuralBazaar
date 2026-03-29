import yfinance as yf
import pandas as pd

# Stock select kar (e.g. TCS)
ticker = "TCS.NS"

# Data download karein last 5 years ka
df = yf.download(ticker, start="2019-01-01", end="2024-12-31")

# Show first few rows
print(df.head())
