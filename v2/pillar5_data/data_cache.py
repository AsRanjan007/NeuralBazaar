"""
Pillar 5.3: Data Caching & Storage
Performance optimization via caching

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import logging
from typing import Optional, Any
import pickle
import os

logger = logging.getLogger(__name__)


class DataCache:
    """Caches features and model predictions"""
    
    def __init__(self, cache_dir: str = 'data/cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        logger.info(f"DataCache initialized at {cache_dir}")
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve from cache"""
        path = os.path.join(self.cache_dir, f"{key}.pkl")
        if os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
        return None
    
    def set(self, key: str, value: Any) -> None:
        """Store in cache"""
        path = os.path.join(self.cache_dir, f"{key}.pkl")
        with open(path, 'wb') as f:
            pickle.dump(value, f)
