# Tag Merge Script for Obsidian Vault Cleanup
# Run in PowerShell to merge duplicate tags

$vaultPath = "C:\Users\Hung\Desktop\Smee Obsidian\Smee"
$tagMerges = @(
    @{Old="#bac-giang"; New="#bacgiang"},
    @{Old="#BacGiang"; New="#bacgiang"},
    @{Old="#bac-ninh"; New="#bacninh"},
    @{Old="#BacNinh"; New="#bacninh"},
    @{Old="#Area"; New="#area"},
    @{Old="#areas"; New="#area"},
    @{Old="#Project"; New="#project"},
    @{Old="#projects"; New="#project"}
)

Write-Host "Starting tag merge process..." -ForegroundColor Green

foreach ($merge in $tagMerges) {
    $oldTag = $merge.Old
    $newTag = $merge.New
    Write-Host "Merging $oldTag → $newTag" -ForegroundColor Yellow
    
    $mdFiles = Get-ChildItem $vaultPath -Filter "*.md" -Recurse | Where-Object { $_.FullName -notmatch "\\scripts\\" }
    
    foreach ($file in $mdFiles) {
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        
        if ($content -match [regex]::Escape($oldTag)) {
            $newContent = $content -replace [regex]::Escape($oldTag), $newTag
            Set-Content $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
            Write-Host "  Updated: $($file.Name)" -ForegroundColor Cyan
        }
    }
}

Write-Host "Tag merge complete!" -ForegroundColor Green
