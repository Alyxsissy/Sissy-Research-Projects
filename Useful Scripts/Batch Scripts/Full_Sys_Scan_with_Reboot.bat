REM Performs a full system scan and repair of the local computer, then reboots the computer.

@Echo Off

Echo Y | chkdsk /f /r /x 

sfc /scannow

start /wait findstr /c:"[SR]" %windir%\Logs\CBS\CBS.log >"%userprofile%\Desktop\sfcdetails.txt"

start /wait dism.exe /online /cleanup-image /restorehealth

start /wait shutdown /r /t 0
@Echo On