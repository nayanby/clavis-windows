$ErrorActionPreference='Stop'
$root=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$bundled=Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$python=if (Test-Path -LiteralPath $bundled) {$bundled} else {(Get-Command python).Source}
$env:PYTHONPATH=Join-Path $root 'python_vendor'
& $python (Join-Path $root 'python_app\host.py')
exit $LASTEXITCODE
