#!/usr/bin/env python3
"""QA checks for the Vietnamese Markdown translation files."""
import re, pathlib, sys

VI = pathlib.Path(__file__).resolve().parent.parent / 'vi'
files = sorted(VI.glob('*.md'))

SUP = '¹²³⁴⁵⁶⁷⁸⁹⁰'
problems = 0

def warn(f, line, kind, extra=''):
    global problems
    problems += 1
    print(f"{f.name}:{line}: [{kind}] {extra[:110]}")

for f in files:
    text = f.read_text()
    lines = text.split('\n')
    infence = False
    fences = 0
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fences += 1
            infence = not infence
            continue
        if infence:
            continue
        if re.fullmatch(r'\s*\d{1,3}\s*', line):
            warn(f, i, 'standalone number (PDF folio?)', line)
        if re.match(r'\s*(Chapter|Appendix)\s+[A-Z0-9]', line) and not line.startswith('#'):
            warn(f, i, 'running head left in prose', line)
        if '—' in line:
            warn(f, i, 'em dash', line)
    if fences % 2:
        warn(f, 0, 'unbalanced code fences', f'{fences} fence lines')

    # whole-file checks
    if '\t' in text:
        warn(f, 0, 'tab characters', '')
    md_refs = set(re.findall(r'\[\^(\d+)\](?!:)', text))
    md_defs = set(re.findall(r'^\[\^(\d+)\]:', text, re.M))
    if md_refs - md_defs:
        warn(f, 0, 'footnote refs without definition', str(sorted(md_refs - md_defs))[:80])
    if md_defs - md_refs:
        warn(f, 0, 'footnote definitions without ref', str(sorted(md_defs - md_refs))[:80])
    sup_refs = set(re.findall('[' + SUP + ']+', text))
    # superscript "definitions" = paragraph starting with superscript token
    sup_defs = set()
    for line in lines:
        m = re.match(r'^([' + SUP + r']+)[\.\s]', line)
        if m:
            sup_defs.add(m.group(1))
    missing = sup_refs - sup_defs
    if missing:
        warn(f, 0, 'superscript markers without definition line', str(sorted(missing))[:80])

print(f"\n{problems} problem(s) across {len(files)} files")
sys.exit(1 if problems else 0)
