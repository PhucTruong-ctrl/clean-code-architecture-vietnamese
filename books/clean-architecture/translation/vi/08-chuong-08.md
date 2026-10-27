# Chương 8: OCP: Nguyên tắc đóng-mở
![Minh họa](assets/illustrations/08-chuong-08-opener.png){w=180}

Nguyên tắc đóng-mở (OCP) được Bertrand Meyer đặt ra năm 1988.[^1] Nguyên tắc phát biểu:

> Một tạo phẩm phần mềm nên mở cho việc mở rộng nhưng đóng cho việc sửa đổi.

Nói cách khác, hành vi của một tạo phẩm phần mềm nên có thể mở rộng mà không phải sửa đổi tạo phẩm đó.

Đây, tất nhiên, là lý do cơ bản nhất khiến chúng ta học kiến trúc phần mềm. Rõ ràng, nếu những mở rộng đơn giản của yêu cầu ép buộc phải thay đổi mã lớn trong phần mềm, thì các kiến trúc sư của hệ thống phần mềm đó đã thất bại một cách ngoạn mục.
Hầu hết học viên thiết kế phần mềm nhận ra OCP là một nguyên tắc hướng dẫn họ trong thiết kế lớp và mô-đun. Nhưng nguyên tắc này mang ý nghĩa lớn hơn nữa khi xét ở cấp độ các thành phần kiến trúc.

Một thử nghiệm tư duy sẽ làm rõ điều này.


## Một thử nghiệm tư duy

Hãy tưởng tượng, chỉ trong giây lát, rằng chúng ta có một hệ thống hiển thị tóm tắt tài chính trên một trang web. Dữ liệu trên trang có thể cuộn, và các số âm được hiển thị bằng màu đỏ.

Bây giờ hãy tưởng tượng các bên liên quan yêu cầu chuyển thông tin cùng loại đó thành một báo cáo để in trên máy in đen trắng. Báo cáo cần được phân trang đúng cách, có tiêu đề trang, chân trang và nhãn cột thích hợp. Các số âm nên được bao quanh bởi dấu ngoặc đơn.

Rõ ràng, một số mã mới phải được viết. Nhưng bao nhiêu mã cũ sẽ phải thay đổi?

Một kiến trúc phần mềm tốt sẽ giảm lượng mã thay đổi xuống mức tối thiểu. Lý tưởng là không thay đổi gì cả.

Làm sao? Bằng cách tách đúng các thứ thay đổi vì lý do khác nhau (Nguyên tắc trách nhiệm đơn nhất), rồi tổ chức các phụ thuộc giữa chúng đúng cách (Nguyên tắc đảo ngược phụ thuộc).

Áp dụng SRP, chúng ta có thể đến được khung nhìn luồng dữ liệu như trong Hình 8.1. Một thủ tục phân tích kiểm tra dữ liệu tài chính và sinh ra dữ liệu có thể báo cáo, dữ liệu đó sau đó được định dạng thích hợp bởi hai tiến trình báo cáo.
**Hình 8.1** Áp dụng SRP

Điểm mấu chốt ở đây là việc tạo báo cáo bao gồm hai trách nhiệm riêng biệt: tính toán dữ liệu báo cáo, và trình bày dữ liệu đó dưới dạng thân thiện với web và máy in.

Sau khi đã tách biệt, chúng ta cần tổ chức các phụ thuộc mã nguồn để đảm bảo thay đổi ở một trách nhiệm không gây thay đổi ở trách nhiệm kia. Cũng như vậy, tổ chức mới nên đảm bảo hành vi có thể mở rộng mà không cần sửa đổi.

Chúng ta đạt được điều này bằng cách phân chia các tiến trình thành các lớp, và tách các lớp đó thành các thành phần, như đường kẻ đôi trong sơ đồ Hình 8.2. Trong hình này, thành phần góc trên bên trái là Controller (Bộ điều khiển). Góc trên bên phải là Interactor (Bộ tương tác). Góc dưới bên phải là Database (Cơ sở dữ liệu). Cuối cùng, góc dưới bên trái là bốn thành phần đại diện cho các Presenter (Bộ trình bày) và View (Giao diện).
**Hình 8.2** Phân chia tiến trình thành các lớp và tách các lớp thành các thành phần

Các lớp được đánh dấu `<I>` là giao diện; các lớp đánh dấu `<DS>` là cấu trúc dữ liệu. Mũi tên mở là quan hệ sử dụng. Mũi tên kín là quan hệ triển khai hoặc kế thừa.

