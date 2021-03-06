@echo off
echo.
echo [%~nx0] ===============================
echo [%~nx0] Continuous Delivery CD Starting
echo [%~nx0] ===============================

set ENVIRONMENT=%1
set RELEASE=%2
set OPT_ARG=%3
set WORK_DIR_DEFAULT=%4
set SOLUTION=%5
set BUILDNUMBER=%6

rem Launcher script that overides execution policy
rem cannot elevate powershell

IF [%WORK_DIR_DEFAULT%] == [] (
	set workDirLocal=TasksLocal
) ELSE (
	set workDirLocal=%WORK_DIR_DEFAULT%
)

call powershell -NoProfile -ExecutionPolicy ByPass -command %cd%\%workDirLocal%\delivery.ps1 %ENVIRONMENT% %RELEASE% %OPT_ARG% %WORK_DIR_DEFAULT% %SOLUTION% %BUILDNUMBER% %AUTOMATION_ROOT%
set result=%errorlevel%
if %result% NEQ 0 (
	echo.
	echo [%~nx0] Error %result% returned from ... 
	echo [%~nx0]   call powershell -NoProfile -ExecutionPolicy ByPass -command %cd%\%workDirLocal%\delivery.ps1 %ENVIRONMENT% %RELEASE% %OPT_ARG% %WORK_DIR_DEFAULT% %SOLUTION% %BUILDNUMBER% %AUTOMATION_ROOT%
	exit /b %result%
)
