# NeuralBazaar v2.0.0 - Setup & Installation Guide

## 🚀 Quick Start

### Step 1: Run Setup Script

```bash
python setup_v2.py
```

This will create the complete directory structure and all module files:

```
NeuralBazaar/
├── main.py                          # Entry point with version switching
├── setup_v2.py                      # Setup script (just ran this)
├── file_templates.py                # Template contents
├── config/
│   ├── __init__.py
│   └── config.py                    # Global configuration
├── v2/                              # ✨ V2.0.0 IMPLEMENTATION
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── trading_system.py       # Main orchestrator
│   │   └── version_manager.py      # Version management
│   ├── pillar1_timeseries/         # ⏱️ Time-Series Forecasting Engine
│   │   ├── __init__.py
│   │   ├── models.py               # LSTM, Transformer, Prophet, XGBoost
│   │   └── forecaster.py           # Forecasting orchestrator
│   ├── pillar2_news/               # 📰 News Intelligence Engine
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py   # FinBERT sentiment scoring
│   │   ├── knowledge_graph.py      # Neo4j indirect impact detection
│   │   └── news_processor.py       # News ingestion pipeline
│   ├── pillar3_signal_fusion/      # 🔀 Signal Fusion & Decision Layer
│   │   ├── __init__.py
│   │   ├── ensemble.py             # Ensemble voting logic
│   │   ├── rl_agent.py             # RL policy (PPO/SAC)
│   │   └── signal_generator.py     # Buy/Hold/Exit signal generation
│   ├── pillar4_risk/               # ⚠️ Risk & Volatility Monitor
│   │   ├── __init__.py
│   │   ├── anomaly_detector.py     # Isolation Forest, autoencoders
│   │   ├── risk_manager.py         # Kelly Criterion, position sizing
│   │   └── regime_classifier.py    # HMM market regime detection
│   ├── pillar5_data/               # 🌊 Real-time Data Pipeline
│   │   ├── __init__.py
│   │   ├── data_ingester.py        # Kafka/streaming ingestion
│   │   ├── feature_engineer.py     # Technical, statistical, NLP features
│   │   └── data_cache.py           # Caching & storage layer
│   └── utils/
│       ├── __init__.py
│       ├── logger.py               # Logging utility
│       ├── metrics.py              # Performance metrics
│       └── validators.py           # Data validation
├── v1/                             # Legacy version (stub)
│   └── __init__.py
├── data/
│   ├── cache/                      # Feature cache
│   └── models/                     # Model storage
├── docs/
│   └── architecture_v2.md          # Detailed architecture
├── requirements.txt                # Python dependencies
└── README_V2_SETUP.md             # This file
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies**:
- **ML/DL**: torch, tensorflow, scikit-learn, xgboost, lightgbm
- **Time-Series**: statsmodels, prophet, darts
- **NLP**: transformers, spacy, faiss
- **Graph**: neo4j-driver
- **Streaming**: confluent-kafka
- **RL**: stable-baselines3

### Step 3: Run the System

#### Use v2.0.0 (Default - Recommended)

```bash
# Paper trading mode (simulated)
python main.py --version 2.0.0 --mode paper --symbol AAPL

# Backtest mode
python main.py --version 2.0.0 --mode backtest --symbol MSFT

# Real-time mode (live trading)
python main.py --version 2.0.0 --mode realtime --symbol GOOGL

# With custom config
python main.py --version 2.0.0 --config config/config.yaml

# Debug mode
python main.py --version 2.0.0 --debug
```

#### Use v1.0.0 (Legacy)

```bash
python main.py --version 1.0.0 --mode paper
```

---

## 🏛️ Architecture Overview (v2.0.0)

### Five Core Pillars

#### **Pillar 1: Time-Series Forecasting Engine** ⏱️
Predicts future price/volume movements using multiple deep learning models.

**Models**:
- **LSTM** - Captures long-range temporal dependencies
- **Transformer (TFT/Informer)** - State-of-the-art multi-horizon forecasting
- **Prophet** - Trend + seasonality decomposition
- **XGBoost/LightGBM** - Gradient boosting on engineered features
- **Ensemble** - Weighted combination of all models

**Location**: `v2/pillar1_timeseries/`

---

#### **Pillar 2: News Intelligence Engine** 📰
Analyzes news streams using NLP and LLMs to detect direct and indirect market impacts.

**Components**:
- **Sentiment Analysis** - FinBERT for financial text (-1 to +1 scoring)
- **Knowledge Graph** - Neo4j for supply chain impact detection
- **Entity Recognition** - Extracts company, person, location from news
- **Earnings Intelligence** - Surprise ratio, management tone analysis
- **Indirect Impact** - Second-order effects (e.g., oil price → airline costs)

**Location**: `v2/pillar2_news/`

**Example** 🔗 Causal chain:
```
OPEC cuts output 
  ↓
