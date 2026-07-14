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

function ConvertTo-Slug {
    param([Parameter(Mandatory)][string]$Text)

    $normalized = $Text.Normalize([Text.NormalizationForm]::FormD)
    $builder = [Text.StringBuilder]::new()
    foreach ($character in $normalized.ToCharArray()) {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($character) -ne
            [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$builder.Append($character)
        }
    }
    $slug = $builder.ToString().Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
    $slug = $slug -replace "[^a-z0-9]+", "-"
    return $slug.Trim("-")
}

function Get-NoteDefaults {
    param([Parameter(Mandatory)][string]$RelativePath)

    $root = ($RelativePath -split "/")[0]
    switch ($root) {
        "00-Meta" { return @{ Category = "meta"; Type = "reference"; Status = "reference" } }
        "01-Inbox" { return @{ Category = "inbox"; Type = "atomic-note"; Status = "draft" } }
        "02-Daily" { return @{ Category = "daily"; Type = "daily"; Status = "active" } }
        "10-Projects" { return @{ Category = "project"; Type = "project"; Status = "active" } }
        "20-Areas" { return @{ Category = "area"; Type = "atomic-note"; Status = "active" } }
        "30-Resources" { return @{ Category = "resource"; Type = "literature-note"; Status = "reference" } }
        "40-Knowledge-Synthesis" { return @{ Category = "knowledge"; Type = "atomic-note"; Status = "draft" } }
        "50-Reviews" { return @{ Category = "review"; Type = "review"; Status = "draft" } }
        "70-Outputs" { return @{ Category = "output"; Type = "output"; Status = "output" } }
        "Agent Training" { return @{ Category = "training"; Type = "exercise"; Status = "draft" } }
        default { throw "Unsupported note root: $root" }
    }
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
    if ($content -match "\A---\s*\r?\n") {
        continue
    }

    $defaults = Get-NoteDefaults -RelativePath $relative
    $created = $file.CreationTime.ToString("yyyy-MM-dd")
    $updated = $file.LastWriteTime.ToString("yyyy-MM-dd")
    $title = [IO.Path]::GetFileNameWithoutExtension($file.Name).Replace('"', '\"')
    $slug = ConvertTo-Slug -Text $title
    if ([string]::IsNullOrWhiteSpace($slug)) {
        Write-Warning "Skipped; title cannot produce a safe slug: $relative"
        continue
    }

    $frontmatter = @(
        "---",
        "title: `"$title`"",
        "slug: `"$slug`"",
        "category: $($defaults.Category)",
        "tags: []",
        "status: $($defaults.Status)",
        "type: $($defaults.Type)",
        "created: $created",
        "last_updated: $updated",
        "---",
        ""
    ) -join "`n"

    $changes++
    $mode = if ($Apply) { "APPLY" } else { "DRY-RUN" }
    Write-Output "[$mode] add frontmatter: $relative"
    if ($Apply) {
        [IO.File]::WriteAllText($file.FullName, $frontmatter + $content, $utf8NoBom)
    }
}

Write-Output "Frontmatter additions: $changes. Apply=$Apply"
