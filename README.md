# Vietnamese book-translation workspace

This repository contains two independent Vietnamese book translations. Shared build and QA tools live at the root; each book owns its source, Markdown, assets, translation guide, and LaTeX layout under `books/<book-id>/`.

## Workspace layout

```text
books/
  clean-code/
    source.pdf
    translation/vi/
    assets/
    reference/
    tools/
    layout.tex
    translation-guide.md
    book.py
  clean-architecture/
    source.pdf
    source.txt
    translation/vi/
    assets/
    layout.tex
    translation-guide.md
    book.py
tools/
  md2tex.py       shared Markdown-to-LaTeX converter
  build_book.py   generic configured build runner
  qa_check.py     structural checks for one book
build/             generated TeX and XeLaTeX working files
out/               transient build outputs
dist/               retained Vietnamese PDF editions
```

`books/<book-id>/book.py` defines the book's chapters, assets, LaTeX layout, and output path. The shared tools select a book by ID and store generated fragments under `build/<book-id>/`.

## Build and QA

```bash
./build.sh clean-code
./build.sh clean-architecture
./build.sh clean-code clean
./build.sh clean-architecture clean
python3 tools/qa_check.py clean-code
python3 tools/qa_check.py clean-architecture
```

Builds require XeLaTeX, Python 3, and Poppler's `pdfinfo`. The retained editions are `dist/clean-code-vi.pdf` and `dist/clean-architecture-vi.pdf`. `clean` removes generated files under `build/<book-id>/` and `out/`, while leaving retained PDFs in `dist/` untouched. Temporary extraction work stays under the ignored `work/` directory.

## Clean Code

- Original: `books/clean-code/source.pdf`
- Vietnamese Markdown: `books/clean-code/translation/vi/`
- Translation rules: `books/clean-code/translation-guide.md`
- Original text references: `books/clean-code/reference/original-extracts/`
- Figures, openers, and illustrations: `books/clean-code/assets/`
- Existing translated edition: `dist/clean-code-vi.pdf`
- Book-specific extraction utilities: `books/clean-code/tools/`

## Clean Architecture

- Original: `books/clean-architecture/source.pdf`
- Extracted source text: `books/clean-architecture/source.txt`
- Vietnamese Markdown: `books/clean-architecture/translation/vi/`
- Translation rules: `books/clean-architecture/translation-guide.md`
- Book-specific LaTeX layout and configuration: `books/clean-architecture/layout.tex` and `books/clean-architecture/book.py`

Translate and review one chapter at a time against `source.txt` and the PDF. The Clean Architecture translation now includes the front matter, Parts II–VII, Chapters 1–34, and Appendix A. `python3 tools/qa_check.py clean-architecture` reports 34/34 chapter files and 0 problems. Build the complete edition with `./build.sh clean-architecture`.

## Shared translation conventions

Both book guides follow the same workflow: faithful, complete translation; natural Vietnamese; preservation of names, code, figures, tables, numbers, and citations; no added conclusions; and source-based review before moving to the next chapter. Each book keeps its own source materials and generated PDF.
