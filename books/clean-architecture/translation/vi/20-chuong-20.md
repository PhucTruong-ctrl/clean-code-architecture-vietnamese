# Chương 20: Quy tắc nghiệp vụ
![Minh họa](assets/illustrations/20-chuong-20-opener.png){w=300}

Nếu muốn chia ứng dụng thành quy tắc nghiệp vụ và plugin, trước hết chúng ta cần hiểu rõ quy tắc nghiệp vụ là gì. Hóa ra có nhiều loại quy tắc khác nhau.

Nói chính xác, quy tắc nghiệp vụ là những quy tắc hoặc thủ tục tạo ra hay tiết kiệm tiền cho doanh nghiệp. Nói chặt chẽ hơn, các quy tắc ấy vẫn tạo ra hoặc tiết kiệm tiền cho doanh nghiệp bất kể chúng có được thực thi bằng máy tính hay không. Ngay cả khi được thực hiện thủ công, chúng vẫn tạo ra hoặc tiết kiệm tiền.

Việc ngân hàng tính lãi suất N% cho một khoản vay là quy tắc nghiệp vụ giúp ngân hàng kiếm tiền. Lãi suất do chương trình máy tính tính hay do một nhân viên dùng bàn tính tính đều không quan trọng.

Chúng ta gọi những quy tắc này là **Quy tắc Nghiệp vụ Cốt lõi**, vì chúng thiết yếu đối với chính doanh nghiệp và vẫn tồn tại ngay cả khi không có hệ thống tự động hóa chúng.

Quy tắc nghiệp vụ cốt lõi thường cần dữ liệu để xử lý. Chẳng hạn, khoản vay cần số dư nợ, lãi suất và lịch thanh toán.

Chúng ta gọi dữ liệu này là **Dữ liệu Nghiệp vụ Cốt lõi**. Đây là dữ liệu vẫn tồn tại ngay cả khi hệ thống không được tự động hóa.

Quy tắc cốt lõi và dữ liệu cốt lõi gắn bó không thể tách rời, nên thích hợp để kết hợp thành một đối tượng. Chúng ta gọi loại đối tượng này là một **Entity**.[^1]

## Entity

Entity là một đối tượng trong hệ thống máy tính, chứa một tập nhỏ các quy tắc nghiệp vụ cốt lõi hoạt động trên dữ liệu nghiệp vụ cốt lõi. Đối tượng Entity tự chứa dữ liệu nghiệp vụ cốt lõi hoặc có thể truy cập dữ liệu đó dễ dàng. Giao diện của Entity gồm các hàm triển khai những quy tắc nghiệp vụ cốt lõi vận hành trên dữ liệu ấy.

Ví dụ, Hình 20.1 cho thấy Entity `Loan` có thể được biểu diễn như một lớp UML. Lớp này có ba mục dữ liệu nghiệp vụ cốt lõi và cung cấp ba quy tắc nghiệp vụ cốt lõi qua giao diện của nó.

**Hình 20.1** Entity khoản vay dưới dạng lớp UML

Khi tạo loại lớp này, chúng ta gom phần mềm triển khai một khái niệm thiết yếu đối với doanh nghiệp lại với nhau, tách nó khỏi mọi mối quan tâm khác trong hệ thống tự động đang xây dựng. Lớp này đứng độc lập, đại diện cho doanh nghiệp. Nó không bị vướng bận bởi cơ sở dữ liệu, giao diện người dùng hay framework của bên thứ ba. Nó có thể phục vụ doanh nghiệp trong bất kỳ hệ thống nào, bất kể hệ thống được trình bày ra sao, lưu dữ liệu ở đâu hay bố trí máy tính thế nào. Entity chỉ chứa nghiệp vụ, không có gì khác.

Một số bạn có thể băn khoăn vì tôi gọi nó là một lớp. Đừng lo. Không nhất thiết phải dùng ngôn ngữ hướng đối tượng để tạo Entity. Chỉ cần gắn dữ liệu nghiệp vụ cốt lõi với các quy tắc nghiệp vụ cốt lõi trong một mô-đun phần mềm riêng biệt.

## Ca sử dụng

Không phải quy tắc nghiệp vụ nào cũng thuần túy như trong Entity. Một số quy tắc tạo ra hoặc tiết kiệm tiền cho doanh nghiệp bằng cách xác định và giới hạn cách hệ thống tự động vận hành. Chúng không được dùng trong môi trường thủ công vì chỉ có ý nghĩa khi nằm trong một hệ thống tự động.

Chẳng hạn, hãy tưởng tượng một ứng dụng được nhân viên ngân hàng dùng để tạo khoản vay mới. Ngân hàng có thể quyết định rằng nhân viên cho vay không được đưa ra ước tính khoản thanh toán cho đến khi đã thu thập và xác thực thông tin liên hệ, đồng thời xác nhận điểm tín dụng của khách hàng tiềm năng từ 500 trở lên. Vì vậy, ngân hàng có thể quy định hệ thống không được chuyển sang màn hình ước tính khoản thanh toán cho đến khi thông tin liên hệ đã được điền và xác minh, đồng thời điểm tín dụng được xác nhận là cao hơn ngưỡng quy định.

Đây là một ca sử dụng.[^2] Ca sử dụng mô tả cách một hệ thống tự động được sử dụng. Nó quy định dữ liệu người dùng cần cung cấp, dữ liệu hệ thống trả lại và các bước xử lý để tạo ra kết quả đó. Ca sử dụng mô tả những quy tắc nghiệp vụ riêng của ứng dụng, khác với các quy tắc nghiệp vụ cốt lõi nằm trong Entity.

