"""
Pillar 4.2: Risk Management Engine
Position sizing, Kelly Criterion, stop-loss management

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
import numpy as np
from typing import Dict, Any

logger = logging.getLogger(__name__)


class RiskManager:
    """Manages position sizing and risk controls"""
    
    def __init__(self, config):
        self.config = config
        logger.info("RiskManager initialized")
    
    def calculate_position_size(self, 
                               signal: str,
                               confidence: float,
                               account_balance: float = 100000) -> float:
        """Calculate optimal position size using Kelly Criterion
        
        Args:
            signal: 'BUY', 'HOLD', 'SELL'
            confidence: Signal confidence (0 to 1)
            account_balance: Current account balance
        
        Returns:
            Position size in dollars
        """
        if signal == 'HOLD':
            return 0.0
        
        kelly_fraction = self.config.risk.kelly_fraction
        max_size = account_balance * self.config.risk.max_position_size
        
        # Kelly Criterion: position_size = kelly_fraction * win_ratio
        kelly_size = account_balance * kelly_fraction * confidence
        
        return min(kelly_size, max_size)
    
    def apply_stop_loss(self, entry_price: float, atr: float) -> float:
        """Calculate ATR-based stop loss
        
        Args:
            entry_price: Entry price
            atr: Average True Range
        
        Returns:
            Stop loss price
        """
        multiplier = self.config.risk.atr_multiplier
        return entry_price - (atr * multiplier)
