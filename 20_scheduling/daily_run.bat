@echo off
setlocal

REM ----------------------------
REM Day 20 - Daily Runner (Windows)
REM ----------------------------

REM Run from the same folder as this .bat file
cd /d "%~dp0"

echo =======================================
echo Running Daily Checks...
echo Folder: %cd%
echo Time  : %date% %time%
echo =======================================

REM Create/append a log file
echo ======================================= >> daily_log.txt
echo Run time: %date% %time% >> daily_log.txt
echo Folder  : %cd% >> daily_log.txt
echo ======================================= >> daily_log.txt

echo [1/2] DNS Check...
python dns_check.py >> daily_log.txt 2>&1

echo [2/2] Port Check...
python port_check.py >> daily_log.txt 2>&1

echo Done. Reports generated:
echo - dns_report.txt
echo - port_report.txt
echo - daily_log.txt

pause
endlocal
