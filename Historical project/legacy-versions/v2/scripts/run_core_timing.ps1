param([ValidateSet('baseline','round1','round2')][string]$Round='baseline')
$ErrorActionPreference='Stop'
$PSNativeCommandUseErrorActionPreference=$true
if($PSVersionTable.PSVersion.Major -lt 7){throw 'Use PowerShell 7'}
if(-not $env:VIVADO_BIN){throw 'Set VIVADO_BIN to Vivado 2025.2 bin'}
$root=Split-Path $PSScriptRoot -Parent
$work=Join-Path $root "build/core_timing/$Round"
$out=Join-Path $root "evidence/core_timing_real_loop/$Round"
New-Item -ItemType Directory -Force $work,$out | Out-Null
Push-Location $work
try {
 & (Join-Path $env:VIVADO_BIN 'vivado.bat') -mode batch -source (Join-Path $PSScriptRoot 'core_timing.tcl') -log (Join-Path $out 'vivado.log') -journal (Join-Path $work 'vivado.jou') -tclargs $Round
 if($LASTEXITCODE){throw 'Vivado failed; preserve logs'}
}finally {Pop-Location}
