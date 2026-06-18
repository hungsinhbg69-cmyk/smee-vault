const fs = require('fs');
const c = fs.readFileSync('C:/Users/Hung/.openclaw/workspace/memory/fb-ref.html', 'utf8');

// Find all data-test-id attributes
const testIds = c.match(/data-test-id="[^"]*"/g) || [];
console.log('Total data-test-id:', testIds.length);
testIds.forEach(id => console.log(id));

console.log('\n---\n');

// Find nav items / endpoints in the HTML
const navPattern = /<div[^>]*data-test-id="nav-item"[^>]*>[\s\S]*?<\/div>/g;
const navItems = c.match(navPattern) || [];
console.log('Nav items found:', navItems.length);
navItems.forEach(item => {
  const text = item.replace(/<[^>]+>/g, '').trim();
  if (text.length > 2 && text.length < 100) {
    console.log('NAV:', text);
  }
});

console.log('\n---\n');

// Find all h2/h3 sections that look like API endpoints
const headingPattern = /<(h[23])[^>]*>([\s\S]*?)<\/\1>/g;
let match;
while ((match = headingPattern.exec(c)) !== null) {
  const tag = match[1];
  const text = match[2].replace(/<[^>]+>/g, '').trim();
  if (text.length > 2 && text.length < 200 && /[^a-zA-Z0-9]/.test(text)) {
    console.log(tag + ':', text);
  }
}
