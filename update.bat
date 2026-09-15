@echo off

del /Q Files_hash.db 2>null

py create_db.py

if %ERRORLEVEL% NEQ 0 (
   echo Creation database failed
   exit /b 1
   pause
)
 

py find.py

if %ERRORLEVEL% EQU 0 (
    echo Insert values success
) else (
    echo Insert values failed
)

pause