# Disables the lock screen in Windows 10 and 11.

Set-Location HKLM:\SOFTWARE\Policies\Microsoft\Windows\Personalization
New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Personalization" -Name "NoLockScreen" -Value 1 -PropertyType Dword
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Personalization" -Name "NoLockScreen" -Value 1