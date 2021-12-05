cls
color 0a

@ECHO %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM%

@echo off
Title Window's Wifi PAssword Finder 
@Echo  Created By Deadshot0x7
NETSH WLAN SHOW PROFILE
pause>nul 
set /p Var1="Enter NetwOrk SSid"

NETSH WLAN SHOW PROFILE %Var1% Key=clear

@ECHO %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM% %RANDOM%

pause>nul