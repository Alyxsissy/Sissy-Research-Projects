REM Group Policy update and reboot PC.

gpupdate /force

reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 0 /f

net start wuauserv

shutdown /r