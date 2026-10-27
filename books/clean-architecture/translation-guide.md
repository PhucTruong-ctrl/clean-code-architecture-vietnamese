# Hướng dẫn dịch Clean Architecture sang tiếng Việt

Tài liệu này dành cho người dịch (kể cả agent). Đọc hết trước khi bắt tay vào bất kỳ chương nào.

## 1. Mục tiêu

Dịch **toàn bộ** cuốn *Clean Architecture: A Craftsman's Guide to Software Structure and Design* của Robert C. Martin sang tiếng Việt hiện đại, đọc như sách do người Việt viết cho lập trình viên Việt, không phải bản dịch máy từng câu.

Bản dịch phải:
- Giữ đúng nội dung, ví dụ, con số, trích dẫn, thứ tự mục, ghi chú chân trang và sắc thái của tác giả.
- Không tóm tắt, không lược bỏ; chỉ diễn giải thêm khi cần làm rõ thành ngữ hoặc hình ảnh khó hiểu, và không đặt lời giải thích vào trong trích dẫn.
- Dịch đủ mọi đoạn văn xuôi, tiêu đề mục, chú thích hình/đoạn mã, bảng, và lời dẫn.
- Giữ nguyên mã nguồn, tên định danh, tên tệp, tên thư viện, URL, số hiệu đoạn mã.
- Giữ nguyên cấu trúc lập luận, nguyên tắc và ví dụ của tác giả.
- PDF gốc: `books/clean-architecture/source.pdf`; văn bản trích xuất để đối chiếu: `books/clean-architecture/source.txt`.

## 2. Giọng văn

Tác giả viết ở ngôi thứ nhất, kể chuyện nghề, có chỗ tự trào, có chỗ gay gắt. Bản dịch phải giữ được chất giọng đó.

- Xưng "tôi" khi tác giả kể chuyện riêng; "chúng tôi" khi nói thay nhóm tác giả. Gọi người đọc là "bạn".
- Câu văn kỹ thuật: rõ ràng, dứt khoát, không rào đón. Ưu tiên thể chủ động.
- Được phép dùng từ chuyên môn tiếng Anh khi tiếng Việt không có tương đương tự nhiên (xem bảng thuật ngữ). Lần đầu xuất hiện có thể kèm nguyên ngữ trong ngoặc.
- Câu dài ngắn xen kẽ. Đừng dịch mỗi câu tiếng Anh thành một câu tiếng Việt cùng độ dài; hãy tách, gộp, đảo trật tự khi tiếng Việt cần.
- Tránh văn phong "dịch máy": không lặp "của nó", "được thực hiện bởi", "việc mà", "một cách", "những cái". Không dịch sát từng giới từ.
- Với thành ngữ, ẩn dụ hoặc chơi chữ, truyền ý và hiệu ứng bằng tiếng Việt tự nhiên. Nếu giữ hình ảnh gốc là cần thiết, giải thích ngắn trong ngữ cảnh; phân biệt rõ phần giải thích với lời trích dẫn.
- Không dùng dấu gạch ngang dài (—) trong lời dịch. Thay bằng dấu phẩy, dấu hai chấm, ngoặc đơn, hoặc tách câu.
- Không dùng bullet có nhãn in đậm kiểu "**Quan trọng:**" nếu nguyên bản không có.
- Không thêm câu kết luận, câu nhấn mạnh, câu diễn giải lại ý vừa nói. Nguyên bản có gì dịch nấy.

### Những lỗi cần tránh (theo /humanizer)

1. **"Không chỉ X mà còn Y"** và các biến thể "không phải X, mà là Y": chỉ dùng khi nguyên bản thật sự đối lập hai ý. Đừng biến câu bình thường thành cấu trúc này cho "kêu".
2. **Câu chốt một dòng** lặp lại ý đoạn trước ("Đó mới là điều quan trọng."). Nguyên bản có thì dịch, không có thì không thêm.
3. **Bộ ba giả tạo**: tiếng Anh hay có "A, B, and C"; tiếng Việt chỉ giữ ba vế khi ba vế đều mang thông tin.
4. **Từ ngữ phồng**: "đóng vai trò then chốt", "minh chứng cho", "bức tranh toàn cảnh", "hành trình", "nâng tầm", "đậm dấu ấn". Dịch thẳng nghĩa.
5. **Gạch ngang dài** và **in đậm trang trí**: bỏ.
6. **Lặp mở câu**: nhiều câu liên tiếp cùng một chủ ngữ thì đổi cấu trúc.
7. **Giọng chatbot**: "Hãy cùng khám phá", "Như bạn có thể thấy", "Tóm lại". Không có trong nguyên bản thì không có trong bản dịch.

## 3. Những gì giữ nguyên

- Mã nguồn: giữ cú pháp, tên biến/hàm/lớp và chuỗi ký tự; dịch chú thích theo quy định bên dưới.
- Tên định danh, tên tệp, API và tên thư viện: giữ nguyên như trong nguồn.
- Tên người, tên sách, tên bài báo, tên công ty, địa danh: Robert C. Martin, *Clean Architecture*, Pearson Education.
- Số hiệu đoạn mã và số chương, mục phải khớp nguyên bản. Dịch nhãn `Listing` thành `Đoạn mã` khi phù hợp.
- Câu trích dẫn bằng tiếng nước ngoài: giữ nguyên câu gốc, thêm bản dịch trong ngoặc nếu cần.
- Các từ khóa của ngôn ngữ lập trình, thông báo lỗi, chuỗi trong `String.format`.
- Chú thích trong code: dịch sang tiếng Việt, giữ nguyên vị trí và ý nghĩa. Không dịch chuỗi ký tự trong code.

