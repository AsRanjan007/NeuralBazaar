#!/usr/bin/env python
"""
NeuralBazaar v2.0.0 Setup Script
Run this script to create the complete directory structure and all module files
Includes version switching between 2.0.0 and 1.0.0

Copyright (c) 2025 Ashutosh Ranjan. All rights reserved.
Licensed under the MIT License. See LICENSE file for details.
"""

import os
from pathlib import Path
import sys


def create_files():
    """Create all necessary directories and files for v2.0.0"""
    
    base_path = Path.cwd()
    
    # Directory structure to create
    directories = [
        'config',
        'v2/core',
        'v2/pillar1_timeseries',
        'v2/pillar2_news',
        'v2/pillar3_signal_fusion',
        'v2/pillar4_risk',
        'v2/pillar5_data',
        'v2/utils',
        'v1',
        'docs',
        'tests',
        'data/cache',
        'data/models',
    ]
    
    # Create all directories
    print("Creating directory structure...")
    for dir_path in directories:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        
        # Create __init__.py files
        if 'data' not in dir_path:
            init_file = full_path / '__init__.py'
            if not init_file.exists():
                init_file.write_text(f'"""{dir_path} module"""\n', encoding='utf-8')
                print(f"  ✓ {init_file}")
    
    # Import file contents
    from file_templates import FILE_CONTENTS
    
    # File path mappings
    files_to_create = [
        ('config/__init__.py', 'config_init'),
        ('config/config.py', 'config_py'),
        ('v2/__init__.py', 'v2_init'),
        ('v2/core/__init__.py', 'v2_core_init'),
        ('v2/core/trading_system.py', 'trading_system_v2'),
        ('v2/pillar1_timeseries/__init__.py', 'pillar1_init'),
        ('v2/pillar1_timeseries/models.py', 'pillar1_models'),
        ('v2/pillar1_timeseries/forecaster.py', 'pillar1_forecaster'),
        ('v2/pillar2_news/__init__.py', 'pillar2_init'),
        ('v2/pillar2_news/sentiment_analyzer.py', 'pillar2_sentiment'),
        ('v2/pillar2_news/knowledge_graph.py', 'pillar2_graph'),
        ('v2/pillar2_news/news_processor.py', 'pillar2_processor'),
        ('v2/pillar3_signal_fusion/__init__.py', 'pillar3_init'),
        ('v2/pillar3_signal_fusion/ensemble.py', 'pillar3_ensemble'),
        ('v2/pillar3_signal_fusion/rl_agent.py', 'pillar3_rl'),
        ('v2/pillar3_signal_fusion/signal_generator.py', 'pillar3_signals'),
        ('v2/pillar4_risk/__init__.py', 'pillar4_init'),
        ('v2/pillar4_risk/anomaly_detector.py', 'pillar4_anomaly'),
        ('v2/pillar4_risk/risk_manager.py', 'pillar4_risk'),
        ('v2/pillar4_risk/regime_classifier.py', 'pillar4_regime'),
        ('v2/pillar5_data/__init__.py', 'pillar5_init'),
        ('v2/pillar5_data/data_ingester.py', 'pillar5_ingester'),
        ('v2/pillar5_data/feature_engineer.py', 'pillar5_features'),
        ('v2/pillar5_data/data_cache.py', 'pillar5_cache'),
        ('v2/utils/__init__.py', 'utils_init'),
        ('v2/utils/logger.py', 'utils_logger'),
        ('v2/utils/metrics.py', 'utils_metrics'),
        ('v2/utils/validators.py', 'utils_validators'),
        ('requirements.txt', 'requirements_txt'),
        ('docs/architecture_v2.md', 'architecture_doc'),
    ]
    
    print("\nCreating Python modules...")
    for file_path, content_key in files_to_create:
        full_path = base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        if full_path.exists():
            print(f"  ⊘ Skipping (exists): {file_path}")
        else:
            # Get content from templates
            content = FILE_CONTENTS.get(content_key, '')
            if content:
                full_path.write_text(content, encoding='utf-8')
                print(f"  ✓ {file_path}")
    
    # Create main.py if doesn't exist
    main_py_path = base_path / 'main.py'
    if not main_py_path.exists():
        main_py_path.write_text(FILE_CONTENTS['main_py'], encoding='utf-8')
        print(f"  ✓ main.py")
    else:
        print(f"  ⊘ Skipping (exists): main.py")
    
    # Create v1 stub
    v1_init_path = base_path / 'v1' / '__init__.py'
    if not v1_init_path.exists():
        v1_init_path.write_text('"""Legacy version 1.0.0"""\n', encoding='utf-8')
        print(f"  ✓ v1/__init__.py")
    
    print("\n✅ NeuralBazaar v2.0.0 structure created successfully!\n")
    print("📋 Next steps:")
    print("   1. pip install -r requirements.txt")
    print("   2. python main.py --version 2.0.0 --help")
    print("   3. python main.py --version 2.0.0 --mode paper --symbol AAPL\n")
    print("💡 Version switching:")
    print("   - python main.py --version 2.0.0  # Use new architecture")
    print("   - python main.py --version 1.0.0  # Use legacy version\n")


if __name__ == '__main__':
    try:
        create_files()
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

