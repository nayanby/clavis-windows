$ErrorActionPreference='Stop'
$workspace=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$target='C:\Users\ANT-PC\OneDrive\Clavis Windows'
$exe=Join-Path $target 'Clavis.exe'
$files=@('bundle.js','index.html','pastel.css')
foreach($name in $files){if(!(Test-Path -LiteralPath (Join-Path $workspace ('ui\'+$name)))){throw "Missing UI file: $name"}}
foreach($process in @(Get-Process -Name Clavis -ErrorAction SilentlyContinue | Where-Object {$_.Path -eq $exe})){
    if($process.MainWindowHandle -ne 0){[void]$process.CloseMainWindow();[void]$process.WaitForExit(30000)}
}
if(@(Get-Process -Name Clavis -ErrorAction SilentlyContinue | Where-Object {$_.Path -eq $exe}).Count){throw 'Clavis must close before the UI update.'}
$backup=Join-Path $target ('Data\Backups\UI-'+(Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $backup -Force | Out-Null
foreach($name in $files){
    $source=Join-Path $workspace ('ui\'+$name)
    $installed=Join-Path $target ('_internal\ui\'+$name)
    Copy-Item -LiteralPath $installed -Destination (Join-Path $backup $name)
    Copy-Item -LiteralPath $source -Destination $installed -Force
    $packaged=Join-Path $workspace ('release\python-0.2.5\Clavis\_internal\ui\'+$name)
    Copy-Item -LiteralPath $source -Destination $packaged -Force
    if((Get-FileHash -LiteralPath $source).Hash -ne (Get-FileHash -LiteralPath $installed).Hash){throw "UI verification failed: $name"}
}
[pscustomobject]@{Updated=$files;Backup=$backup;Executable=$exe} | ConvertTo-Json
