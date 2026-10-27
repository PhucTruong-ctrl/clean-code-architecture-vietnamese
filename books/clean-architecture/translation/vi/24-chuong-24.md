# Chương 24: Ranh giới một phần
![Minh họa](assets/illustrations/24-chuong-24-opener.png){w=300}

Các ranh giới kiến trúc hoàn chỉnh rất tốn kém. Chúng đòi hỏi các giao diện ranh giới đa hình hai chiều, cấu trúc dữ liệu đầu vào và đầu ra, cùng toàn bộ cơ chế quản lý phụ thuộc cần thiết để cách ly hai phía thành các thành phần có thể biên dịch và triển khai độc lập. Việc đó đòi hỏi nhiều công sức, và cũng tốn công duy trì.

Trong nhiều tình huống, kiến trúc sư giỏi có thể kết luận rằng chi phí cho một ranh giới như vậy quá cao, nhưng vẫn muốn chừa sẵn chỗ cho nó nếu sau này cần đến.

Nhiều người trong cộng đồng Agile thường không tán thành kiểu thiết kế dự đoán này vì cho rằng nó vi phạm YAGNI: “You Aren’t Going to Need It” (Bạn sẽ không cần đến nó). Tuy nhiên, đôi khi kiến trúc sư nhìn vào vấn đề và nghĩ: “Đúng vậy, nhưng có thể tôi sẽ cần”. Khi đó, họ có thể triển khai một ranh giới một phần.

## Bỏ qua bước cuối

Một cách tạo ranh giới một phần là thực hiện mọi công việc cần thiết để tạo các thành phần có thể biên dịch và triển khai độc lập, rồi giữ tất cả chúng trong cùng một thành phần. Các giao diện hai chiều đã có, cấu trúc dữ liệu đầu vào và đầu ra đã có, mọi thứ đều được chuẩn bị xong, nhưng chúng ta biên dịch và triển khai tất cả như một thành phần duy nhất.

Rõ ràng, ranh giới một phần kiểu này vẫn cần lượng mã và công việc thiết kế chuẩn bị tương đương một ranh giới hoàn chỉnh. Tuy nhiên, không cần quản lý nhiều thành phần. Không phải theo dõi số phiên bản hay gánh việc quản lý bản phát hành. Khác biệt đó không nên bị xem nhẹ.

Đây là chiến lược ban đầu của FitNesse. Thành phần máy chủ web của FitNesse được thiết kế để có thể tách khỏi phần wiki và kiểm thử. Ý tưởng là có thể dùng thành phần web đó để tạo các ứng dụng chạy trên web khác. Đồng thời, chúng tôi không muốn người dùng phải tải xuống hai thành phần. Hãy nhớ một trong những mục tiêu thiết kế của chúng tôi là “download and go”. Chúng tôi muốn người dùng tải xuống một tệp jar duy nhất và chạy nó mà không phải tìm thêm tệp jar khác hay tự xử lý tính tương thích giữa các phiên bản.

Câu chuyện FitNesse cũng cho thấy một trong những rủi ro của cách tiếp cận này. Theo thời gian, khi thấy rõ sẽ không bao giờ cần một thành phần web riêng, ranh giới giữa thành phần web và thành phần wiki bắt đầu suy yếu. Các phụ thuộc dần vượt qua ranh giới theo hướng sai. Ngày nay, việc tách chúng ra lần nữa sẽ khá vất vả.

## Ranh giới một chiều

Ranh giới kiến trúc hoàn chỉnh dùng các giao diện hai chiều để duy trì sự cách ly ở cả hai hướng. Duy trì sự tách biệt theo cả hai hướng tốn kém, cả lúc thiết lập ban đầu lẫn trong quá trình bảo trì.

Một cấu trúc đơn giản hơn, dùng để chừa chỗ cho việc mở rộng thành ranh giới hoàn chỉnh sau này, được minh họa ở Hình 24.1. Cấu trúc này là mẫu Strategy truyền thống. Các client sử dụng giao diện `ServiceBoundary`, còn các lớp `ServiceImpl` triển khai giao diện đó.

**Hình 24.1** Mẫu Strategy

Rõ ràng cấu trúc này chuẩn bị sẵn nền tảng cho một ranh giới kiến trúc trong tương lai. Cơ chế đảo ngược phụ thuộc cần thiết đã có để cố gắng cách ly `Client` khỏi `ServiceImpl`. Cũng rõ ràng rằng sự tách biệt này có thể suy giảm rất nhanh, như mũi tên chấm khó coi trong sơ đồ cho thấy. Khi không có giao diện hai chiều, không có gì ngăn được kiểu kênh phụ thuộc ngược này ngoài sự cẩn trọng và kỷ luật của các nhà phát triển và kiến trúc sư.

## Mẫu Facade

Một ranh giới còn đơn giản hơn là mẫu Facade, được minh họa trong Hình 24.2. Trong trường hợp này, ngay cả việc đảo ngược phụ thuộc cũng bị bỏ qua. Ranh giới chỉ được xác định bởi lớp `Facade`, lớp này liệt kê tất cả dịch vụ dưới dạng các phương thức và chuyển tiếp lời gọi dịch vụ đến những lớp mà client không nên truy cập.

**Hình 24.2** Mẫu Facade

Tuy nhiên, hãy lưu ý rằng `Client` có phụ thuộc bắc cầu đến tất cả các lớp dịch vụ đó. Trong ngôn ngữ tĩnh, thay đổi mã nguồn của một lớp `Service` sẽ buộc `Client` phải biên dịch lại. Bạn cũng có thể hình dung việc tạo các kênh phụ thuộc ngược dễ dàng đến mức nào trong cấu trúc này.

## Kết luận

Chúng ta đã thấy ba cách đơn giản để triển khai một phần ranh giới kiến trúc. Tất nhiên còn nhiều cách khác. Ba chiến lược này chỉ nhằm làm ví dụ.

Mỗi cách tiếp cận đều có chi phí và lợi ích riêng. Trong một số bối cảnh nhất định, mỗi cách đều phù hợp để làm chỗ giữ chỗ cho một ranh giới hoàn chỉnh trong tương lai. Nếu ranh giới hoàn chỉnh không bao giờ được tạo ra, từng cách cũng có thể suy giảm.

Một trong những nhiệm vụ của kiến trúc sư là quyết định nơi nào có thể cần đến ranh giới kiến trúc trong tương lai, và ranh giới đó nên được triển khai hoàn chỉnh hay chỉ một phần.