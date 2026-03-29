"""
Pillar 3.1: Ensemble Signal Fusion
Multi-model voting and weighted ensemble logic

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
import numpy as np
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)


class SignalEnsemble:
    """Ensemble voting and signal fusion"""
    
    def __init__(self, method: str = "weighted"):
        self.method = method  # weighted, stacking, voting
        self.model_weights = {}
        logger.info(f"Initialized SignalEnsemble with method={method}")
    
    def fuse_signals(self, signals: Dict[str, float]) -> Tuple[str, float]:
        """Fuse multiple sub-signals into unified signal
        
        Args:
            signals: Dictionary of signal types with scores
                {'price_forecast': 0.7, 'sentiment': 0.3, ...}
        
        Returns:
            (unified_signal, confidence_score)
            signal: 'BUY', 'HOLD', 'SELL'
        """
        if self.method == "weighted":
            return self._weighted_fusion(signals)
        elif self.method == "voting":
            return self._voting_fusion(signals)
        else:
            return self._stacking_fusion(signals)
    
    def _weighted_fusion(self, signals: Dict[str, float]) -> Tuple[str, float]:
        """Weighted ensemble fusion"""
        total = np.mean(list(signals.values()))
        
        if total > 0.6:
            return 'BUY', total
        elif total < -0.4:
            return 'SELL', abs(total)
        else:
            return 'HOLD', 0.5
    
    def _voting_fusion(self, signals: Dict[str, float]) -> Tuple[str, float]:
        """Majority voting fusion"""
        buy_votes = sum(1 for s in signals.values() if s > 0.5)
        sell_votes = sum(1 for s in signals.values() if s < -0.4)
        
        if buy_votes > sell_votes:
            return 'BUY', buy_votes / len(signals)
        elif sell_votes > buy_votes:
            return 'SELL', sell_votes / len(signals)
        else:
            return 'HOLD', 0.5
    
    def _stacking_fusion(self, signals: Dict[str, float]) -> Tuple[str, float]:
        """Stacking-based meta-model fusion"""
        # Placeholder for stacking implementation
        return 'HOLD', 0.5
