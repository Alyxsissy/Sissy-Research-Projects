REM Sets the network type to private.

$net = get-netconnectionprofile;
Set-NetConnectionProfile -Name $net.Name -NetworkCategory Private