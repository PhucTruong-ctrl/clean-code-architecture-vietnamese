# Chương 11: DIP: Nguyên tắc đảo ngược phụ thuộc
![Minh họa](assets/illustrations/11-chuong-11-opener.png){w=260}

Nguyên tắc đảo ngược phụ thuộc (DIP) khẳng định rằng các hệ thống linh hoạt nhất là những hệ thống có phụ thuộc mã nguồn chỉ tham chiếu đến các trừu tượng, không tham chiếu đến các phần triển khai cụ thể.

Trong một ngôn ngữ kiểu tĩnh, như Java, điều này có nghĩa là các câu lệnh `use`, `import` và `include` nên chỉ tham chiếu đến các mô-đun nguồn chứa các giao diện (interface), các lớp trừu tượng (abstract class), hoặc một kiểu khai báo trừu tượng nào đó. Không có thứ cụ thể (concrete) nào nên bị phụ thuộc vào.

Quy tắc tương tự cũng áp dụng cho các ngôn ngữ kiểu động, như Ruby và Python. Các sự phụ thuộc của mã nguồn không nên tham chiếu đến các mô-đun cụ thể. Tuy nhiên, trong các ngôn ngữ này, việc xác định một mô-đun cụ thể là gì thì hơi khó khăn hơn một chút. Cụ thể, đó là bất kỳ mô-đun nào mà các hàm được gọi được triển khai bên trong.

Rõ ràng, việc coi ý tưởng này như một quy tắc cứng nhắc là không thực tế, bởi vì các hệ thống phần mềm buộc phải phụ thuộc vào nhiều tiện ích cụ thể. Ví dụ, lớp `String` trong Java là cụ thể, và sẽ không thực tế nếu cố gắng ép buộc nó trở thành trừu tượng. Sự phụ thuộc mã nguồn vào `java.lang.String` cụ thể đó không thể, và cũng không nên, bị tránh né.

Bằng so sánh, lớp `String` rất ổn định. Những thay đổi đối với lớp này rất hiếm và được kiểm soát chặt chẽ. Các lập trình viên và kiến trúc sư không phải lo lắng về những thay đổi thường xuyên và thất thường của `String`.

Với những lý do này, chúng ta có xu hướng bỏ qua nền tảng ổn định của hệ điều hành và các tiện ích nền tảng (platform) khi nói đến DIP. Chúng ta chấp nhận những sự phụ thuộc cụ thể đó vì chúng ta biết rằng chúng ta có thể tin cậy vào việc chúng sẽ không thay đổi.

Đó là những yếu tố cụ thể, thất thường (volatile) của hệ thống chúng ta mà chúng ta muốn tránh việc phụ thuộc vào. Đó là những mô-đun mà chúng ta đang tích cực phát triển, và đang trải qua những thay đổi thường xuyên.

## Trừu tượng ổn định

Mọi thay đổi đối với một giao diện trừu tượng đều tương ứng với thay đổi ở các bản triển khai cụ thể của nó. Ngược lại, thay đổi ở các bản triển khai cụ thể không phải lúc nào, thậm chí thường là không, đòi hỏi thay đổi ở các giao diện mà chúng triển khai. Vì thế, giao diện ít thất thường hơn bản triển khai.

Thực tế, những nhà thiết kế và kiến trúc sư phần mềm giỏi luôn cố gắng giảm thiểu sự thất thường của giao diện. Họ tìm cách thêm chức năng vào các bản triển khai mà không thay đổi giao diện. Đây là bài học Cơ bản về Thiết kế Phần mềm 101.

Hệ quả là kiến trúc phần mềm ổn định tránh phụ thuộc vào các phần triển khai cụ thể, dễ thay đổi, và ưu tiên các giao diện trừu tượng ổn định. Sự chuyển dịch tinh tế này dẫn đến một tập hợp những thực hành viết mã rất cụ thể:

* **Đừng tham chiếu đến các lớp cụ thể và thất thường. Hãy tham chiếu đến các giao diện trừu tượng thay vào đó.** Quy tắc này áp dụng trong mọi ngôn ngữ, dù là kiểu tĩnh hay kiểu động. Nó cũng đặt ra những ràng buộc nghiêm ngặt đối với việc tạo đối tượng (object creation) và nói chung bắt buộc việc sử dụng Abstract Factory (Nhà máy trừu tượng).
* **Đừng kế thừa từ các lớp cụ thể và thất thường.** Đây là một hệ quả của quy tắc trước, nhưng đáng được nhắc riêng. Trong các ngôn ngữ kiểu tĩnh, kế thừa là mối quan hệ mã nguồn mạnh mẽ và cứng nhắc nhất; do đó, nó nên được dùng với sự thận trọng cực đại. Trong các ngôn ngữ kiểu động, kế thừa ít gây vấn đề hơn, nhưng nó vẫn là một sự phụ thuộc, và sự thận trọng luôn là lựa chọn khôn ngoan nhất.
* **Đừng ghi đè (override) các hàm cụ thể.** Hàm cụ thể thường đòi hỏi phụ thuộc mã nguồn. Khi ghi đè những hàm đó, bạn không loại bỏ các phụ thuộc này, mà kế thừa chúng. Để quản lý chúng, hãy làm cho hàm thành trừu tượng (abstract) và tạo ra nhiều bản triển khai.
* **Đừng bao giờ nhắc đến tên của bất cứ thứ gì cụ thể và thất thường.** Điều này thực chất chỉ là cách diễn đạt lại chính nguyên tắc đó.

