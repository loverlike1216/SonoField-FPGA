param([string]$Python = '')
$ErrorActionPreference = 'Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'Use PowerShell 7 (pwsh).' }
$VersionRoot = Split-Path -Parent $PSScriptRoot
if (-not $Python) { $Python = Join-Path (Split-Path -Parent $VersionRoot) '.venv/Scripts/python.exe' }
if (-not (Test-Path -LiteralPath $Python)) { throw 'Pass -Python with the path to a Python environment containing v5/requirements.txt.' }
$Python = (Resolve-Path -LiteralPath $Python).Path
Push-Location -LiteralPath $VersionRoot
try { & $Python -m software.ui.app; if ($LASTEXITCODE) { throw "Motion application exited with code $LASTEXITCODE" } }
finally { Pop-Location }
