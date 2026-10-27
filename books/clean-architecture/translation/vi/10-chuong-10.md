# Chương 10: ISP: Nguyên tắc phân tách giao diện
![Minh họa](assets/illustrations/10-chuong-10-opener.png){w=180}

Nguyên tắc phân tách giao diện (ISP) lấy tên từ sơ đồ được hiển thị trong Hình 10.1.
**Hình 10.1** Nguyên tắc phân tách giao diện

Trong tình huống được minh họa trong Hình 10.1, có một số người dùng sử dụng các thao tác của lớp OPS. Giả sử User1 chỉ dùng op1, User2 chỉ dùng op2, và User3 chỉ dùng op3.

Bây giờ hãy tưởng tượng OPS là một lớp viết bằng ngôn ngữ kiểu Java. Rõ ràng, trong trường hợp này, mã nguồn của User1 sẽ vô tình phụ thuộc vào op2 và op3, ngay cả khi nó không gọi chúng. Sự phụ thuộc này có nghĩa là một thay đổi đối với mã nguồn của op2 trong OPS sẽ buộc User1 phải biên dịch lại và triển khai lại, mặc dù không có gì mà nó quan tâm thực sự đã thay đổi.

Vấn đề này có thể được giải quyết bằng cách phân tách các thao tác thành các giao diện như được hiển thị trong Hình 10.2.

**Hình 10.2** Các thao tác được phân tách

Lại một lần nữa, nếu chúng ta tưởng tượng việc này được triển khai bằng một ngôn ngữ kiểu tĩnh như Java, thì mã nguồn của User1 sẽ phụ thuộc vào U1Ops, và op1, nhưng sẽ *không* phụ thuộc vào OPS. Do đó, một thay đổi đối với OPS mà User1 không quan tâm sẽ không khiến User1 phải biên dịch lại và triển khai lại.

## ISP và ngôn ngữ

Rõ ràng, mô tả trước đây phụ thuộc quan trọng vào loại ngôn ngữ. Các ngôn ngữ kiểu tĩnh như Java buộc lập trình viên phải tạo các khai báo mà người dùng phải import, hoặc use, hoặc theo cách nào đó bao gồm. Chính những khai báo được bao gồm này trong mã nguồn tạo ra các phụ thuộc mã nguồn buộc phải biên dịch lại và triển khai lại.

Trong các ngôn ngữ kiểu động như Ruby và Python, những khai báo như vậy không tồn tại trong mã nguồn. Thay vào đó, chúng được suy diễn tại thời điểm chạy. Do đó không có phụ thuộc mã nguồn nào để buộc biên dịch lại và triển khai lại. Đây là lý do chính khiến các ngôn ngữ kiểu động tạo ra các hệ thống linh hoạt hơn và ít bị ràng buộc chặt chẽ hơn so với các ngôn ngữ kiểu tĩnh.

Thực tế này có thể khiến bạn kết luận rằng ISP là một vấn đề ngôn ngữ, chứ không phải vấn đề kiến trúc.

## ISP và kiến trúc

Nếu bạn lùi lại một bước và nhìn vào động lực cốt lõi của ISP, bạn có thể thấy một mối quan tâm sâu xa hơn tiềm ẩn bên dưới. Nói chung, việc phụ thuộc vào các mô-đun chứa nhiều thứ hơn những gì bạn cần là có hại. Điều này rõ ràng đúng đối với các phụ thuộc mã nguồn có thể buộc biên dịch lại và triển khai lại không cần thiết; nó cũng đúng ở một cấp độ cao hơn nhiều, cấp độ kiến trúc.

Xét ví dụ sau: một kiến trúc sư đang làm việc trên một hệ thống, S. Anh ta muốn đưa một framework nhất định, F, vào hệ thống. Giả sử các tác giả của F đã ràng buộc nó với một cơ sở dữ liệu cụ thể, D. Vậy S phụ thuộc vào F, F phụ thuộc vào D (Hình 10.3).

**Hình 10.3** Một kiến trúc gây vấn đề

Bây giờ giả sử D chứa các tính năng mà F không sử dụng và do đó S không quan tâm. Các thay đổi đối với những tính năng đó bên trong D có thể buộc phải triển khai lại F và do đó triển khai lại S. Tệ hơn, một lỗi của một trong những tính năng bên trong D có thể gây ra lỗi trong F và S.

## Kết luận

Bài học ở đây là việc phụ thuộc vào thứ mang theo hành lý mà bạn không cần có thể gây ra những rắc rối bạn không ngờ tới.

Chúng ta sẽ khám phá ý tưởng này chi tiết hơn khi thảo luận về Nguyên tắc Tái sử dụng Chung (Common Reuse Principle) trong Chương 13, "Tính gắn kết của thành phần" (Component Cohesion).