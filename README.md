# Clean Code — bản dịch tiếng Việt

Bản dịch trọn vẹn cuốn *Clean Code: A Handbook of Agile Software Craftsmanship* của Robert C. Martin (Pearson Education, 2009), kèm pipeline dựng PDF theo đúng khổ sách và phong cách trình bày của ấn bản gốc.

## Sản phẩm

| Đường dẫn | Nội dung |
|---|---|
| `CleanCode-vi.pdf` / `out/CleanCode-vi.pdf` | Bản PDF hoàn chỉnh: 437 trang, khổ 517.61 × 666.36 bp |
| `vi/*.md` | Bản dịch Markdown theo chương, nguồn chân lý của văn bản |
| `build/md2tex.py` | Converter Markdown → LaTeX viết riêng, không dùng pandoc |
| `tex/cleanbook.tex` | Preamble: geometry, font, chapter opener, code box, TOC, running heads |
| `build.sh` | Build toàn sách: `./build.sh` |
| `assets/openers/` | 17 minh họa mở chương trích từ PDF gốc |
| `assets/figures/` | 10 hình có đánh số trong sách, trích từ PDF gốc |
| `assets/illustrations/` | 22 minh họa không chú thích: chân dung các tác giả, tranh dí dỏm, ảnh bìa, huy hiệu Lời kết |

## Build

```bash
cd /home/phuctruong/Life/Learning/clean-code
./build.sh            # xuất out/CleanCode-vi.pdf
./build.sh clean      # xoá sản phẩm trung gian
```

Yêu cầu: TeX Live với XeLaTeX, font Liberation Serif / Liberation Sans / Liberation Mono, Python 3 (chỉ dùng thư viện chuẩn). Chạy `python3 work/qa_check.py` để soát nhanh bản dịch.

## Quy ước bản dịch

- Mã nguồn, tên định danh, tên tệp, URL giữ nguyên. Chú thích trong mã dịch sang tiếng Việt, trừ Phụ lục B (giữ nguyên tiếng Anh như bản in).
- Lỗi chính tả và lỗi mã có sẵn trong bản gốc được giữ nguyên vì chúng là đối tượng phân tích của sách.
- Chỉ mục cuối sách của bản gốc được lược bỏ (gắn với số trang bản tiếng Anh). Các dẫn chiếu "trang N" trong sách vẫn là số trang bản tiếng Anh.
- Không dùng dấu gạch ngang dài (em dash) trong văn xuôi.
- Các câu thơ, trích dẫn tiếng nước ngoài giữ nguyên bản gốc; chú thích và giải thích đã dịch.
- Hình có chú thích dùng `**Hình X-Y**`; minh họa không chú thích dùng `![alt](assets/illustrations/<ten>.png){w=<bề rộng bp>}`. Converter chèn ảnh căn giữa, không in alt text.

Xem `vi/22-ve-ban-dich.md` để biết ghi chú của người dịch in ở cuối sách.
