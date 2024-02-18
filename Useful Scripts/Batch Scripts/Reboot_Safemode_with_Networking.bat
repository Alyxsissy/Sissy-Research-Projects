REM Reboot in Safe Mode with Networking

REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\Splashtop Inc." /f
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\SplashtopRemoteService" /f
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AteraAgent" /f
bcdedit /set {current} safeboot network
shutdown -r -f -t 0