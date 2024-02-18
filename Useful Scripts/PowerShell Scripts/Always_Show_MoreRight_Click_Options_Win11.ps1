# Always shows more options in the right-click context menu in Windows 11.

$reg = 'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve'

if ($reg)
{
    Get-Process explorer | Stop-Process explorer
    Start-Process explorer
}
else
{
    throw "Error adding registry key or key is already present"
}