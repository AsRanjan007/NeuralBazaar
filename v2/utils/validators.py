"""Data validation utilities

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
import pandas as pd
from typing import Tuple

logger = logging.getLogger(__name__)


def validate_ohlcv(df: pd.DataFrame) -> Tuple[bool, str]:
    """Validate OHLCV data format"""
    required_cols = ['open', 'high', 'low', 'close', 'volume']
    
    for col in required_cols:
        if col not in df.columns:
            return False, f"Missing column: {col}"
    
    if df.isnull().any().any():
        return False, "Found null values"
    
    return True, "Valid"


def validate_features(df: pd.DataFrame) -> Tuple[bool, str]:
    """Validate feature data"""
    if df.empty:
        return False, "Empty dataframe"
    
    if df.isnull().any().any():
        return False, "Contains null values"
    
    return True, "Valid"
