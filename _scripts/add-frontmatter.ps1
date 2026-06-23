# Add Frontmatter Script for Obsidian Vault Cleanup
# Run in PowerShell to add missing frontmatter

$vaultPath = "C:\Users\Hung\Desktop\Smee Obsidian\Smee"
$targetDir = "40-Knowledge-Synthesis"

Write-Host "Starting frontmatter standardization..." -ForegroundColor Green

$files = Get-ChildItem "$vaultPath\$targetDir" -Recurse -Filter "*.md" | Where-Object { $_.FullName -notmatch "\\_templates\\" }

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    if ($content -notmatch "^---$") {
        $fileName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
        $slug = $fileName.ToLower() -replace '[^a-z0-9-]', '-'
        
        $frontmatter = @"
---
title: "$([System.IO.Path]::GetFileNameWithoutExtension($file.Name))"
slug: "$slug"
category: $(if ($file.DirectoryName -match "Concepts") {"concepts"} elseif ($file.DirectoryName -match "Frameworks") {"frameworks"} else {"insights"})
tags: [obsidian-cleanup, auto-added]
status: draft
type: $(if ($file.DirectoryName -match "Concepts") {"concept"} elseif ($file.DirectoryName -match "Frameworks") {"framework"} else {"insight"})
created: 2026-06-19
last_updated: 2026-06-19
---

"@
        
        $newContent = $frontmatter + "`n" + $content
        Set-Content $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "  Added frontmatter: $($file.Name)" -ForegroundColor Cyan
    }
}

Write-Host "Frontmatter standardization complete!" -ForegroundColor Green
