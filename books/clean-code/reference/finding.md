# Clean Code VI: kết quả sửa theo rà soát

PDF hiện tại: `dist/clean-code-vi.pdf`, 437 trang, SHA-256 `44756ff3b50faf575969ff68dda31a0bfdad32e3c943fc0f64d308fc3d797ed1`. Nguồn là các tệp `books/clean-code/translation/vi/*.md` và `books/clean-code/layout.tex`.

## Findings đã xử lý

### F1 — P2: “implicity” bị dịch thành thuật ngữ gây hiểu nhầm
- Nguồn: `books/clean-code/translation/vi/02-ten-co-y-nghia.md:42`.
- Trước sửa: “tính hàm ẩn của nó”.
- Gốc Anh: “the implicity of the code (to coin a phrase): the degree to which the context is not explicit in the code itself.”
- Vị trí: PDF tr. 40, folio in 18.
- Vấn đề: “hàm ẩn” thường chỉ một implicit function trong toán học; cụm “tính hàm ẩn” không diễn đạt tự nhiên khái niệm “mức độ thông tin/bối cảnh không được nói rõ trong mã”. Phần giải thích kế tiếp có truyền được ý, nhưng thuật ngữ chính dễ làm người đọc hiểu sai.
- Gợi ý: “tính ngầm ẩn” hoặc “mức độ ngầm ẩn của mã”.
- Đã sửa trong `books/clean-code/translation/vi/02-ten-co-y-nghia.md`: “mức độ ngầm ẩn”.

### F2 — P2: “generation date/timestamp” bị dịch thành “ngày giờ sinh/dấu thời gian sinh”
- Nguồn: `books/clean-code/translation/vi/02-ten-co-y-nghia.md:145,167`.
- Trước sửa: “ngày giờ sinh” và “Dấu thời gian sinh lại được đặt vào ngày mai!”.
- Gốc Anh: “generation date” và “The generation timestamp is set to tomorrow’s date!”
- Vị trí: PDF tr. 44, folio in 22.
- Vấn đề: “generation” ở đây là thời điểm tạo bản ghi, không phải sinh nhật/ngày giờ sinh. Cách dịch làm câu ví dụ về timestamp thành ngày sinh.
- Gợi ý: “ngày giờ tạo” / “thời điểm tạo bản ghi”.
- Đã sửa trong `books/clean-code/translation/vi/02-ten-co-y-nghia.md`: “ngày tạo” và “thời điểm tạo”.

### F3 — P2: Thành ngữ “time to kill” dịch nguyên văn
- Nguồn: `books/clean-code/translation/vi/04-chu-thich.md:175-177`.
- Trước sửa: “Đừng chạy trừ khi bạn có thời gian để giết.”
- Gốc Anh: “Don’t run unless you have some time to kill.”
- Vị trí: PDF tr. 80, folio in 58.
- Vấn đề: “time to kill” nghĩa là có thời gian rảnh/dư dả; “thời gian để giết” không truyền được thành ngữ và nghe như giết người.
- Gợi ý: “Chỉ chạy nếu bạn có nhiều thời gian rảnh” hoặc “Đừng chạy trừ khi bạn đang dư thời gian”.
- Đã sửa chú thích trong `books/clean-code/translation/vi/04-chu-thich.md` thành “có thời gian rảnh rỗi”.

### F4 — P2: “starvation” dùng sai thuật ngữ kỹ thuật
- Nguồn: `books/clean-code/translation/vi/13-dong-thoi.md:159-160`.
- Trước sửa, nhãn bảng: “Nghẽn tài nguyên”.
- Gốc Anh: “Starvation”. Cùng mục giải thích một luồng bị ngăn không cho tiếp tục; các chỗ khác trong chính chương dùng “bị bỏ đói” cho trường hợp này.
- Vị trí: PDF tr. 204, folio in 182.
- Vấn đề: tên thuật ngữ trong bảng không khớp với khái niệm được định nghĩa và cách dịch dùng ở phần sau.
- Gợi ý: thống nhất thành “bỏ đói luồng” hoặc thuật ngữ chuẩn khác, rồi dùng nhất quán.
- Đã đổi nhãn thuật ngữ trong `books/clean-code/translation/vi/13-dong-thoi.md` thành “Bỏ đói luồng”.

