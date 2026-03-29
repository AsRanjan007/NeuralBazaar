"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

import pandas as pd

def atr(df, period=14):
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift(1)).abs()
    low_close = (df['Low'] - df['Close'].shift(1)).abs()
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.rolling(window=period).mean()

def supertrend(df, period=10, multiplier=3):
    df_copy = df.copy()
    atr_val = atr(df_copy, period)
    hl2 = (df_copy['High'] + df_copy['Low']) / 2
    upperband = hl2 + (multiplier * atr_val)
    lowerband = hl2 - (multiplier * atr_val)
    
    supertrend = pd.Series(index=df_copy.index)
    trend = pd.Series(index=df_copy.index, dtype=int)  # 1 for uptrend, -1 for downtrend
    
    trend.iloc[0] = 1
    supertrend.iloc[0] = lowerband.iloc[0]
    
    for i in range(1, len(df_copy)):
        if trend.iloc[i-1] == 1:
            if df_copy['Close'].iloc[i] > supertrend.iloc[i-1]:
                trend.iloc[i] = 1
                supertrend.iloc[i] = max(lowerband.iloc[i], supertrend.iloc[i-1])
            else:
                trend.iloc[i] = -1
                supertrend.iloc[i] = upperband.iloc[i]
        else:
            if df_copy['Close'].iloc[i] < supertrend.iloc[i-1]:
                trend.iloc[i] = -1
                supertrend.iloc[i] = min(upperband.iloc[i], supertrend.iloc[i-1])
            else:
                trend.iloc[i] = 1
                supertrend.iloc[i] = lowerband.iloc[i]
    
    df['Supertrend'] = supertrend
    df['Supertrend_Trend'] = trend
    return df

def vwap(df):
    df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()
    return df

def pivot_points(df):
    df['Pivot'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['R1'] = 2 * df['Pivot'] - df['Low']
    df['S1'] = 2 * df['Pivot'] - df['High']
    df['R2'] = df['Pivot'] + (df['High'] - df['Low'])
    df['S2'] = df['Pivot'] - (df['High'] - df['Low'])
    return df

def stochastic(df, k_period=14, d_period=3):
    lowest_low = df['Low'].rolling(window=k_period).min()
    highest_high = df['High'].rolling(window=k_period).max()
    df['%K'] = 100 * (df['Close'] - lowest_low) / (highest_high - lowest_low)
    df['%D'] = df['%K'].rolling(window=d_period).mean()
    return df

def add_technical_indicators(df):
    # Simple Moving Average and EMA
    df["SMA_14"] = df["Close"].rolling(window=14).mean()
    
    '''
    EMA_t = alpha * P_t + (1 - alpha)*EMA_(t-1)
    EMA_t = EMA at time t
    P_t = Price at value time t 
    alpha = smoothing factor 
    EMA_(t-1) = EMA at previous step
    '''
    df["EMA_14"] = df["Close"].ewm(span=14, adjust=False).mean()

    # RSI with Wilder's smoothing
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.where(delta < 0, 0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss
    df["RSI_14"] = 100 - (100 / (1 + rs))

    # MACD
    ema_12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = ema_12 - ema_26
    df["Signal_Line"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # Bollinger Bands
    df["BB_Middle"] = df["Close"].rolling(window=20).mean()
    df["BB_Std"] = df["Close"].rolling(window=20).std()
    df["BB_Upper"] = df["BB_Middle"] + 2 * df["BB_Std"]
    df["BB_Lower"] = df["BB_Middle"] - 2 * df["BB_Std"]

    # Additional indicators for India market
    df = supertrend(df)
    df = vwap(df)
    df = pivot_points(df)
    df = stochastic(df)
    df['ATR'] = atr(df)

    return df
