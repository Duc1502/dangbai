@echo off
echo Installing Python dependencies...
python -m pip install -r requirements.txt
if %errorlevel% equ 0 (
    echo.
    echo Installation successful!
    echo.
) else (
    echo.
    echo Installation failed. Please check the error above.
    echo.
)
pause
