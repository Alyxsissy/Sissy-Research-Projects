REM Enables logons to Domains Accounts using Biometics Fingerprinter Readers.

reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\System\" /v "AllowDomainPINLogon" /t REG_SZ /d 1 /f
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\WinBio\Credential Provider\" /v "Domain Accounts" /t REG_SZ /d 1 /f