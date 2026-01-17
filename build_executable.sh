#!/bin/bash
# Build standalone executable for Linux/Mac
# Создание автономного исполняемого файла для Linux/Mac

echo ""
echo "============================================================"
echo "Building Constitution Quiz Executable"
echo "Создание исполняемого файла Викторины о Конституции"
echo "============================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "ОШИБКА: Python 3 не установлен"
    exit 1
fi

# Install PyInstaller if not already installed
echo "Checking for PyInstaller..."
python3 -m pip list | grep -q PyInstaller
if [ $? -ne 0 ]; then
    echo "Installing PyInstaller..."
    python3 -m pip install pyinstaller
fi

# Create the executable
echo ""
echo "Creating executable..."
echo "Создание исполняемого файла..."
echo ""

python3 -m PyInstaller --onefile --name="constitution_quiz" \
    --distpath=dist \
    --workpath=build \
    --specpath=build \
    main.py

echo ""
if [ -f "dist/constitution_quiz" ]; then
    echo "============================================================"
    echo "SUCCESS! Executable created successfully!"
    echo "УСПЕХ! Исполняемый файл создан успешно!"
    echo ""
    echo "Location: dist/constitution_quiz"
    echo "Расположение: dist/constitution_quiz"
    echo ""
    echo "Make it executable:"
    echo "chmod +x dist/constitution_quiz"
    echo ""
    echo "You can now copy this file to a USB drive!"
    echo "Теперь вы можете скопировать этот файл на флэшку!"
    echo "============================================================"
else
    echo "ERROR: Failed to create executable"
    echo "ОШИБКА: Не удалось создать исполняемый файл"
fi

echo ""
