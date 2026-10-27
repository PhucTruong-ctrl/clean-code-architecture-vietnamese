#!/usr/bin/env python3
"""Build a translated book selected by its books/<id>/book.py config."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from book_config import ROOT, load_book


def run(book_id: str, action: str | None) -> int:
    try:
        book = load_book(book_id)
    except ValueError as exc:
        print("build: ERROR: %s" % exc, file=sys.stderr)
        return 2

    build_dir = ROOT / book["build_dir"]
    output = ROOT / book["output"]
    distribution = ROOT / book["distribution"]
    if action == "clean":
        shutil.rmtree(build_dir, ignore_errors=True)
        output.unlink(missing_ok=True)
        print("build: cleaned %s" % book_id)
        return 0
    if action is not None:
        print("usage: ./build.sh <book-id> [clean]", file=sys.stderr)
        return 2

    for tool in ("xelatex", "pdfinfo"):
        if shutil.which(tool) is None:
            print("build: ERROR: %s not found in PATH" % tool, file=sys.stderr)
            return 1

    build_dir.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    distribution.parent.mkdir(parents=True, exist_ok=True)
    import md2tex
    if md2tex.main([book_id]) != 0:
        return 1

    layout = book["layout"]
    job = book["job_name"]
    for pass_num in range(1, 4):
        pass_out = build_dir / ("pass%d.out" % pass_num)
        command = [
            "xelatex", "-interaction=nonstopmode", "-halt-on-error",
            "-output-directory=%s" % build_dir,
            "-jobname=%s" % job,
            layout,
        ]
        with pass_out.open("w", encoding="utf-8") as log:
            result = subprocess.run(command, cwd=ROOT, stdout=log,
                                    stderr=subprocess.STDOUT, check=False)
        if result.returncode:
            print("build: ERROR in XeLaTeX pass %d, see %s" %
                  (pass_num, build_dir / (job + ".log")), file=sys.stderr)
            try:
                lines = pass_out.read_text(encoding="utf-8", errors="replace").splitlines()
                print("\n".join(lines[-40:]), file=sys.stderr)
            except OSError:
                pass
            return result.returncode

    generated_pdf = build_dir / (job + ".pdf")
    shutil.copy2(generated_pdf, output)
    info = subprocess.run(["pdfinfo", str(output)], cwd=ROOT, text=True,
                          capture_output=True, check=False)
    if info.returncode:
        print("build: ERROR: pdfinfo failed for %s" % output, file=sys.stderr)
        return info.returncode
    pages = next((line.split(":", 1)[1].strip() for line in info.stdout.splitlines()
                  if line.startswith("Pages:")), "unknown")
    log_path = build_dir / (job + ".log")
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    overfull = log_text.count("Overfull \\hbox")
    underfull = log_text.count("Underfull \\hbox")
    shutil.copy2(output, distribution)
    print("build: OK -> %s (%s pages, %d overfull, %d underfull hboxes)" %
          (distribution.relative_to(ROOT), pages, overfull, underfull))
    status = build_dir / "gen" / "status.txt"
    if status.is_file():
        print("build: source status:")
        for line in status.read_text(encoding="utf-8").splitlines():
            print("  " + line)
    return 0


def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) not in (1, 2):
        print("usage: ./build.sh <book-id> [clean]", file=sys.stderr)
        return 2
    return run(args[0], args[1] if len(args) == 2 else None)


if __name__ == "__main__":
    sys.exit(main())
