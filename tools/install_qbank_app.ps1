$ErrorActionPreference = 'Stop'
$taskInstall = [IO.Path]::GetFullPath('C:/Users/ANT-PC/OneDrive/Cortex Windows')
$taskBuild = [IO.Path]::GetFullPath('C:/Users/ANT-PC/AppData/Local/Temp/cortex-qbank-cardiology-20261105/dist/Clinical Notes Library')
$taskExe = Join-Path $taskInstall 'Clinical Notes Library.exe'
$taskSourceExe = Join-Path $taskBuild 'Clinical Notes Library.exe'
if (-not (Test-Path -LiteralPath $taskSourceExe)) { throw 'Validated build is missing' }
if ($taskInstall -ne [IO.Path]::GetFullPath('C:/Users/ANT-PC/OneDrive/Cortex Windows')) { throw 'Unexpected install directory' }
Get-Process -Name 'Clinical Notes Library' -ErrorAction SilentlyContinue |
    Where-Object { $_.Path -eq $taskExe } | Stop-Process -Force
$taskBackup = Join-Path $env:LOCALAPPDATA ('Temp/cortex-before-qbank-install-' + [DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $taskBackup | Out-Null
if (Test-Path -LiteralPath $taskExe) { Copy-Item -LiteralPath $taskExe -Destination $taskBackup }
Copy-Item -LiteralPath $taskSourceExe -Destination $taskExe -Force
Copy-Item -LiteralPath (Join-Path $taskBuild '_internal') -Destination $taskInstall -Recurse -Force
$taskExpected = (Get-FileHash -LiteralPath $taskSourceExe -Algorithm SHA256).Hash
$taskInstalled = (Get-FileHash -LiteralPath $taskExe -Algorithm SHA256).Hash
if ($taskExpected -ne $taskInstalled) { throw 'Installed executable verification failed' }
foreach ($taskAsset in @('qbank-explanations.js','qbank-explanations.css','study-rich-text.js','qbank-html-import.js')) {
    $taskSourceAsset = Join-Path $taskBuild ('_internal/assets/vendor/' + $taskAsset)
    $taskTargetAsset = Join-Path $taskInstall ('_internal/assets/vendor/' + $taskAsset)
    if ((Get-FileHash -LiteralPath $taskSourceAsset).Hash -ne (Get-FileHash -LiteralPath $taskTargetAsset).Hash) { throw ('Asset verification failed: ' + $taskAsset) }
}
Start-Process -FilePath $taskExe -WorkingDirectory $taskInstall -WindowStyle Hidden
Write-Output ('Installed and launched: ' + $taskExe)
Write-Output ('Previous executable backup: ' + $taskBackup)
Write-Output ('SHA256: ' + $taskInstalled)
