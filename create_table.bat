@echo off

py create_db.py

if %ERRORLEVEL% EQU 0 (
    echo Create table success
 ) else (
    echo Create table failed
 )

pause