### F5 — P3: Tên hàm bị đổi một chữ
- Nguồn: `books/clean-code/translation/vi/07-xu-ly-loi.md:306`.
- Trước sửa: “Nếu sửa `getEmployee` để nó trả về một danh sách rỗng”.
- Gốc Anh: “If we change `getEmployees` so that it returns an empty list”.
- Vị trí: PDF tr. 134, folio in 112.
- Vấn đề: tên hàm số nhiều trong bản gốc thành số ít; không khớp với các đoạn mã trước và sau.
- Gợi ý: sửa thành `getEmployees`.
- Đã sửa thành `getEmployees` trong `books/clean-code/translation/vi/07-xu-ly-loi.md`.

### F6 — P3: “nearly every other line” bị phóng đại
- Nguồn: `books/clean-code/translation/vi/07-xu-ly-loi.md:273`.
- Trước sửa: “gần như dòng nào cũng có một phép kiểm tra null”.
- Gốc Anh: “nearly every other line was a check for null.”
- Vị trí: PDF tr. 133, folio in 111.
- Vấn đề: “every other line” nghĩa là gần như cứ cách một dòng lại có một phép kiểm tra; bản Việt biến thành gần như dòng nào cũng có, phóng đại tần suất.
- Gợi ý: “gần như cứ hai dòng thì một dòng là kiểm tra null”.
- Đã đổi thành “gần như cứ hai dòng mã lại có một lần kiểm tra null”.

### F7 — P2: Thuật ngữ SRP không nhất quán xuyên sách
- Ví dụ nguồn: `books/clean-code/translation/vi/01-ma-sach.md:272`; `books/clean-code/translation/vi/03-ham.md:220`; `books/clean-code/translation/vi/10-lop.md:136-137`; `books/clean-code/translation/vi/13-dong-thoi.md:88-90`; `books/clean-code/translation/vi/17-mui-code-va-nguyen-tac.md:268`; `books/clean-code/translation/vi/18-phu-luc-a-dong-thoi-2.md:108`.
- Các bản Việt gồm: “Nguyên lý Trách nhiệm Đơn nhất”, “Nguyên lý Trách nhiệm Đơn”, “Nguyên tắc trách nhiệm đơn nhất”, “Nguyên tắc trách nhiệm đơn” và “Nguyên tắc trách nhiệm đơn lẻ”.
- Gốc Anh: đều là “Single Responsibility Principle (SRP)”.
- Vị trí ví dụ: PDF tr. 38/folio 16; tr. 162/folio 140; tr. 202/folio 180; các chỗ còn lại ở chương 17 và Phụ lục A.
- Vấn đề: cùng một nguyên tắc thiết kế có nhiều tên và hai cách dịch “principle”, làm khó tra cứu và gây cảm giác không nhất quán.
- Gợi ý: thống nhất một dạng, chẳng hạn “Nguyên tắc Trách nhiệm Đơn nhất (SRP)”.
- Đã thống nhất thành “Nguyên tắc Trách nhiệm Đơn nhất” ở những chỗ trước đây dùng biến thể khác.

### F8 — P3: Chơi chữ trong “Team Rules” chưa được tái tạo
- Nguồn: `books/clean-code/translation/vi/05-dinh-dang.md:544-550`.
- Trước sửa: tiêu đề “Quy tắc của nhóm”; câu mở nói đây là “một cách chơi chữ”, rồi viết “quy tắc của nhóm là trên hết”.
- Gốc Anh: “Team Rules”; “The title of this section is a play on words. Every programmer has his own favorite formatting rules, but if he works in a team, then the team rules.”
- Vị trí: PDF tr. 113, folio 91.
- Vấn đề: ý ưu tiên quy tắc chung của nhóm vẫn có, nhưng cách chơi chữ “rules” (danh từ “quy tắc”, động từ “chi phối”) không được tái tạo. Lời giới thiệu về chơi chữ vì vậy hứa một hiệu ứng không còn hiện diện rõ trong bản dịch.
- Gợi ý: viết lại câu để tái tạo ý chơi chữ hoặc bỏ câu dẫn “một cách chơi chữ”.
- Đã đổi tiêu đề thành “Luật chơi của nhóm” và dùng cụm “theo luật chơi chung” thay cho lời giải thích dựa trên tiếng Anh.

