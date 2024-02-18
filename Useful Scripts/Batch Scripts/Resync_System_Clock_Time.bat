REM Resyncs Windows Clock's time with time.windows.com (real life time)

net stop w32time 
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" 
net start w32time 
w32tm /config /update 
w32tm /resync /rediscover 