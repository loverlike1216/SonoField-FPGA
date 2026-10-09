param([Parameter(Mandatory=$true)][string]$Pattern,[ValidateSet('rg','git')][string]$Engine='rg')
$ErrorActionPreference='Stop'
if ($PSVersionTable.PSVersion.Major -lt 7) { throw 'PowerShell 7 required' }
$repoRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..'))
$scope=@('v5','shared','AI-problem','AI-chat-memory','AI-interaction-memory','README.md','AGENTS.md')
Push-Location -LiteralPath $repoRoot
try {
    if ($Engine -eq 'git') { & git grep -n -I -e $Pattern -- @scope }
    else { & rg -- $Pattern @scope }
    $resultCode=$LASTEXITCODE
} finally { Pop-Location }
exit $resultCode
