@echo off
cd /d "C:\Users\Administrator\PycharmProjects\PythonProject3"

:: Generate datetime format YYYY-MM-DD_HHMM
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (
    set mm=%%a
    set dd=%%b
    set yyyy=%%c
)
for /f "tokens=1-2 delims=: " %%i in ("%time%") do (
    set hour=%%i
    set min=%%j
)
set commitmsg=Auto-backup_%yyyy%-%mm%-%dd%_%hour%%min%

:: Git push routine
git add .
git commit -m "%commitmsg%"
git push origin main
