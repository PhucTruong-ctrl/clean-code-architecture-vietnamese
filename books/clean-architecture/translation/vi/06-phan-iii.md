# Phần III: Các nguyên tắc thiết kế

![Minh họa](assets/illustrations/part-iii-design-principles.png){w=300}

Hệ thống phần mềm tốt bắt đầu từ mã nguồn sạch. Về một mặt, nếu những viên gạch không được làm tốt, thì kiến trúc của tòa nhà không còn quan trọng lắm. Về mặt khác, bạn có thể tạo ra một hỗn độn đáng kể ngay cả với những viên gạch làm tốt. Chính lúc này các nguyên tắc SOLID phát huy tác dụng.

Các nguyên tắc SOLID cho chúng ta biết cách sắp xếp các hàm và cấu trúc dữ liệu thành các lớp, và những lớp đó nên được kết nối với nhau như thế nào. Việc dùng từ "lớp" (class) không ngụ ý rằng các nguyên tắc này chỉ áp dụng cho phần mềm hướng đối tượng. Một lớp đơn giản chỉ là một nhóm hàm và dữ liệu được gắn kết chặt chẽ. Mọi hệ thống phần mềm đều có những nhóm như vậy, dù chúng có được gọi là lớp hay không. Các nguyên tắc SOLID áp dụng cho những nhóm đó.

Mục tiêu của các nguyên tắc là tạo ra các cấu trúc phần mềm trung cấp mà:

- Chịu đựng được sự thay đổi,
- Dễ hiểu, và
- Là nền tảng của các thành phần (component) có thể dùng trong nhiều hệ thống phần mềm.

Thuật ngữ "trung cấp" (mid-level) ám chỉ việc các nguyên tắc này được áp dụng bởi các lập trình viên làm việc ở cấp độ mô-đun. Chúng được áp dụng ngay trên cấp độ mã nguồn và giúp định nghĩa những loại cấu trúc phần mềm được sử dụng bên trong các mô-đun và thành phần.

Cũng giống như có thể tạo ra một hỗn độn đáng kể với những viên gạch làm tốt, ta cũng có thể tạo ra một hỗn độn trải rộng toàn hệ thống với những thành phần trung cấp được thiết kế tốt. Vì lý do này, sau khi đã trình bày xong các nguyên tắc SOLID, chúng ta sẽ chuyển sang những đối ứng của chúng trong thế giới thành phần (component), và sau đó là các nguyên tắc của kiến trúc cấp cao.

Lịch sử của các nguyên tắc SOLID đã kéo dài nhiều năm. Tôi bắt đầu tập hợp chúng vào cuối thập niên 1980, khi tranh luận về nguyên tắc thiết kế phần mềm với những người khác trên USENET, một mạng xã hội sơ khai. Theo thời gian, các nguyên tắc thay đổi: một số bị loại bỏ, một số được gộp lại, số khác được bổ sung. Nhóm nguyên tắc cuối cùng ổn định vào đầu những năm 2000, dù tôi trình bày chúng theo một thứ tự khác.

Khoảng năm 2004, Michael Feathers gửi email cho tôi và chỉ ra rằng nếu sắp xếp lại các nguyên tắc, chữ cái đầu sẽ ghép thành từ SOLID. Từ đó, các nguyên tắc SOLID ra đời.

Những chương tiếp theo sẽ mô tả từng nguyên tắc kỹ hơn. Dưới đây là tóm tắt điều hành:

- **SRP: Nguyên tắc Trách nhiệm Đơn nhất (Single Responsibility Principle)**
  Một hệ quả chủ động của định luật Conway: Cấu trúc tốt nhất cho một hệ thống phần mềm chịu ảnh hưởng lớn bởi cấu trúc xã hội của tổ chức sử dụng nó, sao cho mỗi mô-đun phần mềm có một, và chỉ có một, lý do để thay đổi.

- **OCP: Nguyên tắc Đóng-Mở (Open-Closed Principle)**
  Bertrand Meyer làm cho nguyên tắc này nổi tiếng trong những năm 1980. Ý chính là để hệ thống phần mềm dễ thay đổi, chúng phải được thiết kế để cho phép hành vi của những hệ thống đó được thay đổi bằng cách thêm mã mới, thay vì sửa đổi mã hiện có.

- **LSP: Nguyên tắc Thay thế Liskov (Liskov Substitution Principle)**
  Định nghĩa nổi tiếng của Barbara Liskov về kiểu con (subtype), từ năm 1988. Tóm lại, nguyên tắc này nói rằng để xây dựng hệ thống phần mềm từ các bộ phận có thể hoán đổi cho nhau, những bộ phận đó phải tuân thủ một hợp đồng cho phép chúng được thay thế lẫn nhau.

- **ISP: Nguyên tắc Tách biệt Giao diện (Interface Segregation Principle)**
  Nguyên tắc này khuyên các nhà thiết kế phần mềm tránh phụ thuộc vào những thứ mà họ không sử dụng.

- **DIP: Nguyên tắc Đảo ngược Phụ thuộc (Dependency Inversion Principle)**
  Mã triển khai chính sách cấp cao không nên phụ thuộc vào mã triển khai chi tiết cấp thấp. Ngược lại, chi tiết nên phụ thuộc vào chính sách.

Các nguyên tắc này đã được mô tả chi tiết trong nhiều ấn bản khác nhau[^1] qua nhiều năm. Những chương tiếp theo sẽ tập trung vào những hàm ý kiến trúc của các nguyên tắc thay vì lặp lại những thảo luận chi tiết đó. Nếu bạn chưa quen thuộc với các nguyên tắc này, nội dung tiếp theo không đủ để hiểu chúng một cách chi tiết và bạn nên học chúng trong các tài liệu được trích dẫn ở chân trang.

[^1]: Ví dụ, *Agile Software Development, Principles, Patterns, and Practices*, Robert C. Martin, Prentice Hall, 2002, http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod, và https://en.wikipedia.org/wiki/SOLID_(object-oriented_design) (hoặc chỉ cần google SOLID).