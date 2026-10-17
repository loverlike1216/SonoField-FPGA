param(
 [string]$Python='E:\Codex_project\SonoField_v5_MinimalBOM_Audit\20261016_BTX_MultiSolution_Validation\.venv\Scripts\python.exe'
)
$ErrorActionPreference='Stop'
if(-not(Test-Path -LiteralPath $Python)){throw 'Supply an available Python 3.10+ interpreter with -Python.'}
$env:PYTHONIOENCODING='utf-8'
& $Python (Join-Path $PSScriptRoot 'scripts/check_guide_consistency.py')
if($LASTEXITCODE){throw 'Guide consistency failed. Keep the log and do not use an unchecked guide.'}
