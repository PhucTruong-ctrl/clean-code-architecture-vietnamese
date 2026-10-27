# Chương 28: Ranh giới kiểm thử
![Minh họa](assets/illustrations/28-chuong-28-opener.png){w=300}

Đúng vậy: kiểm thử là một phần của hệ thống và tham gia vào kiến trúc như mọi phần khác. Có khía cạnh mà sự tham gia này khá bình thường. Nhưng ở khía cạnh khác, nó có thể rất đặc thù.

## Kiểm thử là thành phần của hệ thống

Có nhiều nhầm lẫn về kiểm thử. Chúng có thuộc hệ thống không? Chúng tách biệt khỏi hệ thống không? Có những loại kiểm thử nào? Kiểm thử đơn vị và kiểm thử tích hợp có khác nhau không? Còn kiểm thử chấp nhận, kiểm thử chức năng, kiểm thử Cucumber, kiểm thử TDD, kiểm thử BDD, kiểm thử thành phần, v.v. thì sao?

Cuốn sách này không nhằm sa vào cuộc tranh luận đó, và may mắn là cũng không cần thiết. Từ góc nhìn kiến trúc, mọi kiểm thử đều giống nhau. Dù là những kiểm thử nhỏ xíu do TDD tạo ra, hay các kiểm thử lớn bằng FitNesse, Cucumber, SpecFlow hoặc JBehave, chúng đều tương đương về mặt kiến trúc.

Bản chất của kiểm thử là tuân theo Quy tắc Phụ thuộc. Chúng rất chi tiết và cụ thể, đồng thời luôn phụ thuộc vào trong, về phía mã được kiểm thử. Thực tế, bạn có thể xem kiểm thử là vòng tròn ngoài cùng của kiến trúc. Không thành phần nào trong hệ thống phụ thuộc vào kiểm thử, còn kiểm thử luôn phụ thuộc vào trong, vào các thành phần của hệ thống.

Kiểm thử cũng có thể được triển khai độc lập. Thực tế, phần lớn thời gian chúng được triển khai trong các hệ thống kiểm thử chứ không phải hệ thống production. Vì vậy, ngay cả trong hệ thống không cần triển khai độc lập ở nơi khác, kiểm thử vẫn được triển khai độc lập.

Kiểm thử là thành phần bị cô lập nhất trong hệ thống. Chúng không cần thiết để hệ thống vận hành. Không người dùng nào phụ thuộc vào chúng. Vai trò của chúng là hỗ trợ phát triển, không phải vận hành. Dù vậy, chúng vẫn là thành phần của hệ thống như mọi thành phần khác. Thực tế, ở nhiều khía cạnh, chúng là hình mẫu mà các thành phần khác nên noi theo.

## Thiết kế để dễ kiểm thử

Kiểm thử bị cô lập rất mạnh và thường không được triển khai cùng hệ thống. Điều này khiến các nhà phát triển nghĩ rằng kiểm thử nằm ngoài thiết kế hệ thống. Đây là một quan điểm tai hại. Kiểm thử không được tích hợp tốt vào thiết kế thường trở nên mong manh, đồng thời khiến hệ thống cứng nhắc và khó thay đổi.

Vấn đề nằm ở sự phụ thuộc. Kiểm thử phụ thuộc chặt chẽ vào hệ thống thì phải thay đổi cùng hệ thống. Ngay cả thay đổi nhỏ nhất trong một thành phần hệ thống cũng có thể làm nhiều kiểm thử phụ thuộc bị hỏng hoặc buộc phải sửa.

Tình trạng này có thể trở nên nghiêm trọng. Thay đổi ở một thành phần hệ thống dùng chung có thể làm hỏng hàng trăm, thậm chí hàng nghìn kiểm thử. Đây được gọi là Vấn đề Kiểm thử Mong manh (Fragile Tests Problem).

Không khó để thấy điều này xảy ra như thế nào. Chẳng hạn, hãy tưởng tượng một bộ kiểm thử dùng giao diện đồ họa để xác minh quy tắc nghiệp vụ. Kiểm thử có thể bắt đầu từ màn hình đăng nhập rồi điều hướng qua cấu trúc trang cho đến khi kiểm tra được một quy tắc nghiệp vụ cụ thể. Bất kỳ thay đổi nào ở trang đăng nhập hoặc cấu trúc điều hướng đều có thể làm hỏng vô số kiểm thử.

