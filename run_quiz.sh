#!/bin/bash
# Constitution Quiz Application - Linux/Mac Launcher
# Запуск приложения "Викторина о Конституции" на Linux/Mac

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "============================================================"
    echo "ERROR: Python 3 is not installed"
    echo "ОШИБКА: Python 3 не установлен"
    echo ""
    echo "Please install Python 3.7 or higher:"
    echo "Пожалуйста установите Python 3.7 или выше:"
    echo ""
    echo "On macOS (with Homebrew):"
    echo "  brew install python3"
    echo ""
    echo "On Ubuntu/Debian:"
    echo "  sudo apt-get install python3"
    echo ""
    echo "On Fedora:"
    echo "  sudo dnf install python3"
    echo "============================================================"
    echo ""
    exit 1
fi

# Run the quiz application
clear
python3 main.py
