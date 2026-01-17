@echo off
REM Build standalone executable for Windows
REM Создание автономного исполняемого файла для Windows

echo.
echo ============================================================
echo Building Constitution Quiz Executable
echo Создание исполняемого файла Викторины о Конституции
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed
    echo ОШИБКА: Python не установлен
    pause
    exit /b 1
)

REM Install PyInstaller if not already installed
echo Checking for PyInstaller...
python -m pip list | findstr PyInstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
)

REM Create the executable
echo.
echo Creating executable...
echo Создание исполняемого файла...
echo.

python -m PyInstaller --onefile --windowed --icon=icon.ico ^
    --name="Constitution_Quiz" ^
    --distpath=dist ^
    --workpath=build ^
    --specpath=build ^
    main.py

echo.
if exist "dist\Constitution_Quiz.exe" (
    echo ============================================================
    echo SUCCESS! Executable created successfully!
    echo УСПЕХ! Исполняемый файл создан успешно!
    echo.
    echo Location: dist\Constitution_Quiz.exe
    echo Расположение: dist\Constitution_Quiz.exe
    echo.
    echo You can now copy this file to a USB drive!
    echo Теперь вы можете скопировать этот файл на флэшку!
    echo ============================================================
) else (
    echo ERROR: Failed to create executable
    echo ОШИБКА: Не удалось создать исполняемый файл
)

echo.
pause
