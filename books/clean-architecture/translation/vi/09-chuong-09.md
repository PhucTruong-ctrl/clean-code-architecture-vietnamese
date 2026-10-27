# Chương 9: LSP: Nguyên tắc thay thế Liskov
![Minh họa](assets/illustrations/09-chuong-09-opener.png){w=300}

Năm 1988, Barbara Liskov đã viết điều sau như một cách để định nghĩa các kiểu con:

> *Điều mong muốn ở đây là một tính chất thay thế như sau: Nếu với mỗi đối tượng o1 kiểu S thì tồn tại một đối tượng o2 kiểu T sao cho với tất cả các chương trình P được định nghĩa dựa trên T, hành vi của P không thay đổi khi o1 được dùng thay cho o2 thì S là một kiểu con của T.*[^1]

Để hiểu ý tưởng này, được gọi là **Nguyên tắc thay thế Liskov (LSP)**, hãy xem xét một số ví dụ.

## Dẫn dắt việc sử dụng kế thừa

Hãy tưởng tượng rằng chúng ta có một lớp tên là `License`, như minh họa trong Hình 9.1. Lớp này có một phương thức tên `calcFee()`, được gọi bởi ứng dụng Billing. Có hai "kiểu con" của `License`: `PersonalLicense` và `BusinessLicense`. Chúng sử dụng các thuật toán khác nhau để tính phí giấy phép.

**Hình 9.1** License, và các lớp dẫn xuất của nó, tuân thủ LSP

Thiết kế này tuân thủ LSP vì hành vi của ứng dụng Billing **không** phụ thuộc theo bất kỳ cách nào vào hai kiểu con mà nó sử dụng. Cả hai kiểu con đều có thể thay thế cho kiểu `License`.

## Vấn đề vuông/hình chữ nhật

Ví dụ điển hình của một vi phạm LSP là bài toán nổi tiếng (hay tồi tệ, tùy góc nhìn) về vuông/hình chữ nhật (Hình 9.2).

**Hình 9.2** Bài toán vuông/hình chữ nhật tồi tệ

Trong ví dụ này, `Square` **không** phải là một kiểu con thích hợp của `Rectangle` vì chiều cao và chiều rộng của `Rectangle` có thể thay đổi độc lập; ngược lại, chiều cao và chiều rộng của `Square` phải thay đổi cùng nhau. Vì `User` tin rằng nó đang giao tiếp với một `Rectangle`, nên nó rất dễ bị nhầm lẫn. Đoạn mã sau cho thấy lý do:

```java
Rectangle r = …

r.setW(5);

r.setH(2);

assert(r.area() == 10);
```

Nếu mã `…` tạo ra một `Square`, thì khẳng định (assertion) sẽ thất bại.

Cách duy nhất để phòng thủ trước loại vi phạm LSP này là thêm các cơ chế vào `User` (như một câu lệnh `if`) để phát hiện xem `Rectangle` có thực sự là một `Square` hay không. Vì hành vi của `User` phụ thuộc vào các kiểu mà nó sử dụng, nên những kiểu đó **không** thể thay thế cho nhau.

## LSP và kiến trúc

Trong những năm đầu của cuộc cách mạng hướng đối tượng, chúng ta coi LSP là một cách để dẫn dắt việc sử dụng kế thừa, như đã trình bày ở các phần trước. Tuy nhiên, qua nhiều năm, LSP đã biến hình thành một nguyên tắc thiết kế phần mềm rộng hơn, liên quan đến các giao diện (interface) và các triển khai (implementation).

Các giao diện trong vấn đề này có thể mang nhiều hình thức. Chúng ta có thể có một giao diện kiểu Java, được triển khai bởi nhiều lớp. Hoặc chúng ta có thể có một vài lớp Ruby chia sẻ cùng các chữ ký phương thức. Hoặc chúng ta có thể có một tập hợp các dịch vụ đều phản hồi cùng một giao diện REST.

Trong tất cả các tình huống đó, và nhiều tình huống khác, LSP đều áp dụng được vì có những người dùng (user) phụ thuộc vào các giao diện được định nghĩa rõ ràng, và vào tính khả thi của việc thay thế các triển khai của những giao diện đó.

Cách tốt nhất để hiểu LSP từ góc độ kiến trúc là xem xét điều gì xảy ra với kiến trúc của một hệ thống khi nguyên tắc này bị vi phạm.

