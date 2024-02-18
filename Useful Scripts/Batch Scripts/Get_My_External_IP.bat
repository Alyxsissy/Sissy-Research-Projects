REM Retrieves what the world sees as your external IP address.

@echo off

nslookup -type=txt whoami.Cloudflare.com ns3.Cloudflare.com
exit