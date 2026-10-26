#!/usr/bin/env python3
"""Trich xuat Phu luc B (org.jfree.date.SerialDate) tu ban text cua PDF
sang Markdown, GIU NGUYEN so dong in o le trai tung dong ma.

Nguon : work/chapters/19-phu-luc-b-serialdate.txt (PDF trang 349-407)
Dich   : vi/19-phu-luc-b-serialdate.md

Cau truc mot trang in: dong chay dau trang ("Appendix B: ...") + so folio
(o mep phai hoac gan lien sau form-feed), caption "Listing B-x [(continued)]",
ten file, roi cac dong ma dang "  <so dong> <noi dung>".
Cac dong ma bi PDF xuong dong (khong co so dong) duoc noi lai vao dong truoc.
"""

import re
import sys

SRC = "work/chapters/19-phu-luc-b-serialdate.txt"
OUT = "vi/19-phu-luc-b-serialdate.md"
TITLE = "# Phụ lục B: org.jfree.date.SerialDate"

CAPTION_RE = re.compile(r"^[ \t]*Listing B-(\d+)( \(continued\))?[ \t]*$")
FILE_RE = re.compile(r"^[ \t]*([^\s]+\.(?:Java|java))( \(Final\))?[ \t]*$")
CODE_RE = re.compile(r"^[ ]{0,4}(\d{1,4}) (.*)$")
BLANK_CODE_RE = re.compile(r"^[ ]{0,4}(\d{1,4})[ ]*$")
FOLIO_RE = re.compile(r"^[ ]{20,}\d{3}[ ]*$")
ELISION_RE = re.compile(r"^[ \t]*\.\.\.[ \t]*$")
HEADER_RE = re.compile(r"Appendix B")


class Page:
    def __init__(self, index):
        self.index = index
        self.listing = None
        self.continued = False
        self.filename = None
        self.lines = []  # list of (lineno:int|None, text:str); None = dấu "..."

    def __repr__(self):
        return (f"Page({self.index}, B-{self.listing}, cont={self.continued}, "
                f"file={self.filename}, lines={len(self.lines)})")


def parse_pages(text):
    pages = []
    raw_pages = text.split("\f")
    for pi, raw in enumerate(raw_pages):
        if raw.strip() == "":
            continue
        page = Page(pi)
        in_code = False
        for raw_line in raw.split("\n"):
            line = raw_line.rstrip("\r")
            stripped = line.strip()

            # 1. Dong chay dau trang / folio / tieu de trang dau
            if HEADER_RE.search(line):
                continue
            if FOLIO_RE.match(line):
                continue
            if pi == 0 and stripped in ("Appendix B", "org.jfree.date.SerialDate"):
                continue

            # 2. Caption va ten file
            m = CAPTION_RE.match(line)
            if m:
                if page.listing is not None:
                    raise SystemExit(f"Trang {pi}: hai caption lien tiep")
                page.listing = int(m.group(1))
                page.continued = bool(m.group(2))
                continue
            m = FILE_RE.match(line)
            if m and page.listing is not None and page.filename is None:
                page.filename = m.group(1) + (m.group(2) or "")
                continue

            # 3. Dong ma co so dong
            m = CODE_RE.match(line)
            if m:
                in_code = True
                page.lines.append((int(m.group(1)), m.group(2)))
                continue
            m = BLANK_CODE_RE.match(line)
            if m:
                in_code = True
                page.lines.append((int(m.group(1)), ""))
                continue

            # 4. Dong trong (khoang trang giua cac phan cua trang in)
            if stripped == "":
                continue

            # 5. Dong ma bi xuong dong (PDF cat dong): noi vao dong truoc
            if in_code:
                if ELISION_RE.match(line):
                    page.lines.append((None, "..."))
                    continue
                if not page.lines or page.lines[-1][0] is None:
                    raise SystemExit(f"Trang {pi}: dong noi mo coi: {line!r}")
                prev_no, prev_text = page.lines[-1]
                page.lines[-1] = (prev_no, prev_text.rstrip() + " " + stripped.lstrip())
                continue

            raise SystemExit(f"Trang {pi}: khong nhan dang duoc dong: {line!r}")

        if page.listing is None:
            raise SystemExit(f"Trang {pi}: khong co caption Listing")
        if page.filename is None:
            raise SystemExit(f"Trang {pi}: khong co ten file")
        pages.append(page)
    return pages


def fmt_line(no, text):
    """So dong canh phai trong o rong 4, cach noi dung mot dau cach."""
    if no is None:
        return text
    return (f"{no:4d} {text}").rstrip()