Crude oil price rises 20%
  ↓
Airline fuel costs increase
  ↓
IndiGo margin compression detected
  ↓
SELL signal generated for IndiGo
```

---

#### **Pillar 3: Signal Fusion & Decision Layer** 🔀
Fuses signals from all sources using ensemble methods and reinforcement learning.

**Components**:
- **Ensemble Voting** - Weighted fusion of technical, sentiment, forecast signals
- **RL Agent (PPO/SAC)** - Learns optimal Buy/Hold/Sell policy
- **Conformal Prediction** - Confidence intervals with statistical guarantees
- **Output** - BUY/HOLD/SELL with 0-1 confidence score

**Location**: `v2/pillar3_signal_fusion/`

---

#### **Pillar 4: Risk & Volatility Monitor** ⚠️
Detects anomalies, classifies market regimes, and manages position sizing.

**Components**:
- **Anomaly Detection** - Isolation Forest, LSTM Autoencoder
- **Regime Classification** - HMM for Bull/Bear/Sideways detection
- **Position Sizing** - Kelly Criterion algorithm
- **Portfolio Controls** - Max 5% per position, 10% portfolio drawdown circuit breaker, 30% sector cap

**Location**: `v2/pillar4_risk/`

---

#### **Pillar 5: Real-time Data Pipeline** 🌊
High-performance data ingestion, feature engineering, and caching.

**Components**:
- **Data Ingestion** - Kafka for streaming, batch ingestion
- **Feature Engineering** - 50+ technical + statistical + NLP features
- **Caching Layer** - Redis/pickle for performance

**Location**: `v2/pillar5_data/`

---

## 📊 Data Flow

```
┌─────────────────────────────────────────────┐
│ Raw Data: OHLCV + News + Order Book         │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ Pillar 5: Feature Engineering               │
│ - Technical indicators (SMA, RSI, MACD...)  │
│ - Statistical (volatility, returns...)      │
│ - NLP features (sentiment, entities)        │
└──────┬─────────────────┬──────────────┬─────┘
       │                 │              │
       ▼                 ▼              ▼
┌────────────────┐ ┌──────────────┐ ┌─────────────────┐
│ Pillar 1:      │ │ Pillar 2:    │ │ Pillar 4:       │
│ Price          │ │ News Impact  │ │ Risk Analysis   │
│ Forecasting    │ │ & Sentiment  │ │ & Anomalies     │
└────────┬───────┘ └──────┬───────┘ └────────┬────────┘
         │                │                  │
         └────────┬───────┴──────────────────┘
                  │
                  ▼
         ┌──────────────────────────┐
         │ Pillar 3:                │
         │ Signal Fusion + RL Agent │
         │ Ensemble Voting          │
         └────────┬─────────────────┘
                  │
                  ▼
         ┌──────────────────────────┐
         │ Output Signal:           │
         │ - Signal (BUY/HOLD/SELL) │
         │ - Confidence (0-1)       │
         │ - Position Size ($)      │
         │ - Stop Loss Level        │
         └──────────────────────────┘
```

---

## 🎯 Signal Generation Examples

### BUY Signal Conditions (AND logic)

```
✅ Price > 200-day EMA (long-term uptrend intact)
✅ RSI crosses 50 from oversold territory
✅ MACD histogram shows bullish crossover
✅ Volume > 1.5× 20-day average (institutional buying)
✅ News sentiment > +0.4 over last 24 hours
✅ RL agent Q-value > 0.65
✅ Bollinger Band squeeze breakout
```
**Result**: **BUY signal with high confidence**

### EXIT Signal Conditions

```
⏹️ RSI crosses 70 (overbought, take profits)
⏹️ MACD bearish divergence detected
⏹️ Price hits Fibonacci 1.618 extension (profit target)
⏹️ Breaking negative news (sentiment < -0.5)
⏹️ Anomaly: unusual volume dump by isolation forest
⏹️ Trailing stop-loss trigger
```
**Result**: **EXIT signal**

---

## ⚙️ Configuration

Edit `config/config.py` to customize:

```python
# Buy signal thresholds
buy_rules = {
    'min_price_ema_ratio': 1.0,      # Price > EMA
    'min_rsi': 50,                   # RSI above 50
    'min_sentiment_score': 0.4,      # Sentiment > 0.4
    'min_volume_ratio': 1.5,         # Volume surge
    'min_rl_confidence': 0.65,       # RL confidence
}

