param([string]$Destination='C:\Users\ANT-PC\OneDrive\Clavis Windows')
$ErrorActionPreference='Stop'
$source=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\release\python-0.2.5\Clavis'))
$target=[IO.Path]::GetFullPath($Destination)
if ($target -ne 'C:\Users\ANT-PC\OneDrive\Clavis Windows') { throw 'Unexpected install destination' }
if (!(Test-Path -LiteralPath (Join-Path $source 'Clavis.exe'))) { throw 'Python build is missing' }
if (!(Test-Path -LiteralPath (Join-Path $source '_internal\python312.dll'))) { throw 'Python runtime is missing' }
$exe=Join-Path $target 'Clavis.exe'
$running=@(Get-Process -Name Clavis -ErrorAction SilentlyContinue | Where-Object { $_.Path -eq $exe })
foreach ($process in $running) {
    if ($process.MainWindowHandle -ne 0) { [void]$process.CloseMainWindow(); [void]$process.WaitForExit(30000) }
}
$remaining=@(Get-Process -Name Clavis -ErrorAction SilentlyContinue | Where-Object { $_.Path -eq $exe })
if (@($remaining | Where-Object { $_.MainWindowHandle -ne 0 }).Count -gt 0) { throw 'Clavis did not close. No files were replaced.' }
foreach ($process in $remaining) {
    if (Get-Process -Id $process.Id -ErrorAction SilentlyContinue) {
        Stop-Process -Id $process.Id -ErrorAction SilentlyContinue
        [void]$process.WaitForExit(5000)
    }
}
$backup=[IO.Path]::GetFullPath((Join-Path $target ('Data\Backups\Before-Python-'+(Get-Date -Format 'yyyyMMdd-HHmmss'))))
if (!$backup.StartsWith($target+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid backup destination' }
New-Item -ItemType Directory -Path $backup -Force | Out-Null
$library=Join-Path $target 'Data\library.json'
if (Test-Path -LiteralPath $library) { Copy-Item -LiteralPath $library -Destination (Join-Path $backup 'library.json') }
# Preserve the previous executable and runtime as a recoverable local backup.
$legacy=@('Clavis.exe','_internal','resources','locales','README.md','chrome_100_percent.pak','chrome_200_percent.pak','d3dcompiler_47.dll','dxcompiler.dll','electron_wer.dll','ffmpeg.dll','icudtl.dat','LICENSE.electron.txt','LICENSES.chromium.html','resources.pak','snapshot_blob.bin','v8_context_snapshot.bin','vk_swiftshader_icd.json','vk_swiftshader.dll','vulkan-1.dll')
foreach ($entry in $legacy) {
    $old=[IO.Path]::GetFullPath((Join-Path $target $entry))
    if (!$old.StartsWith($target+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid runtime source' }
    if (Test-Path -LiteralPath $old) { Move-Item -LiteralPath $old -Destination (Join-Path $backup $entry) }
}
Copy-Item -LiteralPath (Join-Path $source '_internal') -Destination $target -Recurse
Copy-Item -LiteralPath (Join-Path $source 'Clavis.exe') -Destination $exe
Copy-Item -LiteralPath (Join-Path $source '_internal\README-Python.md') -Destination (Join-Path $target 'README.md')
if ((Get-FileHash -LiteralPath $exe).Hash -ne (Get-FileHash -LiteralPath (Join-Path $source 'Clavis.exe')).Hash) { throw 'Installed executable did not match build' }
[pscustomobject]@{Executable=$exe;Backup=$backup;Data=Join-Path $target 'Data';Version=(Get-Item -LiteralPath $exe).VersionInfo.ProductVersion} | ConvertTo-Json
