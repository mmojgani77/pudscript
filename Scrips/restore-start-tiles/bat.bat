@echo off
cls
taskkill /f /im explorer.exe
taskkill /f /im shellexperiencehost.exe
timeout /t 3 /NOBREAK > nul
del %localappdata%\Packages\Microsoft.Windows.ShellExperienceHost_cw5n1h2txyewy\TempState\* /q
timeout /t 2 /NOBREAK > nul
start explorer
echo start menu tiles restored.
@echo on
pause>nul