### F9 — Tham chiếu G23 `??-44` trong bản gốc
- Nguồn: `books/clean-code/translation/vi/20-phu-luc-c-tham-chieu-cheo.md:38`.
- Trước sửa: `G23: ??-44, 14-239, 16-295, 17-313`.
- Gốc Anh trong Appendix C cũng ghi `G23 ... ??-44, 14-239, 16-295, 17-313`.
- Vị trí: PDF tr. 434, folio 412.
- Vấn đề: `??-44` không phải tham chiếu tra cứu dùng được. Đây là lỗi đã có trong bản gốc, không phải lỗi dịch. README chủ động giữ các dẫn chiếu trang tiếng Anh, nhưng không giải thích placeholder này.
- Gợi ý: tra cứu ngược G23 tại đoạn gốc ở trang 44; nếu không xác định được, bỏ placeholder hoặc ghi chú rõ đây là lỗi của bản gốc.
- Đã bỏ tham chiếu hỏng `??-44` khỏi `books/clean-code/translation/vi/20-phu-luc-c-tham-chieu-cheo.md`; giữ lại ba tham chiếu còn dùng được. Trang 44 của bản Anh không xác nhận được G23 nên không tự suy đoán số chương.

### F10 — P2: Bìa gán mơ hồ Pearson Education cho bản dịch tiếng Việt
- Vị trí: PDF tr. 1.
- Bìa đặt “Pearson Education” ngay dưới nhãn “Bản dịch tiếng Việt”, nên có thể được hiểu là Pearson là đơn vị dịch hoặc phát hành bản dịch này.
- Ghi chú “Về bản dịch” ở PDF tr. 437 nói đây là bản dịch phục vụ học tập cá nhân; không nêu Pearson là đơn vị dịch/phát hành bản Việt. Pearson là nhà xuất bản của ấn bản gốc.
- Vấn đề: ghi nhận hiện tại gây nhầm lẫn về nguồn gốc/đơn vị phát hành bản dịch.
- Gợi ý: bỏ dòng này hoặc ghi rõ vai trò của Pearson (nhà xuất bản bản gốc), và nêu đúng dịch giả/đơn vị phát hành nếu có.
- Đã thay Pearson Education trên trang tên sách bằng “Dùng cho mục đích học tập cá nhân”; thông tin bản quyền Pearson vẫn giữ ở trang bản quyền.

### F11 — Thành ngữ “deadly embrace”
- Nguồn: `books/clean-code/translation/vi/18-phu-luc-a-dong-thoi-2.md:726`.
- Trước sửa: “vòng ôm chết người”.
- Đã đổi thành “vòng tay tử thần”, một cách nói tự nhiên hơn trong ngữ cảnh hai luồng giữ tài nguyên của nhau.

### F12 — Câu đùa về tên biến `genymdhms`
- Nguồn: `books/clean-code/translation/vi/02-ten-co-y-nghia.md:145`.
- Bản dịch đã làm rõ mọi người đánh vần các chữ viết tắt theo tên chữ cái tiếng Anh, còn người kể đọc chuỗi theo mặt chữ. Giữ nguyên tên biến và hai cách phát âm trong bản gốc.

## Ghi chú

- “Don’t Pun” được dịch là “Đừng chơi chữ”; phần giải thích và ví dụ `add`/`insert`/`append` vẫn có nghĩa trong tiếng Việt. Giữ nguyên các tên phương thức.
- “Temporal coupling” đã thống nhất thành “sự phụ thuộc vào thời điểm” trong `books/clean-code/translation/vi/03-ham.md`, `books/clean-code/translation/vi/15-ben-trong-junit.md` và `books/clean-code/translation/vi/17-mui-code-va-nguyen-tac.md`.
- Appendix A có `startAllThreadsw`, nhưng bản gốc cũng có cùng lỗi; theo README, lỗi trong mã gốc được giữ nguyên. Một số lỗi code/sample prose ở Appendix A cũng có trong bản gốc và không được tính là lỗi dịch.
- Chú thích tác giả ở đầu Lời tựa trông liền dòng với đoạn văn khi trích xuất chữ, nhưng ảnh trang cho thấy nó được căn giữa riêng; không tính là lỗi dàn trang.

## Trạng thái

Rà soát nội dung bao phủ phần trước lời tựa, Chương 1–17, Phụ lục A–C, Lời kết và ghi chú Về bản dịch. Findings đã được sửa trong nguồn và dựng lại PDF.
Kiểm chứng: `./build.sh clean-code` thành công với 437 trang, 0 overfull và 1 underfull hbox; `python3 tools/qa_check.py clean-code` báo 0 vấn đề trên 23 tệp. Hai bản PDF có cùng SHA-256. Font được nhúng; kiểm tra bounding box cả 437 trang không thấy chữ vượt lề hay trang rỗng. Đã xem trực quan các trang có chỉnh sửa.
Giới hạn: chưa hiệu đính song ngữ từng câu theo quy trình chuyên nghiệp; không thể chứng nhận bản dịch không còn lỗi.
