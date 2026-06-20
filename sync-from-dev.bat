@echo off
REM 从 dev 模式源目录同步到工作区源码目录（排除 .git）
set DEV_SRC=E:\HanakoData\.hanakopro\plugin-dev-sources\git-save-load-v2
set WORKSPACE=E:\Desktop_E\Plugins\GitQuery\Git_Save-Load

powershell -Command "$exclude='.git'; Get-ChildItem '%DEV_SRC%' -Exclude $exclude | ForEach-Object { Copy-Item $_.FullName '%WORKSPACE%\$($_.Name)' -Recurse -Force }"

echo 已同步：dev → workspace（已排除 .git）
