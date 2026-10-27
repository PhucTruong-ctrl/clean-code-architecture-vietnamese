# Chương 23: Presenter và đối tượng khiêm tốn
![Minh họa](assets/illustrations/23-chuong-23-opener.png){w=300}

Trong Chương 22, chúng ta đã giới thiệu khái niệm presenter. Presenter là một dạng của mẫu Đối tượng Khiêm tốn, giúp nhận diện và bảo vệ các ranh giới kiến trúc. Thực tế, Kiến trúc Sạch ở chương trước có rất nhiều cách triển khai mẫu Đối tượng Khiêm tốn.

## Mẫu Đối tượng Khiêm tốn

Mẫu Đối tượng Khiêm tốn[^1] là một mẫu thiết kế ban đầu được xác định như cách giúp người viết kiểm thử đơn vị tách hành vi khó kiểm thử khỏi hành vi dễ kiểm thử. Ý tưởng rất đơn giản: chia hành vi thành hai mô-đun hoặc lớp. Một mô-đun là đối tượng khiêm tốn, chứa những hành vi khó kiểm thử đã được rút gọn đến mức tối thiểu. Mô-đun còn lại chứa các hành vi có thể kiểm thử đã được tách khỏi đối tượng khiêm tốn.

Chẳng hạn, giao diện đồ họa khó kiểm thử đơn vị vì rất khó viết kiểm thử có thể quan sát màn hình và xác nhận các thành phần thích hợp được hiển thị. Tuy nhiên, phần lớn hành vi của giao diện đồ họa thực ra dễ kiểm thử. Với mẫu Đối tượng Khiêm tốn, chúng ta có thể tách hai loại hành vi này vào hai lớp khác nhau, gọi là Presenter và View.

## Presenter và View

View là đối tượng khiêm tốn, khó kiểm thử. Mã trong đối tượng này được giữ đơn giản hết mức có thể. Nó đưa dữ liệu lên giao diện đồ họa nhưng không xử lý dữ liệu đó.

Presenter là đối tượng có thể kiểm thử. Nhiệm vụ của nó là nhận dữ liệu từ ứng dụng và định dạng để View chỉ cần đưa dữ liệu lên màn hình. Chẳng hạn, nếu ứng dụng muốn hiển thị ngày tháng trong một trường, nó sẽ chuyển cho Presenter một đối tượng `Date`. Presenter định dạng dữ liệu thành chuỗi thích hợp rồi đặt chuỗi vào một cấu trúc dữ liệu đơn giản gọi là ViewModel, nơi View có thể lấy dữ liệu.

Nếu ứng dụng muốn hiển thị số tiền, nó có thể chuyển cho Presenter một đối tượng `Currency`. Presenter định dạng đối tượng đó với số chữ số thập phân và ký hiệu tiền tệ thích hợp, rồi tạo chuỗi để đặt vào ViewModel. Nếu giá trị tiền tệ cần hiển thị màu đỏ khi âm, một cờ boolean đơn giản trong ViewModel sẽ được đặt cho phù hợp.

Mỗi nút trên màn hình đều có tên. Tên đó là một chuỗi trong ViewModel do Presenter đặt vào. Nếu các nút cần chuyển sang màu xám, Presenter đặt một cờ boolean thích hợp trong ViewModel. Tên từng mục menu cũng là chuỗi trong ViewModel do Presenter nạp vào. Presenter nạp tên của mọi nút radio, hộp kiểm và trường văn bản vào các chuỗi và giá trị boolean phù hợp trong ViewModel. Các bảng số liệu cần hiển thị cũng được Presenter chuyển thành những bảng chuỗi đã định dạng phù hợp trong ViewModel.

Mọi thứ xuất hiện trên màn hình và nằm trong phạm vi kiểm soát của ứng dụng đều được biểu diễn trong ViewModel dưới dạng chuỗi, giá trị boolean hoặc enum. View không còn việc gì khác ngoài nạp dữ liệu từ ViewModel lên màn hình. Vì vậy, View là đối tượng khiêm tốn.

## Kiểm thử và kiến trúc

Từ lâu người ta đã biết khả năng kiểm thử là đặc tính của kiến trúc tốt. Mẫu Đối tượng Khiêm tốn là một ví dụ điển hình, vì việc tách hành vi thành phần có thể kiểm thử và phần không thể kiểm thử thường xác định một ranh giới kiến trúc. Ranh giới Presenter/View là một trong những ranh giới đó, nhưng còn nhiều ranh giới khác.

