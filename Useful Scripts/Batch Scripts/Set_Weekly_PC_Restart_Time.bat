REM Set time at the end of the command before running.

schtasks /create /sc weekly /d THU /tn restart /ru system  /tr "shutdown - r -f ""restart""" /st 23:00