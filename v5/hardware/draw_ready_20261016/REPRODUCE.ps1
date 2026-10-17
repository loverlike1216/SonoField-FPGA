param(
 [ValidateSet('Validate','Full')][string]$Mode='Validate',
 [string]$Python='E:\Codex_project\SonoField_v5_MinimalBOM_Audit\20261016_BTX_MultiSolution_Validation\.venv\Scripts\python.exe',
 [switch]$RunVivado,
 [switch]$BuildWorkbook
)
$ErrorActionPreference='Stop'
$auditRoot=[System.IO.Path]::GetFullPath($PSScriptRoot)
if(-not(Test-Path -LiteralPath $Python)){throw 'Set -Python to a Python environment matching requirements-lock.txt.'}
$env:PYTHONUTF8='1';$env:PYTHONIOENCODING='utf-8';$env:PYTHONDONTWRITEBYTECODE='1'
$env:IVERILOG_BIN='C:/iverilog/bin';$env:VIVADO_BIN='D:/Vivado/2025.2/2025.2/Vivado/bin'
function Run-Python([string[]]$ArgumentList){ & $Python @ArgumentList; if($LASTEXITCODE){throw "Python failed: $($ArgumentList -join ' ')"} }
if($Mode -eq 'Validate'){
 Run-Python @('-m','pytest','-q',(Join-Path $auditRoot 'tests'),'--disable-warnings','-p','no:cacheprovider')
 Write-Output 'PASS: saved evidence, current source hashes, census and pin contracts verified. This is not a new circuit simulation or hardware test.'
 exit
}
$replayRoot=Join-Path $auditRoot ('replays/replay-'+[DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss'))
$resolvedReplay=[System.IO.Path]::GetFullPath($replayRoot)
if(-not $resolvedReplay.StartsWith($auditRoot+[System.IO.Path]::DirectorySeparatorChar)){throw 'Replay must stay under this audit directory.'}
if(Test-Path -LiteralPath $resolvedReplay){throw 'Fresh replay path required.'}
New-Item -ItemType Directory -Path $resolvedReplay | Out-Null
foreach($dir in @('scripts','candidate_rtl','inputs','sources','tests')){
 Copy-Item -LiteralPath (Join-Path $auditRoot $dir) -Destination $resolvedReplay -Recurse
}
New-Item -ItemType Directory -Path (Join-Path $resolvedReplay 'results'),(Join-Path $resolvedReplay 'logs'),(Join-Path $resolvedReplay 'results/feature_before') | Out-Null
Get-ChildItem -LiteralPath (Join-Path $auditRoot 'results') -File | Where-Object { $_.Extension -in @('.json','.csv','.txt') } | Copy-Item -Destination (Join-Path $resolvedReplay 'results')
Copy-Item -LiteralPath (Join-Path $auditRoot 'results/feature_before/export.c') -Destination (Join-Path $resolvedReplay 'results/feature_before/export.c')
Copy-Item -LiteralPath (Join-Path $auditRoot '03_AX7020_J10_J11_PINMAP.csv') -Destination $resolvedReplay
Run-Python @((Join-Path $resolvedReplay 'scripts/build_final_database.py'))
Run-Python @((Join-Path $resolvedReplay 'scripts/run_selected_si.py'))
Run-Python @((Join-Path $resolvedReplay 'scripts/run_convergence.py'))
Run-Python @((Join-Path $resolvedReplay 'scripts/run_electrical_checks.py'))
Run-Python @((Join-Path $resolvedReplay 'scripts/run_final_digital.py'),'qualified_final')
Run-Python @((Join-Path $resolvedReplay 'scripts/run_production_profile.py'),'adc_final_fixed')
Run-Python @((Join-Path $resolvedReplay 'scripts/run_capture_physical.py'),'--output',(Join-Path $resolvedReplay 'results/capture_adc_final'))
if($RunVivado){
 $shortDrive=$null
 foreach($candidate in @('W','Y','Z','T','S')){if(-not(Get-PSDrive -Name $candidate -ErrorAction SilentlyContinue)){$shortDrive=$candidate;break}}
 if(-not $shortDrive){throw 'A free short drive letter is required for Vivado Windows path lengths.'}
 & subst.exe ($shortDrive+':') $resolvedReplay
 if($LASTEXITCODE){throw 'Could not create isolated replay drive; no existing mapping overwritten.'}
 $nativeRoot=$shortDrive+':/'
 try {
 & (Join-Path $env:VIVADO_BIN 'vivado.bat') -mode batch -source (Join-Path $nativeRoot 'scripts/build_native.tcl') -tclargs native_replay
 if($LASTEXITCODE){throw 'Native implementation failed; preserve its logs.'}
 'native_replay' | Set-Content -LiteralPath (Join-Path $resolvedReplay 'results/FINAL_NATIVE_LABEL.txt') -Encoding ascii
 $inspect=(Get-Content -LiteralPath (Join-Path $resolvedReplay 'scripts/final_native_inspect.tcl') -Raw).Replace('native21','native_replay')
 Set-Content -LiteralPath (Join-Path $resolvedReplay 'scripts/replay_inspect.tcl') -Value $inspect -Encoding utf8
 & (Join-Path $env:VIVADO_BIN 'vivado.bat') -mode batch -source (Join-Path $nativeRoot 'scripts/replay_inspect.tcl')
 if($LASTEXITCODE){throw 'Native inspection failed.'}
 Run-Python @((Join-Path $resolvedReplay 'scripts/make_delivery.py'))
 Run-Python @((Join-Path $resolvedReplay 'scripts/finish_package.py'))
 } finally { & subst.exe ($shortDrive+':') /D }
}else{
 Write-Output 'Fresh electrical/digital replay completed; no fresh Vivado implementation requested. Do not claim full timing closure for this replay.'
}
if($BuildWorkbook){
 $runtimeBase=Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/node'
 New-Item -ItemType Junction -Path (Join-Path $resolvedReplay 'node_modules') -Target (Join-Path $runtimeBase 'node_modules') | Out-Null
 & (Join-Path $runtimeBase 'bin/node.exe') (Join-Path $resolvedReplay 'scripts/build_workbook.mjs')
 if($LASTEXITCODE){throw 'Workbook generation failed.'}
}
Write-Output "Replay evidence: $resolvedReplay"
