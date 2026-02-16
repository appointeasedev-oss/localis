@echo off
echo ============================================================
echo   LOCALIS - Git Setup & Push to GitHub
echo ============================================================
echo.

REM Change to localis directory
cd /d "%~dp0"

REM Check if git initialized
if not exist ".git" (
    echo [1/5] Initializing Git...
    git init
    echo [✓] Git initialized
) else (
    echo [✓] Git already initialized
)

REM Check if remote exists
git remote -v origin >nul 2>&1
if errorlevel 1 (
    echo.
    echo [2/5] Adding remote origin...
    echo ENTER YOUR GITHUB REPO URL
    echo Create empty repo at https://github.com/new first!
    echo.
    set /p REPO_URL="   Repo URL: "
    if defined REPO_URL (
        git remote add origin %REPO_URL%
        echo [✓] Remote added
    ) else (
        echo [SKIP] No URL provided
    )
) else (
    echo [✓] Remote already configured
)

REM Stage all files
echo.
echo [3/5] Staging all files...
git add -A
echo [✓] Files staged

REM Create initial commit
echo.
echo [4/5] Creating initial commit...
git commit -m "Initial commit: localis v1.0.0 by Sparrow

🐦 localis - A powerful local AI coding assistant
- 100% local, powered by Ollama
- Auto-install Ollama and models
- Workspace management with GitHub clone
- Interactive chat with memory
- Git integration
- Premium ASCII UI

Repo: https://github.com/appointeasedev-oss/localis"
echo [✓] Commit created

REM Push to GitHub
echo.
echo [5/5] Pushing to GitHub...
echo.
git branch -M main
git push -u origin main

echo.
echo ============================================================
echo   ✅ UPLOAD COMPLETE!
echo ============================================================
echo.
echo NEXT STEP - Create release:
echo.
echo   1. Go to: https://github.com/appointeasedev-oss/localis/releases
echo   2. Click: Draft a new release
echo   3. Tag: v1.0.0
echo   4. Title: Release v1.0.0
echo   5. Publish release
echo.
echo OR via command:
echo   git tag v1.0.0
echo   git push origin v1.0.0
echo.
pause
