#!/usr/bin/env python3
"""Convert the Vietnamese Markdown sources in vi/ to LaTeX fragments.

Purpose-built converter, standard library only.  No pandoc, no markdown
package.  Reads the dialect described in work/HUONG-DAN-DICH.md:

  # .. ####      headings
  ```lang         fenced code (java, c, cpp, xml, bash, text)
  > quote         blockquotes (epigraphs, pull quotes)
  - / 1.          lists, nested
  [^n] + [^n]:    footnotes, type A (definition at end of file)
  \u00b9 \u00b2 ...     footnotes, type B (superscript marker, inline definition)
  [Ref]: text     bibliography / citation labels
  ---             horizontal rule
  | tables |

The fragment for each source file is written to build/gen/<stem>.tex and a
couple of manifests (front/main/back) are written for tex/cleanbook.tex.

Run:  python3 build/md2tex.py
Exit status is non-zero only for real syntax errors (e.g. an unclosed code
fence).  Missing chapter files are reported as warnings and skipped so the
book can be rebuilt while translation is still in progress.
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VI = os.path.join(ROOT, "vi")
GEN = os.path.join(ROOT, "build", "gen")
ASSETS_REL = "assets/openers"

# ---------------------------------------------------------------------------
# Book structure.  `num` is the printed chapter number (the LaTeX chapter
# counter is forced to it, so a missing file never renumbers later chapters).
# `opener` is the PDF page of the original chapter-opening illustration, `w`
# is the width *measured from the original PDF*, in points.
# ---------------------------------------------------------------------------
PARTS = [
    dict(md="00-loi-tua-va-gioi-thieu.md", kind="front", section="front",
         toc="true"),
    dict(md="01-ma-sach.md", kind="chapter", num=1, opener=23, w=355.6),
    dict(md="02-ten-co-y-nghia.md", kind="chapter", num=2, opener=38, w=358.2),
    dict(md="03-ham.md", kind="chapter", num=3, opener=52, w=233.1),
    dict(md="04-chu-thich.md", kind="chapter", num=4, opener=74, w=353.9),
    dict(md="05-dinh-dang.md", kind="chapter", num=5, opener=96, w=287.7),
    dict(md="06-doi-tuong-va-cau-truc-du-lieu.md", kind="chapter", num=6,
         opener=114, w=197.8),
    dict(md="07-xu-ly-loi.md", kind="chapter", num=7, opener=123, w=356.3),
    dict(md="08-ranh-gioi.md", kind="chapter", num=8, opener=133, w=350.3),
    dict(md="09-kiem-thu-don-vi.md", kind="chapter", num=9, opener=141, w=251.8),
    dict(md="10-lop.md", kind="chapter", num=10, opener=154, w=356.1),
    dict(md="11-he-thong.md", kind="chapter", num=11, opener=171, w=222.4),
    dict(md="12-thiet-ke-noi-len.md", kind="chapter", num=12, opener=189, w=263.7),
    dict(md="13-dong-thoi.md", kind="chapter", num=13, opener=195, w=223.6),
    dict(md="14-tinh-chinh-tung-buoc.md", kind="chapter", num=14, opener=210,
         w=308.1),
    dict(md="15-ben-trong-junit.md", kind="chapter", num=15, opener=268, w=302.1),
    dict(md="16-tai-cau-truc-serialdate.md", kind="chapter", num=16, opener=283,
         w=359.7),
    dict(md="17-mui-code-va-nguyen-tac.md", kind="chapter", num=17, opener=301,
         w=333.3),
    dict(md="18-phu-luc-a-dong-thoi-2.md", kind="appendix", letter="A"),
    dict(md="19-phu-luc-b-serialdate.md", kind="appendix", letter="B"),
    dict(md="20-phu-luc-c-tham-chieu-cheo.md", kind="appendix", letter="C"),
    dict(md="21-epilogue.md", kind="front", section="back", toc="true"),
    dict(md="22-ve-ban-dich.md", kind="front", section="back", toc="true"),
]

# Figure widths measured from the original PDF (SVG placement matrix of the
# embedded image, points).  "Hình 8-1" has no bitmap in the original: the
# method list was translated as a normal list, so only the caption is printed.
FIG_WIDTH = {
    "1-1": 244.6, "5-1": 339.5, "5-2": 345.3, "8-2": 305.7,
    "11-1": 217.2, "11-2": 285.3, "11-3": 263.7,
    "A-1": 335.7, "A-2": 335.7, "A-3": 143.9,
}
CAPTION_ONLY = {"8-1"}

# Unicode superscript digits -> ASCII digits.
SUP = {
    "\u2070": "0", "\u00b9": "1", "\u00b2": "2", "\u00b3": "3",
    "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
    "\u2078": "8", "\u2079": "9",
}
SUPCLASS = "".join(SUP)

PLACEHOLDER = "\x01"
EXTRA = {"\x03": "[", "\x04": "]", "\x05": "\\\\\n"}
TEX_SPECIALS = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "$": r"\$",
    "&": r"\&",
    "#": r"\#",
    "_": r"\_",
    "%": r"\%",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "|": r"\textbar{}",
    "<": r"\textless{}",
    ">": r"\textgreater{}",
}


class ConvertError(Exception):
    pass


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def strip_sup(run: str) -> str:
    return "".join(SUP.get(ch, "") for ch in run)


def join_lines(lines) -> str:
    return " ".join(ln.strip() for ln in lines if ln.strip())


def tex_escape(text: str) -> str:
    out = []
    n = len(text)
    for i, ch in enumerate(text):
        if ch in EXTRA:
            out.append(EXTRA[ch])
        elif ch in TEX_SPECIALS:
            out.append(TEX_SPECIALS[ch])
            # plain-text identifiers (HTTP_DATE_REGEXP) need a break point
            if ch == "_":
                out.append("\\allowbreak{}")
        else:
            out.append(ch)
            if ch == "." and 0 < i < n - 1:
                before, after = text[i - 1], text[i + 1]
                if before.isalnum() and (after.isalnum() or after.isupper()):
                    out.append("\\allowbreak{}")
    return "".join(out)


# ---------------------------------------------------------------------------
# Inline markdown -> LaTeX
# ---------------------------------------------------------------------------

class Inline:
    """Inline formatter.  Keeps a per-instance table of protected fragments
    (code spans, footnote commands, link targets) so escaping never touches
    them."""

    def __init__(self, footnotes, warn):
        self.footnotes = footnotes          # number -> LaTeX body
        self.warn = warn
        self.used = set()
        self.buf = []

    # -- placeholders ------------------------------------------------------
    def _hold(self, latex: str) -> str:
        self.buf.append(latex)
        return "\x02%d\x02" % (len(self.buf) - 1)

    def _restore(self, text: str) -> str:
        def repl(m):
            return self.buf[int(m.group(1))]
        return re.sub("\x02(\\d+)\x02", repl, text)

    # -- code spans --------------------------------------------------------
    # Characters after which an inline code span may break when it does not
    # fit the measure (long identifiers and API names).
    _CODE_BREAKS = set(" /._-,()[]{}:;<>=")

    def _code_span(self, body: str) -> str:
        out = []
        run = 0
        for ch in body:
            if ch == " ":
                out.append("\\ ")
                run = 0
                continue
            out.append(TEX_SPECIALS.get(ch, ch))
            run += 1
            if ch in self._CODE_BREAKS or run >= 8:
                out.append("\\allowbreak{}")
                run = 0
        return self._hold(
            r"{\fontsize{9}{10.8}\selectfont\ttfamily %s}" % "".join(out))

    # -- public ------------------------------------------------------------
    def convert(self, text: str) -> str:
        # Markdown escapes used by the translators: \[ and \]
        text = text.replace("\\[", "\x03").replace("\\]", "\x04")

        # 1. code spans
        def code(m):
            return self._code_span(m.group(1))
        text = re.sub(r"`([^`\n]+)`", code, text)

        # 2. math: $$...$$ (display) and $...$ (inline)
        def mathdisplay(m):
            return self._hold("\\[%s\\]" % m.group(1).strip())
        text = re.sub(r"\$\$(.+?)\$\$", mathdisplay, text, flags=re.S)

        def mathrun(m):
            body = m.group(1).strip()
            return self._hold("$%s$" % body)
        text = re.sub(r"(?<!\\)\$([^$\n]+?)\$", mathrun, text)

        # 3. footnotes: [^n]
        def fn(m):
            num = int(m.group(1))
            return self._hold(self._footnote(num))
        text = re.sub(r"\[\^(\d+)\]", fn, text)

        # 4. superscript footnote markers (type B)
        def supfn(m):
            run = m.group(1)
            num = int(strip_sup(run))
            if num in self.footnotes:
                return self._hold(self._footnote(num))
            self.warn("footnote marker \u00b9...%s has no definition" %
                      strip_sup(run))
            return self._hold(r"\textsuperscript{%d}" % num)
        text = re.sub("([%s]+)" % SUPCLASS, supfn, text)

        # 5. exponents written with ** or ^: N!**T, 6^3
        def exp(m):
            left, op, right = m.group(1), m.group(2), m.group(3)
            return self._hold("%s\\textsuperscript{%s}" %
                              (tex_escape(left), tex_escape(right)))
        text = re.sub(r"([A-Za-z0-9!)]+)(\*\*|\^)([A-Za-z0-9]+)", exp, text)

        # 5b. bare URLs -> \url{} so xurl can break them at any character
        def url(m):
            raw = m.group(0)
            trail = ""
            while raw and raw[-1] in ".,;:":
                trail = raw[-1] + trail
                raw = raw[:-1]
            return self._hold(r"\url{%s}" % raw) + trail
        text = re.sub(r"https?://[^\s\"<>\x00-\x1f]+", url, text)

        # 6. inline links and images
        def link(m):
            label, url = m.group(1), m.group(2)
            return self._hold(r"%s\\footnote{\\texttt{%s}}" %
                              (self.convert(label), tex_escape(url)))
        text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", link, text)

        def image(m):
            alt = m.group(1)
            self.warn("inline image ignored: %s" % alt)
            return self._hold(tex_escape(alt))
        text = re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", image, text)

        # 7. straight double quotes -> Vietnamese typographic quotes
        def dq(m):
            return "\u201c%s\u201d" % m.group(1)
        text = re.sub(r'"([^"\n]{1,400})"', dq, text)

        # 8. escape everything that is left
        text = tex_escape(text)

        # 9. emphasis (markdown flanking rules, so `N * T` stays literal)
        text = re.sub(r"(?<!\*)\*\*(?![\s*])(.+?)(?<![\s*])\*\*(?!\*)",
                      r"\\textbf{\1}", text)
        text = re.sub(r"(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])",
                      r"\\emph{\1}", text)
        # 10. a literal ellipsis
        text = text.replace("...", r"\ldots{}")

        return self._restore(text)

    @staticmethod
    def strip_footnotes(text: str) -> str:
        """Remove footnote markers: used for running heads and TOC titles."""
        text = re.sub(r"\[\^\d+\]", "", text)
        return re.sub("[%s]+" % SUPCLASS, "", text)

    def _footnote(self, num: int) -> str:
        body = self.footnotes.get(num)
        if body is None:
            self.warn("footnote [^%d] has no definition" % num)
            return r"\textsuperscript{%d}" % num
        if num in self.used:
            # Duplicate reference: keep the content, let LaTeX number it again.
            self.warn("footnote %d referenced more than once" % num)
        self.used.add(num)
        return r"\footnote{%s}" % self.convert(body)


# ---------------------------------------------------------------------------
# Footnote extraction
# ---------------------------------------------------------------------------

def extract_footnotes(lines):
    """Return (cleaned_lines, footnotes, warnings).

    Handles both footnote conventions in the sources.  Definitions are
    removed from the body; markers are replaced later by the inline
    formatter.
    """
    footnotes = {}
    warnings = []
    out = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s{0,3}```", line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence:
            out.append(line)
            i += 1
            continue

        # type A: [^n]: definition (may continue on indented lines)
        m = re.match(r"^\[\^(\d+)\]:\s*(.*)$", line)
        if m:
            num = int(m.group(1))
            body = [m.group(2)]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    break
                if nxt.startswith("  ") or nxt.startswith("\t"):
                    body.append(nxt.strip())
                    i += 1
                    continue
                break
            text = "\x05".join(x.strip() for x in body if x.strip())
            if num in footnotes:
                warnings.append("duplicate footnote definition %d" % num)
            footnotes[num] = text
            continue

        # type B: superscript run starts the line -> inline footnote definition
        m = re.match(r"^([%s]+)\.?\s*(.*)$" % SUPCLASS, line)
        if m:
            num = int(strip_sup(m.group(1)))
            body = [m.group(2)]
            i += 1
            # swallow an indented continuation if there is one
            while i < len(lines) and lines[i].strip() and (
                    lines[i].startswith("  ") or lines[i].startswith("\t")):
                body.append(lines[i].strip())
                i += 1
            text = "\x05".join(x.strip() for x in body if x.strip())
            if num in footnotes:
                warnings.append("duplicate footnote definition %d" % num)
            footnotes[num] = text
            continue

        out.append(line)
        i += 1
    return out, footnotes, warnings


# ---------------------------------------------------------------------------
# Block parser
# ---------------------------------------------------------------------------

class Block:
    __slots__ = ("kind", "level", "lines", "extra")

    def __init__(self, kind, lines=None, level=0, extra=None):
        self.kind = kind
        self.lines = lines or []
        self.level = level
        self.extra = extra or {}

    def __repr__(self):
        return "<%s %r>" % (self.kind, self.lines[:2])


LIST_RE = re.compile(r"^(\s*)([-*+]|(\d+)\.)\s+(.*)$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^(\s{0,3})```\s*([A-Za-z0-9_+-]*)\s*$")
HR_RE = re.compile(r"^\s*([-*_])\s*(?:\1\s*){2,}$")
BOLD_LINE_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
CAPTION_RE = re.compile(r"^(Đoạn mã|Hình|Bảng)\b")
BIB_RE = re.compile(r"^\[([^\]]+)\]:\s*(.*)$")


def list_item_match(line):
    m = LIST_RE.match(line)
    if not m:
        return None
    indent = len(m.group(1).expandtabs(4))
    return dict(indent=indent, ordered=bool(m.group(3)),
                text=m.group(4), space=line)


def is_block_start(line, in_paragraph=True):
    if not line.strip():
        return True
    if HEAD_RE.match(line) or FENCE_RE.match(line) or HR_RE.match(line):
        return True
    if line.lstrip().startswith(">"):
        return True
    if line.lstrip().startswith("|"):
        return True
    if LIST_RE.match(line):
        return True
    if in_paragraph and BIB_RE.match(line):
        return True
    return False


def parse_blocks(lines):
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        m = FENCE_RE.match(line)
        if m:
            lang = m.group(2)
            body = []
            i += 1
            closed = False
            while i < n:
                if re.match(r"^\s{0,3}```\s*$", lines[i]):
                    closed = True
                    i += 1
                    break
                body.append(lines[i])
                i += 1
            if not closed:
                raise ConvertError("unclosed code fence")
            blk = Block("code", body, extra={"lang": lang})
            # A caption paragraph directly before the fence?
            if blocks and blocks[-1].kind == "para" and all(
                    BOLD_LINE_RE.match(x) for x in blocks[-1].lines):
                cap = blocks.pop()
                blk.extra["caption"] = [
                    BOLD_LINE_RE.match(x).group(1).strip()
                    for x in cap.lines]
            blocks.append(blk)
            continue

        m = HEAD_RE.match(line)
        if m:
            blocks.append(Block("heading", [m.group(2)], level=len(m.group(1))))
            i += 1
            continue

        if HR_RE.match(line):
            blocks.append(Block("hr"))
            i += 1
            continue

        if line.lstrip().startswith(">"):
            qlines = []
            while i < n and lines[i].lstrip().startswith(">"):
                q = re.sub(r"^\s*>\s?", "", lines[i])
                qlines.append(q)
                i += 1
            blocks.append(Block("quote", qlines))
            continue

        if line.lstrip().startswith("|"):
            tbl = []
            while i < n and lines[i].lstrip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            blocks.append(Block("table", tbl))
            continue

        li = list_item_match(line)
        if li:
            items, i = parse_list(lines, i)
            blocks.append(Block("list", extra={"items": items,
                                               "ordered": li["ordered"]}))
            continue

        # display math: $$ ... $$ (single line or a block)
        if line.lstrip().startswith("$$"):
            if line.count("$$") >= 2:
                blocks.append(Block("math", [line]))
                i += 1
                continue
            math = [line]
            i += 1
            while i < n and "$$" not in lines[i]:
                math.append(lines[i])
                i += 1
            if i < n:
                math.append(lines[i])
                i += 1
            blocks.append(Block("math", math))
            continue

        # paragraph
        para = [line]
        i += 1
        while i < n and lines[i].strip():
            nxt = lines[i]
            if HEAD_RE.match(nxt) or FENCE_RE.match(nxt) or HR_RE.match(nxt):
                break
            if nxt.lstrip().startswith(">"):
                break
            if list_item_match(nxt):
                break
            if nxt.lstrip().startswith("|"):
                break
            if nxt.startswith("    "):
                # indented continuation of the paragraph, keep it
                para.append(nxt)
                i += 1
                continue
            para.append(nxt)
            i += 1
        fig = re.match(r"^\*\*Hình\s+([0-9]+-[0-9]+|[A-Z]-[0-9]+)\*\*", para[0])
        if fig:
            blocks.append(Block("figure", para, extra={"num": fig.group(1)}))
        else:
            blocks.append(Block("para", para))
    return blocks


def parse_list(lines, i):
    """Parse one list starting at lines[i]; returns (items, next_index).

    Each item is a list of raw lines (already de-indented by two spaces) that
    can be fed back into parse_blocks().
    """
    first = list_item_match(lines[i])
    base = first["indent"]
    ordered = first["ordered"]
    items = []
    n = len(lines)
    while i < n:
        m = list_item_match(lines[i])
        if not m or m["indent"] != base or m["ordered"] != ordered:
            break
        cur = [m["text"]]
        i += 1
        while i < n:
            ln = lines[i]
            if not ln.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                if j < n:
                    nm = list_item_match(lines[j])
                    if nm and nm["indent"] > base:
                        cur.append("")
                        i = j
                        continue
                    if nm and nm["indent"] == base:
                        i = j
                        break
                    if len(lines[j]) - len(lines[j].lstrip()) > base:
                        cur.append("")
                        i = j
                        continue
                break
            nm = list_item_match(ln)
            if nm and nm["indent"] <= base:
                break
            indent = len(ln) - len(ln.lstrip())
            if indent > base:
                # nested list or indented continuation: keep two-space shift
                cur.append(ln[base + 2:] if len(ln) > base + 2 else ln.lstrip())
                i += 1
                continue
            # lazy continuation of the item text
            cur.append(ln.strip())
            i += 1
        items.append(cur)
    else:
        pass
    return items, i


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------

class Renderer:
    def __init__(self, inline: Inline, warn):
        self.inline = inline
        self.warn = warn

    def blocks(self, blocks, ctx=None):
        ctx = dict(ctx or {})
        out = []
        prev = None
        for blk in blocks:
            out.append(self.block(blk, ctx, prev))
            if blk.kind not in ("hr",):
                prev = blk
        return "".join(x for x in out if x)

    def block(self, blk, ctx, prev=None):
        kind = blk.kind
        if kind == "heading":
            return self._heading(blk, ctx)
        if kind == "para":
            text = join_lines(blk.lines)
            latex = self.inline.convert(text)
            noindent = prev is None or prev.kind in (
                "heading", "code", "quote", "list", "hr", "table")
            lead = "\\noindent " if noindent else ""
            if ctx.get("quote"):
                return "%s%s\\par\n" % (lead, latex)
            return "%s%s\\par\n" % (lead, latex)
        if kind == "code":
            return self._code(blk, ctx)
        if kind == "quote":
            return self._quote(blk, ctx)
        if kind == "list":
            return self._list(blk, ctx)
        if kind == "hr":
            return ("\\par\\addvspace{10pt}\\noindent\\hfill"
                    "\\rule{72pt}{0.4pt}\\hfill\\par\\addvspace{10pt}\n")
        if kind == "table":
            return self._table(blk, ctx)
        if kind == "math":
            body = " ".join(x.strip() for x in blk.lines)
            body = body.strip().strip("$").strip()
            return "\\par\\addvspace{6pt}\\[%s\\]\\addvspace{6pt}\n" % body
        if kind == "figure":
            return self._figure(blk, ctx)
        raise ConvertError("unknown block %r" % kind)

    # -- headings ----------------------------------------------------------
    def _heading(self, blk, ctx):
        # Chapter level headings are handled by the caller (Converter); this
        # handles ## and deeper inside a chapter.
        level = blk.level
        raw = blk.lines[0]
        title = self.inline.convert(raw)
        toc = self.inline.convert(self.inline.strip_footnotes(raw))
        if level == 2:
            return "\\ccsection{%s}{%s}\n" % (toc, title)
        if level == 3:
            return "\\ccsubsection{%s}{%s}\n" % (toc, title)
        if level == 4:
            return "\\ccsubsubsection{%s}{%s}\n" % (toc, title)
        return "\\ccparagraph{%s}\n" % title

    # -- figures -----------------------------------------------------------
    _FIG_RE = re.compile(r"^\*\*Hình\s+([0-9]+-[0-9]+|[A-Z]-[0-9]+)\*\*")

    def _figure(self, blk, ctx):
        num = blk.extra["num"]
        rest = list(blk.lines)
        rest[0] = self._FIG_RE.sub("", rest[0], count=1).strip()
        title_lines = [x.strip() for x in rest if x.strip()]
        title = " ".join(title_lines)
        title_tex = self.inline.convert(title)
        out = ["\\par\\addvspace{10pt}\n\\begin{ccfigure}\n"]
        if num in CAPTION_ONLY:
            pass
        elif num in FIG_WIDTH:
            out.append("\\includegraphics[width=%.1fpt]{%s/fig-%s.png}\n"
                       % (FIG_WIDTH[num], ASSETS_REL.replace("openers",
                                                             "figures"),
                          num))
        else:
            self.warn("no image or width for Hình %s (caption only)" % num)
        out.append("\\par\\addvspace{2pt}\n"
                   "{\\centering\\fontsize{10}{12}\\selectfont\n"
                   "\\textbf{Hình %s}\\par" % num)
        if title_tex:
            out.append("\\vspace{1pt}{\\itshape %s}\\par" % title_tex)
        out.append("}\n")
        out.append("\\end{ccfigure}\n\\addvspace{10pt}\n")
        return "".join(out)

    # -- code --------------------------------------------------------------
    def _code(self, blk, ctx):
        body = "\n".join(blk.lines)
        caption = blk.extra.get("caption") or []
        if caption:
            cap_tex = "\\\\\n".join(
                "\\textbf{%s}" % self.inline.convert(c) for c in caption)
            head = ("{\\fontsize{10}{12}\\selectfont\\bfseries %s\\par}\n"
                    "\\vspace{2pt}\\hrule height 0.5pt\\vspace{5pt}\n"
                    % cap_tex)
        else:
            head = ""
        return (
            "\\par\\addvspace{6pt}\n"
            "\\begin{cccode}\n"
            "%s"
            "\\begin{Verbatim}[breaklines=true,breakanywhere=true,"
            "breakindent=18pt,breakautoindent=false,breaksymbolleft={},breaksymbolright={},"
            "fontsize=\\fontsize{7.2}{9}\\selectfont,"
            "xleftmargin=10pt]\n"
            "%s\n"
            "\\end{Verbatim}\n"
            "\\end{cccode}\n"
            "\\addvspace{8pt}\n" % (head, body))

    # -- quotes ------------------------------------------------------------
    def _quote(self, blk, ctx):
        lines = list(blk.lines)
        # trim empty leading/trailing lines
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        if ctx.get("epigraph"):
            return ""  # handled by Converter
        if not lines:
            return ""
        inner_blocks = parse_blocks(lines)
        inner = self.blocks(inner_blocks, dict(ctx, quote=True))
        return ("\\begin{ccblockquote}\n%s\\end{ccblockquote}\n" % inner)

    # -- lists -------------------------------------------------------------
    REF_RE = re.compile(r"^\*\*([A-Z]\d+)\*\*:\s*(.+)$")

    def _is_ref_list(self, items):
        if not items:
            return False
        for item in items:
            if len(item) != 1 or not self.REF_RE.match(item[0].strip()):
                return False
        return True

    def _ref_list(self, items):
        out = []
        for item in items:
            m = self.REF_RE.match(item[0].strip())
            out.append("\\ccrefitem{%s}{%s}\n"
                       % (m.group(1), self.inline.convert(m.group(2))))
        return "".join(out)

    def _list(self, blk, ctx):
        items = blk.extra["items"]
        if self._is_ref_list(items):
            return self._ref_list(items)
        env = "enumerate" if blk.extra["ordered"] else "itemize"
        out = ["\\begin{%s}\n" % env]
        for item in items:
            inner_blocks = parse_blocks(item)
            inner = self.blocks(inner_blocks, dict(ctx, quote=ctx.get("quote")))
            inner = inner.strip()
            # inline the first paragraph to keep list items tight
            out.append("\\item %s\n" % inner)
        out.append("\\end{%s}\n" % env)
        return "".join(out)

    # -- tables ------------------------------------------------------------
    def _table(self, blk, ctx):
        rows = []
        for line in blk.lines:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
        if len(rows) >= 2 and re.match(r"^:?-{2,}", rows[1][0] or ""):
            header, rows = rows[0], rows[2:]
        else:
            header, rows = rows[0], rows[1:]
        ncols = max(len(r) for r in rows + [header])
        if ncols >= 2:
            spec = "@{}l" + "X" * (ncols - 1) + "@{}"
        else:
            spec = "@{}X@{}"
        out = ["\\par\\addvspace{8pt}\\noindent\n"
               "{\\footnotesize\n"
               "\\renewcommand{\\arraystretch}{1.2}\n"
               "\\begin{tabularx}{\\dimexpr\\linewidth-2pt\\relax}{%s}\n"
               "\\hline\n" % spec]
        out.append(" & ".join(self.inline.convert(c)
                              for c in header) + " \\\\\n\\hline\n")
        for r in rows:
            r = r + [""] * (ncols - len(r))
            out.append(" & ".join(self.inline.convert(c) for c in r) +
                       " \\\\\n")
        out.append("\\hline\n\\end{tabularx}}\n"
                   "\\addvspace{8pt}\n")
        return "".join(out)

    # -- output ------------------------------------------------------------
    def render(self, blocks):
        return self.blocks(blocks)


# ---------------------------------------------------------------------------
# Per-file conversion
# ---------------------------------------------------------------------------

class Converter:
    def __init__(self, part):
        self.part = part
        self.warnings = []

    def warn(self, msg):
        self.warnings.append(msg)

    def convert(self, text):
        path = os.path.join(VI, self.part["md"])
        lines = text.splitlines()
        lines, footnotes, fw = extract_footnotes(lines)
        self.warnings.extend(fw)
        blocks = parse_blocks(lines)

        # Strip leading blank blocks
        while blocks and blocks[0].kind == "para" and not join_lines(
                blocks[0].lines):
            blocks.pop(0)

        blocks = self._merge_figure_titles(blocks)

        inline = Inline(footnotes, self.warn)
        renderer = Renderer(inline, self.warn)
        kind = self.part["kind"]
        out = []

        if kind == "front":
            out.append(self._front_matter(blocks, inline, renderer))
        elif kind == "chapter":
            out.append(self._chapter(blocks, inline, renderer))
        elif kind == "appendix":
            out.append(self._appendix(blocks, inline, renderer))
        else:
            raise ConvertError("unknown part kind %r" % kind)

        # Whatever footnotes were defined but never referenced: report them.
        unused = set(footnotes) - inline.used
        if unused:
            self.warnings.append(
                "footnote definitions never referenced: %s"
                % ", ".join(str(x) for x in sorted(unused)))

        body = "".join(out)
        head = "%% %s -- generated by build/md2tex.py, do not edit\n" % \
            self.part["md"]
        return head + body

    @staticmethod
    def _merge_figure_titles(blocks):
        """Chapters put the figure title either on the caption line or in the
        paragraph right after it (sometimes separated by a blank line)."""
        out = []
        i = 0
        while i < len(blocks):
            blk = blocks[i]
            if blk.kind == "figure" and i + 1 < len(blocks):
                nxt = blocks[i + 1]
                if nxt.kind == "para":
                    text = join_lines(nxt.lines)
                    if 0 < len(text) <= 90 and "\n" not in text:
                        blk.lines = blk.lines + nxt.lines
                        i += 1
            out.append(blk)
            i += 1
        return out

    # -- front matter parts (Foreword, Preface, Epilogue, ...) -------------
    def _front_matter(self, blocks, inline, renderer):
        out = []
        current = []          # blocks collected for the current chapter

        def flush():
            if current:
                out.append(renderer.blocks(current))
                current.clear()

        i = 0
        n = len(blocks)
        while i < n:
            blk = blocks[i]
            if blk.kind == "heading" and blk.level == 1:
                flush()
                title = inline.convert(blk.lines[0])
                out.append("\\ccfrontchapter{%s}\n" % title)
                i += 1
                # optional byline/epigraph blockquotes
                if i < n and blocks[i].kind == "quote":
                    body, i = self._author_block(blocks, i)
                    if body is not None:
                        out.append(body)
                    if i < n and blocks[i].kind == "quote":
                        out.append(self._epigraph(blocks[i], inline))
                        i += 1
                continue
            current.append(blk)
            i += 1
        flush()
        return "".join(out)

    # -- numbered chapters -------------------------------------------------
    def _chapter(self, blocks, inline, renderer):
        out = []
        if not blocks or blocks[0].kind != "heading" or blocks[0].level != 1:
            raise ConvertError("chapter file must start with a level-1 heading")
        heading = blocks[0].lines[0]
        title = self._chapter_title(heading)
        num = self.part["num"]
        out.append("\\setcounter{chapter}{%d}\n" % (num - 1))
        out.append("\\ccchapter{%s}\n" % inline.convert(title))

        i = 1
        # byline (original: "by <author>", right aligned under the title)
        if i < len(blocks) and blocks[i].kind == "quote":
            body, j = self._author_block(blocks, i)
            if body is not None:
                out.append(body)
                i = j
        # opener illustration
        if self.part.get("opener"):
            img = "%s/opener-%d.png" % (ASSETS_REL, self.part["opener"])
            out.append("\\ccopenerimage{%s}{%.1fpt}\n" %
                       (img, self.part["w"]))
        # epigraph, when the translator put one directly under the title
        if i < len(blocks) and blocks[i].kind == "quote":
            # Chapter 1's opening paragraph is printed left aligned across the
            # full measure at the bottom of the opener page, not right aligned
            # like the epigraphs of chapters 4, 11 and 13.
            out.append(self._epigraph(blocks[i], inline,
                                      left=(num == 1)))
            i += 1
        out.append(renderer.blocks(blocks[i:]))
        return "".join(out)

    # -- appendices --------------------------------------------------------
    def _appendix(self, blocks, inline, renderer):
        out = []
        if not blocks or blocks[0].kind != "heading":
            raise ConvertError("appendix file must start with a heading")
        heading = blocks[0].lines[0]
        title = self._chapter_title(heading, appendix=True)
        letter = self.part["letter"]
        idx = "ABC".index(letter) + 1
        out.append("\\ccappendixsetup{%d}\n" % idx)
        out.append("\\ccappendix{%s}\n" % inline.convert(title))
        i = 1
        has_author = False
        if i < len(blocks) and blocks[i].kind == "quote":
            body, j = self._author_block(blocks, i)
            if body is not None:
                out.append(body)
                has_author = True
                i = j
        # In the original, the appendix body starts well below the title
        # (measured on pp. 317, 337 and 409 of the source PDF).
        out.append("\\addvspace{%dpt}\n" % (70 if has_author else 34))
        out.append(renderer.blocks(blocks[i:]))
        return "".join(out)

    # -- helpers -----------------------------------------------------------
    def _chapter_title(self, heading, appendix=False):
        text = heading.strip()
        if appendix:
            m = re.match(r"^(?:Phụ lục|PHỤ LỤC)\s+([A-Za-z])\s*[:.]\s*(.+)$",
                         text)
            return m.group(2).strip() if m else text
        m = re.match(r"^(?:Chương|CHƯƠNG)\s+\d+\s*[:.]\s*(.+)$", text)
        return m.group(1).strip() if m else text

    def _author_block(self, blocks, i):
        """If blocks[i] is a byline quote, render it and return (latex, i+1)."""
        lines = [x.strip() for x in blocks[i].lines if x.strip()]
        if not lines:
            return None, i + 1
        text = " ".join(lines)
        if len(text) > 160:
            return None, i
        if re.match(r"^(Tác giả|tác giả|TÁC GIẢ|với|Với|by)\b", text):
            return ("{\\raggedleft\\fontsize{10}{12}\\selectfont %s\\par}"
                    "\\addvspace{2pt}\n" % self._inline_author(text)), i + 1
        return None, i

    def _inline_author(self, text):
        return tex_escape(text)

    def _epigraph(self, blk, inline, left=False):
        """Return the LaTeX for a chapter epigraph.

        Sources put the attribution either as a second paragraph (ch. 4), as a
        final line after the quotation mark (ch. 11) or as a line beginning
        with an em dash (ch. 13).  All three are handled.
        """
        raw = [x.strip() for x in blk.lines]
        while raw and not raw[0]:
            raw.pop(0)
        while raw and not raw[-1]:
            raw.pop()
        # split into paragraphs on empty quote lines
        paras = [[]]
        for ln in raw:
            if ln:
                paras[-1].append(ln)
            elif paras[-1]:
                paras.append([])
        paras = [p for p in paras if p]
        attr = ""
        if len(paras) >= 2:
            cand = " ".join(paras[-1])
            if len(cand) <= 120:
                attr = cand
                paras = paras[:-1]
        if not attr and paras and len(paras[0]) >= 2:
            first = paras[0]
            if first[-1].startswith("\u2014"):
                attr = first[-1]
                paras[0] = first[:-1]
            elif re.search(r"[\u201d\"]$", first[-2]):
                attr = first[-1]
                paras[0] = first[:-1]
        body_tex = "\\\\\n".join(
            " ".join(inline.convert(x) for x in para) for para in paras)
        if attr:
            attr_tex = inline.convert(attr)
            if not attr_tex.startswith("\u2014"):
                attr_tex = "\u2014" + attr_tex
        else:
            attr_tex = ""
        macro = "ccepigraphleft" if left else "ccepigraph"
        return ("\\%s{%s}{%s}\n" % (macro, body_tex, attr_tex))


# ---------------------------------------------------------------------------
# Manifest generation
# ---------------------------------------------------------------------------

def write_manifest(name, inputs):
    path = os.path.join(GEN, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("%% generated by build/md2tex.py -- do not edit\n")
        for tex in inputs:
            fh.write("\\input{%s}\n" % tex)
    return path


def main(argv=None):
    os.makedirs(GEN, exist_ok=True)

    sections = {"front": [], "main": [], "back": []}
    missing = []
    empty = []
    all_warnings = []

    for part in PARTS:
        path = os.path.join(VI, part["md"])
        if not os.path.exists(path):
            missing.append(part["md"])
            continue
        text = open(path, encoding="utf-8").read()
        if not text.strip():
            empty.append(part["md"])
            continue
        conv = Converter(part)
        try:
            tex = conv.convert(text)
        except ConvertError as exc:
            sys.stderr.write("ERROR %s: %s\n" % (part["md"], exc))
            return 1
        except Exception as exc:  # pragma: no cover - defensive
            import traceback
            traceback.print_exc()
            sys.stderr.write("ERROR %s: %s\n" % (part["md"], exc))
            return 1
        stem = os.path.splitext(part["md"])[0]
        rel = "build/gen/%s.tex" % stem
        with open(os.path.join(GEN, stem + ".tex"), "w",
                  encoding="utf-8") as fh:
            fh.write(tex)
        sections[part.get("section", "main")].append(rel)
        for w in conv.warnings:
            all_warnings.append("%s: %s" % (part["md"], w))

    write_manifest("front.tex", sections["front"])
    write_manifest("main.tex", sections["main"])
    write_manifest("back.tex", sections["back"])

    # status report
    status = []
    total_chapters = sum(1 for p in PARTS if p["kind"] == "chapter")
    present_chapters = sum(1 for p in PARTS if p["kind"] == "chapter"
                           and os.path.exists(os.path.join(VI, p["md"]))
                           and os.path.getsize(os.path.join(VI, p["md"])) > 0)
    status.append("chapters present: %d/%d" %
                  (present_chapters, total_chapters))
    if missing:
        status.append("MISSING files (skipped): " + ", ".join(missing))
    if empty:
        status.append("EMPTY files (skipped): " + ", ".join(empty))
    if all_warnings:
        status.append("warnings:")
        status.extend("  - " + w for w in all_warnings)
    status_path = os.path.join(GEN, "status.txt")
    with open(status_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(status) + "\n")

    print("md2tex: %d chapters, %d warnings"
          % (present_chapters, len(all_warnings)))
    if missing:
        print("md2tex: WARNING missing files causing chapters to be skipped:")
        for m in missing:
            print("  - vi/" + m)
    if empty:
        print("md2tex: WARNING empty files skipped:")
        for m in empty:
            print("  - vi/" + m)
    for w in all_warnings:
        print("md2tex: note: " + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
