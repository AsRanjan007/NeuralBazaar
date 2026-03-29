"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

# import numpy as np
# import pandas as pd
# import yfinance as yf
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
# import datetime

# def forecast_next_7_days(ticker):
#     # Load historical data for the past 1 year
#     end = datetime.datetime.today()
#     start = end - datetime.timedelta(days=365)
#     df = yf.download(ticker, start=start, end=end)

#     if df.empty:
#         raise ValueError("No data found for ticker:", ticker)

#     df = df[['Close']].dropna()

#     # Normalize the data
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(df)

#     sequence_length = 60
#     x = []
#     y = []

#     for i in range(sequence_length, len(scaled_data)):
#         x.append(scaled_data[i-sequence_length:i])
#         y.append(scaled_data[i])

#     x, y = np.array(x), np.array(y)
#     x = np.reshape(x, (x.shape[0], x.shape[1], 1))

#     # Build an optimized LSTM model for better accuracy
#     model = Sequential()
#     model.add(LSTM(units=128, return_sequences=True, input_shape=(x.shape[1], 1)))
#     model.add(LSTM(units=128, return_sequences=True))
#     model.add(LSTM(units=64, return_sequences=False))
#     model.add(Dense(units=64, activation='relu'))
#     model.add(Dense(units=32, activation='relu'))
#     model.add(Dense(units=1))
#     model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

#     # Train the model with increased epochs and a smaller batch size for better accuracy
#     model.fit(x, y, epochs=50, batch_size=16, verbose=1)

#     # Forecast the next 7 days
#     forecast_input = scaled_data[-sequence_length:]
#     forecast_input = forecast_input.reshape(1, sequence_length, 1)

#     future_predictions = []
#     for _ in range(7):
#         pred = model.predict(forecast_input, verbose=0)
#         future_predictions.append(pred[0][0])
#         # Correct reshaping and appending
#         forecast_input = np.append(forecast_input[:, 1:, :], [[[pred[0][0]]]], axis=1)

#     future_prices = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1)).flatten()
#     future_dates = [df.index[-1] + datetime.timedelta(days=i) for i in range(1, 8)]

#     return df, future_dates, future_prices

def forecast_next_7_days(ticker, df=None, start_date=None, end_date=None):
    import datetime
    import numpy as np
    import pandas as pd
    import yfinance as yf
    from sklearn.preprocessing import MinMaxScaler
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Input, LSTM, Dense, Layer
    import tensorflow.keras.backend as K

    # 🔥 Attention Layer
    class AttentionLayer(Layer):
        def __init__(self):
            super().__init__()

        def build(self, input_shape):
            self.W = self.add_weight(shape=(input_shape[-1], 1),
                                     initializer="normal")
            self.b = self.add_weight(shape=(input_shape[1], 1),
                                     initializer="zeros")

        def call(self, x):
            e = K.tanh(K.dot(x, self.W) + self.b)
            a = K.softmax(e, axis=1)
            context = x * a
            return K.sum(context, axis=1)

    # 📊 Add Indicators
    def add_indicators(df):
        # RSI
        delta = df['Close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / (avg_loss + 1e-10)
        df['RSI'] = 100 - (100 / (1 + rs))

        # MACD
        ema12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema12 - ema26
        df['MACD_signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

        return df

    # Load Data
    if df is None:
        end = datetime.datetime.today()
        start = end - datetime.timedelta(days=365)
        df = yf.download(ticker, start=start, end=end)

        if df.empty:
            raise ValueError("No data found for ticker:", ticker)

        df = df[['Close']].dropna()
    else:
        # Use provided dataframe (already processed)
        pass

    df = add_indicators(df)
    df = df.dropna()

    # 🔥 Features
    features = ['Close', 'RSI', 'MACD', 'MACD_signal']

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[features])

    sequence_length = 60
    x, y = [], []

    for i in range(sequence_length, len(scaled_data)):
        x.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i][0])  # predict Close

    x, y = np.array(x), np.array(y)

    # 🔥 Model
    inputs = Input(shape=(x.shape[1], x.shape[2]))

    x1 = LSTM(128, return_sequences=True)(inputs)
    x2 = LSTM(128, return_sequences=True)(x1)

    # Attention mechanism to focus on important time steps
    # This allows the model to weigh recent data more heavily, improving forecast accuracy.
    # The attention layer computes a context vector that emphasizes relevant time steps in the LSTM output, helping the model capture important patterns for forecasting.
    context = AttentionLayer()(x2)

    d1 = Dense(64, activation='relu')(context)
    d2 = Dense(32, activation='relu')(d1)
    outputs = Dense(1)(d2)

    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    # ⚡ Recency weighting
    weights = np.linspace(0.3, 1.0, len(y))

    model.fit(
        x, y,
        epochs=100,
        batch_size=16,
        sample_weight=weights,
        verbose=1
    )

    # 🔮 Forecast
    forecast_input = scaled_data[-sequence_length:]
    forecast_input = forecast_input.reshape(1, sequence_length, len(features))

    future_predictions = []

    # Fix location: prevent assignment of array to scalar and avoid sequence warning.
    for _ in range(7):
        pred = model.predict(forecast_input, verbose=0)
        pred_value = float(pred[0][0])  # scalar fix
        future_predictions.append(pred_value)

        # Create next timestep (only Close predicted, rest zero-filled)
        next_step = np.zeros((1, 1, len(features)))
        next_step[0, 0, 0] = pred_value  # Close

        forecast_input = np.concatenate(
            (forecast_input[:, 1:, :], next_step),
            axis=1
        )

    # Inverse transform (only Close)
    dummy = np.zeros((len(future_predictions), len(features)))
    dummy[:, 0] = future_predictions

    future_prices = scaler.inverse_transform(dummy)[:, 0]

    # Generate market trading dates (skip weekends and known holidays)
    def next_trading_date(start_date, holidays):
        candidate = start_date + datetime.timedelta(days=1)
        while candidate.weekday() >= 5 or candidate.date() in holidays:
            candidate += datetime.timedelta(days=1)
        return candidate

    # Example holiday list for NSE (add more as needed)
    nse_holidays = {
        # 2025
        datetime.date(2025, 1, 1),  # New Year's Day
        datetime.date(2025, 1, 26), # Republic Day
        datetime.date(2025, 3, 29), # Holi
        datetime.date(2025, 8, 15), # Independence Day
        datetime.date(2025, 10, 2), # Gandhi Jayanti
        datetime.date(2025, 12, 25),# Christmas Day
        # 2026 (example major holidays)
        datetime.date(2026, 1, 1),  # New Year's Day
        datetime.date(2026, 1, 26), # Republic Day
        datetime.date(2026, 3, 17), # Holi
        datetime.date(2026, 8, 15), # Independence Day
        datetime.date(2026, 10, 2), # Gandhi Jayanti
        datetime.date(2026, 12, 25),# Christmas Day
    }

    last_date = df.index[-1]
    future_dates = []
    while len(future_dates) < 7:
        next_date = next_trading_date(last_date, nse_holidays)
        future_dates.append(next_date)
        last_date = next_date

    return df, future_dates, future_prices