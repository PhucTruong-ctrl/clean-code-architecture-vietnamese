"""Load a book's data-only configuration from ``books/<id>/book.py``."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def load_book(book_id: str) -> dict:
    if not BOOK_ID_RE.fullmatch(book_id):
        raise ValueError("invalid book id: %r" % book_id)
    config_path = ROOT / "books" / book_id / "book.py"
    if not config_path.is_file():
        raise ValueError("unknown book %r (expected %s)" % (book_id, config_path))
    spec = importlib.util.spec_from_file_location("book_config_%s" % book_id, config_path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot load book config: %s" % config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    book = getattr(module, "BOOK", None)
    if not isinstance(book, dict) or book.get("id") != book_id:
        raise ValueError("invalid BOOK config in %s" % config_path)
    return book
