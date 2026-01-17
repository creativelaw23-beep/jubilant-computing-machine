@echo off
REM Constitution Quiz Application - Windows Launcher
REM Запуск приложения "Викторина о Конституции" на Windows

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ============================================================
    echo ERROR: Python is not installed or not in PATH
    echo ОШИБКА: Python не установлен или не в переменной PATH
    echo.
    echo Please install Python 3.7 or higher from:
    echo Пожалуйста установите Python 3.7 или выше с:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo Убедитесь что выбрали "Add Python to PATH" при установке!
    echo ============================================================
    echo.
    pause
    exit /b 1
)

REM Run the quiz application
cls
python main.py
pause
