[CmdletBinding()]
param(
    [switch]$Apply,
    [string]$VaultPath = "C:\Users\Hung\Desktop\Smee Obsidian\Smee"
)

$ErrorActionPreference = "Stop"
$rootPath = (Resolve-Path -LiteralPath $VaultPath).Path
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$protectedRootNotes = @("AGENTS.md", ".hermes.md")

Write-Output "Vault maintenance mode: $(if ($Apply) { 'APPLY' } else { 'DRY-RUN' })"
Write-Output "Vault: $rootPath"

$unexpectedRootNotes = Get-ChildItem -LiteralPath $rootPath -File -Filter "*.md" |
    Where-Object { $_.Name -notin $protectedRootNotes }
foreach ($file in $unexpectedRootNotes) {
    Write-Warning "Root note requires manual routing; no automatic move: $($file.Name)"
}

$arguments = @{ VaultPath = $rootPath }
if ($Apply) { $arguments.Apply = $true }

try {
    & (Join-Path $scriptRoot "add-frontmatter.ps1") @arguments
    if (-not $?) { throw "add-frontmatter.ps1 reported failure" }
} catch {
    throw "add-frontmatter.ps1 failed: $($_.Exception.Message)"
}

try {
    & (Join-Path $scriptRoot "merge-tags.ps1") @arguments
    if (-not $?) { throw "merge-tags.ps1 reported failure" }
} catch {
    throw "merge-tags.ps1 failed: $($_.Exception.Message)"
}

Write-Output "No files were moved or deleted. Archive, templates, dot-directories, and governance files are excluded."
