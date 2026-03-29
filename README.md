# NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

**Version: 1.0.0**

**GitHub Author**: AsRanjan007 (Ashutosh Ranjan)

**Copyright**: Ashutosh Ranjan

**License**: Custom Non-Commercial License with Trademark Protection

⚠️ **IMPORTANT**: This project is protected under a custom license that **prohibits commercial use**. See [LICENSE](LICENSE) for full details.
- ✅ Personal & educational use allowed
- ✅ Modifications for personal use allowed
- ❌ **Commercial use prohibited** (requires explicit written permission)
- ❌ "NeuralBazaar" name and logo are protected trademarks

📁 **Note**: Virtual environment (`.venv`) is excluded from version control. Follow the installation steps below to set up your environment.


NeuralBazaar is a comprehensive, AI-driven stock market analysis platform designed specifically for Indian markets. Built with Streamlit, TensorFlow, and advanced technical indicators, it provides traders and investors with intelligent insights through LSTM forecasting, multiple trading strategies, and real-time technical analysis.

## 🚀 Features

### Core Functionality
- **Multi-Asset Support**: Analyze stocks from NSE, BSE, and international markets
- **Currency Intelligence**: Automatic INR/USD currency detection and conversion for Indian stocks
- **Real-time Data**: Live stock data fetching via Yahoo Finance API
- **Interactive Dashboard**: Modern web interface with tabbed navigation

### AI & Machine Learning
- **LSTM Forecasting**: 7-day price prediction using attention-based neural networks
- **Holiday-Aware Predictions**: Considers Indian market holidays and weekends
- **Feature Engineering**: Multi-indicator input for robust predictions

### Technical Analysis
- **Advanced Indicators**: RSI, MACD, Bollinger Bands, Supertrend, VWAP, Pivot Points, Stochastic, ATR
- **India Market Optimized**: Indicators tailored for Indian trading patterns
- **Real-time Calculations**: Live indicator computation and visualization

### Trading Strategies
- **RSI Strategy**: Momentum-based buy/sell signals
- **MACD Strategy**: Trend-following crossover signals
- **Bollinger Bands Strategy**: Mean-reversion signals
- **Supertrend Strategy**: Trend-following with ATR-based stops

### Backtesting Engine
- **Performance Metrics**: Profit/loss calculation, win rate, trade statistics
- **Signal Validation**: Robust signal processing and trade execution
- **Portfolio Simulation**: Investment amount-based backtesting

## 🏗️ Architecture

### System Components
```
User Interface (Streamlit)
    ↓
Data Layer (YFinance API)
    ↓
Processing Layer (Pandas, Technical Indicators)
    ↓
AI Layer (TensorFlow LSTM)
    ↓
Strategy Layer (Trading Algorithms)
    ↓
Output Layer (Charts, Tables, Reports)
```

### Data Flow
1. **Input**: User selects ticker, date range, strategy, and investment amount
2. **Data Fetching**: Historical OHLC data retrieved from Yahoo Finance
3. **Currency Processing**: Automatic INR conversion for Indian stocks
4. **Indicator Calculation**: 10+ technical indicators computed
5. **Strategy Application**: Buy/sell signals generated based on selected strategy
6. **AI Forecasting**: LSTM model predicts next 7 trading days
7. **Backtesting**: Strategy performance evaluated with investment simulation
8. **Visualization**: Results displayed in interactive charts and tables

## 🤖 Models Used

### LSTM with Attention Mechanism
- **Architecture**: Sequential LSTM with attention layers
- **Input Features**: Close price, RSI, MACD, and other indicators
- **Training**: Historical data with 80/20 train-validation split
- **Output**: 7-day price forecast with confidence intervals
- **Holiday Handling**: Skips weekends and NSE holidays in predictions

