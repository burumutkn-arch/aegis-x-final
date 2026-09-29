@echo off
title AEGIS-X FINAL COMMAND CENTER
cd /d "C:\Users\Casper\Desktop\AEGIS-X ENGINEERING PLATFORM\aegis-x-final"

if not exist ".venv" (
    echo Karargah sistemleri baslatiliyor...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

echo.
echo =====================================================
echo  AEGIS-X FINAL - ISTIHBARAT COZUMLEME MERKEZI
echo =====================================================
echo.
python main.py
pause