## 4. Xử lý mã nguồn khi chuyển sang Markdown

Bản PDF khi trích xuất làm xô lệch thở lề và đôi khi cắt dòng. Người dịch phải dựng lại đoạn mã thành khối ``` ngôn ngữ``` sao cho:
- Đúng logic, đúng thứ tự dòng, đúng dấu ngoặc. Không sáng tác thêm, không "sửa" code.
- Thụt lề theo cấu trúc (2 hoặc 4 dấu cách, thống nhất trong cùng một đoạn).
- Giữ tiêu đề đoạn mã ngay trên khối code:

```markdown
**Số hiệu đoạn mã như trong nguyên bản**
**Tên tệp như trong nguyên bản (nếu có)**

```java
...
```
```

- Nếu đoạn mã bị cắt sang trang, nối lại thành một khối duy nhất trừ khi nguyên bản in "continued" ở một đoạn mã mới.
- Nếu không thể khôi phục chính xác một ký tự bị mất do trích xuất, giữ nguyên dòng đó theo cách đọc được, không thêm ghi chú vào thân bài.
- Trong mọi đoạn mã, giữ nguyên code và chuỗi ký tự; dịch chú thích trong code theo mục 3.

## 5. Bảng thuật ngữ

| English | Tiếng Việt dùng trong bản dịch |
|---|---|
| architecture | kiến trúc |
| software architecture | kiến trúc phần mềm |
| design | thiết kế |
| design decision | quyết định thiết kế |
| structure | cấu trúc |
| system | hệ thống |
| source code | mã nguồn |
| component | thành phần |
| package | gói |
| dependency | phụ thuộc |
| dependency rule | quy tắc phụ thuộc |
| entity | thực thể |
| use case | ca sử dụng |
| boundary | ranh giới |
| interface | giao diện |
| policy | chính sách |
| mechanism | cơ chế |
| plugin | plugin |
| framework | framework |
| database | cơ sở dữ liệu |
| service | dịch vụ |
| test | kiểm thử |
| test double | đối tượng thay thế trong kiểm thử |
| test-driven development (TDD) | phát triển hướng kiểm thử |
| deployment | triển khai |
| build | build |

## 6. Định dạng đầu ra

Mỗi chương là một tệp Markdown trong `books/clean-architecture/translation/vi/`, tên tệp đã định sẵn. Cấu trúc:

```markdown
# Chương 1: Thiết kế và kiến trúc là gì?

> Tác giả: Robert C. Martin

## Nội dung mục

Đoạn văn...
```

- Cấp tiêu đề: `#` cho tên chương, `##` cho mục lớn, `###` cho mục con, `####` cho mục nhỏ hơn. Bám theo cấu trúc nguyên bản.
- Bỏ dòng chạy đầu trang/chân trang và số folio của PDF.
- Không chèn mục lục hoặc lời bạt không có trong nguyên bản.
- Mục lục cuối sách gắn với số trang bản gốc nên được lược bỏ.
- File `00-front-matter.md` gồm Lời tựa, Lời nói đầu, Lời cảm ơn, Về tác giả và phần Introduction trước Chương 1.
- File `02-phan-ii.md` chứa tiêu đề Phần II và phần dẫn nhập trước Chương 3.
- File `01-chuong-01.md` đến `34-chuong-34.md` chứa từng chương theo số thứ tự gốc.
- File `35-phu-luc-a.md` chứa Phụ lục A.
- Chỉ giữ tài liệu tham khảo, chú thích và nội dung mã như trong nguồn.

## 7. Mẫu giọng văn

### Nguyên bản (Chương 1, mục tiêu)

> The goal of software architecture is to minimize the human resources required to build and maintain the required system.

### Bản dịch

> Mục tiêu của kiến trúc phần mềm là giảm thiểu nguồn lực con người cần thiết để xây dựng và bảo trì hệ thống theo yêu cầu.

### Khi rà bản dịch

- Giữ nguyên số liệu, tên riêng, định danh, số thứ tự chương và hình.
- Dịch thuật ngữ nhất quán theo ngữ cảnh, giữ nguyên tên nguyên tắc khi cần đối chiếu với tiếng Anh.
- Đối chiếu ví dụ và chú thích hình với PDF để không bỏ mất thông tin khi văn bản ngắt qua trang.
- Không tự sửa lỗi trong mã hay thêm kết luận ngoài nguyên bản.

Mỗi batch chỉ gồm một chương. Đối chiếu toàn chương với nguồn, đọc lại tiếng Việt và rà checklist bên dưới trước khi chuyển sang chương tiếp theo.

## 8. Tự kiểm tra trước khi giao

- [ ] Đã dịch đủ mọi mục, mọi đoạn, mọi chú thích hình/đoạn mã chưa?
- [ ] Có câu nào bị bỏ sót vì PDF xuống dòng lạ không?
- [ ] Code có đúng logic, đúng thụt lề, đúng tên định danh không?
- [ ] Có dấu gạch ngang dài nào trong lời dịch không? (phải bằng 0)
- [ ] Có câu kết luận/thêm thắt nào không có trong nguyên bản không?
- [ ] Đọc thành tiếng một đoạn: nghe như tiếng Việt tự nhiên hay như bản dịch?
