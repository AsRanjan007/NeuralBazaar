# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from tensorflow.keras.models import Sequential
# # from tensorflow.keras.layers import LSTM, Dense
# # from sklearn.preprocessing import MinMaxScaler
# # import yfinance as yf

# # # Load data
# # meta = yf.Ticker("META")
# # df = meta.history(period="1y")[['Close']]
# # df.dropna(inplace=True)

# # # Scale data
# # scaler = MinMaxScaler(feature_range=(0, 1))
# # scaled_data = scaler.fit_transform(df.values)

# # # Prepare training data
# # look_back = 60
# # X_train, y_train = [], []
# # for i in range(look_back, len(scaled_data)):
# #     X_train.append(scaled_data[i - look_back:i, 0])
# #     y_train.append(scaled_data[i, 0])

# # X_train, y_train = np.array(X_train), np.array(y_train)
# # X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

# # # Build LSTM model
# # model = Sequential()
# # model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
# # model.add(LSTM(units=50))
# # model.add(Dense(1))
# # model.compile(optimizer='adam', loss='mean_squared_error')
# # model.fit(X_train, y_train, epochs=10, batch_size=32)

# # # Predict next 7 days
# # future_input = scaled_data[-look_back:].reshape(1, look_back, 1)
# # predictions = []
# # for _ in range(7):
# #     pred = model.predict(future_input)[0][0]
# #     predictions.append(pred)
# #     future_input = np.append(future_input[:, 1:, :], [[[pred]]], axis=1)

# # predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# # # Create date range for prediction
# # last_date = df.index[-1]
# # future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)

# # # Plot
# # plt.figure(figsize=(10, 5))
# # plt.plot(df.index, df['Close'], label='Actual')
# # plt.plot(future_dates, predicted_prices, label='LSTM 7-Day Forecast')
# # plt.title('LSTM Forecast for META')
# # plt.xlabel('Date')
# # plt.ylabel('Price')
# # plt.legend()
# # plt.grid()
# # plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
# from sklearn.preprocessing import MinMaxScaler
# import yfinance as yf
# from indicators.technical_indicators import add_technical_indicators

# # Load data
# df = yf.Ticker("META").history(period="1y")
# df = add_technical_indicators(df)

# # Use only 'Close' price for prediction
# data = df[['Close']].values

# # Scale data
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(data)

# look_back = 60
# X_train, y_train = [], []

# for i in range(look_back, len(scaled_data)):
#     X_train.append(scaled_data[i - look_back:i, 0])
#     y_train.append(scaled_data[i, 0])

# X_train, y_train = np.array(X_train), np.array(y_train)
# X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# # Build LSTM model
# model = Sequential()
# model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
# model.add(LSTM(units=50))
# model.add(Dense(1))

# model.compile(loss='mean_squared_error', optimizer='adam')

# # Train model
# model.fit(X_train, y_train, epochs=10, batch_size=32)

# # Predict
# predicted = model.predict(X_train)
# predicted_prices = scaler.inverse_transform(predicted)

# # Plot results
# plt.figure(figsize=(12, 6))
# plt.plot(df.index[look_back:], df['Close'][look_back:], label='Actual Price')
# plt.plot(df.index[look_back:], predicted_prices, label='Predicted Price')
# plt.title('Stock Price Prediction with LSTM')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()






import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

# Load data
meta = yf.Ticker("META")
df = meta.history(period="1y")[['Close']]
df.dropna(inplace=True)

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df.values)

# Prepare training data
look_back = 60
X_train, y_train = [], []
for i in range(look_back, len(scaled_data)):
    X_train.append(scaled_data[i - look_back:i, 0])
    y_train.append(scaled_data[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

# Build LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
model.add(LSTM(units=50))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Predict next 7 days
future_input = scaled_data[-look_back:].reshape(1, look_back, 1)
predictions = []
for _ in range(7):
    pred = model.predict(future_input)[0][0]
    predictions.append(pred)
    future_input = np.append(future_input[:, 1:, :], [[[pred]]], axis=1)

predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Create date range for prediction
last_date = df.index[-1]
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='Actual')
plt.plot(future_dates, predicted_prices, label='LSTM 7-Day Forecast')
plt.title('LSTM Forecast for META')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
