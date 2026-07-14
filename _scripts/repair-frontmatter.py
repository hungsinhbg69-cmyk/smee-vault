"""Audit and repair Obsidian frontmatter without rewriting note bodies.

Dry-run is the default. Pass --apply explicitly to write changes.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import yaml


CANONICAL_ROOTS = {
    "00-Meta": "meta",
    "01-Inbox": "inbox",
    "02-Daily": "daily",
    "10-Projects": "project",
    "20-Areas": "area",
    "30-Resources": "resource",
    "40-Knowledge-Synthesis": "knowledge",
    "50-Reviews": "review",
    "60-Archive": "archive",
    "70-Outputs": "output",
    "Agent Training": "training",
}
PROTECTED = {
    "00-Meta/Protocol.md",
    "00-Meta/Tag-Taxonomy.md",
    "00-Meta/Vault-Quick-Ref.md",
}
REQUIRED = ("title", "slug", "category", "tags", "status", "type", "created", "last_updated")
STATUS_MAP = {
    "finished": "completed",
    "stable": "reference",
    "active-reference": "reference",
    "active-test": "active",
    "locked": "reference",
    "v1-complete": "completed",
    "completed-not-passed": "completed",
}
SLUG_OVERRIDES = {
    "00-Meta/DASHBOARD.md": "vault-dashboard",
    "40-Knowledge-Synthesis/Insights/vault-master-index.md": "vault-master-index-insight",
    "40-Knowledge-Synthesis/Smee-Content-Template-Framework.md": "smee-content-template-framework-overview",
    "40-Knowledge-Synthesis/Frameworks/quickadd-macros-reference.md": "quickadd-macros-reference",
}
TAG_OVERRIDES = {
    "30-Resources/ngay-xua-co-mot-con-bo-cau-chuyen-ve-su-tam-thuong.md": [
        "psychology", "personal-development", "camilo-cruz", "con-bo", "vietnamese-book"
    ],
    "40-Knowledge-Synthesis/Thuat-Ban-Hang-Brian-Tracy-Phan-Bien-Toan-Dien.md": [
        "sales", "brian-tracy", "sales-funnel", "relationship-selling", "clv-cac"
    ],
    "60-Archive/obsidian-vault-knowledge-base.md": [
        "obsidian", "pkm", "zettelkasten", "para", "workflow"
    ],
    "40-Knowledge-Synthesis/Frameworks/Facebook-Ads-Budgeting-Bidding-Metrics-2026.md": [
        "facebook-ads", "budgeting", "bidding", "metrics", "cbo"
    ],
    "40-Knowledge-Synthesis/Insights/bac-giang-real-estate-poster-insights-june2026.md": [
        "real-estate", "facebook", "bac-giang", "marketing", "social-housing"
    ],
    "40-Knowledge-Synthesis/Insights/marketing-bat-dong-san-mien-bac-noxh-2026.md": [
        "real-estate", "marketing", "social-housing", "northern-vietnam", "facebook-ads"
    ],
}


def read_exact(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_exact(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def slugify(value: str) -> str:
    value = value.replace("Đ", "D").replace("đ", "d")
    value = "".join(
        character
        for character in unicodedata.normalize("NFKD", value)
        if not unicodedata.combining(character)
    )
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value


def canonical_tag(value: object) -> str:
    tag = str(value).strip().strip('"\'').lstrip("#").lower()
    tag = re.sub(r"[\s_]+", "-", tag)
    tag = re.sub(r"-+", "-", tag).strip("-")
    if tag.isdigit():
        tag = f"year/{tag}"
    aliases = {
        "bacgiang": "bac-giang",
        "bacninh": "bac-ninh",
        "fb-api": "facebook-api",
        "fb-graph": "facebook-graph",
    }
    return aliases.get(tag, tag)


def infer_type(relative: str, category: str, title: str) -> str:
    lowered = title.lower()
    if category == "meta":
        return "reference"
    if category == "daily":
        return "daily"
    if category == "project":
        return "project"
    if category == "review":
        return "review"
    if category == "output":
        return "output"
    if category == "training":
        if "nhật ký" in lowered or "log" in lowered:
            return "log"
        if "báo cáo" in lowered or "bao-cao" in relative.lower():
            return "report"
        if "protocol" in lowered or "cầm tay" in lowered:
            return "reference"
        if "evidence" in lowered:
            return "evidence"
        return "exercise"
    if category == "resource":
        return "literature-note"
    return "atomic-note"


def infer_date(relative: str, timestamp: float) -> str:
    matches = re.findall(r"\b(20\d{2}-\d{2}-\d{2})\b", relative)
    if matches:
        return matches[-1]
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def is_template(relative: str) -> bool:
    lowered = relative.lower()
    return "/_templates/" in f"/{lowered}" or "template" in Path(relative).stem.lower()


def make_parseable(frontmatter: str) -> str:
    fixed = re.sub(
        r"(?m)^([A-Za-z_][A-Za-z0-9_-]*):\s*(\{\{[^\n]+\}\})\s*$",
        lambda match: f'{match.group(1)}: "{match.group(2)}"',
        frontmatter,
    )
    fixed = re.sub(r"(?m)^tags:\s*\[project,\s*#status/active\]\s*$", 'tags: [project, "status/active"]', fixed)
    return fixed


def split_note(text: str) -> tuple[str | None, str, str]:
    newline = "\r\n" if "\r\n" in text else "\n"
    match = re.match(r"\A---\s*\r?\n(?P<yaml>[\s\S]*?)\r?\n---(?P<body>[\s\S]*)\Z", text)
    if not match:
        return None, text, newline
    return match.group("yaml"), match.group("body"), newline


def scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    text = str(value)
    if re.fullmatch(r"[a-z0-9][a-z0-9_./-]*", text):
        return text
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}(?: \d{2}:\d{2})?", text):
        return text
    return json.dumps(text, ensure_ascii=False)


def render_field(key: str, value: object) -> list[str]:
    if key == "tags":
        return ["tags: [" + ", ".join(json.dumps(str(item), ensure_ascii=False) for item in value) + "]"]
    return [f"{key}: {scalar(value)}"]


def set_field(frontmatter: str, key: str, value: object, newline: str) -> str:
    lines = re.split(r"\r?\n", frontmatter)
    start = next((index for index, line in enumerate(lines) if re.match(rf"^{re.escape(key)}\s*:", line)), None)
    replacement = render_field(key, value)
    if start is None:
        lines.extend(replacement)
        return newline.join(lines)
    end = start + 1
    while end < len(lines) and (not lines[end] or lines[end][0].isspace()):
        end += 1
    lines[start:end] = replacement
    return newline.join(lines)


def build_frontmatter(data: dict[str, object], newline: str) -> str:
    return newline.join(line for key in REQUIRED for line in render_field(key, data[key]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=r"C:\Users\Hung\Desktop\Smee Obsidian\Smee")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    vault = Path(args.vault).resolve()

    changed_files: list[str] = []
    change_counts: Counter[str] = Counter()
    residual: list[str] = []
    seen_slugs: defaultdict[str, list[str]] = defaultdict(list)

    notes = sorted(
        path
        for path in vault.rglob("*.md")
        if path.relative_to(vault).parts[0] in CANONICAL_ROOTS
    )
    for path in notes:
        relative = path.relative_to(vault).as_posix()
        if relative in PROTECTED:
            continue
        original = read_exact(path)
        frontmatter, body, newline = split_note(original)
        had_frontmatter = frontmatter is not None
        stat = path.stat()

        if frontmatter is None:
            title = path.stem
            category = CANONICAL_ROOTS[relative.split("/")[0]]
            data: dict[str, object] = {
                "title": title,
                "slug": SLUG_OVERRIDES.get(relative, slugify(title)),
                "category": category,
                "tags": [],
                "status": "archived" if category == "archive" else "output" if category == "output" else "draft",
                "type": infer_type(relative, category, title),
                "created": infer_date(relative, stat.st_ctime),
                "last_updated": infer_date(relative, stat.st_mtime),
            }
            frontmatter = build_frontmatter(data, newline)
            change_counts["added_frontmatter"] += 1
        else:
            syntactic_repairs: set[str] = set()
            for date_key in ("created", "last_updated"):
                if re.search(rf"(?m)^{date_key}:\s*\{{\{{[^\n]+\}}\}}\s*$", frontmatter):
                    syntactic_repairs.add(date_key)
            if re.search(r"(?m)^tags:\s*\[project,\s*#status/active\]\s*$", frontmatter):
                syntactic_repairs.add("tags")
            parseable = make_parseable(frontmatter)
            try:
                data = yaml.safe_load(parseable) or {}
                if not isinstance(data, dict):
                    raise TypeError("frontmatter is not a mapping")
            except Exception as error:
                residual.append(f"{relative}: YAML parse failed: {error}")
                continue

            title = str(data.get("title") or path.stem)
            category = CANONICAL_ROOTS[relative.split("/")[0]]
            desired: dict[str, object] = {
                "title": title,
                "slug": SLUG_OVERRIDES.get(relative, str(data.get("slug") or slugify(title))),
                "category": category,
            }

            raw_tags = data.get("tags")
            if raw_tags is None:
                raw_tags = []
            elif isinstance(raw_tags, str):
                raw_tags = [raw_tags]
            elif not isinstance(raw_tags, list):
                raw_tags = [raw_tags]
            normalized_tags: list[str] = []
            for raw_tag in raw_tags:
                tag = canonical_tag(raw_tag)
                if tag and tag not in {"obsidian-cleanup", "auto-added"} and tag not in normalized_tags:
                    normalized_tags.append(tag)
            normalized_tags = TAG_OVERRIDES.get(relative, normalized_tags)
            if len(normalized_tags) > 5:
                residual.append(f"{relative}: {len(normalized_tags)} tags require semantic review")
            desired["tags"] = normalized_tags

            current_status = str(data.get("status") or "draft")
            current_status = STATUS_MAP.get(current_status, current_status)
            if category == "archive":
                current_status = "archived"
            elif category == "output":
                current_status = "output"
            desired["status"] = current_status
            desired["type"] = data.get("type") or infer_type(relative, category, title)

            created = data.get("created")
            if not created or (created == "{{date}}" and not is_template(relative)):
                created = infer_date(relative, stat.st_ctime)
            updated = data.get("last_updated")
            if not updated or (updated == "{{date}}" and not is_template(relative)):
                updated = infer_date(relative, stat.st_mtime)
            desired["created"] = created
            desired["last_updated"] = updated

            for key in REQUIRED:
                if data.get(key) != desired[key] or key in syntactic_repairs:
                    frontmatter = set_field(frontmatter, key, desired[key], newline)
                    change_counts[f"field_{key}"] += 1
                    data[key] = desired[key]

        slug = str(data["slug"])
        seen_slugs[slug].append(relative)
        body_separator = "" if had_frontmatter else newline + newline
        updated_note = f"---{newline}{frontmatter}{newline}---{body_separator}{body}"
        if updated_note != original:
            changed_files.append(relative)
            if args.apply:
                write_exact(path, updated_note)

    duplicates = {slug: paths for slug, paths in seen_slugs.items() if len(paths) > 1}
    for slug, paths in duplicates.items():
        residual.append(f"duplicate slug {slug}: {' | '.join(paths)}")

    result = {
        "mode": "apply" if args.apply else "dry-run",
        "scanned": len(notes),
        "changed": len(changed_files),
        "change_counts": change_counts,
        "changed_files": changed_files,
        "residual": residual,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if residual else 0


if __name__ == "__main__":
    raise SystemExit(main())
