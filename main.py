#!/usr/bin/env python
"""
NeuralBazaar - Intelligent Multi-Signal Trading Assistant
Main entry point with version switching support

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import argparse
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class VersionManager:
    """Manages switching between different versions"""
    
    SUPPORTED_VERSIONS = ['2.0.0', '1.0.0']
    DEFAULT_VERSION = '2.0.0'
    
    @staticmethod
    def load_version(version: str):
        """Load and initialize specified version"""
        if version not in VersionManager.SUPPORTED_VERSIONS:
            raise ValueError(f"Unsupported version {version}. Supported: {VersionManager.SUPPORTED_VERSIONS}")
        
        logger.info(f"Loading NeuralBazaar version {version}")
        
        if version == '2.0.0':
            from v2.core.trading_system import TradingSystemV2
            return TradingSystemV2()
        elif version == '1.0.0':
            logger.warning("Legacy version 1.0.0 loaded")
            from v2.core.trading_system import TradingSystemV1
            return TradingSystemV1()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='NeuralBazaar - Multi-Signal Intelligent Trading Assistant',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        '--version',
        type=str,
        default=VersionManager.DEFAULT_VERSION,
        choices=VersionManager.SUPPORTED_VERSIONS,
        help=f'Trading system version (default: {VersionManager.DEFAULT_VERSION})'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['backtest', 'realtime', 'paper'],
        default='paper',
        help='Execution mode (default: paper)'
    )
    parser.add_argument(
        '--symbol',
        type=str,
        default=None,
        help='Stock symbol to trade'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config/config.yaml',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        logger.info(f"NeuralBazaar Starting...")
        logger.info(f"Version: {args.version}")
        logger.info(f"Mode: {args.mode}")
        
        # Load version
        trading_system = VersionManager.load_version(args.version)
        
        # Initialize system
        trading_system.initialize(
            config_path=args.config,
            mode=args.mode,
            symbol=args.symbol
        )
        
        # Run system
        trading_system.run()
        
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