def build_markdown(pages):
    out = [TITLE, ""]
    prev_listing = None
    for page in pages:
        cap = f"**Đoạn mã B-{page.listing}"
        if page.continued:
            cap += " (tiếp theo)"
        cap += "**"
        out.append(cap)
        out.append(f"**{page.filename}**")
        out.append("")
        out.append("```java")
        for no, text in page.lines:
            out.append(fmt_line(no, text))
        out.append("```")
        out.append("")
        prev_listing = page.listing
    # bo dong trong cuoi
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def validate(pages):
    """Kiem tra so dong lien tuc trong tung listing va can bang ngoac."""
    problems = []
    by_listing = {}
    for page in pages:
        by_listing.setdefault(page.listing, []).extend(page.lines)
    for listing, lines in sorted(by_listing.items()):
        nums = [no for no, _ in lines if no is not None]
        expected = list(range(1, max(nums) + 1))
        if nums != expected:
            missing = sorted(set(expected) - set(nums))
            dup = sorted({n for n in nums if nums.count(n) > 1})
            problems.append(
                f"B-{listing}: so dong khong lien tuc (thieu {missing[:10]}, trung {dup[:10]})")
        code = "\n".join(text for _, text in lines if _ is not None)
        for open_ch, close_ch in (("{", "}"), ("(", ")"), ("[", "]")):
            a, b = code.count(open_ch), code.count(close_ch)
            if a != b:
                problems.append(f"B-{listing}: lech ngoac {open_ch}{close_ch}: {a} vs {b}")
    return problems


# Cac so dong ma vi/16-tai-cau-truc-serialdate.md nhac toi, kem listing chua
# dong do va mot manh noi dung de doi chieu nghia. Chuoi None = chi kiem tra
# su ton tai cua so dong (vi du cac dong dau/cuoi cua mot khoang).
REF_CHECKS = [
    # bai kiem thu trong BobsSerialDateTest (Listing B-4)
    (4, 23, "//todo"), (4, 32, 'stringToWeekdayCode("tues")'),
    (4, 45, 'stringToWeekdayCode("thurs")'),
    (4, 63, 'stringToWeekdayCode("sun")'),
    (4, 153, 'stringToMonthCode("0")'), (4, 154, 'stringToMonthCode("13")'),
    (4, 163, 'stringToMonthCode("jan")'),
    (4, 213, 'stringToMonthCode("DECEMBER")'),
    (4, 318, "getFollowingDayOfWeek(SATURDAY, d(25, DECEMBER, 2004))"),
    (4, 329, "public void testGetNearestDayOfWeek()"),
    (4, 411, 'weekInMonthToString(FIRST_WEEK_IN_MONTH)'),
    (4, 415, "LAST_WEEK_IN_MONTH"),
    (4, 417, "//todo"),
    (4, 429, "//todo"),
    # SerialDate.java (Listing B-1)
    (1, 43, "12-Nov-2001"),
    (1, 67, "/**"),
    (1, 71, "Requirement 1 : match at least what Excel does for dates;"),
    (1, 72, "Requirement 2 : class is immutable;"),
    (1, 91, "serialVersionUID"),
    (1, 93, "Date format symbols"),
    (1, 97, "The serial number for 1 January 1900"),
    (1, 98, "SERIAL_LOWER_BOUND = 2;"),
    (1, 100, "The serial number for 31 December 9999"),
    (1, 101, "SERIAL_UPPER_BOUND = 2958465;"),
    (1, 104, "MINIMUM_YEAR_SUPPORTED = 1900;"),
    (1, 107, "MAXIMUM_YEAR_SUPPORTED = 9999;"),
    (1, 109, "Useful constant for Monday"),
    (1, 140, "LAST_DAY_OF_MONTH"),
    (1, 162, None), (1, 163, "FIRST_WEEK_IN_MONTH = 1;"),
    (1, 177, None), (1, 178, "INCLUDE_NONE = 0;"), (1, 187, "INCLUDE_BOTH = 3;"),
    (1, 205, "FOLLOWING = 1;"), (1, 208, "private String description;"),
    (1, 213, "protected SerialDate()"),
    (1, 216, None), (1, 238, None), (1, 242, None),
    (1, 259, "s.equals(shortWeekdayNames[i])"),
    (1, 263, "s.equals(weekDayNames[i])"),
    (1, 270, None), (1, 272, None), (1, 286, None), (1, 288, None),
    (1, 316, None), (1, 326, "public static boolean isValidMonthCode"),
    (1, 334, "case JUNE:"),
    (1, 346, None), (1, 356, "public static int monthCodeToQuarter"),
    (1, 377, None), (1, 426, None), (1, 428, None), (1, 472, None),
    (1, 495, None), (1, 517, None), (1, 519, None), (1, 536, None),
    (1, 538, None), (1, 560, None), (1, 562, None),
    (1, 571, "public static SerialDate addDays"),
    (1, 576, None), (1, 578, None), (1, 602, None), (1, 604, None),
    (1, 626, None), (1, 628, None),
    (1, 638, "getPreviousDayOfWeek(final int targetWeekday"),
    (1, 660, None), (1, 662, None),
    (1, 672, "getFollowingDayOfWeek(final int targetWeekday"),
    (1, 685, "if (baseDOW > targetWeekday) {"),
    (1, 693, None), (1, 695, None),
    (1, 705, "getNearestDayOfWeek(final int targetDOW"),
    (1, 718, "if (adjust >= 4) {"),
    (1, 719, "adjust = 7 - adjust;"),
    (1, 724, "return SerialDate.addDays(adjust, base);"),
    (1, 726, None), (1, 728, None), (1, 740, None), (1, 742, None),
    (1, 761, None), (1, 765, None), (1, 781, None),
    (1, 808, "createInstance(final int serial)"),
    (1, 829, None), (1, 830, "Returns the serial number for the date"),
    (1, 838, None), (1, 844, "toDate()"),
    (1, 895, None), (1, 899, None),
    (1, 902, None), (1, 913, "compare(SerialDate other)"),
    (1, 915, None), (1, 980, "isInRange(SerialDate d1, SerialDate d2)"),
    (1, 982, None), (1, 995, "int include);"),
    (1, 997, None), (1, 1008, None),
    # SpreadsheetDate.java (Listing B-5)
    (5, 71, "Excel uses the convention that 1-Jan-1900 = 1"),
    (5, 198, None), (5, 203, "public Date toDate()"),
    (5, 207, None),
    (5, 247, "return (this.serial + 6) % 7 + 1;"),
    (5, 434, "AGGREGATE_DAYS_TO_END_OF_PRECEDING_MONTH[m];"),
    (5, 473, "AGGREGATE_DAYS_TO_END_OF_PRECEDING_MONTH;"),
    # RelativeDayOfWeekRule.java (Listing B-6)
    (6, 174, "public SerialDate getDate(final int year)"),
    (6, 177, "SerialDate.MINIMUM_YEAR_SUPPORTED"),
    (6, 178, "SerialDate.MAXIMUM_YEAR_SUPPORTED"),
    (6, 187, "if (base != null) {"),
    (6, 205, "return result;"),
]


