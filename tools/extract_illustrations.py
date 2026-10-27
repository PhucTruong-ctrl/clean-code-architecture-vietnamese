#!/usr/bin/env python3
"""Extract the inline illustrations of the original edition into assets/illustrations.

The original has 50 image blocks: 17 chapter openers, 11 numbered figures,
and 22 uncaptioned illustrations (portraits, cartoons, cover photos).  The
first two groups already live in assets/openers and assets/figures; this
script extracts the third group at its printed display size.

Run:  python3 tools/extract_illustrations.py
"""
import re
import subprocess
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / 'CleanCode.pdf'
OUT = ROOT / 'assets/illustrations'
TMP = ROOT / 'work/audit/illustrations-raw'
OUT.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)

XML = ROOT / 'work/pdfxml/cc2.xml'
xml = XML.read_text(encoding='utf-8', errors='replace')
pages = {int(m.group(1)): m.group(2)
         for m in re.finditer(r'<page number="(\d+)"[^>]*>(.*?)</page>', xml, re.S)}

# XML units -> bp (the dump uses the MediaBox: 1172 units = 781.6 bp)
UNIT = 781.6 / 1172.0

# (pdf page, image index on that page, output name)
ITEMS = [
    (19, 0, '00-introduction-wtfs'),
    (22, 0, '00-cover-photo-1'),
    (22, 1, '00-cover-photo-2'),
    (25, 0, '01-kent-beck'),
    (29, 0, '01-bjarne-stroustrup'),
    (30, 0, '01-grady-booch'),
    (31, 0, '01-dave-thomas'),
    (32, 0, '01-michael-feathers'),
    (32, 1, '01-ron-jeffries'),
    (33, 0, '01-ward-cunningham'),
    (34, 0, '01-uncle-bob'),
    (41, 0, '02-avoid-disinformation'),
    (47, 0, '02-dont-be-cute'),
    (56, 0, '03-do-one-thing'),
    (61, 0, '03-use-descriptive-names'),
    (69, 0, '03-error-java'),
    (79, 0, '04-warning-of-consequences'),
    (105, 0, '05-vertical-distance'),
    (111, 0, '05-team-rules'),
    (119, 0, '06-train-wrecks'),
    (129, 0, '07-define-the-normal-flow'),
    (424, 0, '21-epilogue-badge'),
]


def image_boxes(page):
    body = pages[page]
    return [(int(a), int(b), int(c), int(d)) for a, b, c, d in re.findall(
        r'<image top="(\d+)" left="(\d+)" width="(\d+)" height="(\d+)"', body)]


print('name, page, width_bp, height_bp')
for page, idx, name in ITEMS:
    boxes = image_boxes(page)
    if idx >= len(boxes):
        raise SystemExit(f'{name}: page {page} has only {len(boxes)} images')
    _, _, w_units, h_units = boxes[idx]
    # extract every image of the page, then keep the one at idx
    prefix = TMP / f'p{page:03d}'
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page),
                    str(PDF), str(prefix)], check=True)
    src = pathlib.Path(f'{prefix}-{idx:03d}.png')
    if not src.exists():
        raise SystemExit(f'{name}: expected {src}')
    dest = OUT / f'{name}.png'
    dest.write_bytes(src.read_bytes())
    print(f'{name}, {page}, {w_units * UNIT:.1f}, {h_units * UNIT:.1f}')