# Risk management
kelly_fraction = 0.25               # Kelly Criterion (conservative)
max_position_size = 0.05            # 5% per position
max_portfolio_drawdown = 0.10       # 10% circuit breaker
atr_multiplier = 1.5                # Stop loss distance
sector_concentration_cap = 0.30     # 30% per sector
```

---

## 🔄 Version Switching

### Why Two Versions?

- **v2.0.0**: Production-ready 5-pillar architecture with state-of-the-art ML
- **v1.0.0**: Legacy system for backward compatibility and comparison

### Switching Between Versions

```bash
# Default (v2.0.0)
python main.py --mode paper

# Explicitly v2.0.0
python main.py --version 2.0.0 --mode paper

# Legacy v1.0.0
python main.py --version 1.0.0 --mode paper
```

### Version Manager Code

```python
# In main.py
class VersionManager:
    SUPPORTED_VERSIONS = ['2.0.0', '1.0.0']
    DEFAULT_VERSION = '2.0.0'
    
    @staticmethod
    def load_version(version: str):
        if version == '2.0.0':
            from v2.core.trading_system import TradingSystemV2
            return TradingSystemV2()
        elif version == '1.0.0':
            from v2.core.trading_system import TradingSystemV1
            return TradingSystemV1()
```

---

## 📈 Execution Modes

### 1. **Backtest** 📊
```bash
python main.py --version 2.0.0 --mode backtest --symbol AAPL
```
- Processes historical data
- Generates signals without execution
- Evaluates performance metrics
- Useful for strategy testing

### 2. **Paper Trading** 📋
```bash
python main.py --version 2.0.0 --mode paper --symbol MSFT
```
- Real-time simulation
- NO actual trades
- Tests system response
- Validates configuration

### 3. **Real-time (Live)** 🚀
```bash
python main.py --version 2.0.0 --mode realtime --symbol GOOGL
```
- **CAUTION**: Real money at risk!
- Live market data
- Actual trade execution
- Portfolio management

---

## 📝 Feature Engineering Details

### Technical Indicators (50+ features)
```
Trend:
  - SMA (20, 50, 200)
  - EMA (12, 26)
  - DEMA, TEMA
  - VWAP

Momentum:
  - RSI (14)
  - Stochastic %K/%D
  - Williams %R
  - Rate of Change (ROC)
  - CCI

Volatility:
  - Bollinger Bands (20, 2)
  - ATR (14)
  - Keltner Channels
  - Historical volatility

Volume:
  - OBV (On-Balance Volume)
  - Chaikin Money Flow
  - Volume RSI

Pattern:
  - MACD (12, 26, 9)
  - Ichimoku Cloud
  - Fibonacci (23.6%, 38.2%, 61.8%)
  - Support/Resistance zones (K-Means)
```

### Statistical Features
```
- Log returns (daily, weekly)
- Rolling volatility
- Z-scores (normalized returns)
- Rolling correlation vs benchmark (beta)
- Fractal dimension
- Hurst Exponent
- ACF/PACF lags
- Market regime (Bull/Bear/Sideways)
- Price range features
```

### NLP Features
```
- Sentiment score (-1 to +1)
- Sentiment velocity (trend)
- News impact score (volume × sentiment × credibility)
- Named entities (company, person, location)
- Indirect impacts (supply chain)
- Earnings surprise ratio
- Management tone (forward guidance)
```

---

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run with specific verbosity
pytest tests/ -v

# Run specific test file
pytest tests/test_pillar1.py
```

---

## 📚 Documentation

- [Architecture Specification](docs/architecture_v2.md) - Detailed system design
- [API Reference](docs/api_reference.md) - (To be generated)
- [Configuration Guide](docs/config_guide.md) - (To be generated)
- [Deployment Guide](docs/deployment.md) - (To be generated)

---

## 🐛 Troubleshooting

### Import Errors
```bash
# Make sure you're in the right directory
cd <your_project_folder>

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Missing Modules
```bash
# If setup didn't complete, manually run
python setup_v2.py

# Verify structure
ls -la v2/
```

### Configuration Issues
```bash
# Create default config
cp config/config.py config/config.yaml

# Edit as needed
nano config/config.yaml
```

---

## 📞 Support

- **Documentation**: See `docs/` folder
- **Issues**: Check logs with `--debug` flag
- **Version Info**: `python main.py --version`

---

## 📄 License

NeuralBazaar v2.0.0 - Multi-Signal Intelligent Trading System

---

## 🎯 Next Steps

1. ✅ Run `python setup_v2.py` (creates all files)
2. ✅ Run `pip install -r requirements.txt` (install deps)
3. ✅ Try `python main.py --version 2.0.0 --help` (see options)
4. ✅ Run `python main.py --version 2.0.0 --mode paper --symbol AAPL` (start trading!)
5. 📚 Read `docs/architecture_v2.md` for deep dive

Happy trading! 🚀
