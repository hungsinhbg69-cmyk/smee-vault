---
title: "QuickAdd Macros Configuration"
tags: [automation, quickadd]
status: active
type: config-reference
created: 2026-06-20
last_updated: {{date}}
---

# QuickAdd Macro Library

All macros accessible via `Ctrl+Q` (default) or command palette.

## Capture Macros

### New Idea
**Trigger:** `Ctrl+Q > New Idea`
**Action:** Create note in 01-Inbox/ with idea template, auto-tagged #idea + date
**Template:** See _templates/quick-idea.md

### Quick Note
**Trigger:** `Ctrl+Q > Quick Note`
**Action:** Create atomic note in 40-Knowledge-Synthesis/Insights/ with timestamp
**Template:** See _templates/atomic-note.md (already exists)

### Capture Web Clip
**Trigger:** `Ctrl+Q > Web Clip`
**Action:** Open browser, prompt for URL, save to clipboard then paste into new note in 30-Resources/
**Variables:** url, title, author, date_clipped

### Task from Selection
**Trigger:** `Ctrl+Q > New Task (from selection)`
**Action:** Creates task with selected text as description, auto-due tomorrow unless specified
**Variables:** selected_text, due_date

### Meeting Capture
**Trigger:** `Ctrl+Q > New Meeting`
**Action:** Create meeting note in 10-Projects/<project>/ or 02-Daily/ if no project selected
**Template:** See _templates/meeting-note.md (already exists)

## Output Macros

### Generate Flashcards from Note
**Trigger:** `Ctrl+Q > Flashcards from [[note]]`
**Action:** Extract key concepts and create spaced repetition cards with #flashcard tag
**Variables:** source_note, card_count (default 10)

### Export to PDF
**Trigger:** `Ctrl+Q > Export PDF`
**Action:** Use Pandoc to export current note as formatted PDF
**Variables:** output_filename

## Workflow Macros

### Daily Standup Summary
**Trigger:** `Ctrl+Q > Daily Standup`
**Action:** Query tasks, review recent notes, generate daily summary with dataview queries
**Output:** Appends to 02-Daily/ today's note

### Weekly Review Prep
**Trigger:** `Ctrl+Q > Weekly Review`
**Action:** Scan all folders for unprocessed items, list orphaned notes, suggest connections
**Template:** See _templates/weekly-review.md (already exists)

---
*Configured: 2026-06-20 by Smee — Layer 3 (QuickAdd Automation)*
