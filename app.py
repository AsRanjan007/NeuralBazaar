"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

# import streamlit as st
# import yfinance as yf
# import pandas as pd
# from indicator.technical_indicator import add_technical_indicators
# from strategy.rsi_strategy import rsi_strategy
# from strategy.macd_strategy import macd_strategy
# from strategy.bollinger_strategy import bollinger_strategy
# from strategy.backtest import backtest_strategy

# # 1. Page configuration
# st.set_page_config(page_title="Stock Strategy Dashboard 📈", layout="wide", page_icon="💹")

# # 2. Sidebar inputs
# st.sidebar.title("Settings")
# ticker = st.sidebar.text_input("Enter Stock Ticker", value="META")
# start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-05-30"))
# end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2025-05-30"))
# strategy_name = st.sidebar.selectbox("Select Strategy", ["RSI", "MACD", "Bollinger"])

# # 3. Fetch data and process on button click
# if st.sidebar.button("Run Strategy"):

#     with st.spinner(f"Fetching data for {ticker}..."):
#         df = yf.Ticker(ticker).history(start=start_date, end=end_date)
#         if df.empty:
#             st.error("No data found for this ticker and date range.")
#             st.stop()

#     with st.spinner("Adding technical indicators..."):
#         df = add_technical_indicators(df)

#     with st.spinner(f"Applying {strategy_name} strategy..."):
#         if strategy_name == "RSI":
#             df_strategy = rsi_strategy(df)
#         elif strategy_name == "MACD":
#             df_strategy = macd_strategy(df)
#         else:
#             df_strategy = bollinger_strategy(df)

#     with st.spinner("Backtesting strategy..."):
#         total_profit, trades = backtest_strategy(df_strategy)

#     # 4. Show last 5 rows of signals
#     st.subheader(f"{strategy_name} Strategy - Last 5 signals")
#     st.dataframe(df_strategy[['Close', 'Signal']].tail(5))

#     # 5. Show total profit
#     st.subheader("Strategy Performance")
#     st.metric(label="Total Profit (₹)", value=f"{total_profit:.2f}")

#     # 6. Show trade count
#     st.write(f"Number of trades executed: {len(trades)}")


# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt

# from indicator.technical_indicator import add_technical_indicators
# from strategy.rsi_strategy import rsi_strategy
# from strategy.macd_strategy import macd_strategy
# from strategy.bollinger_strategy import bollinger_strategy
# from strategy.backtest import backtest_strategy

# # 1. Page configuration
# st.set_page_config(page_title="Stock Strategy Dashboard 📈", layout="wide", page_icon="💹")

# # 2. Sidebar inputs
# st.sidebar.title("⚙️ Settings")
# ticker = st.sidebar.text_input("Enter Stock Ticker", value="META")
# start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-05-30"))
# end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2025-05-30"))
# strategy_name = st.sidebar.selectbox("Select Strategy", ["RSI", "MACD", "Bollinger"])

# # 3. Run strategy button
# if st.sidebar.button("🚀 Run Strategy"):

#     with st.spinner(f"Fetching data for {ticker}..."):
#         df = yf.Ticker(ticker).history(start=start_date, end=end_date)
#         if df.empty:
#             st.error("No data found for this ticker and date range.")
#             st.stop()

#     with st.spinner("Adding technical indicators..."):
#         df = add_technical_indicators(df)

#     with st.spinner(f"Applying {strategy_name} strategy..."):
#         if strategy_name == "RSI":
#             df_strategy = rsi_strategy(df)
#         elif strategy_name == "MACD":
#             df_strategy = macd_strategy(df)
#         else:
#             df_strategy = bollinger_strategy(df)

#     with st.spinner("Backtesting strategy..."):
#         total_profit, trades = backtest_strategy(df_strategy)

#     # 4. Last 5 signals
#     st.subheader(f"📋 {strategy_name} Strategy - Last 5 signals")
#     st.dataframe(df_strategy[['Close', 'Signal']].tail(5))

#     # 5. Performance metrics
#     st.subheader("📈 Strategy Performance")
#     st.metric(label="💰 Total Profit (₹)", value=f"{total_profit:.2f}")
#     st.write(f"🛒 Number of trades executed: {len(trades)}")

#     # 6. Strategy chart with buy/sell markers
#     st.subheader("📉 Strategy Chart")

#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.plot(df_strategy['Close'], label='Close Price', color='lightgray')

#     buy_signals = df_strategy[df_strategy['Signal'] == 'Buy']
#     sell_signals = df_strategy[df_strategy['Signal'] == 'Sell']

#     ax.plot(buy_signals.index, buy_signals['Close'], '^', markersize=10, color='green', label='Buy')
#     ax.plot(sell_signals.index, sell_signals['Close'], 'v', markersize=10, color='red', label='Sell')

#     ax.set_title(f"{ticker} - {strategy_name} Strategy", fontsize=14)
#     ax.set_ylabel("Price (₹)")
#     ax.legend()
#     st.pyplot(fig)

