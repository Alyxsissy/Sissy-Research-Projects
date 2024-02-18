REM Reboots the PC to normal mode from Safe Mode

bcdedit /deletevalue {current} safeboot
shutdown -r -f -t 0