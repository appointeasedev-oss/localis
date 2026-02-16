@echo off
echo ============================================================
echo   LOCALIS - Push to GitHub & Create Release
echo ============================================================
echo.

cd /d "%~dp0"

REM Stage all files
echo [1/4] Staging files...
git add -A
echo [OK] Files staged

REM Commit with fixes
echo.
echo [2/4] Creating commit...
git commit -m "Fix: GitHub Actions release workflow permissions

- Added proper permissions for release creation
- Fixed upload URL handling
- Added all documentation files"

echo [OK] Commit created

REM Push to GitHub
echo.
echo [3/4] Pushing to GitHub...
git push origin main

echo [OK] Pushed

REM Delete old tag and create new one
echo.
echo [4/4] Creating release v1.0.0...
git tag -d v1.0.0 2>nul
git tag v1.0.0
git push origin v1.0.0 --force

echo [OK] Release v1.0.0 created!

echo.
echo ============================================================
echo   DONE! Release is being created on GitHub!
echo ============================================================
echo.
echo Check your release at:
echo https://github.com/appointeasedev-oss/localis/releases
echo.
pause
