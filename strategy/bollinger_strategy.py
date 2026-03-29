"""

NeuralBazaar - AI-Powered Stock Market Intelligence Dashboard

Copyright (c) 2026 Ashutosh Ranjan. All rights reserved.

Licensed under the MIT License. See LICENSE file for details.

Version: 1.0.0

"""

def bollinger_strategy(df):
    df = df.copy()
    df['Signal'] = 0
    df.loc[df['Close'] < df['BB_Lower'], 'Signal'] = 1   # Buy
    df.loc[df['Close'] > df['BB_Upper'], 'Signal'] = -1  # Sell
    return df
