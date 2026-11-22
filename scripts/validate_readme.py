#!/usr/bin/env python3
"""Validate README.md structure so contributions stay consistent.

Checks:
  1. Every resource line matches: * [**Language**: _Title_](https://url) [`[video]`]
  2. No duplicate URLs.
  3. Every Contents / "Where to start" anchor resolves to a heading.
  4. Every `### Build your own ...` section is listed in Contents.
  5. No empty sections.

Exit code 1 on any error. Warnings (non-HTTPS links) do not fail the run.
Usage: python3 scripts/validate_readme.py [path/to/README.md]
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ENTRY = re.compile(
    r"^\* \[\*\*(?P<lang>[^*]+?)\*\*: _(?P<title>.+?)_\]\((?P<url>https?://[^)\s]+)\)"
    r"(?: `\[video\]`)?(?P<tail>.*)$"
)
# Full-course lines use a different shape: * [**Title**](url): description
COURSE = re.compile(r"^\* \[\*\*(?P<title>[^*]+)\*\*\]\((?P<url>https?://[^)\s]+)\)")
HEADING = re.compile(r"^(#{2,3}) (.+?)\s*$")
ANCHOR_LINK = re.compile(r"\]\(#([^)]+)\)")


def slug(heading: str) -> str:
    """GitHub-style anchor: lowercase, drop punctuation except - and space, spaces to -."""
    text = re.sub(r"[^\w\- ]", "", heading.lower())
    return text.replace(" ", "-")


def main(path: str) -> int:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    warnings: list[str] = []
    urls: list[str] = []

    headings: dict[str, int] = {}
    sections: list[tuple[str, int]] = []  # (heading text, line no) for ### sections
    in_resources = False
    in_courses = False
    section_counts: Counter[str] = Counter()
    current: str | None = None

    for no, line in enumerate(lines, 1):
        m = HEADING.match(line)
        if m:
            headings[slug(m.group(2))] = no
            current = m.group(2)
            in_courses = m.group(2).strip() == "Full Courses"
            if m.group(1) == "###" and m.group(2).startswith("Build your own"):
                sections.append((m.group(2), no))
                in_resources = True
            elif m.group(1) == "##" and not in_courses:
                in_resources = False
            continue

        if not line.startswith("* ["):
            continue

        if in_courses:
            c = COURSE.match(line)
            if not c:
                errors.append(f"L{no}: course line malformed: {line[:80]}")
            else:
                urls.append(c.group("url"))
                section_counts[current] += 1
            continue

        if in_resources:
            e = ENTRY.match(line)
            if not e:
                errors.append(
                    f"L{no}: bad entry format (want `* [**Language**: _Title_](https://url)`): {line[:80]}"
                )
                continue
            url = e.group("url")
            urls.append(url)
            section_counts[current] += 1
            if url.startswith("http://"):
                warnings.append(f"L{no}: non-HTTPS link: {url}")

    # duplicates
    for url, n in Counter(u.rstrip("/") for u in urls).items():
        if n > 1:
            errors.append(f"duplicate URL ({n}x): {url}")

    # anchors resolve
    for no, line in enumerate(lines, 1):
        for a in ANCHOR_LINK.findall(line):
            if a not in headings:
                errors.append(f"L{no}: anchor #{a} has no matching heading")

    # every ### section is in Contents; none empty
    start = next((i for i, l in enumerate(lines) if l.strip() == "## Contents"), None)
    if start is None:
        errors.append("no '## Contents' heading found")
        contents = ""
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() == "---"), len(lines))
        contents = "\n".join(lines[start:end])
    for title, no in sections:
        if f"](#{slug(title)})" not in contents:
            errors.append(f"L{no}: section '{title}' missing from Contents")
        if section_counts[title] == 0:
            errors.append(f"L{no}: section '{title}' has no entries")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(urls)} resources, {len(sections)} sections, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "README.md"))
