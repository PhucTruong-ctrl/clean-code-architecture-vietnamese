# Chương 22: Kiến trúc sạch
![Minh họa](assets/illustrations/22-chuong-22-opener.png){w=300}

Trong vài thập kỷ qua, chúng ta đã thấy rất nhiều ý tưởng về kiến trúc hệ thống. Trong số đó có:

- Kiến trúc Lục giác, còn gọi là Cổng và Bộ chuyển đổi (Ports and Adapters), do Alistair Cockburn phát triển và được Steve Freeman cùng Nat Pryce áp dụng trong cuốn sách tuyệt vời *Growing Object Oriented Software with Tests*.
- DCI của James Coplien và Trygve Reenskaug.
- BCE, do Ivar Jacobson giới thiệu trong cuốn *Object Oriented Software Engineering: A Use-Case Driven Approach*.

Dù các kiến trúc này khác nhau đôi chút về chi tiết, chúng rất giống nhau. Tất cả đều hướng đến cùng một mục tiêu: phân tách các mối quan tâm. Chúng đều đạt được sự phân tách đó bằng cách chia phần mềm thành các lớp. Mỗi kiến trúc có ít nhất một lớp dành cho quy tắc nghiệp vụ và một lớp khác dành cho giao diện người dùng và hệ thống.

Mỗi kiến trúc này tạo ra các hệ thống có những đặc điểm sau:

- **Độc lập với framework.** Kiến trúc không phụ thuộc vào sự tồn tại của một thư viện phần mềm nhiều tính năng. Nhờ vậy, bạn có thể dùng framework như công cụ, thay vì phải nhồi hệ thống vào những giới hạn chật hẹp của framework.
- **Có thể kiểm thử.** Có thể kiểm thử các quy tắc nghiệp vụ mà không cần giao diện người dùng, cơ sở dữ liệu, máy chủ web hay bất kỳ yếu tố bên ngoài nào khác.
- **Độc lập với giao diện người dùng.** Có thể dễ dàng thay đổi giao diện mà không làm thay đổi phần còn lại của hệ thống. Chẳng hạn, có thể thay giao diện web bằng giao diện console mà không thay đổi quy tắc nghiệp vụ.
- **Độc lập với cơ sở dữ liệu.** Bạn có thể thay Oracle hoặc SQL Server bằng Mongo, BigTable, CouchDB hay một hệ thống khác. Quy tắc nghiệp vụ không bị ràng buộc với cơ sở dữ liệu.
- **Độc lập với mọi tác nhân bên ngoài.** Thực tế, quy tắc nghiệp vụ hoàn toàn không biết gì về các giao diện với thế giới bên ngoài.

Sơ đồ ở Hình 22.1 là nỗ lực kết hợp tất cả những kiến trúc này thành một ý tưởng có thể áp dụng.

**Hình 22.1** Kiến trúc sạch

## Quy tắc phụ thuộc

Các vòng tròn đồng tâm trong Hình 22.1 biểu thị những khu vực phần mềm khác nhau. Nhìn chung, càng đi vào trong, cấp độ phần mềm càng cao. Các vòng tròn bên ngoài là cơ chế. Các vòng tròn bên trong là chính sách.

Quy tắc chi phối giúp kiến trúc này hoạt động là Quy tắc Phụ thuộc:

> Phụ thuộc mã nguồn chỉ được hướng vào trong, về phía các chính sách cấp cao hơn.

Không có thành phần nào ở vòng tròn bên trong được biết bất kỳ điều gì về thành phần ở vòng tròn bên ngoài. Cụ thể, mã trong vòng tròn bên trong không được nhắc đến tên của bất kỳ thứ gì được khai báo ở vòng tròn bên ngoài. Điều đó bao gồm hàm, lớp, biến hay bất kỳ thực thể phần mềm nào có tên.

Tương tự, không nên dùng trong vòng tròn bên trong các định dạng dữ liệu được khai báo ở vòng tròn bên ngoài, nhất là khi những định dạng đó do một framework ở vòng ngoài tạo ra. Chúng ta không muốn bất kỳ thứ gì ở vòng ngoài ảnh hưởng đến các vòng tròn bên trong.

## Entity

Entity đóng gói các quy tắc nghiệp vụ cốt lõi trên phạm vi toàn doanh nghiệp. Entity có thể là một đối tượng với các phương thức, hoặc một tập hợp cấu trúc dữ liệu và hàm. Điều quan trọng là Entity có thể được dùng trong nhiều ứng dụng khác nhau của doanh nghiệp.

Nếu bạn không làm việc trong một doanh nghiệp lớn mà chỉ viết một ứng dụng đơn lẻ, thì các Entity này là đối tượng nghiệp vụ của ứng dụng. Chúng đóng gói những quy tắc tổng quát và cấp cao nhất. Chúng ít có khả năng thay đổi nhất khi có thay đổi bên ngoài. Chẳng hạn, bạn không kỳ vọng các đối tượng này bị ảnh hưởng khi thay đổi điều hướng trang hoặc bảo mật. Không thay đổi vận hành nào của một ứng dụng cụ thể nên ảnh hưởng đến lớp Entity.

