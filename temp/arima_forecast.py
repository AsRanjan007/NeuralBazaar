# # import yfinance as yf
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # from statsmodels.tsa.arima.model import ARIMA
# # from indicators.technical_indicators import add_technical_indicators

# # # Step 1: Download stock data (META for the past 1 year)
# # ticker = "META"
# # data = yf.download(ticker, period="1y")
# # df = data[['Close']]
# # df = add_technical_indicators(df)


# # # Step 2: Fit ARIMA model (p=5, d=1, q=0) — tune if needed
# # model = ARIMA(df['Close'], order=(5,1,0))
# # model_fit = model.fit()

# # # Step 3: Forecast for the next 7 days
# # forecast = model_fit.forecast(steps=7)

# # # Step 4: Create forecast date index
# # last_date = df.index[-1]
# # forecast_index = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7, freq='B')  # 'B' = business days
# # forecast_df = pd.DataFrame({'Forecast': forecast}, index=forecast_index)

# # # Step 5: Plot results
# # plt.figure(figsize=(12, 6))
# # plt.plot(df['Close'], label="Actual Price")
# # plt.plot(forecast_df['Forecast'], label="7-Day Forecast", color='red', marker='o')
# # plt.title(f'{ticker} Stock Price Forecast with ARIMA')
# # plt.xlabel('Date')
# # plt.ylabel('Close Price (USD)')
# # plt.legend()
# # plt.grid(True)
# # plt.tight_layout()
# # plt.show()

# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA
# from indicators.technical_indicators import add_technical_indicators

# # Load data
# df = yf.Ticker("META").history(period="1y")
# df = add_technical_indicators(df)

# # Use 'Close' price series
# close_series = df['Close']

# # Fit ARIMA model (order can be tuned)
# model = ARIMA(close_series, order=(5, 1, 0))
# model_fit = model.fit()

# # Forecast next 7 days
# forecast = model_fit.forecast(steps=7)

# # Plot historical + forecast
# plt.figure(figsize=(12, 6))
# plt.plot(close_series, label='Historical Close Price')
# plt.plot(pd.date_range(start=close_series.index[-1], periods=8, freq='B')[1:], forecast, label='7-Day Forecast')
# plt.title('ARIMA Stock Price Forecast')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()

import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def add_technical_indicators(df):
    # Example: Adding simple moving average (SMA)
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    return df

# Step 1: Data load karo
df = yf.Ticker("META").history(period="1y")

# Step 2: Technical indicators add karo (optional)
df = add_technical_indicators(df)

# Step 3: Date index ko frequency do (Business Day)
df.index = pd.DatetimeIndex(df.index)
df = df.asfreq('B')

# Step 4: Close price ka series banao
close_series = df['Close']

# Step 5: ARIMA model banaye (order ko apne hisab se adjust kar sakte ho)
model = ARIMA(close_series, order=(5, 1, 0))
model_fit = model.fit()

# Step 6: 7 din ka forecast nikalo
forecast = model_fit.forecast(steps=7)
print("7-Day Forecast:\n", forecast)

# Step 7: Plot actual vs forecast
plt.figure(figsize=(12,6))
plt.plot(close_series, label='Actual Price')
plt.plot(forecast.index, forecast, label='7-Day Forecast', color='red')
plt.title('Stock Price Prediction with ARIMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

