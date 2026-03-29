"""Global configuration management for NeuralBazaar

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import os
import yaml
import logging
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


@dataclass
class ModelConfig:
    """ML model configuration"""
    timeseries_model: str = "lstm"  # lstm, transformer, prophet, xgboost
    sentiment_model: str = "finbert"  # finbert, roberta
    ensemble_method: str = "weighted"  # voting, stacking, weighted
    confidence_threshold: float = 0.65
    
    
@dataclass
class PipelineConfig:
    """Data pipeline configuration"""
    kafka_brokers: List[str] = field(default_factory=lambda: ['localhost:9092'])
    batch_size: int = 32
    lookback_period: int = 250  # trading days
    forecast_horizon: int = 5   # days ahead
    update_frequency: str = "5min"  # 5min, 1hour, daily
    
    
@dataclass
class RiskConfig:
    """Risk management configuration"""
    kelly_fraction: float = 0.25  # Conservative Kelly Criterion fraction
    max_position_size: float = 0.05  # 5% per position
    max_portfolio_drawdown: float = 0.10  # 10% circuit breaker
    atr_multiplier: float = 1.5  # ATR-based stop loss
    sector_concentration_cap: float = 0.30  # 30% max per sector
    min_sharpe_ratio: float = 0.5  # Alert if below this
    

@dataclass
class FeatureConfig:
    """Feature engineering configuration"""
    technical_indicators: List[str] = field(default_factory=lambda: [
        'sma', 'ema', 'rsi', 'macd', 'bollinger', 'atr', 'obv', 'ichimoku'
    ])
    statistical_features: List[str] = field(default_factory=lambda: [
        'returns', 'volatility', 'correlation', 'hurst_exponent'
    ])
    sentiment_lookback: int = 24  # hours
    normalize: bool = True
    

@dataclass
class SignalConfig:
    """Signal generation configuration"""
    buy_rules: Dict[str, float] = field(default_factory=lambda: {
        'min_price_ema_ratio': 1.0,
        'min_rsi': 50,
        'min_sentiment_score': 0.4,
        'min_volume_ratio': 1.5,
        'min_rl_confidence': 0.65
    })
    exit_rules: Dict[str, float] = field(default_factory=lambda: {
        'max_rsi': 70,
        'max_sentiment_score': -0.5,
        'fibonacci_multiple': 1.618,
        'atr_stop_loss_multiple': 1.5
    })
    hold_confidence_threshold: float = 0.5
    

class Config:
    """Global configuration manager singleton"""
    _instance = None
    
    def __new__(cls, config_path: Optional[str] = None):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, config_path: Optional[str] = None):
        if self._initialized:
            return
            
        self.model = ModelConfig()
        self.pipeline = PipelineConfig()
        self.risk = RiskConfig()
        self.feature = FeatureConfig()
        self.signal = SignalConfig()
        
        if config_path and os.path.exists(config_path):
            self._load_from_yaml(config_path)
        
        self._initialized = True
    
    def _load_from_yaml(self, config_path: str):
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as f:
                config_dict = yaml.safe_load(f) or {}
            
            for section_key, section_values in config_dict.items():
                if hasattr(self, section_key):
                    config_obj = getattr(self, section_key)
                    if isinstance(section_values, dict):
                        for field_key, field_val in section_values.items():
                            if hasattr(config_obj, field_key):
                                setattr(config_obj, field_key, field_val)
            
            logger.info(f"Loaded configuration from {config_path}")
        except Exception as e:
            logger.warning(f"Could not load config from {config_path}: {e}. Using defaults.")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            'model': vars(self.model),
            'pipeline': vars(self.pipeline),
            'risk': vars(self.risk),
            'feature': vars(self.feature),
            'signal': vars(self.signal),
        }
