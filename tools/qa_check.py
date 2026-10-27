#!/usr/bin/env python3
"""Check structural conventions in one book's Vietnamese Markdown sources."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from book_config import load_book


def check(book_id: str) -> int:
    try:
        book = load_book(book_id)
    except ValueError as exc:
        print("qa: ERROR: %s" % exc, file=sys.stderr)
        return 2

    source_dir = Path(__file__).resolve().parents[1] / book["translation_dir"]
    parts = book["parts"]
    problems = 0

    def warn(path, line, kind, extra=""):
        nonlocal problems
        problems += 1
        print("%s:%d: [%s] %s" % (path.name, line, kind, extra[:110]))

    available = {path.name: path for path in source_dir.glob("*.md")}
    for part in parts:
        path = available.get(part["md"])
        if path is None:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        in_fence = False
        fences = 0
        for line_number, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                fences += 1
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if re.fullmatch(r"\s*\d{1,3}\s*", line):
                warn(path, line_number, "standalone number (PDF folio?)", line)
            if re.match(r"\s*(Chapter|Appendix)\s+[A-Z0-9]", line) and not line.startswith("#"):
                warn(path, line_number, "running head left in prose", line)
            if "—" in line:
                warn(path, line_number, "em dash", line)
        if fences % 2:
            warn(path, 0, "unbalanced code fences", "%d fence lines" % fences)
        if "\t" in text:
            warn(path, 0, "tab characters")

        md_refs = set(re.findall(r"\[\^(\d+)\](?!:)", text))
        md_defs = set(re.findall(r"^\[\^(\d+)\]:", text, re.M))
        if md_refs - md_defs:
            warn(path, 0, "footnote refs without definition",
                 str(sorted(md_refs - md_defs))[:80])
        if md_defs - md_refs:
            warn(path, 0, "footnote definitions without ref",
                 str(sorted(md_defs - md_refs))[:80])

    chapters = [part for part in parts if part["kind"] == "chapter"]
    present = sum(1 for part in chapters
                  if (source_dir / part["md"]).is_file()
                  and (source_dir / part["md"]).stat().st_size > 0)
    missing = [part["md"] for part in chapters
               if not (source_dir / part["md"]).is_file()]
    print("qa: %s has %d/%d chapter files; %d problem(s)" %
          (book_id, present, len(chapters), problems))
    if missing:
        print("qa: missing chapters: " + ", ".join(missing))
    return 1 if problems else 0


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python3 tools/qa_check.py <book-id>", file=sys.stderr)
        return 2
    return check(args[0])


if __name__ == "__main__":
    sys.exit(main())
