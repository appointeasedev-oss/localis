@echo off
echo.
echo ================================================================================
echo   LOCALIS v1.0.0 Installer by Sparrow
echo   https://github.com/appointeasedev-oss/localis
echo ================================================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.8+
    pause
    exit /b 1
)
echo [OK] Python found

REM Install dependencies
echo.
echo [1/5] Installing dependencies...
pip install -r requirements.txt >nul 2>&1
echo [OK] Dependencies installed

REM Check/Start Ollama
echo.
echo [2/5] Checking Ollama...
where ollama >nul 2>&1
if not errorlevel 1 (
    echo [OK] Ollama found
    
    REM Try to start Ollama
    echo [3/5] Starting Ollama...
    start /B ollama serve >nul 2>&1
    
    REM Wait for Ollama
    timeout /t 5 /nobreak >nul
    
    REM Check if running
    curl -s http://localhost:11434/api/tags >nul 2>&1
    if not errorlevel 1 (
        echo [OK] Ollama is running
    ) else (
        echo [WARNING] Ollama installed but not running
        echo    Run: ollama serve
    )
) else (
    echo [WARNING] Ollama not found
    echo    Download: https://ollama.ai/download
    echo    Run: install_ollama.bat after installing
)

REM Create localis command
echo.
echo [4/5] Creating localis command...

REM Get script directory
set SCRIPT_DIR=%~dp0
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Create localis.bat
setlocal
set "LOCALIS_BAT=%USERPROFILE%\AppData\Local\Microsoft\Windows\Apps\localis.bat"
echo @echo off > "%LOCALIS_BAT%"
echo python "%SCRIPT_DIR%\localis.py" %%* >> "%LOCALIS_BAT%"

REM Add to PATH
setx PATH "%USERPROFILE%\AppData\Local\Microsoft\Windows\Apps;%PATH%" >nul 2>&1

echo [OK] Command 'localis' created

REM Create Start Menu shortcut
set "SHORTCUT_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\localis.lnk"
powershell -Command ^
    $target = '%SCRIPT_DIR%\localis.py'; ^
    $shortcut = '%SHORTCUT_PATH%'; ^
    $ws = New-Object -ComObject WScript.Shell; ^
    $s = $ws.CreateShortcut($shortcut); ^
    $s.TargetPath = 'python.exe'; ^
    $s.Arguments = '"""%TARGET_FILE%"""'; ^
    $s.WorkingDirectory = '%SCRIPT_DIR%'; ^
    $s.Description = 'localis - Local AI by Sparrow'; ^
    $s.Save()

echo [OK] Start Menu shortcut created

REM Create directories
echo.
echo [5/5] Setting up directories...
if not exist "%USERPROFILE%\localis_workspace" mkdir "%USERPROFILE%\localis_workspace"
if not exist "%USERPROFILE%\.localis" mkdir "%USERPROFILE%\.localis"
echo [OK] Directories created

echo.
echo ================================================================================
echo   INSTALLATION COMPLETE!
echo ================================================================================
echo.
echo [INFO] To start localis:
echo    1. Run: localis
echo    2. Or use Start Menu shortcut
echo.
echo [FIRST TIME] Run /setup to configure
echo.
echo ================================================================================
echo   LOCALIS v1.0.0 by Sparrow
echo   Repo: https://github.com/appointeasedev-oss/localis
echo ================================================================================
echo.
pause
