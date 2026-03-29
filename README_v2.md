# 🚀 NeuralBazaar v2.0.0 - AI-Powered Multi-Signal Trading System

**Version**: 2.0.0 | **Updated**: March 29, 2026  
**Author**: Ashutosh Ranjan  
**Copyright**: © 2026 Ashutosh Ranjan. All rights reserved.

---

## 📋 Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [System Architecture](#system-architecture)
4. [Installation](#installation)
5. [Quick Start](#quick-start)
6. [Market Support](#market-support)
7. [Technical Indicators](#technical-indicators)
8. [5-Pillar Architecture](#5-pillar-architecture)
9. [Dashboard Sections](#dashboard-sections)
10. [Configuration](#configuration)

---

## 📌 Overview

**NeuralBazaar v2.0.0** is a comprehensive AI-powered stock market intelligence dashboard designed for multi-market trading analysis. It provides real-time data, sentiment analysis, market timings, and technical indicators across **NSE (India), BSE (India), and NYSE (USA)** with intelligent signal generation using a **5-pillar architecture**.

**New in v2.0:**
- ✅ Multi-market support (NSE/BSE/NYSE)
- ✅ Real-time sentiment analysis with VADER NLP
- ✅ Event-based sentiment understanding
- ✅ Market closure & holiday awareness
- ✅ Company information & profiling
- ✅ Static stock info header with trend indicators
- ✅ Currency auto-switching (₹ vs $)
- ✅ News intelligence with event categorization

---

## 🎯 Key Features

### 🌍 **Multi-Market Support**
- **NSE (National Stock Exchange - India)**: 09:15-15:30 IST
- **BSE (Bombay Stock Exchange - India)**: 09:15-15:30 IST  
- **NYSE (New York Stock Exchange - USA)**: 09:30-16:00 EST

### 💱 **Currency Intelligence**
- Automatic currency symbol switching (₹ for NSE/BSE, $ for NYSE)
- Real-time price displays with correct formatting
- All technical indicators support both currencies

### 📊 **Real-Time Data**
- Live stock data from Yahoo Finance API
- 5-minute caching for optimal performance
- Support for intraday (1h, 15m, 5m) and daily (1d) timeframes
- Historical data up to 365 days lookback

### 📰 **News & Sentiment Analysis**
- Real-time news fetching from Yahoo Finance
- VADER sentiment analysis (Positive/Negative/Neutral)
- Event-based sentiment understanding:
  - **Earnings** announcements
  - **Dividend** declarations
  - **Mergers & Acquisitions**
  - **Product Launches**
  - **Regulatory** news
  - **Partnerships**
  - **Expansion** plans
- Sentiment scoring from -1.0 (most negative) to +1.0 (most positive)

### 🏢 **Company Information**
- Company description and business summary
- Sector and industry classification
- Key metrics: Market cap, P/E ratio, dividend yield
- Employee count and website information

### 🕐 **Market Timings & Holidays**
- Real-time market status detection (Open/Closed/Opening Soon)
- Countdown timers (minutes until market opens/closes)
- 17 official holidays for NSE/BSE
- US federal holidays for NYSE
- Automatic weekend detection
- Next market opening calculation

### 📈 **Technical Indicators** (23 indicators)
- **Trend**: SMA20, SMA50, EMA12, EMA26
- **Momentum**: RSI (14), MACD, Bollinger Bands
- **Volatility**: ATR (14), Daily Returns
- **Plus 14 additional statistical indicators**

### 🎨 **Interactive Dashboard**
- Real-time candlestick charts with moving averages
- RSI chart with overbought/oversold zones
- MACD histogram visualization
- Sentiment distribution pie charts
- Monthly returns heatmap (with month names)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────┐
│         Streamlit Web Interface             │
│  - 6 Tabs (Dashboard, Signals, Trades,      │
│    Architecture, Metrics, Logs)             │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│     Real-Time Data Layer                    │
│  - Yahoo Finance API (yfinance)             │
│  - 5-minute caching                         │
│  - Multi-market ticker mapping              │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│     Processing Layer                        │
│  - Technical Indicators (Pandas/NumPy)      │
│  - News Fetching                            │
│  - Sentiment Analysis (VADER-NLTK)          │
│  - Market Status Detection                  │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│     Analysis Layer                          │
│  - 5-Pillar Signal Generation               │
│  - Event Detection & Classification         │
│  - Signal-to-Noise Filtering                │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│     Visualization Layer                     │
│  - Plotly Charts & Heatmaps                 │
│  - Tables & Metrics                         │
│  - Status Indicators                        │
└─────────────────────────────────────────────┘
```

---

## 🔧 Installation

### Prerequisites
- Python 3.11+
- pip or conda
- Git

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd NeuralBazaar
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🚀 Quick Start

### First Time Setup
1. Open NeuralBazaar in browser
2. Go to **⚙️ Configuration** in sidebar
3. Select your **Market**: NSE, BSE, or NYSE
4. Enter **Stock Symbol** (e.g., INFY for NSE)
5. Adjust **Lookback Period** (30-365 days)
6. Click into tabs to explore features

### Interpreting Results

**Tab 1: Dashboard 📊**
- Real-time candlestick chart with moving averages
- Current price with 52-week high/low
- RSI momentum indicator
- MACD trend confirmation
- Market status banner

**Tab 2: Signals & Analysis 📈**
- Company overview and description
- Event-based sentiment (earnings, mergers, etc.)
- Technical indicators summary
- Price performance over multiple timeframes
- News sentiment analysis

**Tab 3: Trading Signals 🎯**
- Real technical indicators with signals
- Trading signal recommendations
- Signal interpretation guide
- CSV export functionality

**Tab 4: Pillar Architecture 🏗️**
- 5-pillar system explanation
- Pillar descriptions and statuses
- Data flow pipeline
- Component details

**Tab 5: Performance Metrics 📉**
- Risk metrics (Annual Vol, Sharpe, Sortino)
- Monthly returns heatmap
- Performance analysis

**Tab 6: System Logs ⚙️**
- Real-time log viewer
- System initialization logs
- Signal generation traces
- Debug information

---

## 🌍 Market Support

### NSE (National Stock Exchange - India)
**Ticker Suffix**: `.NS`  
**Hours**: 09:15 - 15:30 IST (Mon-Fri)  
**Currency**: INR (₹)  
**Popular Symbols**:
- INFY (Infosys)
- TCS (Tata Consultancy)
- RELIANCE (Reliance Industries)
- HDFC (HDFC Bank)
- ITC (ITC Limited)

### BSE (Bombay Stock Exchange - India)
**Ticker Suffix**: `.BO`  
**Hours**: 09:15 - 15:30 IST (Mon-Fri)  
**Currency**: INR (₹)  
**Popular Symbols**:
- RELIANCE (Reliance Industries)
- TATAMOTORS (Tata Motors)
- HCLTECH (HCL Technologies)

### NYSE (New York Stock Exchange - USA)
**Ticker Suffix**: (none)  
**Hours**: 09:30 - 16:00 EST (Mon-Fri)  
**Currency**: USD ($)  
**Popular Symbols**:
- AAPL (Apple)
- MSFT (Microsoft)
- GOOGL (Alphabet/Google)
- TSLA (Tesla)
- AMZN (Amazon)

---

## 📊 Technical Indicators

### Trend Indicators
| Indicator | Period | Signal |
|-----------|--------|--------|
| SMA20 | 20-day | Short-term trend |
| SMA50 | 50-day | Medium-term trend |
| EMA12 | 12-day | Fast exponential |
| EMA26 | 26-day | Slow exponential |

### Momentum Indicators
| Indicator | Period | Interpretation |
|-----------|--------|-----------------|
| RSI | 14 | <30: Oversold, >70: Overbought |
| MACD | 12/26/9 | Line > Signal: Bullish |
| MACD Histogram | 9 | Divergence strength |

### Volatility Indicators
| Indicator | Period | Use |
|-----------|--------|-----|
| Bollinger Bands | 20/2 | Breakout levels |
| ATR | 14 | Risk measurement |
| BB Width | 20 | Volatility expansion |

---

## 🎯 5-Pillar Architecture

### Pillar 1: Time-Series Forecasting 📐
- **Purpose**: Predict price movements using historical data
- **Method**: Neural networks & statistical models
- **Status**: ✅ Framework ready

### Pillar 2: News Intelligence 📰
- **Purpose**: Extract market sentiment from news & events
- **Method**: VADER sentiment analysis + keyword extraction
- **Status**: ✅ Fully implemented (VADER integration active)

### Pillar 3: Signal Generation 🎯
- **Purpose**: Generate trading signals from multiple indicators
- **Method**: Technical analysis + machine learning
- **Status**: ✅ Framework ready

### Pillar 4: Risk Management ⚠️
- **Purpose**: Assess and manage trading risk
- **Method**: Position sizing, stop-loss calculation
- **Status**: ✅ Framework ready

### Pillar 5: Data Pipeline 📥
- **Purpose**: Ingest and process market data
- **Method**: Real-time fetching, caching, validation
- **Status**: ✅ Fully implemented (yfinance + caching)

---

## 📱 Dashboard Sections

### Static Stock Info Header
```
┌─────────────────────────────────────────────────────────┐
│ Stock: INFY │ INFY.NS │ NSE │ ₹456.20 │ 📈 UP +2.34% │
└─────────────────────────────────────────────────────────┘
```
- Stock name, symbol, market
- Current price with currency
- Trend indicator (up/down)
- Price change percentage

### Market Status Banner
```
✅ LIVE - Closes in 245 min | Trading active until 15:30
```
Shows:
- Market status (Open/Closed/Opening Soon)
- Time to close/open
- Holiday notices
- Next opening when closed

### Configuration Sidebar
- Market selector (NSE/BSE/NYSE)
- Stock symbol input
- Market status indicator
- Trading hours details
- Upcoming holidays
- Timeframe selection (1d/1h/15m/5m)
- Lookback period slider

---

## 🛠️ Configuration

### Sidebar Settings

**Market Data Section**
```yaml
Market: [NSE, BSE, NYSE]
Symbol: [User input]
Status: [Real-time indicator]
Trading Hours: [Expandable]
Holidays: [Expandable list]
```

**Time Period Section**
```yaml
Timeframe: [1d, 1h, 15m, 5m]
Lookback Period: 30-365 days
```

**Execution Mode**
```yaml
Mode: [backtest, paper_trading, realtime]
Version: [2.0.0, 1.0.0]
```

### Caching Strategy
- **Stock Data**: 5 minutes (ttl=300)
- **Company Info**: 1 hour (ttl=3600)
- **News Data**: 1 hour (ttl=3600)
- **Holiday List**: Session-based (recalculated daily)

---

## 📚 Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | latest | Web framework |
| yfinance | latest | Stock data API |
| pandas | latest | Data manipulation |
| numpy | latest | Numerical operations |
| plotly | latest | Interactive charts |
| nltk | latest | Sentiment analysis (VADER) |
| pytz | latest | Timezone handling |
| holidays | latest | Holiday calendars |
| tensorflow | 2.20.0 | Neural networks (future) |
| scikit-learn | latest | ML algorithms |

---

## 🎓 Usage Examples

### Example 1: Analyzing Indian Stock (RELIANCE)
1. Market: **NSE**
2. Symbol: **RELIANCE**
3. Auto-converts to **RELIANCE.NS**
4. Shows in **₹ (INR)**
5. Trading hours: **09:15-15:30 IST**

### Example 2: Analyzing US Stock (AAPL)
1. Market: **NYSE**
2. Symbol: **AAPL**
3. No suffix needed
4. Shows in **$ (USD)**
5. Trading hours: **09:30-16:00 EST**

### Example 3: Checking Market Closure
1. Navigate to sidebar
2. Click "📅 Trading Hours" expander
3. View upcoming holidays
4. See market status (🟢 Open / 🔴 Closed)
5. Get next opening time

### Example 4: Understanding Event Impact
1. Go to Tab 2: Signals & Analysis
2. Scroll to "Upcoming Events & Sentiment"
3. View event categories (Earnings, Dividend, etc.)
4. Check sentiment scores
5. See overall impact color code

---

## 🔍 Troubleshooting

### Market Status Shows "CLOSED" on Trading Day
- Check if it's before market opening (before 09:15 for NSE)
- Verify your timezone is set correctly
- Restart app if stuck

### "pytz is not defined" Error
- Solution: Run `pip install pytz holidays`
- Both libraries handle market timings

### No News Data Showing
- Yahoo Finance may be rate-limiting
- Fallback data includes sample headlines
- Try different symbol or wait/refresh

### Symbol Not Found
- Check market suffix mapping:
  - NSE: Use .NS (INFY.NS)
  - BSE: Use .BO (RELIANCE.BO)
  - NYSE: No suffix (AAPL)
- Verify symbol exists on selected market

---

## 📈 What's Next (Roadmap)

- [ ] Real-time Kafka data streaming (Pillar 5 enhancement)
- [ ] RL Agent training for portfolio optimization (Pillar 3)
- [ ] FinBERT for advanced sentiment (Pillar 2 enhancement)
- [ ] Multi-symbol portfolio tracking
- [ ] Watchlist and alerts
- [ ] Mobile app version
- [ ] API endpoint for external integrations

---

## 📞 Support

For issues, suggestions, or feedback:
- Check existing GitHub issues
- Review documentation in `/docs` folder
- Check system logs in Tab 6

---

## 📜 License

© 2026 Ashutosh Ranjan. All rights reserved.  
Custom Non-Commercial License - See LICENSE file for details.

- ✅ Personal & educational use
- ✅ Modifications allowed
- ❌ **Commercial use prohibited**
- ❌ Trademark "NeuralBazaar" protected

---

## 🙏 Acknowledgments

Built with ❤️ for Indian traders using cutting-edge AI and data science technologies.

**Made with ❤️ for Indian traders**

---

**Version**: 2.0.0 | **Last Updated**: March 29, 2026
