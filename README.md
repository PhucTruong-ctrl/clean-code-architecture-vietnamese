# Clean Code — bản dịch tiếng Việt

Bản dịch trọn vẹn cuốn *Clean Code: A Handbook of Agile Software Craftsmanship* của Robert C. Martin (Pearson Education, 2009), kèm pipeline dựng PDF theo đúng khổ sách và phong cách trình bày của ấn bản gốc.

## Sản phẩm

| Đường dẫn | Nội dung |
|---|---|
| `CleanCode-vi.pdf` / `out/CleanCode-vi.pdf` | Bản PDF: 437 trang, khổ 517.61 × 666.36 bp |
| `CleanCode.pdf` | Ấn bản gốc, dùng làm nguồn đối chiếu và trích xuất tài sản |
| `vi/*.md` | Bản dịch Markdown theo chương, nguồn chân lý của văn bản |
| `tools/md2tex.py` | Converter Markdown → LaTeX, không dùng pandoc |
| `tools/qa_check.py` | Kiểm tra nhanh cấu trúc bản dịch |
| `tools/` | Script trích xuất hình và tái tạo Phụ lục B từ nguồn |
| `docs/translation-guide.md` | Hướng dẫn dịch và quy ước văn phong |
| `reference/original-extracts/` | Văn bản gốc trích từ PDF để đối chiếu |
| `tex/cleanbook.tex` | Preamble: khổ trang, font, chapter opener, code box, TOC, running heads |
| `build.sh` | Build toàn sách: `./build.sh` |
| `assets/` | Minh họa, hình trong sách và opener đã trích từ bản gốc |

## Build

```bash
./build.sh
./build.sh clean      # xoá sản phẩm trung gian
python3 tools/qa_check.py
```

Yêu cầu build: TeX Live với XeLaTeX, font Liberation Serif / Liberation Sans / Liberation Mono, Python 3 và Poppler (`pdfinfo`). Chạy `python3 tools/qa_check.py` để soát nhanh bản dịch.

Tái tạo figures và illustrations là tùy chọn, không cần cho build thường. Các script trong `tools/` cần Poppler (`pdftohtml`, `pdfimages`, `pdftoppm`), Pillow và XML trung gian trong thư mục cục bộ bị ignore `work/pdfxml/`.

## Quy ước bản dịch

- Mã nguồn, tên định danh, tên tệp, URL giữ nguyên. Chú thích trong mã dịch sang tiếng Việt, trừ Phụ lục B (giữ nguyên tiếng Anh như bản in).
- Lỗi chính tả và lỗi mã có sẵn trong bản gốc được giữ nguyên vì chúng là đối tượng phân tích của sách.
- Chỉ mục cuối sách của bản gốc được lược bỏ (gắn với số trang bản tiếng Anh). Các dẫn chiếu "trang N" trong sách vẫn là số trang bản tiếng Anh.
- Không dùng dấu gạch ngang dài (em dash) trong văn xuôi.
- Các câu thơ, trích dẫn tiếng nước ngoài giữ nguyên bản gốc; chú thích và giải thích đã dịch.
- Hình có chú thích dùng `**Hình X-Y**`; minh họa không chú thích dùng `![alt](assets/illustrations/<ten>.png){w=<bề rộng bp>}`. Cặp ảnh bìa có thêm `wrap=cover` để dàn cạnh đoạn văn mô tả. Converter không in alt text.

Xem `vi/22-ve-ban-dich.md` để biết ghi chú của người dịch in ở cuối sách.
