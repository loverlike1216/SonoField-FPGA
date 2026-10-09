# Read-only inventory. Raw machine identifiers remain local, excluded from Git.
# No serial port opens, network probes, device reset, or driver changes.
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
$outDir = Join-Path $PSScriptRoot 'local_raw'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
function Save-Json($name, $value) {
    ConvertTo-Json -InputObject @($value | Where-Object { $null -ne $_ }) -Depth 12 | Set-Content -LiteralPath (Join-Path $outDir $name) -Encoding utf8
}
Save-Json 'environment.json' @{ timestamp=(Get-Date).ToUniversalTime().ToString('o'); shell=$PSVersionTable.PSVersion.ToString(); head=(git rev-parse HEAD); branch=(git branch --show-current) }
$devices = @(Get-PnpDevice -PresentOnly)
Save-Json 'usb_devices.json' ($devices | Where-Object InstanceId -Match '^(USB|FTDIBUS)\\' | Select-Object Status,Class,FriendlyName,InstanceId)
$ftdi = @($devices | Where-Object { $_.InstanceId -match 'VID_0403' -or $_.FriendlyName -match 'FTDI|FT2232|USB Serial' })
Save-Json 'ftdi_properties.json' @($ftdi | ForEach-Object {
    [pscustomobject]@{device=$_.FriendlyName; instance_id=$_.InstanceId; properties=@(Get-PnpDeviceProperty -InstanceId $_.InstanceId | Select-Object KeyName,Type,Data)}
})
Save-Json 'serial_ports.json' (Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,PNPDeviceID,Status,ProviderType)
Save-Json 'serial_port_names.json' ([System.IO.Ports.SerialPort]::GetPortNames())
Save-Json 'ftdi_drivers.json' (Get-CimInstance Win32_PnPSignedDriver | Where-Object DeviceID -Match 'VID_0403' | Select-Object DeviceName,DeviceID,DriverProviderName,DriverVersion,DriverDate,InfName,IsSigned)
Save-Json 'network_adapters.json' (Get-NetAdapter -IncludeHidden | Select-Object Name,InterfaceDescription,Status,LinkSpeed,MacAddress,InterfaceGuid,ifIndex,HardwareInterface,Virtual,PnPDeviceID)
Save-Json 'network_addresses.json' (Get-NetIPAddress | Select-Object InterfaceIndex,InterfaceAlias,AddressFamily,IPAddress,PrefixLength,AddressState)
Save-Json 'board_reference_hashes.json' (Get-ChildItem (Join-Path $PSScriptRoot '../../../Zynq7020') -Recurse -File | Get-FileHash -Algorithm SHA256 | Select-Object Path,Hash)
$ftdi | Select-Object Status,Class,FriendlyName,InstanceId | Format-Table -AutoSize
Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,Status | Format-Table
Get-NetAdapter | Select-Object Name,InterfaceDescription,Status,LinkSpeed | Format-Table
