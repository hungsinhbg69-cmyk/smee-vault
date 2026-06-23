// Get yesterday's daily note and extract links
const yesterday = app.workspace.activePaper?.file?.path.replace(/\.md$/, "") || "";
const yDate = moment().subtract(1, "days").format("YYYY-MM-DD");

// Find yesterday's file in vault
let prevFile = null;
for (const f of app.vault.getMarkdownFiles()) {
  if (f.path.includes(yDate) && f.path.startsWith("02-Daily/")) {
    prevFile = f;
    break;
  }
}

if (!prevFile) return "";

// Read file content and extract [[links]]
const content = await app.vault.read(prevFile);
const links = [];
const linkRegex = /\[\[([^\]]+)\]\]/g;
let match;
while ((match = linkRegex.exec(content)) !== null) {
  const text = match[1];
  if (!links.includes(text)) links.push(text);
}

if (links.length === 0) return "";
return "\n" + links.map(l => `- [[${l}]]`).join("\n");
