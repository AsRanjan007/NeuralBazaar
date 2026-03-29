import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential #type: ignore
from tensorflow.keras.layers import LSTM, Dense#type: ignore
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

# Step 1: CSV file load karo with correct header and index
# df = pd.read_csv('AAPL_data.csv', header=2, index_col=0, parse_dates=True)
meta = yf.Ticker("META")
df = meta.history(period="1y")
print("Dataframe columns:", df.columns)  # Columns check karne ke liye

# Step 2: Close column numeric banao aur NaN hatao
# df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
# df.dropna(subset=['Close'], inplace=True)

# Step 3: Scaling of data for LSTM
data = df[['Close']].values

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)

# Step 4: Prepare training data for LSTM (e.g., use past 60 days to predict next day)
look_back = 60
X_train, y_train = [], []

for i in range(look_back, len(scaled_data)):
    X_train.append(scaled_data[i-look_back:i, 0])
    y_train.append(scaled_data[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

# LSTM input shape = (samples, time_steps, features)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Step 5: LSTM Model Banaye
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

# Step 6: Model Train karo
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Step 7: Prediction karne ke liye example (same training data pe)
predicted = model.predict(X_train)
predicted_prices = scaler.inverse_transform(predicted)

# Step 8: Actual aur predicted prices plot karo
plt.figure(figsize=(12,6))
plt.plot(df.index[look_back:], df['Close'][look_back:], label='Actual Price')
plt.plot(df.index[look_back:], predicted_prices, label='Predicted Price')
plt.title('Stock Price Prediction with LSTM')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
