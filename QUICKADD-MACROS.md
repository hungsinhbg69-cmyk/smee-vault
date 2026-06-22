---
title: "QuickAdd Macros"
slug: "quickadd-macros"
category: automation
tags: [automation, quickadd, capture]
status: active
type: macro-config
created: 2026-06-20
last_updated: 2026-06-20
---

# ⚡ QuickAdd Macros Configuration

> Config cho QuickAdd plugin — các macro capture nhanh.
> Mở Obsidian → Settings → QuickAdd để import macros này.

## Macro 1: Quick Capture vào Inbox

**Action:** Input + Create file from template
```json
{
  "name": "Quick Capture",
  "description": "Capture idea/insight quickly into Inbox",
  "commands": [
    {
      "type": "input",
      "id": "capture-input",
      "options": {
        "title": "💡 Quick Capture",
        "placeholder": "Nhập ý tưởng/nhận định...",
        "multiline": true
      }
    },
    {
      "type": "create-from-template",
      "id": "capture-file",
      "options": {
        "folder": "01-Inbox",
        "template": "_templates/atomic-note.md",
        "filename": "{{date:YYYY-MM-DD}}-{{capture-input|slugify}}"
      }
    },
    {
      "type": "javascript",
      "id": "auto-tag-inbox",
      "options": {
        "code": "// Auto-add #Status/inbox tag\nconst file = app.metadataCache.getFirstLinkpathDest(captureInput, '');\nif (file) {\n  await app.plugins.get('obsidian-dataview').api.executeInlineQuery(\n    `\\`\\`\\`dataview\\nTABLE status FROM \"01-Inbox\"\\n\\`\\`\\``, ''\n  );\n}"
      }
    }
  ]
}
```

## Macro 2: Meeting Note Capture

**Action:** Input + Create file from template
```json
{
  "name": "Meeting Capture",
  "description": "Quick meeting note with action items",
  "commands": [
    {
      "type": "input",
      "id": "meeting-title",
      "options": {"title": "📝 Meeting Title", "placeholder": "Tên cuộc họp..."}
    },
    {
      "type": "create-from-template",
      "id": "meeting-file",
      "options": {
        "folder": "01-Inbox",
        "template": "_templates/meeting-note.md",
        "filename": "{{date:YYYY-MM-DD}}-{{meeting-title|slugify}}"
      }
    },
    {
      "type": "append-to-file",
      "id": "daily-log",
      "options": {
        "file": "02-Daily/{{date:YYYY-MM-DD}}.md",
        "content": "[{{time:H:mm}}] capture: \"{{meeting-title}}\" → 01-Inbox"
      }
    }
  ]
}
```

## Macro 3: Atomic Note from Daily

**Action:** Input + Create atomic note with auto-links
```json
{
  "name": "Promote to Atomic",
  "description": "Create permanent knowledge note from daily idea",
  "commands": [
    {
      "type": "input",
      "id": "note-title",
      "options": {"title": "🔬 Atomic Note Title", "placeholder": "Concept name..."}
    },
    {
      "type": "create-from-template", 
      "id": "atomic-file",
      "options": {
        "folder": "40-Knowledge-Synthesis/Insights",
        "template": "_templates/atomic-note.md",
        "filename": "{{note-title|slugify}}"
      }
    },
    {
      "type": "input-link",
      "id": "related-concept",
      "options": {"title": "🔗 Related concept (optional)"}
    }
  ]
}
```

## Macro 4: Source Capture (Web/Paper)

**Action:** URL input + Literature note template
```json
{
  "name": "Source Capture",
  "description": "Capture web source or paper into literature note",
  "commands": [
    {
      "type": "input",
      "id": "source-url",
      "options": {"title": "🔗 Source URL", "placeholder": "https://..."}
    },
    {
      "type": "input",
      "id": "source-title", 
      "options": {"title": "📚 Title", "placeholder": "Source title..."}
    },
    {
      "type": "create-from-template",
      "id": "lit-note",
      "options": {
        "folder": "30-Resources",
        "template": "_templates/literature-note.md",
        "filename": "{{date:YYYY-MM-DD}}-{{source-title|slugify}}"
      }
    }
  ]
}
```

---

*Created: 2026-06-20 by Smee — Layer 4 Deploy (QuickAdd Macros)*
*To use: Obsidian → Settings → QuickAdd → Add Macro → paste JSON config.*
