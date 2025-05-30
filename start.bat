@echo off
pip install -r requirements.txt >nul 2>&1
cls
cd results/aamain
python main.py

