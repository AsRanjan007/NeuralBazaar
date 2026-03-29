# # from prophet import Prophet
# # import yfinance as yf
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Load data
# # meta = yf.Ticker("META")
# # df = meta.history(period="1y")[['Close']].reset_index()
# # df.columns = ['ds', 'y']
# # df['ds'] = df['ds'].dt.tz_localize(None)  # remove timezone

# # # Build Prophet model
# # model = Prophet()
# # model.fit(df)

# # # Predict next 7 days
# # future = model.make_future_dataframe(periods=7)
# # forecast = model.predict(future)

# # # Plot full forecast
# # model.plot(forecast)
# # plt.title('Prophet Forecast for META')
# # plt.xlabel('Date')
# # plt.ylabel('Price')
# # plt.grid()
# # plt.show()

# # # Show only the 7-day forecast
# # print(forecast[['ds', 'yhat']].tail(7))


# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt
# from prophet import Prophet
# from indicators.technical_indicators import add_technical_indicators

# # Load data
# df = yf.Ticker("META").history(period="1y")
# df = add_technical_indicators(df)

# # Prepare DataFrame for Prophet
# prophet_df = df.reset_index()[['Date', 'Close']]
# prophet_df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

# # Initialize and train Prophet model
# model = Prophet(daily_seasonality=True)
# model.fit(prophet_df)

# # Create dataframe for future 7 days
# future = model.make_future_dataframe(periods=7)

# # Forecast
# forecast = model.predict(future)

# # Plot results
# model.plot(forecast)
# plt.title("Prophet Stock Price Forecast")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.show()
import yfinance as yf
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Step 1: Data fetch karo
meta = yf.Ticker("META")
df = meta.history(period="1y")

# Step 2: Prophet ke liye data prepare karo
prophet_df = df.reset_index()[['Date', 'Close']]
prophet_df.columns = ['ds', 'y']

# Step 3: Timezone info hatao (important!)
prophet_df['ds'] = prophet_df['ds'].dt.tz_localize(None)

# Step 4: Prophet model banaye aur fit karein
model = Prophet()
model.fit(prophet_df)

# Step 5: Future dataframe (7 din ka forecast)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# Step 6: Forecast print karo (sirf future 7 din ka)
print("7-Day Forecast:")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7))

# Step 7: Actual vs Predicted plot
plt.figure(figsize=(10,6))
plt.plot(prophet_df['ds'], prophet_df['y'], label='Actual')
plt.plot(forecast['ds'], forecast['yhat'], label='Predicted')
plt.title('Meta Stock Price Prediction using Prophet')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
