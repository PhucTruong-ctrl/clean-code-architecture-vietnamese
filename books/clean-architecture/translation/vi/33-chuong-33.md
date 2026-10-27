# Chương 33: Nghiên cứu tình huống: Bán video
![Minh họa](assets/illustrations/33-chuong-33-opener.png){w=300}

Đã đến lúc tập hợp các quy tắc và ý tưởng về kiến trúc vào một nghiên cứu tình huống. Nghiên cứu này ngắn và đơn giản, nhưng minh họa quy trình mà kiến trúc sư giỏi sử dụng cùng những quyết định họ đưa ra.

## Sản phẩm

Trong nghiên cứu tình huống này, tôi chọn sản phẩm mà mình khá am hiểu: phần mềm cho một trang web bán video. Tất nhiên, nó gợi nhớ đến cleancoders.com, trang web nơi tôi bán các video hướng dẫn phần mềm.

Ý tưởng cơ bản rất đơn giản. Chúng ta có một bộ video muốn bán trên web cho cả cá nhân và doanh nghiệp. Cá nhân có thể trả một mức giá để xem trực tuyến và mức giá cao hơn để tải video về và sở hữu vĩnh viễn. Giấy phép doanh nghiệp chỉ cho phép xem trực tuyến, được mua theo lô và có chiết khấu theo số lượng.

Thông thường, cá nhân vừa là người xem vừa là người mua. Ngược lại, trong doanh nghiệp, người mua video thường khác với người sẽ xem chúng.

Tác giả video cần cung cấp tệp video, phần mô tả bằng văn bản và các tệp bổ trợ gồm bài thi, bài tập, lời giải, mã nguồn cùng những tài liệu khác.

Quản trị viên cần thêm loạt video mới, thêm hoặc xóa video khỏi loạt và thiết lập giá cho các loại giấy phép khác nhau.

Bước đầu tiên để xác định kiến trúc ban đầu của hệ thống là nhận diện các tác nhân và ca sử dụng.

## Phân tích ca sử dụng

Hình 33.1 cho thấy một phân tích ca sử dụng điển hình.

**Hình 33.1** Một phân tích ca sử dụng điển hình

Có thể nhận ra bốn tác nhân chính. Theo Nguyên tắc Trách nhiệm Đơn nhất, bốn tác nhân này sẽ là bốn nguồn thay đổi chính của hệ thống. Mỗi khi thêm tính năng mới hoặc thay đổi tính năng hiện có, thay đổi đó sẽ nhằm phục vụ một trong các tác nhân. Vì vậy, ta muốn phân chia hệ thống sao cho thay đổi phục vụ một tác nhân không ảnh hưởng đến các tác nhân khác.

Các ca sử dụng trong Hình 33.1 không phải danh sách đầy đủ. Chẳng hạn, bạn sẽ không thấy ca sử dụng đăng nhập hay đăng xuất. Lý do bỏ chúng chỉ đơn giản là để giữ quy mô vấn đề trong phạm vi cuốn sách. Nếu đưa vào mọi ca sử dụng khác nhau, riêng chương này đã phải thành một cuốn sách.

Hãy chú ý các ca sử dụng nét đứt ở giữa Hình 33.1. Đây là các ca sử dụng trừu tượng.[^1] Ca sử dụng trừu tượng xác định một chính sách chung mà một ca sử dụng khác sẽ cụ thể hóa. Như bạn thấy, các ca sử dụng *View Catalog as Viewer* và *View Catalog as Purchaser* đều kế thừa từ ca sử dụng trừu tượng *View Catalog*.

Một mặt, tôi không nhất thiết phải tạo sự trừu tượng này. Tôi có thể bỏ ca sử dụng trừu tượng khỏi sơ đồ mà không ảnh hưởng đến tính năng của toàn sản phẩm. Mặt khác, hai ca sử dụng này rất giống nhau, nên tôi nghĩ tốt hơn là nhận ra điểm chung và thống nhất chúng ngay từ đầu trong quá trình phân tích.

## Kiến trúc thành phần

Giờ đã biết các tác nhân và ca sử dụng, ta có thể tạo kiến trúc thành phần sơ bộ (Hình 33.2).

Các đường đôi trong sơ đồ biểu thị ranh giới kiến trúc như thường lệ. Bạn có thể thấy cách phân chia điển hình giữa view, presenter, interactor và controller. Bạn cũng thấy tôi chia mỗi nhóm đó theo các tác nhân tương ứng.