## Ví dụ vi phạm LSP

Giả sử chúng ta đang xây dựng một bộ tổng hợp (aggregator) cho nhiều dịch vụ điều phối taxi. Khách hàng sử dụng trang web của chúng ta để tìm taxi phù hợp nhất, bất kể công ty taxi nào. Khi khách hàng quyết định, hệ thống của chúng ta điều phối taxi đã chọn bằng cách sử dụng một dịch vụ RESTful.

Bây giờ giả sử URI của dịch vụ điều phối RESTful là một phần của thông tin chứa trong cơ sở dữ liệu tài xế. Khi hệ thống của chúng ta đã chọn một tài xế phù hợp cho khách hàng, nó lấy URI đó từ bản ghi tài xế và dùng nó để điều phối tài xế.

Giả sử tài xế Bob có URI điều phối trông như sau:

```
purplecab.com/driver/Bob
```

Hệ thống của chúng ta sẽ gắn thông tin điều phối vào URI này và gửi nó bằng một yêu cầu PUT, như sau:

```
purplecab.com/driver/Bob
/pickupAddress/24 Maple St.
/pickupTime/153
/destination/ORD
```

Rõ ràng, điều này có nghĩa là **tất cả** các dịch vụ điều phối, của **tất cả** các công ty khác nhau, phải tuân thủ **cùng một** giao diện REST. Chúng phải xử lý các trường `pickupAddress`, `pickupTime` và `destination` theo cách hoàn toàn giống nhau.

Bây giờ giả sử công ty taxi Acme thuê một vài lập trình viên không đọc kỹ spec. Họ viết tắt trường `destination` thành chỉ `dest`. Acme là công ty taxi lớn nhất trong khu vực của chúng ta, và vợ cũ của CEO Acme là vợ mới của CEO chúng ta, và... Bạn hiểu ý rồi. Điều gì sẽ xảy ra với kiến trúc của hệ thống chúng ta?

Chắc chắn, chúng ta sẽ phải thêm một trường hợp đặc biệt (special case). Yêu cầu điều phối cho bất kỳ tài xế Acme nào sẽ phải được xây dựng bằng một bộ quy tắc khác so với tất cả các tài xế còn lại.

Cách đơn giản nhất để đạt được mục tiêu này là thêm một câu lệnh `if` vào mô-đun xây dựng lệnh điều phối:

```java
if (driver.getDispatchUri().startsWith("acme.com"))…
```

Không kiến trúc sư giỏi nào lại để kiểu cấu trúc đó tồn tại trong hệ thống. Đưa từ "acme" thẳng vào mã nguồn sẽ mở đường cho đủ loại lỗi khó lường, chưa kể đến các lỗ hổng bảo mật.

Ví dụ, nếu Acme trở nên còn thành công hơn và mua công ty taxi Purple thì sao? Nếu công ty hợp nhất giữ nguyên các thương hiệu riêng biệt và các trang web riêng biệt, nhưng thống nhất tất cả hệ thống của các công ty ban đầu? Chúng ta có phải thêm một câu `if` khác cho "purple" không?

Kiến trúc sư của chúng ta sẽ phải cách ly hệ thống khỏi các lỗi như thế này bằng cách tạo ra một loại mô-đun tạo lệnh điều phối được điều khiển bởi một cơ sở dữ liệu cấu hình (configuration database) được tra cứu theo URI điều phối. Dữ liệu cấu hình có thể trông như sau:

```
URI          Định dạng điều phối
Acme.com     /pickupAddress/%s/pickupTime/%s/dest/%s
*.*          /pickupAddress/%s/pickupTime/%s/destination/%s
```

Và như vậy, kiến trúc sư của chúng ta đã phải thêm một cơ chế đáng kể và phức tạp để đối phó với thực tế rằng các giao diện của các dịch vụ RESTful **không** đều có thể thay thế cho nhau.

## Kết luận

LSP có thể, và nên, được mở rộng đến mức độ kiến trúc. Một vi phạm đơn giản về khả năng thay thế, có thể làm ô nhiễm kiến trúc của một hệ thống bằng một lượng lớn các cơ chế thêm vào.

[^1]: Barbara Liskov, "Data Abstraction and Hierarchy," SIGPLAN Notices 23, 5 (Tháng 5 năm 1988).