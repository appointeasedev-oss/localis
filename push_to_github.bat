@echo off
echo ============================================================
echo   LOCALIS - Git Setup & First Push
echo ============================================================
echo.

REM Initialize git if not already
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
    echo ENTER YOUR GITHUB REPO URL (create at https://github.com/new first!)
    set /p REPO_URL="   Repo URL: "
    git remote add origin %REPO_URL%
    echo [✓] Remote added
) else (
    echo [✓] Remote already configured
)

REM Stage all files
echo.
echo [3/5] Staging files...
git add -A
echo [✓] Files staged

REM Create initial commit
echo.
echo [4/5] Creating initial commit...
git commit -m "Initial commit: Localis v1.0.0 - Local AI CLI System

Features:
- AI-powered coding assistant
- Ollama integration with auto-install
- Model management (auto-download)
- Workspace management with GitHub clone
- Interactive chat with memory
- Git integration
- Premium ASCII UI

See README.md for full documentation."
echo [✓] Commit created

REM Push to GitHub
echo.
echo [5/5] Pushing to GitHub...
echo NOTE: Create empty repo at https://github.com/new first!
echo.
git branch -M main
git push -u origin main

echo.
echo ============================================================
echo   UPLOAD COMPLETE!
echo ============================================================
echo.
echo NEXT STEP: Create a release to trigger auto-build:
echo.
echo   1. Go to: https://github.com/appointeasedev-oss/localis/releases
echo   2. Click: Draft a new release
echo   3. Tag: v1.0.0
echo   4. Title: Release v1.0.0
echo   5. Publish release
echo.
echo OR via command line:
echo   git tag v1.0.0
echo   git push origin v1.0.0
echo.
pause
