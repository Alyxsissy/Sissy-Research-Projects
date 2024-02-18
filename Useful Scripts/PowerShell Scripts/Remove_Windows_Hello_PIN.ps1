# Remove Windows Hello PIN

$passportFolder = 'C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc'

if (Test-Path $passportFolder)
{
    takeown /f $passportFolder /r /d y
    icacls $passportFolder /reset /t /c /l /q
    
    Remove-Item $passportFolder ?recurse -force
}