#!/usr/bin/env python
"""
NeuralBazaar Application Launcher
Handles graceful shutdown and proper resource cleanup
"""

import sys
import os
import signal
import threading
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress asyncio warnings during shutdown
def setup_shutdown_handler():
    """Setup signal handlers for graceful shutdown"""
    
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, initiating graceful shutdown...")
        sys.exit(0)
    
    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

def suppress_event_loop_warning():
    """Suppress 'Event loop is closed' warning from Streamlit shutdown"""
    import warnings
    import asyncio
    
    # Suppress specific warning
    warnings.filterwarnings("ignore", category=RuntimeError, message="Event loop is closed")
    
    # Patch the event loop closing to be more graceful
    original_close = asyncio.BaseEventLoop._close
    
    def patched_close(self):
        try:
            original_close(self)
        except Exception:
            pass
    
    asyncio.BaseEventLoop._close = patched_close

def setup_thread_cleanup():
    """Setup cleanup for thread pools"""
    import atexit
    import concurrent.futures
    
    def cleanup_thread_pools():
        """Cleanup any remaining thread pools"""
        try:
            # Give threads a moment to finish
            import time
            time.sleep(0.1)
        except Exception:
            pass
    
    atexit.register(cleanup_thread_pools)

def main():
    """Main entry point for running NeuralBazaar"""
    
    try:
        # Setup handlers
        setup_shutdown_handler()
        suppress_event_loop_warning()
        setup_thread_cleanup()
        
        logger.info("🚀 Starting NeuralBazaar v2.0.0...")
        
        # Import and run streamlit
        import streamlit.cli as stcli
        
        # Set up arguments for streamlit
        sys.argv = [
            "streamlit",
            "run",
            str(Path(__file__).parent / "app.py"),
            "--logger.level=warning"
        ]
        
        # Run the app
        stcli.main()
        
    except KeyboardInterrupt:
        logger.info("⌛ Shutting down NeuralBazaar...")
        print("\n✅ NeuralBazaar closed gracefully")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"❌ Error starting NeuralBazaar: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