Điều đầu tiên cần nhận thấy là tất cả các phụ thuộc đều là phụ thuộc mã nguồn. Một mũi tên chỉ từ lớp A đến lớp B nghĩa là mã nguồn của lớp A nhắc đến tên lớp B, nhưng lớp B không nhắc đến gì về lớp A. Do đó, trong Hình 8.2, `FinancialDataMapper` biết đến `FinancialDataGateway` qua quan hệ triển khai, nhưng `FinancialGateway` không biết bất cứ điều gì về `FinancialDataMapper`.

Điều tiếp theo cần nhận thấy là mỗi đường kẻ đôi chỉ bị cắt theo một chiều. Điều này nghĩa là tất cả các quan hệ giữa các thành phần đều đơn hướng, như đồ thị thành phần trong Hình 8.3. Các mũi tên này chỉ về phía các thành phần chúng ta muốn bảo vệ khỏi sự thay đổi.
**Hình 8.3** Các quan hệ giữa các thành phần là đơn hướng

Để tôi nói lại lần nữa: Nếu thành phần A nên được bảo vệ khỏi các thay đổi trong thành phần B, thì thành phần B nên phụ thuộc vào thành phần A.

Chúng ta muốn Interactor được bảo vệ khỏi mọi thay đổi, bất kể chúng đến từ đâu.

Interactor nằm ở vị trí phù hợp nhất với OCP. Thay đổi Database, hoặc Controller, hoặc Presenter, hoặc View sẽ không có tác động nào đến Interactor.

Tại sao Interactor lại được đặc quyền như vậy? Vì nó chứa các quy tắc nghiệp vụ. Interactor chứa các chính sách cấp cao nhất của ứng dụng. Tất cả các thành phần khác lo việc ngoại vi. Interactor lo việc cốt lõi.

Dù Controller là ngoại vi đối với Interactor, nó vẫn là cốt lõi đối với Presenter và View. Và trong khi Presenter có thể là ngoại vi đối với Controller, chúng lại là cốt lõi đối với View.

Chú ý cách này tạo ra một thứ bậc bảo vệ dựa trên khái niệm "cấp độ". Interactor là khái niệm cấp cao nhất, nên được bảo vệ nhất. View nằm trong số các khái niệm cấp thấp nhất, nên được bảo vệ kém nhất. Presenter cấp cao hơn View, nhưng thấp hơn Controller hoặc Interactor.

Đây là cách OCP hoạt động ở cấp độ kiến trúc. Kiến trúc sư tách biệt chức năng dựa trên *cách*, *lý do* và *thời điểm* xảy ra thay đổi, rồi tổ chức các chức năng đã tách biệt thành một thứ bậc thành phần. Các thành phần cấp cao hơn trong thứ bậc đó được bảo vệ khỏi những thay đổi ở các thành phần cấp thấp hơn.


## Kiểm soát chiều

Nếu thiết kế lớp ở trên khiến bạn hoảng hốt, hãy nhìn lại. Phần lớn độ phức tạp trong sơ đồ đó nhằm đảm bảo các phụ thuộc giữa các thành phần chỉ đúng chiều.

Ví dụ, giao diện `FinancialDataGateway` nằm giữa `FinancialReportGenerator` và `FinancialDataMapper` để đảo ngược phụ thuộc vốn sẽ hướng từ thành phần Interactor sang thành phần Database. Điều tương tự cũng đúng với giao diện `FinancialReportPresenter` và hai giao diện View.


## Che giấu thông tin

Giao diện `FinancialReportRequester` phục vụ mục đích khác. Nó ở đó để bảo vệ `FinancialReportController` khỏi việc biết quá nhiều về nội bộ của Interactor. Nếu giao diện đó không có, Controller sẽ có phụ thuộc bắc cầu đến `FinancialEntities`.

Phụ thuộc bắc cầu vi phạm nguyên tắc chung là các thực thể phần mềm không nên phụ thuộc vào những thứ chúng không sử dụng trực tiếp. Chúng ta sẽ gặp nguyên tắc đó lại khi nói về Nguyên tắc phân tách giao diện và Nguyên tắc tái sử dụng chung.

Vì vậy, dù ưu tiên đầu tiên là bảo vệ Interactor khỏi các thay đổi của Controller, chúng ta cũng muốn bảo vệ Controller khỏi các thay đổi của Interactor bằng cách che giấu nội bộ của Interactor.


## Kết luận

OCP là một trong những lực đẩy đằng sau kiến trúc của các hệ thống. Mục tiêu là làm cho hệ thống dễ dàng mở rộng mà không gánh chịu tác động thay đổi lớn. Mục tiêu này đạt được bằng cách phân chia hệ thống thành các thành phần, và sắp xếp các thành phần đó thành một thứ bậc phụ thuộc bảo vệ các thành phần cấp cao khỏi các thay đổi trong các thành phần cấp thấp.

[^1]: Bertrand Meyer. *Object Oriented Software Construction*, Prentice Hall, 1988, tr. 23.