REM Releases local IP, obtains new IP, clears ARP cache, clears NetBIOS cache, flushes DNS cache, and registers DNS.
REM Basically just hard resets your network connection.

ipconfig /release
ipconfig /renew
arp -d *
nbtstat -R
nbtstat -RR
ipconfig /flushdns
ipconfig /registerdns