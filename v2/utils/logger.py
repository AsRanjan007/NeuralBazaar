"""Logging configuration and utilities

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
import sys
from typing import Optional


def setup_logger(name: Optional[str] = None, 
                level: int = logging.INFO) -> logging.Logger:
    """Setup logger with standard format"""
    logger = logging.getLogger(name or __name__)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.setLevel(level)
    
    return logger
