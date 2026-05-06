# Quick shortcut to run /dang-bai skill
$ScriptDir = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir
python skills/dang-bai/main.py
