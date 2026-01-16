#!/usr/bin/env python3
"""
Main entry point for Constitution Quiz Application
Главная точка входа для приложения викторины о Конституции
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from quiz.app import main

if __name__ == "__main__":
    main()
