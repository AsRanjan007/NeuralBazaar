"""Performance metrics tracking

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
from typing import Dict, Any
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)


class MetricsTracker:
    """Tracks trading metrics and performance"""
    
    def __init__(self):
        self.signals = []
        self.trades = []
        logger.info("MetricsTracker initialized")
    
    def record_signal(self, signal: str, confidence: float, 
                     position_size: float) -> None:
        """Record a generated signal"""
        self.signals.append({
            'timestamp': datetime.now(),
            'signal': signal,
            'confidence': confidence,
            'position_size': position_size,
        })
    
    def record_trade(self, entry_price: float, exit_price: float,
                    quantity: int) -> None:
        """Record executed trade"""
        self.trades.append({
            'entry_price': entry_price,
            'exit_price': exit_price,
            'quantity': quantity,
            'pnl': (exit_price - entry_price) * quantity,
        })
    
    def get_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        total_signals = len(self.signals)
        total_trades = len(self.trades)
        
        if total_trades > 0:
            total_pnl = sum(t['pnl'] for t in self.trades)
            avg_return = total_pnl / total_trades
        else:
            avg_return = 0.0
        
        return {
            'total_signals': total_signals,
            'total_trades': total_trades,
            'total_pnl': total_pnl if total_trades > 0 else 0.0,
            'avg_return_per_trade': avg_return,
        }
