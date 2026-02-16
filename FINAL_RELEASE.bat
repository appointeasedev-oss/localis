@echo off
echo ============================================================
echo   🐦 LOCALIS - FINAL VERIFICATION & RELEASE
echo ============================================================
echo.

REM Check files exist
if exist "localis.py" (
    for %%I in (localis.py) do echo ✓ localis.py (%%~zI bytes)
) else echo ✗ localis.py MISSING

if exist "install.sh" echo ✓ install.sh
if exist "install.bat" echo ✓ install.bat
if exist "requirements.txt" echo ✓ requirements.txt
if exist "README.md" echo ✓ README.md
if exist "INSTALL.md" echo ✓ INSTALL.md
if exist ".github\workflows\release.yml" echo ✓ release.yml

echo.
echo ============================================================
echo   Git Commands to Run:
echo ============================================================
echo.
echo git add -A
echo git commit -m "Release v1.0.0: localis by Sparrow"
echo git remote add origin https://github.com/appointeasedev-oss/localis.git
echo git branch -M main
echo git push -u origin main
echo git tag v1.0.0
echo git push origin v1.0.0
echo.
pause