Hình 20.2 là một ví dụ về ca sử dụng. Lưu ý dòng cuối có nhắc đến `Customer`. Đây là tham chiếu đến Entity `Customer`, nơi chứa các quy tắc nghiệp vụ cốt lõi chi phối mối quan hệ giữa ngân hàng và khách hàng.

**Hình 20.2** Ví dụ về ca sử dụng

Ca sử dụng chứa các quy tắc xác định cách thức và thời điểm gọi các quy tắc nghiệp vụ cốt lõi trong Entity. Ca sử dụng điều khiển nhịp phối hợp của các Entity.

Cũng cần lưu ý rằng ca sử dụng không mô tả giao diện người dùng, ngoài việc nêu không chính thức dữ liệu đi vào từ giao diện và dữ liệu được gửi ngược ra qua giao diện đó. Chỉ dựa vào ca sử dụng, không thể biết ứng dụng được cung cấp qua web, qua ứng dụng máy tính cài đặt cục bộ, qua console hay dưới dạng dịch vụ thuần túy.

Điều này rất quan trọng. Ca sử dụng không mô tả hệ thống xuất hiện như thế nào với người dùng. Thay vào đó, nó mô tả các quy tắc nghiệp vụ riêng của ứng dụng, chi phối tương tác giữa người dùng và Entity. Cách dữ liệu đi vào và ra khỏi hệ thống không liên quan đến ca sử dụng.

Ca sử dụng là một đối tượng. Nó có một hoặc nhiều hàm triển khai các quy tắc nghiệp vụ riêng của ứng dụng. Nó cũng chứa các phần tử dữ liệu gồm dữ liệu đầu vào, dữ liệu đầu ra và tham chiếu đến những Entity thích hợp mà nó tương tác.

Entity không biết về các ca sử dụng điều khiển chúng. Đây là một ví dụ khác cho thấy hướng phụ thuộc tuân theo Nguyên tắc Đảo ngược Phụ thuộc. Các khái niệm cấp cao như Entity không biết gì về khái niệm cấp thấp hơn như ca sử dụng. Ngược lại, ca sử dụng cấp thấp phụ thuộc vào Entity cấp cao.

Vì sao Entity ở cấp cao còn ca sử dụng ở cấp thấp? Vì ca sử dụng dành riêng cho một ứng dụng, nên gần với đầu vào và đầu ra của hệ thống đó hơn. Entity là khái quát hóa có thể được dùng trong nhiều ứng dụng, nên nằm xa đầu vào và đầu ra hơn. Ca sử dụng phụ thuộc vào Entity; Entity không phụ thuộc vào ca sử dụng.

## Mô hình yêu cầu và phản hồi

Ca sử dụng nhận dữ liệu đầu vào và tạo dữ liệu đầu ra. Tuy nhiên, một đối tượng ca sử dụng được thiết kế tốt không nên biết dữ liệu được truyền đến người dùng hay thành phần khác bằng cách nào. Chúng ta chắc chắn không muốn mã trong lớp ca sử dụng biết về HTML hay SQL!

Lớp ca sử dụng nhận các cấu trúc dữ liệu yêu cầu đơn giản làm đầu vào và trả về các cấu trúc dữ liệu phản hồi đơn giản làm đầu ra. Những cấu trúc dữ liệu này không phụ thuộc vào bất kỳ thứ gì. Chúng không kế thừa từ các giao diện chuẩn của framework như `HttpRequest` và `HttpResponse`. Chúng không biết gì về web và cũng không mang theo những đặc điểm của giao diện người dùng đang được sử dụng.

Việc không có phụ thuộc này rất quan trọng. Nếu mô hình yêu cầu và phản hồi không độc lập, các ca sử dụng phụ thuộc vào chúng sẽ bị ràng buộc gián tiếp với mọi phụ thuộc mà mô hình mang theo.

Bạn có thể muốn đặt tham chiếu đến các đối tượng Entity trong những cấu trúc dữ liệu này, vì Entity và mô hình yêu cầu/phản hồi có nhiều dữ liệu chung. Đừng làm vậy! Mục đích của hai loại đối tượng này rất khác nhau. Theo thời gian, chúng sẽ thay đổi vì những lý do rất khác nhau. Gắn chúng với nhau dưới bất kỳ hình thức nào đều vi phạm Nguyên tắc Đóng chung và Nguyên tắc Trách nhiệm Đơn nhất. Kết quả là mã nguồn phải chuyển tiếp nhiều dữ liệu thừa và chứa thêm nhiều câu lệnh điều kiện.

## Kết luận

Quy tắc nghiệp vụ là lý do một hệ thống phần mềm tồn tại. Chúng là chức năng cốt lõi, chứa mã tạo ra hoặc tiết kiệm tiền. Chúng là những báu vật quý giá nhất của doanh nghiệp.

Quy tắc nghiệp vụ cần được giữ nguyên vẹn, không bị vấy bẩn bởi những mối quan tâm thứ yếu như giao diện người dùng hay cơ sở dữ liệu được sử dụng. Lý tưởng nhất, mã thể hiện quy tắc nghiệp vụ phải là trái tim của hệ thống, còn các mối quan tâm ít quan trọng hơn được cắm vào nó. Quy tắc nghiệp vụ nên là phần mã độc lập và có thể tái sử dụng nhiều nhất trong hệ thống.

[^1]: Đây là tên gọi Ivar Jacobson dùng cho khái niệm này (I. Jacobson và cộng sự, *Object Oriented Software Engineering*, Addison-Wesley, 1992).
[^2]: Như trên.