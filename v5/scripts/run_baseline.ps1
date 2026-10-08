param([string]$Output='evidence/baseline/manual',[string]$Python='')
$ErrorActionPreference='Stop'
$PSNativeCommandUseErrorActionPreference=$true
if($PSVersionTable.PSVersion.Major -lt 7){throw 'PowerShell 7 required'}
$versionRoot=Split-Path $PSScriptRoot -Parent
if(-not $Python){$Python=Join-Path (Split-Path $versionRoot -Parent) '.venv/Scripts/python.exe'}
if(-not(Test-Path -LiteralPath $Python)){throw 'Create a Python environment from requirements-lock.txt or pass -Python'}
foreach($tool in @('VIVADO_BIN','IVERILOG_BIN','CC')){
 if(-not [Environment]::GetEnvironmentVariable($tool)){throw "Declare installed tool path: $tool"}
}
$env:PYTHONUTF8='1';$env:PYTHONIOENCODING='utf-8'
& $Python (Join-Path $PSScriptRoot 'run_baseline.py') --output $Output
