#!/usr/bin/env python3
"""Extract figure regions from the original CleanCode.pdf as PNG files.

Figures in the book are a mix of raster and vector drawings. Rendering the
page region at high dpi captures both, then PIL trims the white margins.
"""
import re
import subprocess
import pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / 'CleanCode.pdf'
XML = ROOT / 'work/pdfxml/cc.xml'
OUT = ROOT / 'assets/figures'
OUT.mkdir(parents=True, exist_ok=True)
DPI = 300
S = DPI / 72.0
PAGE_W = 517.608
LEFT = 78.8
RIGHT = 438.8

xml = XML.read_text(encoding='utf-8', errors='replace')
pages = {int(m.group(1)): m.group(2) for m in re.finditer(r'<page number="(\d+)"[^>]*>(.*?)</page>', xml, re.S)}

# figure label -> rendering page (caption page)
FIGS = {
    '1-1': None, '5-1': None, '5-2': None, '8-1': None, '8-2': None,
    '11-1': None, '11-2': None, '11-3': None,
    'A-1': None, 'A-2': None, 'A-3': None,
}
LABEL_RE = re.compile(r'^Figure\s+((?:\d+-\d+)|(?:A-\d+))$')

def text_items(pn):
    items = []
    for m in re.finditer(r'<text top="(\d+)" left="(\d+)"[^>]*>(.*?)</text>', pages[pn], re.S):
        txt = re.sub(r'<[^>]+>', '', m.group(3)).replace('\n', ' ').strip()
        items.append((int(m.group(1)), int(m.group(2)), txt))
    return items

# locate caption pages
for pn in sorted(pages):
    for top, left, txt in text_items(pn):
        m = LABEL_RE.match(txt)
        if m and m.group(1) in FIGS:
            FIGS[m.group(1)] = (pn, top, left)

print("figure captions found:", FIGS)
missing = [k for k, v in FIGS.items() if v is None]
if missing:
    raise SystemExit(f"missing caption pages: {missing}")

for label, (pn, cap_top, cap_left) in FIGS.items():
    items = text_items(pn)
    above = [t for t, l, txt in items if t < cap_top - 2 and txt]
    top = max(above) + 10 if above else 72
    # crop box in points
    x0 = LEFT * S
    x1 = RIGHT * S
    y0 = top * S
    y1 = (cap_top - 2) * S
    raw = ROOT / 'work' / f'page-{pn}.png'
    if not raw.exists():
        subprocess.run(['pdftoppm', '-png', '-singlefile', '-r', str(DPI), '-f', str(pn), '-l', str(pn),
                        str(PDF), str(ROOT / 'work' / f'page-{pn}')], check=True)
    img = Image.open(raw).convert('L')
    box = (max(0, int(x0)), max(0, int(y0)), min(img.width, int(x1)), min(img.height, int(y1)))
    crop = img.crop(box)
    # trim white margins
    bbox = crop.point(lambda p: 255 if p < 245 else 0).getbbox()
    if bbox is None:
        print(f"{label}: empty region on page {pn}")
        continue
    pad = 12
    crop = crop.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad),
                      min(crop.width, bbox[2] + pad), min(crop.height, bbox[3] + pad)))
    dest = OUT / f'fig-{label}.png'
    crop.save(dest)
    print(f"{label}: page {pn} -> {dest.name} {crop.size}")