## Ca sử dụng

Phần mềm ở lớp ca sử dụng chứa các quy tắc nghiệp vụ riêng của ứng dụng. Nó đóng gói và triển khai tất cả ca sử dụng của hệ thống. Các ca sử dụng điều phối luồng dữ liệu đi đến và đi khỏi Entity, đồng thời chỉ đạo Entity dùng các quy tắc nghiệp vụ cốt lõi để đạt mục tiêu của ca sử dụng.

Chúng ta không kỳ vọng thay đổi ở lớp này sẽ ảnh hưởng đến Entity. Cũng không kỳ vọng lớp này bị ảnh hưởng bởi những thay đổi bên ngoài, chẳng hạn cơ sở dữ liệu, giao diện người dùng hay các framework phổ biến. Lớp ca sử dụng được cách ly khỏi những mối quan tâm đó.

Tuy nhiên, chúng ta kỳ vọng thay đổi trong cách ứng dụng vận hành sẽ ảnh hưởng đến các ca sử dụng và do đó ảnh hưởng đến phần mềm ở lớp này. Nếu chi tiết của một ca sử dụng thay đổi, chắc chắn một phần mã trong lớp này cũng phải thay đổi.

## Bộ chuyển đổi giao diện

Phần mềm ở lớp bộ chuyển đổi giao diện là tập hợp các bộ chuyển đổi, giúp chuyển dữ liệu từ định dạng thuận tiện nhất cho ca sử dụng và Entity sang định dạng thuận tiện nhất cho tác nhân bên ngoài, chẳng hạn cơ sở dữ liệu hoặc web. Chẳng hạn, lớp này chứa toàn bộ kiến trúc MVC của giao diện người dùng đồ họa. Presenter, view và controller đều thuộc lớp bộ chuyển đổi giao diện. Model thường chỉ là các cấu trúc dữ liệu được truyền từ controller đến ca sử dụng, rồi từ ca sử dụng trở lại presenter và view.

Tương tự, ở lớp này dữ liệu được chuyển từ dạng thuận tiện nhất cho Entity và ca sử dụng sang dạng thuận tiện nhất cho framework lưu trữ đang dùng, tức cơ sở dữ liệu. Không mã nào ở phía trong vòng tròn này được biết bất kỳ điều gì về cơ sở dữ liệu. Nếu cơ sở dữ liệu là SQL, thì toàn bộ câu lệnh SQL phải nằm trong lớp này, đặc biệt là những phần liên quan đến cơ sở dữ liệu.

Lớp này cũng chứa mọi bộ chuyển đổi cần thiết để chuyển dữ liệu từ dạng bên ngoài, chẳng hạn dịch vụ bên ngoài, sang dạng nội bộ mà ca sử dụng và Entity sử dụng.

## Framework và trình điều khiển

Lớp ngoài cùng của mô hình trong Hình 22.1 thường gồm framework và công cụ như cơ sở dữ liệu và framework web. Thông thường, bạn không viết nhiều mã trong lớp này, ngoài mã kết nối để giao tiếp với vòng tròn kế tiếp ở phía trong.

Lớp framework và trình điều khiển chứa mọi chi tiết. Web là chi tiết. Cơ sở dữ liệu là chi tiết. Chúng ta giữ những thứ này ở bên ngoài để chúng ít gây hại nhất.

## Chỉ có bốn vòng tròn?

Các vòng tròn trong Hình 22.1 chỉ mang tính sơ đồ. Bạn có thể cần nhiều hơn bốn vòng tròn. Không có quy tắc nào bắt buộc lúc nào cũng phải có đúng bốn vòng tròn. Tuy nhiên, Quy tắc Phụ thuộc luôn được áp dụng. Phụ thuộc mã nguồn luôn hướng vào trong. Càng đi vào trong, mức độ trừu tượng và chính sách càng tăng. Vòng tròn ngoài cùng gồm các chi tiết cụ thể cấp thấp. Khi đi vào trong, phần mềm trở nên trừu tượng hơn và đóng gói các chính sách cấp cao hơn. Vòng tròn trong cùng là cấp cao và tổng quát nhất.

## Vượt qua ranh giới

Ở góc dưới bên phải của sơ đồ Hình 22.1 có ví dụ về cách vượt qua ranh giới giữa các vòng tròn. Sơ đồ cho thấy controller và presenter giao tiếp với ca sử dụng ở lớp kế tiếp. Hãy chú ý luồng điều khiển: nó bắt đầu từ controller, đi qua ca sử dụng rồi kết thúc bằng việc thực thi trong presenter. Cũng hãy chú ý các phụ thuộc mã nguồn, tất cả đều hướng vào trong, về phía các ca sử dụng.

Thông thường, chúng ta giải quyết mâu thuẫn có vẻ như tồn tại này bằng Nguyên tắc Đảo ngược Phụ thuộc. Chẳng hạn, trong Java, chúng ta sắp xếp các giao diện và quan hệ kế thừa sao cho tại những điểm thích hợp trên ranh giới, phụ thuộc mã nguồn đi ngược với luồng điều khiển.

