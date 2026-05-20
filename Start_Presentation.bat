@echo off
setlocal
cd /d "%~dp0"

echo ===================================================
echo   HikariSnowbell Presentation Launcher (USB)
echo ===================================================

:: 1. Check if uv.exe is here
if not exist "uv.exe" (
    echo [ERROR] uv.exe not found in USB! 
    echo Please download uv-x86_64-pc-windows-msvc.zip and put uv.exe here.
    pause
    exit
)

:: 2. Sync environment to USB folder (Quick check)
echo [PROCESS] Checking USB environment...
.\uv.exe sync

:: 3. Launch Backend in another window
echo [PROCESS] Starting VTuber Backend in background...
start "Hikari_Backend" .\uv.exe run run_server.py

:: 4. Wait for server
echo [PROCESS] Waiting 15 seconds for system startup...
timeout /t 15

:: 5. Launch Controller
echo [PROCESS] Starting Presentation Controller...
echo.
echo ---------------------------------------------------
echo  STEP 1: Open Chrome to http://127.0.0.1:12393
echo  STEP 2: Use "Pet Mode" to show Hikari on screen
echo  STEP 3: Open your PowerPoint Fullscreen
echo  STEP 4: Press [F8] to speak
echo ---------------------------------------------------
echo.

.\uv.exe run present_hikari.py

pause
