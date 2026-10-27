# Chương 7: SRP: Nguyên tắc trách nhiệm đơn nhất
![Minh họa](assets/illustrations/07-chuong-07-opener.png){w=240}

Trong số tất cả các nguyên tắc SOLID, Nguyên tắc Trách nhiệm Đơn nhất (SRP) có lẽ là nguyên tắc được hiểu lầm nhiều nhất. Điều này có lẽ vì nó có một cái tên đặc biệt không phù hợp. Quá dễ dàng để các lập trình viên nghe cái tên và giả định rằng nó có nghĩa là mọi mô-đun nên chỉ làm một việc duy nhất.

Đừng nhầm lẫn: có một nguyên tắc nói rằng hàm nên làm một việc, và chỉ một việc. Ta áp dụng nguyên tắc đó khi tái cấu trúc hàm lớn thành các hàm nhỏ hơn, tức ở cấp thấp nhất. Nhưng nguyên tắc ấy không nằm trong SOLID. Đó cũng không phải SRP.

Trước đây, SRP thường được phát biểu như sau:

> Một mô-đun nên có một, và chỉ một, lý do để thay đổi.

Hệ thống phần mềm được thay đổi để thỏa mãn người dùng và các bên liên quan; những người dùng và bên liên quan đó chính là "lý do để thay đổi" mà nguyên tắc đề cập đến. Thực tế, chúng ta có thể diễn đạt lại nguyên tắc như sau:

> Một mô-đun nên chịu trách nhiệm đối với một, và chỉ một, người dùng hoặc bên liên quan.

Thật không may, "người dùng" và "bên liên quan" không phải là những từ thật phù hợp ở đây. Có thể nhiều người dùng hoặc bên liên quan cùng muốn hệ thống được thay đổi theo một cách. Thực ra, ta đang nói đến một nhóm, gồm một hay nhiều người yêu cầu thay đổi đó. Ta gọi nhóm ấy là một **tác nhân (actor)**.

Như vậy, phiên bản cuối cùng của SRP là:

> Một mô-đun nên chịu trách nhiệm đối với một, và chỉ một, tác nhân.

Bây giờ, chúng ta hiểu từ "mô-đun" (module) theo ý gì? Định nghĩa đơn giản nhất chỉ là một tệp nguồn (source file). Hầu như mọi lúc định nghĩa đó đều hoạt động tốt. Một số ngôn ngữ và môi trường phát triển, tuy nhiên, không dùng tệp nguồn để chứa mã của họ. Trong những trường hợp đó, một mô-đun chỉ là một tập hợp các hàm và cấu trúc dữ liệu có sự gắn kết (cohesive).

Từ "gắn kết" hàm ý SRP. Sự gắn kết là lực kết nối mã chịu trách nhiệm cho một tác nhân duy nhất.

Cách tốt nhất để hiểu nguyên tắc này có lẽ là nhìn vào các triệu chứng của việc vi phạm nó.

## Triệu chứng 1: Trùng lặp ngẫu nhiên (Accidental Duplication)

Ví dụ yêu thích của tôi là lớp `Employee` (Nhân viên) từ một ứng dụng tính lương. Nó có ba phương thức: `calculatePay()` (tính lương), `reportHours()` (báo cáo giờ làm), và `save()` (lưu) (Hình 7.1).

**Hình 7.1** Lớp Employee

Lớp này vi phạm SRP vì ba phương thức đó chịu trách nhiệm cho ba tác nhân rất khác nhau.

- Phương thức `calculatePay()` được quy định bởi bộ phận kế toán, bộ phận này báo cáo cho CFO (Giám đốc tài chính).
- Phương thức `reportHours()` được quy định và sử dụng bởi bộ phận nhân sự (human resources), bộ phận này báo cáo cho COO (Giám đốc điều hành).
- Phương thức `save()` được quy định bởi các quản trị cơ sở dữ liệu (DBA), những người báo cáo cho CTO (Giám đốc công nghệ).

Bằng cách đặt mã nguồn của ba phương thức này trong cùng một lớp `Employee`, các nhà phát triển đã khiến ba tác nhân phụ thuộc lẫn nhau. Vì thế, hành động của đội ngũ CFO có thể ảnh hưởng đến công việc mà đội ngũ COO dựa vào.

Ví dụ, giả sử hàm `calculatePay()` và hàm `reportHours()` chia sẻ một thuật toán chung để tính giờ làm không tăng ca (non-overtime hours). Giả sử thêm rằng các nhà phát triển, những người cẩn thận không lặp lại mã, đã đặt thuật toán đó vào một hàm tên là `regularHours()` (Hình 7.2).

**Hình 7.2** Thuật toán chung

Bây giờ giả sử đội ngũ CFO quyết định rằng cách tính giờ không tăng ca cần được điều chỉnh. Ngược lại, đội ngũ COO ở bộ phận nhân sự *không* muốn điều chỉnh cụ thể đó vì họ sử dụng giờ không tăng ca cho một mục đích khác.

Một nhà phát triển được giao làm thay đổi, và thấy hàm `regularHours()` tiện lợi được gọi bởi phương thức `calculatePay()`. Thật không may, nhà phát triển đó không nhận ra hàm này *cũng* được gọi bởi hàm `reportHours()`.

