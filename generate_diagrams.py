"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

import graphviz
import os

# Add Graphviz bin directory to PATH
os.environ['PATH'] += r';C:\Program Files (x86)\Graphviz\bin'

from graphviz import Digraph

# Data Flow Diagram
dfd = Digraph('DFD', filename='data_flow_diagram', format='png')
dfd.attr(rankdir='LR', size='10,5')

dfd.node('U', 'User', shape='actor')
dfd.node('S', 'Streamlit App', shape='box')
dfd.node('Y', 'YFinance', shape='cylinder')
dfd.node('I', 'Indicator Module', shape='box')
dfd.node('T', 'Strategy/Backtest', shape='box')
dfd.node('L', 'LSTM Forecast', shape='box')
dfd.node('V', 'Output (Charts/Tables)', shape='box')

dfd.edge('U', 'S', label='request + parameters')
dfd.edge('S', 'Y', label='fetch OHLC')
dfd.edge('Y', 'S', label='market data')
dfd.edge('S', 'I', label='compute indicators')
dfd.edge('I', 'S', label='indicator data')
dfd.edge('S', 'T', label='generate buy/sell signals')
dfd.edge('T', 'S', label='backtest results')
dfd.edge('S', 'L', label='prepare train data')
dfd.edge('L', 'S', label='future prices')
dfd.edge('S', 'V', label='render dashboard')

dfd.render(directory='.', cleanup=True)

# Sequence Diagram (simplified as directed flow with steps)
s = Digraph('Sequence', filename='sequence_diagram', format='png')
s.attr(rankdir='TB', size='8,6')

s.node('User', 'User', shape='actor')
s.node('App', 'Streamlit App', shape='box')
s.node('YFinance', 'YFinance', shape='cylinder')
s.node('Indicators', 'Indicator Module', shape='box')
s.node('Strategy', 'Strategy Module', shape='box')
s.node('LSTM', 'LSTM Module', shape='box')
s.node('UI', 'UI Renderer', shape='box')

s.edge('User', 'App', label='select ticker/date/strategy')
s.edge('App', 'YFinance', label='get historical price')
s.edge('YFinance', 'App', label='return OHLC data')
s.edge('App', 'Indicators', label='compute indicators')
s.edge('Indicators', 'App', label='return RSI/MACD/Bollinger')
s.edge('App', 'Strategy', label='generate signals')
s.edge('Strategy', 'App', label='return trades/profit')
s.edge('App', 'LSTM', label='train and predict')
s.edge('LSTM', 'App', label='return forecast')
s.edge('App', 'UI', label='render dashboard elements')
s.edge('UI', 'User', label='show results')

s.render(directory='.', cleanup=True)

print('Diagrams generated: data_flow_diagram.png, sequence_diagram.png')