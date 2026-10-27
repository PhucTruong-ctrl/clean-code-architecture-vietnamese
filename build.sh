#!/usr/bin/env bash
# Build out/CleanCode-vi.pdf from the Vietnamese Markdown chapters in vi/.
#
#   ./build.sh            normal build
#   ./build.sh clean      remove generated fragments, aux files and the PDF
#
# Steps: tools/md2tex.py converts Markdown sources into generated LaTeX fragments
# under build/gen/ and writes the front/main/back manifests; XeLaTeX runs three
# passes to resolve the table of contents and page numbers.
set -euo pipefail
cd "$(dirname "$0")"

BUILD_DIR=build/latex
OUT=out/CleanCode-vi.pdf

if [[ "${1:-}" == "clean" ]]; then
  rm -rf "$BUILD_DIR" build/gen build/test
  rm -f "$OUT"
  echo "build: cleaned"
  exit 0
fi

for tool in xelatex python3 pdfinfo; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "build: ERROR: $tool not found in PATH" >&2
    exit 1
  fi
done

mkdir -p build/gen "$BUILD_DIR" out

echo "build: converting Markdown -> LaTeX"
python3 tools/md2tex.py

echo "build: xelatex pass 1/3"
xelatex -interaction=nonstopmode -halt-on-error \
  -output-directory="$BUILD_DIR" -jobname=cleanbook tex/cleanbook.tex \
  >"$BUILD_DIR/pass1.out" 2>&1 || {
    echo "build: ERROR in pass 1, see $BUILD_DIR/cleanbook.log" >&2
    tail -n 40 "$BUILD_DIR/pass1.out" >&2
    exit 1
  }

for pass in 2 3; do
  echo "build: xelatex pass $pass/3 (TOC/page numbers)"
  xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$BUILD_DIR" -jobname=cleanbook tex/cleanbook.tex \
    >"$BUILD_DIR/pass$pass.out" 2>&1 || {
      echo "build: ERROR in pass $pass, see $BUILD_DIR/cleanbook.log" >&2
      tail -n 40 "$BUILD_DIR/pass$pass.out" >&2
      exit 1
    }
done

cp "$BUILD_DIR/cleanbook.pdf" "$OUT"
cp "$OUT" CleanCode-vi.pdf

pages=$(pdfinfo "$OUT" 2>/dev/null | awk '/^Pages:/ {print $2}')
overfull=$(grep -c 'Overfull \\hbox' "$BUILD_DIR/cleanbook.log" || true)
underfull=$(grep -c 'Underfull \\hbox' "$BUILD_DIR/cleanbook.log" || true)
echo "build: OK -> $OUT and CleanCode-vi.pdf (${pages} pages, ${overfull} overfull hboxes, ${underfull} underfull hboxes)"
if [ -s build/gen/status.txt ]; then
  echo "build: source status:"
  sed 's/^/  /' build/gen/status.txt
fi