Kiểm thử mong manh thường khiến hệ thống trở nên cứng nhắc một cách trái ngược với mục đích ban đầu. Khi nhận ra rằng thay đổi đơn giản trong hệ thống có thể gây ra hàng loạt lỗi kiểm thử, nhà phát triển có thể ngần ngại thực hiện thay đổi. Chẳng hạn, hãy tưởng tượng cuộc trao đổi giữa nhóm phát triển và nhóm tiếp thị, khi nhóm tiếp thị yêu cầu thay đổi đơn giản trong cấu trúc điều hướng khiến 1.000 kiểm thử bị hỏng.

Giải pháp là thiết kế để dễ kiểm thử. Quy tắc đầu tiên của thiết kế phần mềm, dù vì khả năng kiểm thử hay vì lý do nào khác, vẫn luôn như nhau: **Đừng phụ thuộc vào những thứ hay biến động.** Giao diện đồ họa hay biến động. Bộ kiểm thử thao tác hệ thống qua giao diện đồ họa sẽ mong manh. Vì vậy, hãy thiết kế hệ thống và kiểm thử sao cho có thể kiểm tra quy tắc nghiệp vụ mà không cần dùng giao diện đồ họa.

## API kiểm thử

Cách đạt được mục tiêu này là tạo một API riêng để kiểm thử mọi quy tắc nghiệp vụ. API này cần có quyền hạn đặc biệt, cho phép kiểm thử vượt qua giới hạn bảo mật, bỏ qua tài nguyên tốn kém như cơ sở dữ liệu, và đưa hệ thống vào các trạng thái cụ thể để kiểm thử. API này sẽ là tập hợp mở rộng của các interactor và bộ chuyển đổi giao diện được giao diện người dùng sử dụng.

Mục đích của API kiểm thử là tách kiểm thử khỏi ứng dụng. Sự tách rời này không chỉ có nghĩa là bỏ phụ thuộc vào giao diện người dùng. Mục tiêu là tách cấu trúc của bộ kiểm thử khỏi cấu trúc của ứng dụng.

## Phụ thuộc cấu trúc

Phụ thuộc cấu trúc là một trong những dạng phụ thuộc kiểm thử mạnh nhất và khó nhận biết nhất. Hãy tưởng tượng một bộ kiểm thử có một lớp kiểm thử cho từng lớp production và một tập phương thức kiểm thử cho từng phương thức production. Bộ kiểm thử như vậy phụ thuộc sâu sắc vào cấu trúc ứng dụng.

Khi một phương thức hoặc lớp production thay đổi, nhiều kiểm thử cũng phải thay đổi. Do đó, kiểm thử trở nên mong manh và khiến mã production cứng nhắc.

Vai trò của API kiểm thử là che giấu cấu trúc ứng dụng khỏi các kiểm thử. Điều này cho phép tái cấu trúc và phát triển mã production mà không ảnh hưởng đến kiểm thử. Nó cũng cho phép tái cấu trúc và phát triển kiểm thử mà không ảnh hưởng đến mã production.

Sự tách biệt trong quá trình phát triển này rất cần thiết vì theo thời gian, kiểm thử thường ngày càng cụ thể và chi tiết. Ngược lại, mã production ngày càng trừu tượng và tổng quát. Phụ thuộc cấu trúc chặt chẽ ngăn cản, hoặc ít nhất cản trở, sự phát triển cần thiết này và khiến mã production kém tổng quát, kém linh hoạt hơn mức có thể.

## Bảo mật

Các quyền hạn đặc biệt của API kiểm thử có thể nguy hiểm nếu được triển khai trong hệ thống production. Nếu đây là mối lo ngại, hãy giữ API kiểm thử và những phần triển khai nguy hiểm của nó trong một thành phần riêng, có thể triển khai độc lập.

## Kết luận

Kiểm thử không nằm ngoài hệ thống. Chúng là một phần của hệ thống và cần được thiết kế tốt để đem lại lợi ích về tính ổn định và hồi quy. Kiểm thử không được thiết kế như một phần của hệ thống thường trở nên mong manh và khó bảo trì. Cuối cùng, chúng có thể bị bỏ xó trong phòng bảo trì vì quá khó duy trì.