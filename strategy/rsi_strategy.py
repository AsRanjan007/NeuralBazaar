"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

import matplotlib.pyplot as plt
def rsi_strategy(df, lower=30, upper=70):
    df = df.copy()
    df['Signal'] = 0
    df.loc[df['RSI_14'] < lower, 'Signal'] = 1   # Buy
    df.loc[df['RSI_14'] > upper, 'Signal'] = -1  # Sell
    return df

def plot_rsi_strategy(df):
    plt.figure(figsize=(14, 7))

    # Price Chart
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(df['Close'], label='Close Price', color='black')
    ax1.set_title('RSI Strategy - Price')
    ax1.set_ylabel('Price')
    ax1.grid(True)

    # Buy & Sell Markers
    buy_signals = df[df['Signal'] == 1]
    sell_signals = df[df['Signal'] == -1]
    ax1.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', s=100, label='Buy Signal')
    ax1.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', s=100, label='Sell Signal')
    ax1.legend()

    # RSI Chart
    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(df['RSI_14'], label='RSI 14', color='purple')
    ax2.axhline(70, color='red', linestyle='--')
    ax2.axhline(30, color='green', linestyle='--')
    ax2.set_title('RSI Value')
    ax2.set_ylabel('RSI')
    ax2.set_xlabel('Date')
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()


# import pandas as pd

# def rsi_strategy(df):
#     df['Buy_Signal'] = df['RSI_14'] < 30
#     df['Sell_Signal'] = df['RSI_14'] > 70
#     return df