## Cổng cơ sở dữ liệu

Giữa các interactor của ca sử dụng và cơ sở dữ liệu là các cổng cơ sở dữ liệu.[^2] Đây là những giao diện đa hình, chứa phương thức cho mọi thao tác tạo, đọc, cập nhật hoặc xóa mà ứng dụng có thể thực hiện trên cơ sở dữ liệu. Chẳng hạn, nếu ứng dụng cần biết họ của tất cả người dùng đã đăng nhập hôm qua, giao diện `UserGateway` sẽ có phương thức tên `getLastNamesOfUsersWhoLoggedInAfter`, nhận một đối tượng `Date` làm đối số và trả về danh sách họ.

Hãy nhớ rằng chúng ta không cho phép SQL xuất hiện trong lớp ca sử dụng. Thay vào đó, ta dùng giao diện cổng với các phương thức thích hợp. Những cổng này được triển khai bằng các lớp trong lớp cơ sở dữ liệu. Phần triển khai là đối tượng khiêm tốn. Nó chỉ dùng SQL, hoặc giao diện cơ sở dữ liệu tương ứng, để truy cập dữ liệu mà mỗi phương thức cần. Ngược lại, interactor không phải đối tượng khiêm tốn vì nó đóng gói các quy tắc nghiệp vụ riêng của ứng dụng. Dù không khiêm tốn, interactor vẫn có thể kiểm thử vì có thể thay cổng bằng stub hoặc đối tượng kiểm thử thích hợp.

## Bộ ánh xạ dữ liệu

Quay lại chủ đề cơ sở dữ liệu, bạn nghĩ các ORM như Hibernate thuộc lớp nào?

Trước hết, hãy làm rõ một điều: không có thứ gọi là bộ ánh xạ quan hệ đối tượng (ORM). Lý do rất đơn giản: đối tượng không phải là cấu trúc dữ liệu, ít nhất là từ góc nhìn của người dùng đối tượng. Người dùng không thể nhìn thấy dữ liệu bên trong đối tượng vì dữ liệu đó đều là private. Họ chỉ thấy các phương thức public. Vì vậy, từ góc nhìn của người dùng, đối tượng chỉ là tập hợp các thao tác.

Ngược lại, cấu trúc dữ liệu là tập hợp các biến dữ liệu public, không hàm ý hành vi nào. Gọi ORM là “bộ ánh xạ dữ liệu” sẽ chính xác hơn, vì chúng nạp dữ liệu từ các bảng trong cơ sở dữ liệu quan hệ vào cấu trúc dữ liệu.

Những hệ thống ORM như vậy nên nằm ở đâu? Dĩ nhiên là trong lớp cơ sở dữ liệu. Thực tế, ORM tạo thành một dạng ranh giới Đối tượng Khiêm tốn khác giữa giao diện cổng và cơ sở dữ liệu.

## Bộ lắng nghe dịch vụ

Còn dịch vụ thì sao? Nếu ứng dụng cần giao tiếp với dịch vụ khác, hoặc nếu ứng dụng cung cấp một tập hợp dịch vụ, liệu mẫu Đối tượng Khiêm tốn có tạo ra ranh giới dịch vụ không?

Tất nhiên là có! Ứng dụng sẽ nạp dữ liệu vào các cấu trúc đơn giản rồi truyền chúng qua ranh giới đến các mô-đun có nhiệm vụ định dạng dữ liệu và gửi đến dịch vụ bên ngoài. Ở phía đầu vào, bộ lắng nghe dịch vụ nhận dữ liệu từ giao diện dịch vụ và định dạng thành cấu trúc dữ liệu đơn giản để ứng dụng sử dụng. Sau đó, cấu trúc dữ liệu được truyền qua ranh giới dịch vụ.

## Kết luận

Tại mỗi ranh giới kiến trúc, có thể sẽ có mẫu Đối tượng Khiêm tốn ở gần đó. Giao tiếp qua ranh giới hầu như luôn dùng một dạng cấu trúc dữ liệu đơn giản, và ranh giới thường phân tách phần khó kiểm thử khỏi phần dễ kiểm thử. Áp dụng mẫu này tại các ranh giới kiến trúc giúp tăng đáng kể khả năng kiểm thử của toàn hệ thống.

[^1]: *xUnit Patterns*, Meszaros, Addison-Wesley, 2007, tr. 695.
[^2]: *Patterns of Enterprise Application Architecture*, Martin Fowler và cộng sự, Addison-Wesley, 2003, tr. 466.