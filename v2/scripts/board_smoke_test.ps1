# Preflight is intentionally separate from deployment. Never guess MIO or a BSP.
$ErrorActionPreference='Stop'
$PSNativeCommandUseErrorActionPreference=$true
if($PSVersionTable.PSVersion.Major -lt 7){throw 'Use PowerShell 7'}
$root=Split-Path $PSScriptRoot -Parent
$profile=Get-Content (Join-Path $root 'config/board_smoke_profile.json') -Raw | ConvertFrom-Json
$out=Join-Path $root 'evidence/core_timing_real_loop/board_smoke'
New-Item -ItemType Directory -Force $out | Out-Null
$blockers=@()
if($profile.uart_route -ne 'VERIFIED'){$blockers+='REAL_UART_ROUTE_BLOCKED_BY_MISSING_EVIDENCE'}
foreach($field in @('ps_preset_tcl','ps_platform_xsa','target_bsp')){
 if(-not $profile.$field -or -not (Test-Path -LiteralPath $profile.$field)){$blockers+="MISSING_$field"}
}
$timing=Join-Path $root 'evidence/core_timing_real_loop/summary.json'
if(-not (Test-Path $timing)){$blockers+='GATE_A_NOT_VERIFIED'}
else { $gate=Get-Content $timing -Raw | ConvertFrom-Json
 if($gate.gate_a -ne 'POST_ROUTE_TIMING_PASS'){$blockers+='GATE_A_NOT_PASSED'}
}
@{status='BLOCKED';blockers=$blockers;programmed=$false;uart_opened=$false;scope='Verified prerequisites required before constructing/running PS deployment'} | ConvertTo-Json -Depth 5 | Set-Content (Join-Path $out 'preflight.json') -Encoding utf8
if($blockers.Count){throw ($blockers -join '; ')}
throw 'Platform prerequisites supplied: review them and build the PS/PL wrapper before enabling deployment. This preflight contains no programming command.'
