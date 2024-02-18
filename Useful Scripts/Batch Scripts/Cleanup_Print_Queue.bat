REM Cleanup Current Print Queue

net stop spooler 
del %windir%\system32\spool\printers\*.shd 
del %windir%\system32\spool\printers\*.spl 
net start spooler