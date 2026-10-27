# Hướng dẫn dịch Clean Code sang tiếng Việt

Tài liệu này dành cho người dịch (kể cả agent). Đọc hết trước khi bắt tay vào bất kỳ chương nào.

## 1. Mục tiêu

Dịch **toàn bộ** cuốn *Clean Code: A Handbook of Agile Software Craftsmanship* của Robert C. Martin sang tiếng Việt hiện đại, đọc như sách do người Việt viết cho lập trình viên Việt, không phải bản dịch máy từng câu.

Bản dịch phải:
- Giữ đúng nội dung, ví dụ, con số, trích dẫn, thứ tự mục, ghi chú chân trang và sắc thái của tác giả.
- Không tóm tắt, không lược bỏ, không thêm bình luận của người dịch vào thân bài.
- Dịch đủ mọi đoạn văn xuôi, tiêu đề mục, chú thích hình/đoạn mã, bảng, và lời dẫn.
- Giữ nguyên mã nguồn, tên định danh, tên tệp, tên thư viện, URL, số hiệu đoạn mã.

## 2. Giọng văn

Tác giả viết ở ngôi thứ nhất, kể chuyện nghề, có chỗ tự trào, có chỗ gay gắt. Bản dịch phải giữ được chất giọng đó.

- Xưng "tôi" khi tác giả kể chuyện riêng; "chúng tôi" khi nói thay nhóm tác giả. Gọi người đọc là "bạn".
- Câu văn kỹ thuật: rõ ràng, dứt khoát, không rào đón. Ưu tiên thể chủ động.
- Được phép dùng từ chuyên môn tiếng Anh khi tiếng Việt không có tương đương tự nhiên (xem bảng thuật ngữ). Lần đầu xuất hiện có thể kèm nguyên ngữ trong ngoặc.
- Câu dài ngắn xen kẽ. Đừng dịch mỗi câu tiếng Anh thành một câu tiếng Việt cùng độ dài; hãy tách, gộp, đảo trật tự khi tiếng Việt cần.
- Tránh văn phong "dịch máy": không lặp "của nó", "được thực hiện bởi", "việc mà", "một cách", "những cái". Không dịch sát từng giới từ.
- Với thành ngữ hoặc ẩn dụ khó hiểu khi dịch sát, ưu tiên cách diễn đạt tự nhiên; nếu cần giữ nguyên hình ảnh của câu trích dẫn, làm rõ nghĩa ngắn gọn trong ngữ cảnh, không gán lời giải thích vào trích dẫn.
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

- Mã nguồn: cú pháp, tên biến/hàm/lớp, chuỗi ký tự, chú thích cuối dòng trong code minh họa.
- Tên tệp, tên lớp, tên gói, API, thư viện, framework: `HtmlUtil.java`, `ArgsException`, `JUnit`, `FitNesse`, `log4j`, `AspectJ`.
- Tên người, tên sách, tên bài báo, tên công ty, địa danh: Robert C. Martin, Kent Beck, *Refactoring*, Object Mentor.
- URL, số ISBN, số hiệu đoạn mã (`Listing 3-1` → `Đoạn mã 3-1`), số chương/mục.
- Câu trích dẫn bằng tiếng nước ngoài: giữ nguyên câu gốc, thêm bản dịch trong ngoặc nếu cần. Ví dụ câu tiếng Đan Mạch trong Lời tựa.
- Các từ khóa của ngôn ngữ lập trình, thông báo lỗi, chuỗi trong `String.format`.

Chú thích trong code: dịch sang tiếng Việt, giữ nguyên vị trí và ý nghĩa. Không dịch chuỗi ký tự trong code.

## 4. Xử lý mã nguồn khi chuyển sang Markdown

Bản PDF khi trích xuất làm xô lệch thụt lề và đôi khi cắt dòng. Người dịch phải dựng lại đoạn mã thành khối ``` ngôn ngữ``` sao cho:
- Đúng logic, đúng thứ tự dòng, đúng dấu ngoặc. Không sáng tác thêm, không "sửa" code.
- Thụt lề theo cấu trúc (2 hoặc 4 dấu cách, thống nhất trong cùng một đoạn).
- Giữ tiêu đề đoạn mã ngay trên khối code:

```markdown
**Đoạn mã 3-1**
**HtmlUtil.java (FitNesse 20070619)**

```java
...
```
```

- Nếu đoạn mã bị cắt sang trang, nối lại thành một khối duy nhất trừ khi nguyên bản in "continued" ở một đoạn mã mới.
- Nếu không thể khôi phục chính xác một ký tự bị mất do trích xuất, giữ nguyên dòng đó theo cách đọc được, không thêm ghi chú vào thân bài.

Với phụ lục B (danh sách mã nguồn dài), giữ nguyên code và chú thích tiếng Anh trong code, chỉ dịch tiêu đề, lời dẫn và chú thích đoạn mã.

## 5. Bảng thuật ngữ

