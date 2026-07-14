[CmdletBinding()]
param(
    [switch]$Apply,
    [string]$VaultPath = "C:\Users\Hung\Desktop\Smee Obsidian\Smee"
)

$ErrorActionPreference = "Stop"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$allowedRoots = @(
    "00-Meta", "01-Inbox", "02-Daily", "10-Projects", "20-Areas",
    "30-Resources", "40-Knowledge-Synthesis", "50-Reviews", "70-Outputs",
    "Agent Training"
)
$protectedFiles = @(
    "AGENTS.md", ".hermes.md", "00-Meta/Protocol.md",
    "00-Meta/Vault-Quick-Ref.md", "00-Meta/Tag-Taxonomy.md"
)
$tagMerges = @{
    "bacgiang" = "bac-giang"
    "bacninh" = "bac-ninh"
    "areas" = "area"
    "projects" = "project"
    "fb-api" = "facebook-api"
    "fb-graph" = "facebook-graph"
}

function Convert-FrontmatterTags {
    param([Parameter(Mandatory)][string]$Frontmatter)

    $changed = $false
    $lines = [Collections.Generic.List[string]]::new()
    foreach ($line in ($Frontmatter -split "\r?\n", 0, "RegexMatch")) {
        $lines.Add($line)
    }

    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -notmatch "^tags:\s*(.*)$") { continue }

        $tail = $Matches[1]
        if ($tail -match "^\[(.*)\]\s*$") {
            $items = @($Matches[1] -split "," | ForEach-Object { $_.Trim() })
            for ($j = 0; $j -lt $items.Count; $j++) {
                $quote = if ($items[$j] -match '^(["''])[\s\S]*\1$') { $Matches[1] } else { "" }
                $name = $items[$j].Trim('"', "'", " ").TrimStart("#")
                $lookup = $name.ToLowerInvariant()
                if ($tagMerges.ContainsKey($lookup)) {
                    $items[$j] = $quote + $tagMerges[$lookup] + $quote
                    $changed = $true
                }
            }
            $lines[$i] = "tags: [" + ($items -join ", ") + "]"
            break
        }

        for ($j = $i + 1; $j -lt $lines.Count -and $lines[$j] -match "^\s*-\s*(.+?)\s*$"; $j++) {
            $raw = $Matches[1]
            $quote = if ($raw -match '^(["''])[\s\S]*\1$') { $Matches[1] } else { "" }
            $name = $raw.Trim('"', "'", " ").TrimStart("#")
            $lookup = $name.ToLowerInvariant()
            if ($tagMerges.ContainsKey($lookup)) {
                $indent = ($lines[$j] -replace "^(\s*).*", '$1')
                $lines[$j] = "$indent- $quote$($tagMerges[$lookup])$quote"
                $changed = $true
            }
        }
        break
    }

    return @{ Text = ($lines -join "`n"); Changed = $changed }
}

$rootPath = (Resolve-Path -LiteralPath $VaultPath).Path
$notes = foreach ($rootName in $allowedRoots) {
    $candidate = Join-Path $rootPath $rootName
    if (Test-Path -LiteralPath $candidate) {
        Get-ChildItem -LiteralPath $candidate -Recurse -File -Filter "*.md"
    }
}

$changes = 0
foreach ($file in $notes) {
    $relative = $file.FullName.Substring($rootPath.TrimEnd("\").Length).TrimStart("\").Replace("\", "/")
    if ($relative -in $protectedFiles -or $relative -match "(^|/)(?:\.[^/]+|_templates)(?:/|$)") {
        continue
    }

    $content = [IO.File]::ReadAllText($file.FullName, [Text.Encoding]::UTF8)
    $match = [regex]::Match($content, "\A---\s*\r?\n(?<yaml>[\s\S]*?)\r?\n---(?<rest>[\s\S]*)\z")
    if (-not $match.Success) { continue }

    $result = Convert-FrontmatterTags -Frontmatter $match.Groups["yaml"].Value
    if (-not $result.Changed) { continue }

    $changes++
    $mode = if ($Apply) { "APPLY" } else { "DRY-RUN" }
    Write-Output "[$mode] normalize frontmatter tags: $relative"
    if ($Apply) {
        $updated = "---`n$($result.Text)`n---" + $match.Groups["rest"].Value
        [IO.File]::WriteAllText($file.FullName, $updated, $utf8NoBom)
    }
}

Write-Output "Tag frontmatter changes: $changes. Apply=$Apply"
