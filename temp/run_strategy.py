# from indicator.technical_indicator import add_technical_indicators
# from strategy.strategy import moving_average_strategy
# import yfinance as yf

# # Data fetch karo
# df = yf.Ticker("META").history(period="1y")

# # Indicators add karo
# df = add_technical_indicators(df)

# # Strategy apply karo
# df = moving_average_strategy(df)

# # Signals dekh lo
# print(df[['Close', 'SMA_20', 'SMA_50', 'Signal']].tail(30))

# from indicator.technical_indicator import add_technical_indicators
# from strategy.strategy import moving_average_strategy
# from strategy.plot import plot_moving_average_strategy  # 👈 This line

# import yfinance as yf

# # Step 1: Data fetch
# df = yf.Ticker("META").history(period="1y")

# # Step 2: Indicators add karo
# df = add_technical_indicators(df)

# # Step 3: Strategy apply karo
# df = moving_average_strategy(df)

# # Step 4: Output print karo
# print(df[['Close', 'SMA_20', 'SMA_50', 'Signal']].tail(30))

# # Step 5: Strategy plot karo
# plot_moving_average_strategy(df)



from strategy.plot import plot_moving_average_strategy, plot_rsi_strategy, plot_macd_strategy, plot_bollinger_strategy
from indicator.technical_indicator import add_technical_indicators
from strategy.rsi_strategy import rsi_strategy
from strategy.macd_strategy import macd_strategy
from strategy.bollinger_strategy import bollinger_strategy
from strategy.backtest import backtest_strategy
import yfinance as yf
import pandas as pd


df = yf.Ticker("META").history(period="1y")
df = add_technical_indicators(df)

# Choose any strategy
df_rsi = rsi_strategy(df)
df_macd = macd_strategy(df)
df_boll = bollinger_strategy(df)

# Show last signals
print("📊 RSI Strategy:")
print(df_rsi[['Close', 'RSI_14', 'Signal']].tail(5))
print("\n📊 MACD Strategy:")
print(df_macd[['Close', 'MACD', 'Signal_Line', 'Signal']].tail(5))
print("\n📊 Bollinger Strategy:")
print(df_boll[['Close', 'BB_Upper', 'BB_Lower', 'Signal']].tail(5))

# df_rsi = rsi_strategy(df)
plot_rsi_strategy(df_rsi)
plot_macd_strategy(df_macd)
plot_bollinger_strategy(df_boll)

# from strategy.backtest import backtest_strategy

# Backtest RSI
rsi_profit, rsi_trades = backtest_strategy(df_rsi)
print(f"\n💰 RSI Strategy Total Profit: ₹{rsi_profit:.2f}")

# Backtest MACD
macd_profit, macd_trades = backtest_strategy(df_macd)
print(f"💰 MACD Strategy Total Profit: ₹{macd_profit:.2f}")

# Backtest Bollinger
boll_profit, boll_trades = backtest_strategy(df_boll)
print(f"💰 Bollinger Strategy Total Profit: ₹{boll_profit:.2f}")

# import pandas as pd

comparison_df = pd.DataFrame({
    'Strategy': ['RSI', 'MACD', 'Bollinger'],
    'Profit (₹)': [rsi_profit, macd_profit, boll_profit]
})

print("\n📊 Strategy Performance Comparison:")
print(comparison_df)


# import pandas as pd

# Export RSI trades
pd.DataFrame(rsi_trades, columns=["Action", "Date", "Price", "Profit"]).to_csv("rsi_trades.csv", index=False)

# Export MACD trades
pd.DataFrame(macd_trades, columns=["Action", "Date", "Price", "Profit"]).to_csv("macd_trades.csv", index=False)

# Export Bollinger trades
pd.DataFrame(boll_trades, columns=["Action", "Date", "Price", "Profit"]).to_csv("boll_trades.csv", index=False)

print("📁 Trade history exported successfully!")





import matplotlib.pyplot as plt

def plot_cumulative_profit(df, title):
    df = df.copy()
    df['Profit'] = 0
    position = 0
    buy_price = 0
    initial_investment = 1000
    profits = []

    for i in range(len(df)):
        signal = df['Signal'].iloc[i]
        price = df['Close'].iloc[i]

        if signal == 1 and position == 0:  # Buy
            position = 1
            buy_price = price
            profits.append(profits[-1] if profits else 0)
        elif signal == -1 and position == 1:  # Sell
            position = 0
            profit = ((price - buy_price) / buy_price) * initial_investment
            profits.append(profits[-1] + profit if profits else profit)
        else:
            profits.append(profits[-1] if profits else 0)

    df['Cumulative_Profit'] = profits

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Cumulative_Profit'], label=title)
    plt.title(f'Cumulative Profit Over Time - {title}')
    plt.xlabel('Date')
    plt.ylabel('Profit (₹)')
    plt.legend()
    plt.grid(True)
    plt.show()



plot_cumulative_profit(df_rsi, 'RSI Strategy')
plot_cumulative_profit(df_macd, 'MACD Strategy')
plot_cumulative_profit(df_boll, 'Bollinger Strategy')