Ví dụ, giả sử ca sử dụng cần gọi presenter. Không thể gọi trực tiếp vì như vậy sẽ vi phạm Quy tắc Phụ thuộc: vòng tròn bên trong không được nhắc đến tên nào thuộc vòng tròn bên ngoài. Vì thế, ca sử dụng gọi một giao diện ở vòng tròn trong, được ghi là “cổng đầu ra của ca sử dụng” trong Hình 22.1, còn presenter ở vòng tròn ngoài triển khai giao diện đó.

Kỹ thuật tương tự được dùng để vượt qua mọi ranh giới trong các kiến trúc này. Chúng ta tận dụng đa hình động để tạo các phụ thuộc mã nguồn đi ngược với luồng điều khiển, nhờ đó tuân theo Quy tắc Phụ thuộc bất kể luồng điều khiển đi theo hướng nào.

## Dữ liệu nào đi qua ranh giới?

Thông thường, dữ liệu đi qua ranh giới là các cấu trúc dữ liệu đơn giản. Bạn có thể dùng struct cơ bản hoặc đối tượng truyền dữ liệu đơn giản. Dữ liệu cũng có thể chỉ là các đối số trong lời gọi hàm. Hoặc bạn có thể gói nó trong một hashmap hay tạo thành một đối tượng. Điều quan trọng là truyền qua ranh giới các cấu trúc dữ liệu đơn giản, độc lập. Chúng ta không được lách quy tắc bằng cách truyền đối tượng Entity hoặc hàng dữ liệu từ cơ sở dữ liệu. Các cấu trúc dữ liệu ấy không được có bất kỳ phụ thuộc nào vi phạm Quy tắc Phụ thuộc.

Chẳng hạn, nhiều framework cơ sở dữ liệu trả về một định dạng dữ liệu tiện dụng sau khi truy vấn. Ta có thể gọi đó là “cấu trúc hàng”. Không nên truyền cấu trúc hàng ấy qua ranh giới vào phía trong. Làm vậy sẽ vi phạm Quy tắc Phụ thuộc vì buộc vòng tròn bên trong phải biết về thứ thuộc vòng tròn bên ngoài.

Vì vậy, khi truyền dữ liệu qua ranh giới, dữ liệu luôn ở dạng thuận tiện nhất cho vòng tròn bên trong.

## Kịch bản điển hình

Sơ đồ ở Hình 22.2 cho thấy một kịch bản điển hình cho hệ thống Java chạy trên web và dùng cơ sở dữ liệu. Máy chủ web thu thập dữ liệu đầu vào từ người dùng rồi chuyển cho `Controller` ở góc trên bên trái. `Controller` đóng gói dữ liệu thành một đối tượng Java thông thường rồi truyền đối tượng này qua `InputBoundary` đến `UseCaseInteractor`. `UseCaseInteractor` diễn giải dữ liệu và dùng nó để điều phối các Entity. Nó cũng dùng `DataAccessInterface` để nạp từ cơ sở dữ liệu vào bộ nhớ dữ liệu mà các Entity cần. Khi hoàn tất, `UseCaseInteractor` thu thập dữ liệu từ các Entity và tạo `OutputData` dưới dạng một đối tượng Java thông thường khác. Sau đó, `OutputData` được truyền qua giao diện `OutputBoundary` đến `Presenter`.

**Hình 22.2** Kịch bản điển hình cho hệ thống Java trên web sử dụng cơ sở dữ liệu

Nhiệm vụ của `Presenter` là đóng gói lại `OutputData` thành dạng có thể hiển thị, gọi là `ViewModel`, cũng là một đối tượng Java thông thường. `ViewModel` chủ yếu chứa chuỗi và cờ mà `View` dùng để hiển thị dữ liệu. Trong khi `OutputData` có thể chứa các đối tượng `Date`, `Presenter` sẽ điền vào `ViewModel` các chuỗi tương ứng đã được định dạng phù hợp cho người dùng. Điều tương tự cũng áp dụng cho đối tượng `Currency` và mọi dữ liệu nghiệp vụ khác. Tên nút bấm và mục menu được đặt trong `ViewModel`, cùng với các cờ cho `View` biết những nút bấm và mục menu nào cần chuyển sang màu xám.

Nhờ vậy, `View` hầu như không phải làm gì ngoài việc chuyển dữ liệu từ `ViewModel` vào trang HTML.

Hãy chú ý hướng của các phụ thuộc. Tất cả đều vượt qua ranh giới và hướng vào trong, đúng theo Quy tắc Phụ thuộc.

## Kết luận

Tuân theo những quy tắc đơn giản này không khó, và điều đó sẽ giúp bạn tránh được nhiều phiền toái về sau. Bằng cách chia phần mềm thành các lớp và tuân theo Quy tắc Phụ thuộc, bạn sẽ tạo ra một hệ thống vốn có thể kiểm thử, cùng mọi lợi ích đi kèm. Khi một thành phần bên ngoài nào đó trở nên lỗi thời, chẳng hạn cơ sở dữ liệu hoặc framework web, bạn có thể thay thế nó mà không gặp nhiều phiền phức.
