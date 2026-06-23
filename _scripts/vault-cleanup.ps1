# Tag consolidation + vault cleanup script
$root = "C:\Users\Hung\Desktop\Smee Obsidian\Smee"
$excludeDirs = @("_cleanup", "_templates", "60-Archive")

$files = Get-ChildItem $root -Recurse -Include *.md | Where-Object {
    foreach ($ex in $excludeDirs) {
        if ($_.FullName.Contains($ex)) { return $false }
    }
    return $true
}

Write-Output "Found $($files.Count) files to scan"

$tagMerges = @{
    "#bac-giang" = "#bacgiang"
    "#bac-ninh" = "#bacninh"
    "#fb-api" = "#facebook-api"
    "#fb-graph" = "#facebook-graph"
}

$totalChanges = 0

foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
        $original = $content
        
        foreach ($oldTag in $tagMerges.Keys) {
            if ($content.Contains($oldTag)) {
                Write-Output "Found '$oldTag' -> $($tagMerges[$oldTag]) in: $($f.Name)"
                $content = $content.Replace($oldTag, $tagMerges[$oldTag])
                $totalChanges++
            }
        }

        if ($content -ne $original) {
            [System.IO.File]::WriteAllText($f.FullName, $content, (New-Object System.Text.UTF8Encoding $false))
        }
    } catch {
        Write-Output "SKIP: $($f.Name) - $_"
    }
}

Write-Output ("Total tag replacements: " + $totalChanges)

# Move remaining root-level markdown files into PARA structure
$rootFiles = Get-ChildItem $root -Include *.md | Where-Object { $_.Name -ne "README.md" }
foreach ($rf in $rootFiles) {
    if (-not (Test-Path "$root\00-Meta\$($rf.Name)" )) {
        Move-Item $rf.FullName "$root\00-Meta\$($rf.Name)" -Force
        Write-Output ("Moved root: " + $rf.Name + " -> 00-Meta/")
    }
}
