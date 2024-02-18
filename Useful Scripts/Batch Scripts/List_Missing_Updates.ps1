#Set-ExecutionPolicy -ExecutionPolicy Unrestricted

#List all missing updates
Write-Output "Creating Microsoft.Update.Session COM object" 
$session1 = New-Object -ComObject Microsoft.Update.Session -ErrorAction silentlycontinue

Write-Output "Creating Update searcher" 
$searcher = $session1.CreateUpdateSearcher()

Write-Output "Searching for missing updates..." 
$result = $searcher.Search("IsInstalled=0")

#Updates are waiting to be installed 
$updates = $result.Updates;

Write-Output "Found $($updates.Count) updates!" 

$updates | Format-Table Title, AutoSelectOnWebSites, IsDownloaded, IsHiden, IsInstalled, IsMandatory, IsPresent, AutoSelection, AutoDownload -AutoSize