Nhà phát triển thực hiện thay đổi yêu cầu và kiểm tra cẩn thận. Đội ngũ CFO xác nhận hàm mới hoạt động như mong muốn, và hệ thống được triển khai.

Đội ngũ COO không biết chuyện đó đang xảy ra. Nhân viên nhân sự vẫn dùng các báo cáo do `reportHours()` tạo ra, nhưng giờ đây chúng chứa số liệu sai. Cuối cùng vấn đề bị phát hiện. COO nổi giận vì dữ liệu sai đã làm ngân sách của ông thiệt hại hàng triệu đô-la.

Chúng ta đều từng thấy chuyện như thế xảy ra. Những vấn đề này xuất hiện vì mã mà các tác nhân khác nhau phụ thuộc vào bị đặt quá gần nhau. SRP yêu cầu tách riêng phần mã mà các tác nhân khác nhau dựa vào.

## Triệu chứng 2: Hợp nhất (Merges)

Không khó để thấy rằng các tệp nguồn chứa nhiều phương thức khác nhau thường xuyên phải hợp nhất. Điều này càng dễ xảy ra khi các phương thức phục vụ những tác nhân khác nhau.

Ví dụ, giả sử đội ngũ DBA của CTO quyết định nên có một thay đổi lược đồ (schema) đơn giản cho bảng `Employee` của cơ sở dữ liệu. Giả sử thêm rằng đội ngũ nhân viên nhân sự của COO quyết định họ cần thay đổi định dạng của báo cáo giờ.

Hai nhà phát triển khác nhau, có thể thuộc hai đội khác nhau, check out lớp `Employee` rồi bắt đầu sửa đổi. Thật không may, các thay đổi của họ xung đột và phải hợp nhất.

Hẳn không cần nói thêm rằng các lần hợp nhất đều rủi ro. Công cụ ngày nay khá tốt, nhưng không công cụ nào xử lý được mọi trường hợp. Cuối cùng vẫn luôn có rủi ro.

Trong ví dụ của chúng ta, lần hợp nhất khiến cả CTO và COO đều phải chịu rủi ro. Không thể loại trừ khả năng CFO cũng bị ảnh hưởng.

Có nhiều triệu chứng khác mà chúng ta có thể điều tra, nhưng tất cả đều liên quan đến việc nhiều người thay đổi cùng một tệp nguồn vì những lý do khác nhau.

Một lần nữa, cách tránh vấn đề này là tách riêng phần mã hỗ trợ các tác nhân khác nhau.

## Giải pháp (Solutions)

Có nhiều giải pháp khác nhau cho vấn đề này. Mỗi giải pháp di chuyển các hàm vào các lớp khác nhau.

Cách rõ ràng nhất để giải quyết vấn đề có lẽ là tách dữ liệu khỏi các hàm. Ba lớp dùng chung `EmployeeData`, một cấu trúc dữ liệu đơn giản không có phương thức nào (Hình 7.3). Mỗi lớp chỉ chứa mã cần thiết cho chức năng riêng. Ba lớp không được phép biết về nhau. Nhờ vậy, tránh được việc vô tình tạo mã trùng lặp.

**Hình 7.3** Ba lớp không biết về nhau

Nhược điểm của giải pháp này là các nhà phát triển phải khởi tạo và quản lý ba lớp. Một cách phổ biến để giải quyết tình thế đó là dùng mẫu Facade (Hình 7.4).

**Hình 7.4** Mẫu Facade

`EmployeeFacade` chứa rất ít mã. Nó chịu trách nhiệm khởi tạo các lớp chứa hàm rồi ủy quyền công việc cho chúng.

Một số nhà phát triển thích giữ các quy tắc nghiệp vụ quan trọng nhất gần với dữ liệu. Điều này có thể làm được bằng cách giữ phương thức quan trọng nhất trong lớp `Employee` ban đầu, rồi dùng lớp đó làm Facade cho các chức năng phụ hơn (Hình 7.5).

**Hình 7.5** Phương thức quan trọng nhất được giữ trong lớp Employee ban đầu và dùng làm Facade cho các chức năng phụ

Bạn có thể phản đối các giải pháp này với lý do rằng mỗi lớp sẽ chỉ chứa một hàm. Điều này hầu như không đúng. Số lượng hàm cần thiết để tính lương, tạo báo cáo, hoặc lưu dữ liệu trong mỗi trường hợp có thể lớn. Mỗi lớp trong số đó sẽ có nhiều phương thức private (riêng tư).

Mỗi lớp chứa một họ các phương thức như vậy là một phạm vi (scope). Bên ngoài phạm vi đó, không ai biết đến sự tồn tại của các thành viên private trong họ đó.

## Kết luận

SRP nói về hàm và lớp, nhưng nó còn xuất hiện dưới hình thức khác ở hai cấp độ nữa. Ở cấp thành phần, nó trở thành Nguyên tắc Đóng chung (Common Closure Principle). Ở cấp kiến trúc, nó trở thành Trục Thay đổi (Axis of Change), yếu tố tạo ra các Ranh giới Kiến trúc (Architectural Boundaries). Các chương sau sẽ bàn về những ý tưởng này.
