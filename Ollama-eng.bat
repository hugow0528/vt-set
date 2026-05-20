@echo off
TITLE HikariSnowbell-Ollama-English
SETLOCAL EnableDelayedExpansion
cd /d "%~dp0"

echo [1/3] Switching to Local Ollama (Qwen3.6) English Config...
copy /y "conf-ollama-eng.yaml" "conf.yaml" >nul

echo [2/3] Checking environment...
where uv >nul 2>nul
if %ERRORLEVEL% neq 0 (
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iEx"
    set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)
uv sync

echo [3/3] Starting HikariSnowbell (Ollama-Qwen3.6-Maisie)...
echo URL: http://127.0.0.1:12393
echo.
echo IMPORTANT: Make sure Ollama app is running in background!
echo.
uv run run_server.py
pause
