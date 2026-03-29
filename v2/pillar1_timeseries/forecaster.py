"""
Pillar 1: Time-Series Forecasting Engine (Orchestrator)
Coordinates multiple forecasting models and generates predictions

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple

from v2.pillar1_timeseries.models import (
    LSTMModel, TransformerModel, ProphetModel, XGBoostModel, EnsembleTimeSeriesModel
)
from config.config import Config

logger = logging.getLogger(__name__)


class TimeSeriesForecaster:
    """Orchestrates time-series forecasting models"""
    
    def __init__(self, config: Config):
        self.config = config
        self.models = {}
        self._initialize_models()
        logger.info("TimeSeriesForecaster initialized")
    
    def _initialize_models(self):
        """Initialize forecasting models based on configuration"""
        self.models = {
            'lstm': LSTMModel(self.config.pipeline.lookback),
            'transformer': TransformerModel(self.config.pipeline.lookback),
            'prophet': ProphetModel(self.config.pipeline.lookback),
            'xgboost': XGBoostModel(self.config.pipeline.lookback),
        }
        
        # Create ensemble if configured
        if self.config.model.ensemble_method:
            self.ensemble = EnsembleTimeSeriesModel(
                list(self.models.values())
            )
        
        logger.info(f"Initialized {len(self.models)} forecasting models")
    
    def forecast(self, features: pd.DataFrame) -> Dict[str, Any]:
        """Generate multi-horizon price forecast
        
        Args:
            features: DataFrame with engineered features
        
        Returns:
            Dictionary with predictions and confidence scores
        """
        try:
            X = features.values
            
            # Generate predictions from ensemble
            predictions, confidence = self.ensemble.predict(X)
            
            return {
                'predictions': predictions,
                'confidence': confidence,
                'horizon': self.config.pipeline.forecast_horizon,
                'timestamp': pd.Timestamp.now(),
            }
            
        except Exception as e:
            logger.error(f"Forecasting error: {e}")
            return {
                'predictions': np.zeros(len(features)),
                'confidence': np.zeros(len(features)),
                'error': str(e),
            }
    
    def fit_models(self, X: np.ndarray, y: np.ndarray):
        """Fit all models on historical data"""
        logger.info(f"Fitting forecasting models on {X.shape[0]} samples")
        
        for model_name, model in self.models.items():
            model.fit(X, y)
            logger.info(f"Fitted {model_name}")
        
        if self.ensemble:
            self.ensemble.fit(X, y)
