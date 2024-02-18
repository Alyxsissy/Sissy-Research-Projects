REM Create restore point named Restore Point XYZ

cmd.exe /k "wmic.exe /Namespace:\\root\default Path SystemRestore Call CreateRestorePoint "Restore Point XYZ", 100, 7"