## Nhà máy (Factories)

Để tuân thủ các quy tắc này, việc tạo ra các đối tượng cụ thể và thất thường đòi hỏi sự xử lý đặc biệt. Sự thận trọng này là cần thiết vì, trong hầu như mọi ngôn ngữ, việc tạo một đối tượng đòi hỏi một sự phụ thuộc mã nguồn vào định nghĩa cụ thể của đối tượng đó.

Trong hầu hết các ngôn ngữ hướng đối tượng, như Java, chúng ta sẽ dùng Abstract Factory (Nhà máy trừu tượng) để quản lý sự phụ thuộc không mong muốn này.

Sơ đồ trong **Hình 11.1** cho thấy cấu trúc đó. `Application` sử dụng `ConcreteImpl` thông qua giao diện `Service`. Tuy nhiên, `Application` phải có cách nào đó để tạo ra các thể hiện (instance) của `ConcreteImpl`. Để đạt được điều này mà không tạo ra sự phụ thuộc mã nguồn vào `ConcreteImpl`, `Application` gọi phương thức `makeSvc` của giao diện `ServiceFactory`. Phương thức này được triển khai bởi lớp `ServiceFactoryImpl`, kế thừa từ `ServiceFactory`. Triển khai đó khởi tạo `ConcreteImpl` và trả về nó dưới kiểu `Service`.

**Hình 11.1** Sử dụng mẫu Abstract Factory để quản lý sự phụ thuộc

Đường cong trong **Hình 11.1** là một ranh giới kiến trúc (architectural boundary). Nó tách biệt trừu tượng với cụ thể. Tất cả các sự phụ thuộc mã nguồn cắt qua đường cong đó đều chỉ theo một hướng, về phía bên trừu tượng.

Đường cong chia hệ thống thành hai thành phần (component): một trừu tượng và một cụ thể. Thành phần trừu tượng chứa tất cả các quy tắc nghiệp vụ (business rules) cấp cao của ứng dụng. Thành phần cụ thể chứa tất cả các chi tiết triển khai (implementation details) mà những quy tắc nghiệp vụ đó thao tác.

Lưu ý rằng luồng điều khiển (flow of control) cắt qua đường cong đó theo hướng ngược lại so với các sự phụ thuộc mã nguồn. Các sự phụ thuộc mã nguồn bị đảo ngược so với luồng điều khiển, đó là lý do chúng ta gọi nguyên tắc này là Đảo ngược phụ thuộc (Dependency Inversion).

## Thành phần cụ thể (Concrete Components)

Thành phần cụ thể trong **Hình 11.1** chứa một sự phụ thuộc duy nhất, vì vậy nó vi phạm DIP. Đây là điều điển hình. Các vi phạm DIP không thể loại bỏ hoàn toàn, nhưng chúng có thể được gom nhóm vào một số nhỏ các thành phần cụ thể và tách biệt khỏi phần còn lại của hệ thống.

Hầu hết các hệ thống sẽ chứa ít nhất một thành phần cụ thể như vậy, thường được gọi là `main` vì nó chứa hàm `main`[^1]. Trong trường hợp được minh họa trong **Hình 11.1**, hàm `main` sẽ khởi tạo `ServiceFactoryImpl` và đặt thể hiện đó vào một biến toàn cục (global variable) kiểu `ServiceFactory`. `Application` sau đó sẽ truy cập nhà máy (factory) thông qua biến toàn cục đó.

## Kết luận

Khi chúng ta tiến về phía trước trong cuốn sách này và đề cập đến các nguyên tắc kiến trúc cấp cao hơn, DIP sẽ xuất hiện lại lần nữa và lần nữa. Nó sẽ là nguyên tắc tổ chức dễ thấy nhất trong các sơ đồ kiến trúc của chúng ta. Đường cong trong **Hình 11.1** sẽ trở thành các ranh giới kiến trúc (architectural boundaries) trong các chương sau. Cách mà các sự phụ thuộc cắt qua đường cong đó theo một hướng, và về phía các thực thể trừu tượng hơn, sẽ trở thành một quy tắc mới mà chúng ta sẽ gọi là Quy tắc phụ thuộc (Dependency Rule).

[^1]: Nói cách khác, hàm được gọi bởi hệ điều hành khi ứng dụng lần đầu được khởi động.