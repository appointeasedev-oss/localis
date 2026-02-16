#!/usr/bin/env python3
"""Test script for localis"""
import sys
import os

# Add localis to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Import localis module
    import localis
    
    # Test basic functionality
    print("Testing localis...")
    print(f"Version: {localis.__version__}")
    print(f"Author: {localis.__author__}")
    print(f"Repo: {localis.__repo__}")
    
    # Test colors
    print(f"Colors work: {localis.Colors.GREEN}GREEN{localis.Colors.ENDC}")
    
    # Test config
    config = localis.LocalisConfig()
    print(f"Config loaded: {config.config['default_model']}")
    
    # Test memory
    memory = localis.MemoryManager()
    print("Memory loaded: OK")
    
    # Test ollama manager
    ollama = localis.OllamaManager()
    print(f"Ollama installed: {ollama.is_installed()}")
    print(f"Ollama running: {ollama.is_running()}")
    print(f"Models available: {len(ollama.list_all_models())}")
    
    # Test workspace
    workspace = localis.WorkspaceManager()
    print(f"Workspace path: {workspace.get_workspace()}")
    
    # Test git
    git = localis.GitManager(workspace)
    print(f"Git manager: OK")
    
    print("\n" + "="*50)
    print("ALL TESTS PASSED!")
    print("="*50)
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
