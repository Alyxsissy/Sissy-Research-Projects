## Set Variables
$messageTitle = "{[messageTitle]}";
$message = "{[message]}"



##
##
## DO NOT EDIT ANYTHING BELOW THIS
##
##

# Set the title of the message box
$messageTitle

# Set the message to be displayed
$message


# Set the message box type (0 = OK)
$mbType = 0

# Set the message box icon (64 = information)
$mbIcon = 64

# Set the message box options (4096 = system modal)
$mbOptions = 4096

# Create a registry key to store the message box settings
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "LegalNoticeCaption" -Value $messageTitle -PropertyType String -Force | Out-Null
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "LegalNoticeText" -Value $message -PropertyType String -Force | Out-Null
New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name "LegalNoticeType" -Value "$mbType $mbIcon $mbOptions" -PropertyType String -Force | Out-Null