def check_references(pages):
    """Doi chieu cac so dong chuong 16 nhac toi voi listing da trich xuat."""
    data = {}
    for page in pages:
        for no, text in page.lines:
            if no is not None:
                data.setdefault(page.listing, {})[no] = text
    fails = []
    for listing, no, needle in REF_CHECKS:
        text = data.get(listing, {}).get(no)
        if text is None:
            fails.append(f"B-{listing} dong {no}: KHONG CO trong listing")
        elif needle is not None and needle not in text:
            fails.append(f"B-{listing} dong {no}: khong thay {needle!r} trong {text!r}")
    return fails


def main():
    text = open(SRC, encoding="utf-8").read()
    pages = parse_pages(text)
    md = build_markdown(pages)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(md)

    starts = sum(1 for p in pages if not p.continued)
    conts = sum(1 for p in pages if p.continued)
    code_lines = sum(1 for p in pages for no, _ in p.lines if no is not None)
    elisions = sum(1 for p in pages for no, t in p.lines
                   if no is None and t.strip() == "...")
    print(f"Trang co caption       : {len(pages)}")
    print(f"Listing bat dau        : {starts}")
    print(f"Trang '(continued)'    : {conts}")
    print(f"Tong so dong ma co so  : {code_lines}")
    print(f"Dau '...' cua ban in   : {elisions}")
    print(f"Fence ``` trong output : {md.count(chr(96) * 3)}")
    for msg in validate(pages):
        print("CANH BAO:", msg)
    for msg in check_references(pages):
        print("LOI DOI CHIEU:", msg)
    print("Doi chieu chuong 16   :",
          "PASS" if not check_references(pages) else "CO LOI")
    for p in pages:
        nums = [no for no, _ in p.lines if no is not None]
        if nums:
            print(f"  B-{p.listing}{' (cont)' if p.continued else ''}: "
                  f"{p.filename:32s} dong {nums[0]}..{nums[-1]} ({len(p.lines)} dong)")


if __name__ == "__main__":
    sys.exit(main())