#     # 7. Export trades
#     st.subheader("📁 Export Trades")

#     if trades:
#         trade_df = pd.DataFrame(trades)
#         st.download_button(
#             label="📥 Download Trade History as CSV",
#             data=trade_df.to_csv(index=False),
#             file_name=f"{ticker}_{strategy_name}_trades.csv",
#             mime='text/csv'
#         )
#     else:
#         st.warning("No trades to export.")

#     # 8. Cumulative profit graph
#     st.subheader("📊 Cumulative Profit Over Time")

#     cumulative_profits = []
#     profit = 0
#     for trade in trades:
#         profit += trade['Profit']
#         cumulative_profits.append(profit)

#     if cumulative_profits:
#         fig2, ax2 = plt.subplots(figsize=(10, 4))
#         ax2.plot(cumulative_profits, color='blue', linewidth=2)
#         ax2.set_title("Cumulative Profit")
#         ax2.set_ylabel("₹")
#         ax2.set_xlabel("Trade Index")
#         st.pyplot(fig2)
#     else:
#         st.info("No profit data available for graph.")







import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from indicator.technical_indicator import add_technical_indicators
from strategy.rsi_strategy import rsi_strategy
from strategy.macd_strategy import macd_strategy
from strategy.bollinger_strategy import bollinger_strategy
from strategy.backtest import backtest_strategy

# 1. Page configuration
st.set_page_config(page_title="📊 Stock Strategy Dashboard", layout="wide", page_icon="💹")

# 2. Sidebar inputs
st.sidebar.title("⚙️ Settings")
user_input = st.sidebar.text_input("Enter the company name")
if user_input:
    tick = yf.Lookup(query = user_input).all.index[0:3]
    ticker = st.sidebar.selectbox("Enter Stock Ticker", options=tick)
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2025-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))
strategy_name = st.sidebar.selectbox("Select Strategy", ["RSI", "MACD", "Bollinger"])

# 3. Run strategy on button click
if st.sidebar.button("🚀 Run Strategy"):

    # --- Data Loading ---
    with st.spinner(f"Fetching data for {ticker}..."):
        df = yf.Ticker(ticker).history(start=start_date, end=end_date)
        if df.empty:
            st.error("No data found for this ticker and date range.")
            st.stop()

    with st.spinner("Adding technical indicators..."):
        df = add_technical_indicators(df)

    with st.spinner(f"Applying {strategy_name} strategy..."):
        if strategy_name == "RSI":
            df_strategy = rsi_strategy(df)
        elif strategy_name == "MACD":
            df_strategy = macd_strategy(df)
        else:
            df_strategy = bollinger_strategy(df)

    with st.spinner("Backtesting strategy..."):
        total_profit, trades = backtest_strategy(df_strategy)

    # --- UI Tabs ---
    tab1, tab2 = st.tabs(["📋 Strategy Report", "📈 Cumulative Profit"])

    with tab1:
        st.subheader(f"📋 {strategy_name} Strategy - Last 5 signals")
        st.dataframe(df_strategy[['Close', 'Signal']].tail(5))

        st.subheader("📊 Strategy Performance")
        st.metric("💰 Total Profit (₹)", f"{total_profit:.2f}")
        st.write(f"🛒 Number of trades executed: {len(trades)}")

        st.subheader("📉 Strategy Chart")

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df_strategy['Close'], label='Close Price', color='lightgray')

        buy_signals = df_strategy[df_strategy['Signal'] == -1]
        sell_signals = df_strategy[df_strategy['Signal'] == 1]

        ax.plot(buy_signals.index, buy_signals['Close'], '^', markersize=10, color='green', label='Buy')
        ax.plot(sell_signals.index, sell_signals['Close'], 'v', markersize=10, color='red', label='Sell')

        ax.set_title(f"{ticker} - {strategy_name} Strategy", fontsize=14)
        ax.set_ylabel("Price (₹)")
        ax.legend()
        st.pyplot(fig)

        st.subheader("📁 Export Trades")
        if trades:
            trade_df = pd.DataFrame(trades)
            st.download_button(
                label="📥 Download Trade History as CSV",
                data=trade_df.to_csv(index=False),
                file_name=f"{ticker}_{strategy_name}_trades.csv",
                mime='text/csv'
            )
        else:
            st.warning("No trades to export.")

    with tab2:
        st.subheader("📈 Cumulative Profit Over Time")

        def compute_cumulative_profit(df):
            profits = []
            position = 0
            buy_price = 0
            initial_investment = 1000
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
            return profits

        if not df_strategy.empty:
            cumulative_profits = compute_cumulative_profit(df_strategy)
            fig2, ax2 = plt.subplots(figsize=(10, 4))
            ax2.plot(df_strategy.index, cumulative_profits, color='blue', linewidth=2)
            ax2.set_title("Cumulative Profit Over Time")
            ax2.set_ylabel("Profit (₹)")
            ax2.set_xlabel("Date")
            st.pyplot(fig2)
        else:
            st.info("No profit data availabl for graph.")



                








