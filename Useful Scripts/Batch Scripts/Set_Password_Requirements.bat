REM Sets verious password requirements for the system.

net accounts /uniquepw:10

net accounts /maxpwage:90

net accounts /minpwage:1

net accounts /minpwlen:8

net accounts /lockoutwindow:15

net accounts /lockoutduration:15

net accounts /lockoutthreshold:5

Auditpol /set /category:"Account Logon" /Success:enable /failure:enable

Auditpol /set /category:"Account Management" /Success:enable /failure:enable

Auditpol /set /category:"Logon/Logoff" /Success:enable /failure:enable