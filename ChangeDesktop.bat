@ECHO OFF
python "%~dp0\changeDesktop.py"
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%~dp0\ChangeDesktop.ps1'"