| English | Tiếng Việt dùng trong bản dịch |
|---|---|
| clean code | mã sạch |
| code | mã (hoặc "code" khi nói về thói quen nghề) |
| craftsmanship | tay nghề |
| Agile | Agile (linh hoạt) |
| function | hàm |
| method | phương thức |
| class | lớp |
| object | đối tượng |
| data structure | cấu trúc dữ liệu |
| variable | biến |
| constant | hằng |
| argument | đối số |
| parameter | tham số |
| return value | giá trị trả về |
| exception | ngoại lệ |
| error handling | xử lý lỗi |
| unit test | kiểm thử đơn vị |
| test | kiểm thử |
| test case | ca kiểm thử |
| refactoring | tái cấu trúc |
| naming | đặt tên |
| comment | chú thích |
| formatting | định dạng mã |
| boundary | ranh giới |
| third-party code | mã của bên thứ ba |
| dependency injection | tiêm phụ thuộc |
| concurrency | xử lý đồng thời |
| thread | luồng |
| deadlock | bế tắc (deadlock) |
| race condition | điều kiện tranh chấp |
| side effect | tác dụng phụ |
| flag argument | đối số cờ |
| code smell | mùi code (code smell) |
| heuristic | nguyên tắc kinh nghiệm (heuristic) |
| readability | khả năng đọc |
| maintainability | khả năng bảo trì |
| duplication | trùng lặp |
| abstraction | trừu tượng hóa |
| encapsulation | đóng gói |
| cohesion | độ gắn kết |
| coupling | sự phụ thuộc |
| polymorphism | đa hình |
| inheritance | kế thừa |
| interface | giao diện |
| library | thư viện |
| framework | framework |
| build | build |
| deployment | triển khai |
| legacy code | mã cũ |
| mess | mớ hỗn độn |
| rot | mục ruỗng |
| schedule | tiến độ |
| estimate | ước lượng |
| customer | khách hàng |
| programmer | lập trình viên |
| developer | nhà phát triển |
| code review | review mã |
| pair programming | lập trình cặp |
| scope | phạm vi |

## 6. Định dạng đầu ra

Mỗi chương là một tệp Markdown trong `vi/`, tên tệp đã định sẵn. Cấu trúc:

```markdown
# Chương 3: Hàm

> Tác giả: ...

## Nội dung mục

Đoạn văn...
```

- Cấp tiêu đề: `#` cho tên chương, `##` cho mục lớn, `###` cho mục con, `####` cho mục nhỏ hơn. Bám theo cấu trúc nguyên bản.
- Giữ số thứ tự mục nếu nguyên bản có (C1, G5, N1...).
- Bỏ dòng chạy đầu trang/chân trang của PDF ("Chapter 2: Meaningful Names", số trang).
- Không chèn mục lục, không chèn lời bạt của người dịch.
- Cuối chương giữ nguyên mục "Bibliography"/"Tài liệu tham khảo": dịch từ "Bibliography" nhưng giữ nguyên tên sách, tác giả, nhà xuất bản, năm.

## 7. Mẫu giọng văn

Nguyên bản (Lời tựa):

> One of our favorite candies here in Denmark is Ga-Jol, whose strong licorice vapors are a perfect complement to our damp and often chilly weather. Part of the charm of Ga-Jol to us Danes is the wise or witty sayings printed on the flap of every box top.

Bản dịch:

> Ở Đan Mạch, một trong những viên kẹo chúng tôi thích nhất là Ga-Jol. Mùi cam thảo nồng của nó hợp một cách hoàn hảo với tiết trời ẩm ướt và thường lạnh lẽo nơi đây. Với người Đan Mạch chúng tôi, một phần duyên dáng của Ga-Jol nằm ở những câu danh ngôn thông thái hoặc dí dỏm in trên nắp mỗi hộp.

Nguyên bản (Chương 2):

> The name of a variable, function, or class, should answer all the big questions. It should tell you why it exists, what it does, and how it is used. If a name requires a comment, then the name does not reveal its intent.

Bản dịch:

> Tên của một biến, một hàm hay một lớp phải trả lời được những câu hỏi lớn. Nó phải cho bạn biết thứ đó tồn tại để làm gì, nó làm gì và được dùng ra sao. Nếu một cái tên cần đến chú thích thì cái tên đó chưa thể hiện được ý định.

## 8. Tự kiểm tra trước khi giao

- [ ] Đã dịch đủ mọi mục, mọi đoạn, mọi chú thích hình/đoạn mã chưa?
- [ ] Có câu nào bị bỏ sót vì PDF xuống dòng lạ không?
- [ ] Code có đúng logic, đúng thụt lề, đúng tên định danh không?
- [ ] Có dấu gạch ngang dài nào trong lời dịch không? (phải bằng 0)
- [ ] Có câu kết luận/thêm thắt nào không có trong nguyên bản không?
- [ ] Đọc thành tiếng một đoạn: nghe như tiếng Việt tự nhiên hay như bản dịch?
