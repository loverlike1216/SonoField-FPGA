param([switch]$BoardIdentification,[switch]$FullRegression)
$ErrorActionPreference='Stop'
$PSNativeCommandUseErrorActionPreference=$true
if($PSVersionTable.PSVersion.Major -lt 7){throw 'PowerShell 7 required'}
$repo=Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
Push-Location $repo
try {
 $python=Join-Path $repo '.venv/Scripts/python.exe'
 if(-not(Test-Path -LiteralPath $python)){throw 'Create .venv using the project guide before running'}
 if(-not $env:VIVADO_BIN){throw 'Set VIVADO_BIN to Vivado2025.2 bin'}
 $env:PYTHONUTF8='1';$env:PYTHONIOENCODING='utf-8'
 & $python v2/scripts/pre_pcb_checks.py --output evidence/pre_pcb_board_ready/reproduced_checks
 & $python v2/scripts/check_migration.py
 if($FullRegression){& $python v2/scripts/motion_gate.py --output evidence/pre_pcb_board_ready/reproduced_regression}
 if($BoardIdentification){
  & (Join-Path $PSScriptRoot 'pre_pcb_detect.ps1') -OutputPath 'v2/evidence/pre_pcb_board_ready/reproduced_board'
  Write-Output 'Read-only Windows enumeration completed. JTAG detection is separate and requires an already running hw_server.'
 }
}finally{Pop-Location}
