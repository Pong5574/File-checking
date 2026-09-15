@echo off

py show.py

if %ERRORLEVEL% EQU 0 (
    echo Success
 ) else (
    echo Error
 )

pause