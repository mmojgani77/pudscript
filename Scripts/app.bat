echo off
cls
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
C:
cd\
IF [%1] == [] goto Help
IF Not Exist "%~dp0%1" goto Invalid

cd "%~dp0%1"
call bat.bat %2 %3 %4 %5 %6 %7 %8 %9
goto End

:Help
call "%~dp0--help/bat.bat"
goto End

:Invalid
echo.
call :ColorText 0c "  [+] Invalid script name"
echo.
echo.
echo   There is no script named "%1" 
call :ColorText 0a "  app --help"
echo  to read manual (help)
goto End

:ColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto End

:End