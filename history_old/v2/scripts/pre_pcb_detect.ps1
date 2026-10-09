param([string]$OutputPath='v2/evidence/pre_pcb_board_ready/board_identity')
$ErrorActionPreference='Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
$dest=Join-Path (Get-Location) $OutputPath
$raw=Join-Path $dest 'local_raw'
New-Item -ItemType Directory -Force -Path $raw | Out-Null
function Write-Inventory($name,$value) { ConvertTo-Json -InputObject @($value) -Depth 10 | Set-Content -LiteralPath (Join-Path $raw $name) -Encoding utf8 }
$devices=@(Get-PnpDevice -PresentOnly)
$usb=@($devices | Where-Object { $_.InstanceId -match '^(USB|FTDIBUS)\\' } | Select-Object Status,Class,FriendlyName,InstanceId)
Write-Inventory 'usb.json' $usb
$ftdi=@($devices | Where-Object { $_.InstanceId -match 'VID_0403' -or $_.FriendlyName -match 'FTDI|FT2232|USB Serial' })
Write-Inventory 'ftdi_properties.json' @($ftdi | ForEach-Object { [PSCustomObject]@{Name=$_.FriendlyName;ID=$_.InstanceId;Properties=@(Get-PnpDeviceProperty -InstanceId $_.InstanceId | Select-Object KeyName,Type,Data)} })
$ports=@(Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,PNPDeviceID,Status)
Write-Inventory 'ports.json' $ports
$drivers=@(Get-CimInstance Win32_PnPSignedDriver | Where-Object DeviceID -Match 'VID_0403' | Select-Object DeviceName,DeviceID,DriverProviderName,DriverVersion,InfName,IsSigned)
Write-Inventory 'drivers.json' $drivers
$net=@(Get-NetAdapter -IncludeHidden | Select-Object Name,InterfaceDescription,Status,LinkSpeed,HardwareInterface,Virtual,PnPDeviceID)
Write-Inventory 'network.json' $net
$visible=@($ftdi | ForEach-Object {
 $usbVid=[regex]::Match($_.InstanceId,'VID_([0-9A-F]{4})').Groups[1].Value
 $usbPid=[regex]::Match($_.InstanceId,'PID_([0-9A-F]{4})').Groups[1].Value
 $usbInterface=[regex]::Match($_.InstanceId,'MI_([0-9A-F]{2})').Groups[1].Value
 [PSCustomObject]@{Name=$_.FriendlyName;Status=$_.Status;Class=$_.Class;VID=$usbVid;PID=$usbPid;Interface=$usbInterface}
})
$summary=[ordered]@{current_model='GPT-6.1 Sol High';timestamp_utc=(Get-Date).ToUniversalTime().ToString('o');shell=$PSVersionTable.PSVersion.ToString();usb_device_count=$usb.Count;ftdi=$visible;com_ports=@($ports | Select-Object DeviceID,Name,Status);ftdi_drivers=@($drivers | Select-Object DeviceName,DriverProviderName,DriverVersion,InfName,IsSigned);network=@($net | Select-Object InterfaceDescription,Status,LinkSpeed,HardwareInterface,Virtual);serial_opened=$false;drivers_changed=$false;hardware_programmed=$false;ethernet_board_identity='NOT_ESTABLISHED_BY_HOST_ADAPTER_ENUMERATION'}
$summary | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $dest 'windows_inventory.json') -Encoding utf8
$summary['managed_port_names']=@([System.IO.Ports.SerialPort]::GetPortNames())
$summary | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath (Join-Path $dest 'windows_inventory.json') -Encoding utf8
$summary | ConvertTo-Json -Depth 10
