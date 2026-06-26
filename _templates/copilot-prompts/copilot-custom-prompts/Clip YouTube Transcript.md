---
title: "Clip YouTube Transcript.md"
copilot-command-context-menu-enabled: false
copilot-command-context-menu-order: 1130
copilot-command-last-used: 0
copilot-command-model-key: ""
copilot-command-slash-enabled: true
tags:  [tool, copilot]
slug: clip-youtube-transcriptmd
category: resource
status: active
type: template
created: 2026-06-27
last_updated: 2026-06-27
---

title: "<video title>"
description: "<first 200 chars of description>"
channel: "<channel name>"
url: "<video url>"
duration: "<duration>"
published: <upload date in YYYY-MM-DD format>
thumbnailUrl: "<YouTube thumbnail URL: i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg with https protocol>"
genre:
  - "<genre>"
watched:
---
![<video title>](<video url>)

> [!summary]- Description
> <full video description, preserve line breaks>

## Summary

<Brief 2-3 paragraph summary of the video content>

## Key Takeaways

<List 5-8 key takeaways as bullet points>

## Mindmap

CRITICAL Mermaid mindmap syntax rules - MUST follow exactly:
- Root node format: root(Topic Name) - use round brackets, NO double brackets
- Child nodes: just plain text, no brackets needed
- Do NOT use quotes, parentheses, brackets, or any special characters in text
- Do NOT use icons or emojis
- Keep all node text short and simple - max 3-4 words per node
- Use only letters, numbers, and spaces

Example of CORRECT syntax:
```mermaid
mindmap
  root(Video Main Topic)
    First Theme
      Detail one
      Detail two
    Second Theme
      Detail three
    Third Theme
```

## Notable Quotes

<List 5-10 notable quotes from the transcript. Format each as:>
- [<timestamp>: <quote text>](<video_url>&t=<seconds>s)

Return only the markdown content without any explanations or comments.