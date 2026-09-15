@echo off

py detect.py

if %ERRORLEVEL% EQU 0 (
    echo Success
 ) else (
    echo Error
 )

pause