### Technical Indicators
- **RSI (Relative Strength Index)**: Momentum oscillator (14-period Wilder's smoothing)
- **MACD**: Trend-following momentum indicator (12/26/9 periods)
- **Bollinger Bands**: Volatility bands (20-period SMA ± 2 SD)
- **Supertrend**: Trend-following indicator with ATR-based bands
- **VWAP**: Volume-weighted average price
- **Pivot Points**: Support/resistance levels (Classic calculation)
- **Stochastic Oscillator**: Momentum indicator (%K/%D)
- **ATR**: Average True Range for volatility measurement

## 📈 Trading Strategies

### RSI Strategy
- **Buy Signal**: RSI < 30 (Oversold)
- **Sell Signal**: RSI > 70 (Overbought)
- **Purpose**: Mean-reversion in ranging markets

### MACD Strategy
- **Buy Signal**: MACD crosses above Signal Line
- **Sell Signal**: MACD crosses below Signal Line
- **Purpose**: Trend-following in trending markets

### Bollinger Bands Strategy
- **Buy Signal**: Price touches lower band
- **Sell Signal**: Price touches upper band
- **Purpose**: Mean-reversion during high volatility

### Supertrend Strategy
- **Buy Signal**: Trend = 1 (Uptrend)
- **Sell Signal**: Trend = -1 (Downtrend)
- **Purpose**: Trend-following with dynamic stops

## 🛠️ Installation

### Prerequisites
- Python 3.8+ (Python 3.11+ recommended)
- pip package manager
- Virtual environment (required)

### Setup Steps (Windows)

1. **Clone or download the repository**
   ```powershell
   git clone https://github.com/AsRanjan007/NeuralBazaar.git
   cd NeuralBazaar
   ```

2. **Create virtual environment**
   ```powershell
   python -m venv .venv
   ```

3. **Activate virtual environment**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   > **Note**: If you get execution policy errors, use: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

4. **Install dependencies**
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Verify installation**
   ```powershell
   python -c "import streamlit, yfinance, tensorflow; print('All dependencies installed successfully!')"
   ```

### Setup Steps (Linux/Mac)

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/AsRanjan007/NeuralBazaar.git
   cd NeuralBazaar
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   ```

3. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Verify installation**
   ```bash
   python -c "import streamlit, yfinance, tensorflow; print('All dependencies installed successfully!')"
   ```

## 🚀 Usage

### Running the Application (Windows)
```powershell
cd path\to\neuralbazaar
.venv\Scripts\python.exe -m streamlit run main.py
```

**The app will open at:** `http://localhost:8501`

### Running the Application (Linux/Mac)
```bash
source .venv/bin/activate
streamlit run main.py
```

### Basic Workflow
1. **Company Selection**: Enter company name and select ticker
2. **Date Range**: Choose start and end dates (min 90 days for LSTM)
3. **Investment Amount**: Set amount in appropriate currency
4. **Strategy Selection**: Choose from RSI, MACD, Bollinger, or Supertrend
5. **Model Option**: Enable LSTM forecasting if desired
6. **Run Analysis**: Click "🚀 Run" to generate insights

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. ModuleNotFoundError (streamlit, yfinance, tensorflow, etc.)
**Problem**: Module not found even though it's in requirements.txt

**Solution - Windows**:
```powershell
# Use the venv python directly to install
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

#### 2. Streamlit won't start
**Problem**: "streamlit.exe not found" or similar launcher errors

**Solution - Windows**:
```powershell
# Use python -m to run streamlit instead of directly calling streamlit.exe
.venv\Scripts\python.exe -m streamlit run main.py
```

#### 3. Port 8501 already in use
**Problem**: "Port 8501 already in use"

**Solution**:
```powershell
# Kill the existing streamlit process
Get-Process streamlit | Stop-Process -Force
# Then restart
.venv\Scripts\python.exe -m streamlit run main.py
```

#### 4. PowerShell execution policy error
**Problem**: "cannot be loaded because running scripts is disabled"

**Solution**:
```powershell
# Use direct python execution instead of activating scripts
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run main.py
```

#### 5. Dependencies conflict or version mismatch
**Problem**: Dependency conflicts when installing tensorflow

**Solution - Clean reinstall**:
```powershell
# Remove and recreate venv
Remove-Item -Recurse -Force .venv
python -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Quick Reference Commands (Windows)

```powershell
# One-liner to get everything running
cd path\to\neuralbazaar; python -m venv .venv; .venv\Scripts\python.exe -m pip install --upgrade pip; .venv\Scripts\python.exe -m pip install -r requirements.txt; .venv\Scripts\python.exe -m streamlit run main.py
```

### Dashboard Tabs
- **Summary**: Key metrics and overview
- **Chart**: Price history visualization
- **Indicators**: Technical indicator table
- **Forecast**: LSTM predictions (if enabled)
- **Strategy**: Backtest results and trade analysis

## 📊 Output Formats

### Charts
- Price history with technical indicators
- LSTM forecast with historical overlay
- Strategy signal visualization

### Tables
- Technical indicators (last 10 periods)
- Trade log with entry/exit details
- Performance metrics

### Downloads
- CSV exports of indicator data
- Trade history files
- Presentation materials

## 🔧 Configuration

### Environment Variables
- No environment variables required
- All configurations handled through UI

### Customization
- Modify indicator parameters in `indicator/technical_indicator.py`
- Adjust strategy thresholds in respective strategy files
- Tune LSTM hyperparameters in `lstm_model.py`

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Update tests for new features
- Ensure compatibility with Python 3.8+

## 📄 License & Usage Rights

**Custom Non-Commercial License with Trademark Protection**

### ✅ What You CAN Do
- Use for personal, non-commercial purposes
- Use for educational and research purposes
- Modify the software for your own use
- Run your own instance of the application
- Share code with others for non-commercial use

### ❌ What You CANNOT Do
- **Commercial Use**: Cannot sell, license, or use commercially without permission
- **Logo & Trademark**: Cannot use "NeuralBazaar" name or logo for commercial purposes
- **Rebranding**: Cannot rebrand and resell under a different name
- **Revenue Generation**: Cannot use in products/services that generate profit

### 🔒 Trademark Protection
The name "NeuralBazaar" and all associated branding materials are protected intellectual property.
Unauthorized commercial use is prohibited.

### 💼 Commercial License
For commercial use or licensing inquiries, please contact: **AsRanjan007**

See the full [LICENSE](LICENSE) file for complete terms and conditions.

**Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.**

## 🙏 Acknowledgments

- Yahoo Finance API for market data
- TensorFlow/Keras for deep learning framework
- Streamlit for web application framework
- Pandas, NumPy, and scikit-learn for data processing
- NSE for market holiday information

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact: ashutosh.ranjan@email.com

## 🔄 Version History

- **v1.0.0** (2026-03-29): Initial release
  - Core dashboard functionality
  - LSTM forecasting with attention
  - 4 trading strategies
  - 10+ technical indicators
  - INR currency support
  - Holiday-aware predictions
  - Presentation and diagram generation

---

**Built with ❤️ for the Indian trading community**