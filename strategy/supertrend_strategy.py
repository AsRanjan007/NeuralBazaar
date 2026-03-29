"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

def supertrend_strategy(df):
    df = df.copy()
    df['Signal'] = 0
    df.loc[df['Supertrend_Trend'] == 1, 'Signal'] = 1   # Buy in uptrend
    df.loc[df['Supertrend_Trend'] == -1, 'Signal'] = -1  # Sell in downtrend
    return df