Mỗi thành phần trong Hình 33.2 có thể được đóng gói thành tệp `.jar` hoặc `.dll` tiềm năng. Mỗi thành phần chứa view, presenter, interactor và controller được phân bổ cho nó.

Hãy chú ý các thành phần đặc biệt dành cho `Catalog View` và `Catalog Presenter`. Đây là cách tôi xử lý ca sử dụng trừu tượng `View Catalog`. Tôi giả định view và presenter đó sẽ được viết thành các lớp trừu tượng trong những thành phần này, còn thành phần kế thừa sẽ chứa các lớp view và presenter kế thừa từ các lớp trừu tượng ấy.

**Hình 33.2** Kiến trúc thành phần sơ bộ

Liệu tôi có thực sự chia hệ thống thành tất cả các thành phần này rồi phân phối chúng dưới dạng tệp `.jar` hoặc `.dll` không? Có và không. Tôi chắc chắn sẽ chia môi trường biên dịch và build theo cách này để có thể tạo các sản phẩm bàn giao độc lập như vậy. Tôi cũng sẽ giữ quyền gộp chúng thành số lượng sản phẩm bàn giao nhỏ hơn nếu cần. Chẳng hạn, với cách phân chia trong Hình 33.2, có thể dễ dàng gộp chúng thành năm tệp `.jar`, lần lượt cho view, presenter, interactor, controller và tiện ích. Khi đó, tôi có thể triển khai độc lập các thành phần có khả năng thay đổi độc lập với nhau cao nhất.

Một cách nhóm khác là đặt view và presenter chung trong một tệp `.jar`, còn interactor, controller và tiện ích nằm trong tệp `.jar` riêng. Cách nhóm thô sơ hơn nữa là tạo hai tệp `.jar`: một tệp chứa view và presenter, tệp còn lại chứa mọi thứ khác.

Giữ các lựa chọn này mở giúp chúng ta điều chỉnh cách triển khai theo sự thay đổi của hệ thống theo thời gian.

## Quản lý phụ thuộc

Luồng điều khiển trong Hình 33.2 đi từ phải sang trái. Đầu vào đi vào controller, rồi interactor xử lý đầu vào để tạo kết quả. Sau đó presenter định dạng kết quả, còn view hiển thị nội dung đã trình bày.

Hãy chú ý rằng không phải mọi mũi tên đều đi từ phải sang trái. Thực tế, phần lớn mũi tên hướng từ trái sang phải vì kiến trúc tuân theo Quy tắc Phụ thuộc. Mọi phụ thuộc đều đi qua ranh giới theo cùng một hướng và luôn hướng về các thành phần chứa chính sách cấp cao hơn.

Cũng lưu ý rằng quan hệ sử dụng, được biểu diễn bằng mũi tên rỗng, cùng hướng với luồng điều khiển, còn quan hệ kế thừa, được biểu diễn bằng mũi tên kín, đi ngược luồng điều khiển. Điều này thể hiện cách chúng ta dùng Nguyên tắc Đóng-Mở để bảo đảm phụ thuộc đi đúng hướng và thay đổi ở chi tiết cấp thấp không lan lên ảnh hưởng đến chính sách cấp cao.

## Kết luận

Sơ đồ kiến trúc ở Hình 33.2 có hai chiều phân tách. Thứ nhất là phân tách tác nhân theo Nguyên tắc Trách nhiệm Đơn nhất. Thứ hai là Quy tắc Phụ thuộc. Cả hai đều nhằm tách các thành phần thay đổi vì những lý do khác nhau và với tốc độ khác nhau. Lý do khác nhau tương ứng với các tác nhân; tốc độ khác nhau tương ứng với các cấp độ chính sách.

Khi cấu trúc mã theo cách này, bạn có thể tùy ý kết hợp các thành phần khi triển khai hệ thống. Bạn có thể nhóm chúng thành các sản phẩm bàn giao có thể triển khai theo bất kỳ cách nào hợp lý, rồi dễ dàng thay đổi cách nhóm khi điều kiện thay đổi.

[^1]: Đây là ký hiệu riêng của tôi cho ca sử dụng “trừu tượng”. Cách chuẩn hơn là dùng một stereotype UML như `<<abstract>>`, nhưng ngày nay tôi không thấy việc tuân thủ những tiêu chuẩn như vậy có nhiều ích lợi.