@echo off

echo ========================================
echo        ProductIQ AI
echo ========================================
echo.

start /b python -m uvicorn main:app --host 127.0.0.1 --port 8000

timeout /t 2 /nobreak > nul

python -m streamlit run ui.py