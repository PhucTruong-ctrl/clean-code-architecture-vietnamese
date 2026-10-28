# Chương 34: Chương còn thiếu
![Minh họa](assets/illustrations/34-chuong-34-opener.png){w=300}
> Simon Brown

Tất cả lời khuyên bạn đã đọc đến đây chắc chắn sẽ giúp thiết kế phần mềm tốt hơn, với các lớp và thành phần có ranh giới rõ ràng, trách nhiệm minh bạch và phụ thuộc được kiểm soát. Nhưng hóa ra ma quỷ lại ẩn trong chi tiết triển khai, và rất dễ thất bại ở chặng cuối nếu không suy nghĩ kỹ về chúng.

Hãy tưởng tượng chúng ta đang xây dựng một hiệu sách trực tuyến. Một trong những ca sử dụng cần triển khai cho phép khách hàng xem trạng thái đơn hàng. Dù ví dụ này dùng Java, các nguyên tắc cũng áp dụng cho ngôn ngữ lập trình khác. Tạm gác Kiến trúc Sạch sang một bên và xem một số cách thiết kế, tổ chức mã.

## Chia gói theo lớp

Cách tiếp cận đầu tiên, và có lẽ đơn giản nhất, là kiến trúc phân lớp ngang truyền thống, trong đó ta tách mã dựa trên chức năng kỹ thuật của nó. Cách này thường được gọi là “chia gói theo lớp”. Hình 34.1 cho thấy một ví dụ dưới dạng sơ đồ lớp UML.

Trong kiến trúc phân lớp điển hình này, có một lớp cho mã web, một lớp cho “logic nghiệp vụ” và một lớp cho lưu trữ. Nói cách khác, mã được chia ngang thành các lớp để nhóm những loại thành phần tương tự. Trong “kiến trúc phân lớp nghiêm ngặt”, mỗi lớp chỉ nên phụ thuộc vào lớp liền kề bên dưới. Trong Java, các lớp thường được triển khai thành các package. Như Hình 34.1 cho thấy, mọi phụ thuộc giữa các lớp (package) đều hướng xuống dưới. Ví dụ này có các kiểu Java sau:

- `OrdersController`: controller web, tương tự controller Spring MVC, xử lý yêu cầu từ web.
- `OrdersService`: giao diện xác định “logic nghiệp vụ” liên quan đến đơn hàng.
- `OrdersServiceImpl`: phần triển khai dịch vụ đơn hàng.[^1]
- `OrdersRepository`: giao diện xác định cách truy cập thông tin đơn hàng đã lưu.
- `JdbcOrdersRepository`: phần triển khai giao diện repository.

**Hình 34.1** Chia gói theo lớp

Trong bài “Presentation Domain Data Layering”,[^2] Martin Fowler nói rằng chọn kiến trúc phân lớp như vậy là cách khởi đầu tốt. Ông không phải người duy nhất nghĩ vậy. Nhiều sách, hướng dẫn, khóa đào tạo và mã ví dụ bạn tìm thấy cũng khuyên tạo kiến trúc phân lớp. Đây là cách nhanh để khởi động hệ thống mà không cần nhiều phức tạp. Tuy nhiên, như Martin chỉ ra, khi phần mềm mở rộng và phức tạp hơn, bạn sẽ sớm thấy ba “xô” mã lớn là không đủ và cần nghĩ đến việc mô-đun hóa sâu hơn.

Một vấn đề khác, như Uncle Bob đã nói, là kiến trúc phân lớp không thể hiện rõ miền nghiệp vụ. Đặt cạnh nhau mã của hai kiến trúc phân lớp thuộc hai miền nghiệp vụ rất khác nhau, chúng có thể trông giống nhau đến kỳ lạ: web, dịch vụ và repository. Còn một vấn đề lớn khác với kiến trúc phân lớp, nhưng chúng ta sẽ nói đến sau.

## Chia gói theo tính năng

Một cách khác để tổ chức mã là dùng phong cách “chia gói theo tính năng”. Đây là cách chia dọc dựa trên các tính năng liên quan, khái niệm miền hoặc aggregate root, theo thuật ngữ thiết kế hướng miền. Trong những cách triển khai điển hình mà tôi từng thấy, mọi kiểu được đặt trong cùng một Java package, tên package phản ánh khái niệm được nhóm lại.

Với cách này, như Hình 34.2 cho thấy, ta vẫn có các giao diện và lớp như trước, nhưng tất cả được đặt trong một Java package thay vì chia thành ba package. Đây là tái cấu trúc rất đơn giản so với cách “chia gói theo lớp”, nhưng cấu trúc cấp cao nhất của mã giờ thể hiện miền nghiệp vụ. Ta thấy mã này liên quan đến đơn hàng chứ không chỉ là web, dịch vụ và repository.

Một lợi ích khác là có thể dễ tìm hơn toàn bộ mã cần sửa khi ca sử dụng “xem đơn hàng” thay đổi. Mọi thứ nằm trong cùng một Java package thay vì rải khắp nơi.[^3]

Tôi thường thấy các nhóm phát triển nhận ra mình gặp vấn đề với phân lớp ngang (“chia gói theo lớp”), rồi chuyển sang phân lớp dọc (“chia gói theo tính năng”). Theo tôi, cả hai cách đều chưa tối ưu. Nếu đã đọc đến đây, có thể bạn đang nghĩ rằng còn cách tốt hơn, và bạn nghĩ đúng.

**Hình 34.2** Chia gói theo tính năng

## Cổng và bộ chuyển đổi

Như Uncle Bob đã nói, các cách tiếp cận như “cổng và bộ chuyển đổi”, “kiến trúc lục giác”, “ranh giới, controller, entity” và những cách tương tự nhằm tạo kiến trúc trong đó mã tập trung vào nghiệp vụ hoặc miền được tách biệt và độc lập với chi tiết triển khai kỹ thuật như framework và cơ sở dữ liệu. Tóm lại, ta thường thấy mã nguồn được chia thành phần “bên trong” (miền) và phần “bên ngoài” (hạ tầng), như Hình 34.3 gợi ý.

**Hình 34.3** Mã nguồn có phần bên trong và bên ngoài

Vùng “bên trong” chứa mọi khái niệm miền, còn vùng “bên ngoài” chứa các tương tác với thế giới bên ngoài, chẳng hạn giao diện người dùng, cơ sở dữ liệu và tích hợp bên thứ ba. Quy tắc chính là phần “bên ngoài” phụ thuộc vào phần “bên trong”, không bao giờ ngược lại. Hình 34.4 cho thấy một phiên bản triển khai ca sử dụng “xem đơn hàng”.

Package `com.mycompany.myapp.domain` là phần “bên trong”; các package khác là phần “bên ngoài”. Hãy chú ý phụ thuộc đều hướng về phía “bên trong”. Độc giả tinh ý sẽ nhận thấy `OrdersRepository` trong các sơ đồ trước đã được đổi tên thành `Orders`. Cách đặt tên này xuất phát từ thiết kế hướng miền, trong đó mọi thứ ở “bên trong” nên được gọi theo “ngôn ngữ phổ quát của miền”. Nói cách khác, khi thảo luận về miền, ta nói về “đơn hàng”, không phải “repository đơn hàng”.

**Hình 34.4** Ca sử dụng xem đơn hàng

Cũng cần lưu ý đây là phiên bản đơn giản hóa của sơ đồ lớp UML, vì nó thiếu các thành phần như interactor và đối tượng dùng để tổ chức dữ liệu qua ranh giới phụ thuộc.

## Chia gói theo thành phần

Dù hoàn toàn đồng ý với các thảo luận về SOLID, REP, CCP và CRP cũng như phần lớn lời khuyên trong cuốn sách này, tôi đi đến kết luận hơi khác về cách tổ chức mã. Vì vậy, tôi sẽ trình bày một lựa chọn khác, gọi là “chia gói theo thành phần”. Để cung cấp bối cảnh, phần lớn sự nghiệp của tôi là xây dựng phần mềm doanh nghiệp, chủ yếu bằng Java, cho nhiều miền nghiệp vụ khác nhau. Các hệ thống ấy cũng rất đa dạng. Phần lớn chạy trên web, nhưng một số dùng kiến trúc máy khách-máy chủ,[^4] phân tán, dựa trên thông điệp hoặc mô hình khác. Công nghệ có khác nhau, nhưng điểm chung là kiến trúc của hầu hết hệ thống dựa trên kiến trúc phân lớp truyền thống.

Tôi đã nêu vài lý do nên xem kiến trúc phân lớp là không tốt, nhưng đó chưa phải toàn bộ câu chuyện. Mục đích của kiến trúc phân lớp là tách mã có cùng chức năng. Phần web được tách khỏi logic nghiệp vụ, rồi logic nghiệp vụ được tách khỏi truy cập dữ liệu. Như ta thấy trong sơ đồ lớp UML, khi triển khai, một lớp thường tương ứng với một Java package. Để `OrdersController` có thể phụ thuộc vào giao diện `OrdersService`, giao diện này phải được đánh dấu `public` vì chúng nằm trong các package khác nhau. Tương tự, giao diện `OrdersRepository` phải là `public` để lớp `OrdersServiceImpl` có thể truy cập từ ngoài package repository.

Trong kiến trúc phân lớp nghiêm ngặt, các mũi tên phụ thuộc luôn phải hướng xuống, mỗi lớp chỉ phụ thuộc vào lớp liền kề bên dưới. Điều này giúp tạo đồ thị phụ thuộc không chu trình gọn gàng, đạt được bằng cách đặt quy tắc về cách các thành phần trong mã nguồn được phép phụ thuộc nhau. Vấn đề lớn là ta có thể gian lận bằng cách tạo phụ thuộc không mong muốn mà vẫn giữ được một đồ thị phụ thuộc không chu trình.

Giả sử bạn tuyển một người mới vào nhóm và giao cho họ triển khai một ca sử dụng khác liên quan đến đơn hàng. Vì mới vào nhóm, người đó muốn gây ấn tượng và hoàn thành ca sử dụng thật nhanh. Sau vài phút ngồi uống cà phê, họ tìm thấy lớp `OrdersController` hiện có và quyết định đặt mã cho trang web mới liên quan đến đơn hàng vào đó. Nhưng trang cần dữ liệu đơn hàng từ cơ sở dữ liệu. Người mới chợt nghĩ ra: “Ồ, đã có giao diện `OrdersRepository` rồi. Mình chỉ cần tiêm phần triển khai vào controller là xong!” Vài phút sau, trang web hoạt động. Nhưng sơ đồ UML thu được trông như Hình 34.5.

Các mũi tên phụ thuộc vẫn hướng xuống, nhưng giờ `OrdersController` bỏ qua `OrdersService` trong một số ca sử dụng. Cách tổ chức này thường gọi là kiến trúc phân lớp lỏng, trong đó một lớp được phép bỏ qua các lớp liền kề. Trong một số tình huống đây là kết quả có chủ ý, chẳng hạn khi áp dụng mẫu CQRS.[^5] Trong nhiều trường hợp khác, bỏ qua lớp logic nghiệp vụ là điều không mong muốn, nhất là khi lớp này chịu trách nhiệm bảo đảm quyền truy cập vào từng bản ghi.

Ca sử dụng mới hoạt động, nhưng có lẽ không được triển khai như ta kỳ vọng. Tôi thường thấy điều này ở các nhóm tư vấn, và thường chỉ lộ ra khi nhóm lần đầu hình dung được cấu trúc thực sự của mã nguồn.

**Hình 34.5** Kiến trúc phân lớp lỏng

Ở đây cần một hướng dẫn, một nguyên tắc kiến trúc, đại loại như: “Controller web không bao giờ được truy cập repository trực tiếp”. Dĩ nhiên, câu hỏi là làm sao thực thi quy tắc đó. Nhiều nhóm tôi gặp chỉ nói: “Chúng tôi thực thi nguyên tắc này bằng kỷ luật tốt và đánh giá mã, vì tin tưởng các nhà phát triển.” Sự tự tin đó thật đáng mừng, nhưng ai cũng biết chuyện gì xảy ra khi ngân sách và hạn chót ngày càng đến gần.

Một số ít nhóm khác cho biết họ dùng công cụ phân tích tĩnh, chẳng hạn NDepend, Structure101 và Checkstyle, để phát hiện và tự động thực thi các vi phạm kiến trúc trong lúc build. Có thể bạn từng thấy các quy tắc như vậy. Chúng thường là biểu thức chính quy hoặc chuỗi ký tự đại diện, quy định rằng “kiểu trong package `**/web` không được truy cập kiểu trong `**/data`”, rồi được chạy sau bước biên dịch.

Cách tiếp cận này hơi thô sơ nhưng có thể hiệu quả. Nó báo cáo các vi phạm nguyên tắc kiến trúc do nhóm xác định và, hy vọng, làm build thất bại. Vấn đề của cả hai cách là chúng có thể sai sót, và vòng phản hồi dài hơn mức cần thiết. Nếu không kiểm soát, mã nguồn có thể biến thành “quả cầu bùn lớn”.[^6] Nếu có thể, cá nhân tôi muốn dùng trình biên dịch để thực thi kiến trúc.

Đó là lúc đến với lựa chọn “chia gói theo thành phần”. Đây là cách tiếp cận lai, kết hợp những gì đã thấy, nhằm gom mọi trách nhiệm liên quan đến một thành phần có độ hạt lớn vào một Java package. Cách này nhìn hệ thống theo hướng lấy dịch vụ làm trung tâm, cũng là điều ta thấy trong kiến trúc vi dịch vụ. Giống như cổng và bộ chuyển đổi xem web chỉ là một cơ chế phân phối khác, “chia gói theo thành phần” vẫn tách giao diện người dùng khỏi các thành phần có độ hạt lớn đó. Hình 34.6 cho thấy một cách triển khai ca sử dụng “xem đơn hàng”.

Về bản chất, cách tiếp cận này gom “logic nghiệp vụ” và mã lưu trữ dữ liệu vào một đơn vị mà tôi gọi là “thành phần”. Trước đó trong sách, Uncle Bob định nghĩa “thành phần” như sau:

> Thành phần là đơn vị triển khai. Chúng là thực thể nhỏ nhất có thể được triển khai trong một hệ thống. Trong Java, chúng là các tệp jar.

**Hình 34.6** Ca sử dụng xem đơn hàng

Định nghĩa thành phần của tôi hơi khác: “Một nhóm chức năng liên quan được đặt sau một giao diện rõ ràng, nằm trong môi trường thực thi như ứng dụng”. Định nghĩa này xuất phát từ “mô hình kiến trúc phần mềm C4” của tôi,[^7] một cách phân cấp đơn giản để hình dung cấu trúc tĩnh của hệ thống phần mềm bằng container, thành phần và lớp (hoặc mã nguồn). Theo mô hình này, hệ thống phần mềm gồm một hoặc nhiều container, chẳng hạn ứng dụng web, ứng dụng di động, ứng dụng độc lập, cơ sở dữ liệu hoặc hệ thống tệp. Mỗi container chứa một hoặc nhiều thành phần, mỗi thành phần được triển khai bằng một hoặc nhiều lớp (hoặc đoạn mã). Việc mỗi thành phần có nằm trong tệp jar riêng hay không là mối quan tâm độc lập với những điều đó.

Lợi ích chính của cách “chia gói theo thành phần” là nếu viết mã cần làm việc với đơn hàng thì chỉ có một nơi cần tìm: `OrdersComponent`. Bên trong thành phần, sự phân tách mối quan tâm vẫn được duy trì, nên logic nghiệp vụ vẫn tách khỏi lưu trữ dữ liệu. Nhưng đó là chi tiết triển khai mà người dùng thành phần không cần biết. Cách này tương tự kết quả khi dùng kiến trúc vi dịch vụ hoặc Kiến trúc Hướng Dịch vụ: một `OrdersService` riêng đóng gói mọi thứ liên quan đến xử lý đơn hàng. Điểm khác biệt chính là chế độ tách rời. Có thể xem các thành phần được định nghĩa rõ trong ứng dụng nguyên khối như bước đệm hướng đến kiến trúc vi dịch vụ.

## Ma quỷ ẩn trong chi tiết triển khai

Thoạt nhìn, cả bốn cách tiếp cận đều có vẻ là những cách tổ chức mã khác nhau, nên có thể được xem là các kiểu kiến trúc khác nhau. Nhưng nhận định này nhanh chóng sụp đổ nếu triển khai sai chi tiết.

Tôi thường xuyên thấy người ta dùng quá thoải mái từ bổ nghĩa truy cập `public` trong các ngôn ngữ như Java. Có vẻ như lập trình viên dùng từ khóa `public` theo bản năng, không cần suy nghĩ. Nó đã thành phản xạ. Nếu không tin, hãy xem các mẫu mã trong sách, hướng dẫn và framework mã nguồn mở trên GitHub. Xu hướng này xuất hiện bất kể mã nguồn hướng đến kiểu kiến trúc nào: lớp ngang, lớp dọc, cổng và bộ chuyển đổi hay kiểu khác. Đánh dấu mọi kiểu là `public` nghĩa là bạn không tận dụng các cơ chế đóng gói mà ngôn ngữ lập trình cung cấp. Trong một số trường hợp, không có gì ngăn ai đó viết mã khởi tạo trực tiếp một lớp triển khai cụ thể, vi phạm kiến trúc dự định.

## Tổ chức và đóng gói

Nhìn vấn đề theo cách khác, nếu mọi kiểu trong ứng dụng Java đều là `public`, package chỉ còn là cơ chế tổ chức, một cách nhóm như thư mục, chứ không còn dùng để đóng gói. Vì kiểu `public` có thể được dùng ở bất kỳ đâu trong mã nguồn, bạn có thể bỏ qua package vì chúng hầu như không đem lại giá trị thực. Kết quả là nếu bỏ qua package vì chúng không cung cấp cách đóng gói và che giấu, thì kiểu kiến trúc bạn muốn tạo ra cũng không còn quan trọng. Nhìn lại các sơ đồ UML, package Java trở thành chi tiết không liên quan nếu mọi kiểu đều được đánh dấu `public`. Về bản chất, cả bốn cách tiếp cận kiến trúc ở trên đều giống nhau khi lạm dụng từ bổ nghĩa này (Hình 34.7).

Hãy xem kỹ các mũi tên giữa các kiểu trong Hình 34.7. Chúng đều giống nhau bất kể bạn đang theo kiểu kiến trúc nào. Về khái niệm, các cách tiếp cận rất khác nhau, nhưng về cú pháp lại giống hệt. Hơn nữa, có thể lập luận rằng nếu mọi kiểu đều `public`, thì thực chất bạn chỉ có bốn cách mô tả kiến trúc phân lớp ngang truyền thống. Đây là một thủ thuật thú vị. Dĩ nhiên, không ai lại đánh dấu mọi kiểu Java là `public`. Trừ những lúc họ làm vậy. Tôi đã thấy chuyện đó.

Từ bổ nghĩa truy cập trong Java không hoàn hảo,[^8] nhưng bỏ qua chúng là tự chuốc rắc rối. Vị trí đặt kiểu Java trong package có thể tạo khác biệt lớn về khả năng truy cập, nếu dùng đúng các từ bổ nghĩa truy cập. Nếu đưa package trở lại sơ đồ và làm mờ các kiểu có thể áp dụng từ bổ nghĩa hạn chế hơn, ta sẽ thấy hình ảnh khá thú vị (Hình 34.8).

**Hình 34.7** Cả bốn cách tiếp cận kiến trúc đều giống nhau

Chuyển từ trái sang phải, trong cách “chia gói theo lớp”, các giao diện `OrdersService` và `OrdersRepository` phải là `public` vì lớp ở package khác phụ thuộc vào chúng. Ngược lại, các lớp triển khai (`OrdersServiceImpl` và `JdbcOrdersRepository`) có thể hạn chế truy cập trong package. Không ai cần biết đến chúng, vì chúng chỉ là chi tiết triển khai.

Trong cách “chia gói theo tính năng”, `OrdersController` là điểm vào duy nhất của package, nên có thể hạn chế truy cập mọi thứ khác trong package. Điều kiện quan trọng là không thành phần nào bên ngoài package được truy cập thông tin về đơn hàng nếu không đi qua controller. Điều này có thể mong muốn hoặc không.

Trong cách cổng và bộ chuyển đổi, các giao diện `OrdersService` và `Orders` có phụ thuộc đi vào từ package khác nên phải là `public`. Một lần nữa, các lớp triển khai có thể bị giới hạn trong package và được tiêm phụ thuộc lúc chạy.

**Hình 34.8** Các kiểu màu xám là những kiểu có thể dùng từ bổ nghĩa truy cập hạn chế hơn

Cuối cùng, trong cách “chia gói theo thành phần”, giao diện `OrdersComponent` có phụ thuộc đi vào từ controller, còn mọi thứ khác có thể bị giới hạn trong package. Càng ít kiểu `public` thì số phụ thuộc tiềm năng càng nhỏ. Giờ không có cách nào[^9] để mã bên ngoài package dùng trực tiếp giao diện hoặc phần triển khai `OrdersRepository`, nên có thể dựa vào trình biên dịch để thực thi nguyên tắc kiến trúc này. Bạn có thể làm tương tự trong .NET bằng từ khóa `internal`, nhưng cần tạo assembly riêng cho từng thành phần.

Để nói thật rõ, điều tôi vừa mô tả áp dụng cho ứng dụng nguyên khối, trong đó toàn bộ mã nằm trong một cây mã nguồn. Nếu bạn xây dựng loại ứng dụng này, như rất nhiều người đang làm, tôi khuyến khích dùng trình biên dịch để thực thi nguyên tắc kiến trúc thay vì dựa vào kỷ luật cá nhân và công cụ hậu biên dịch.

## Các chế độ tách rời khác

Ngoài ngôn ngữ lập trình đang dùng, thường còn có những cách khác để tách phụ thuộc mã nguồn. Trong Java có các framework mô-đun như OSGi và hệ thống mô-đun Java 9 mới. Nếu dùng đúng cách, các hệ thống mô-đun cho phép phân biệt kiểu `public` với kiểu được công bố ra bên ngoài. Chẳng hạn, bạn có thể tạo một mô-đun Orders trong đó mọi kiểu đều được đánh dấu `public`, nhưng chỉ công bố một nhóm nhỏ cho bên ngoài sử dụng. Việc này đã đến muộn, nhưng tôi hào hứng vì hệ thống mô-đun Java 9 sẽ cho ta thêm một công cụ để xây dựng phần mềm tốt hơn và khơi lại sự quan tâm đến tư duy thiết kế.

Một lựa chọn khác là tách phụ thuộc mã nguồn bằng cách chia mã thành các cây mã nguồn riêng. Với ví dụ cổng và bộ chuyển đổi, ta có thể có ba cây mã nguồn:

- Mã nguồn cho nghiệp vụ và miền, tức mọi thứ độc lập với công nghệ và framework: `OrdersService`, `OrdersServiceImpl` và `Orders`.
- Mã nguồn cho web: `OrdersController`.
- Mã nguồn cho lưu trữ dữ liệu: `JdbcOrdersRepository`.

Hai cây mã nguồn sau có phụ thuộc lúc biên dịch vào mã nghiệp vụ và miền. Bản thân phần nghiệp vụ không biết gì về web hay mã lưu trữ dữ liệu. Khi triển khai, có thể cấu hình các mô-đun hoặc dự án riêng trong công cụ build như Maven, Gradle hay MSBuild. Lý tưởng nhất là lặp lại cách làm này, tạo cây mã nguồn riêng cho từng thành phần trong ứng dụng. Tuy nhiên, đây là giải pháp lý tưởng hóa, vì việc chia mã nguồn theo cách này kéo theo các vấn đề thực tế về hiệu năng, độ phức tạp và bảo trì.

Một cách đơn giản hơn mà một số người dùng cho mã cổng và bộ chuyển đổi là chỉ tạo hai cây mã nguồn:

- Mã miền, tức phần “bên trong”.
- Mã hạ tầng, tức phần “bên ngoài”.

Cách này khớp đẹp với sơ đồ ở Hình 34.9, sơ đồ mà nhiều người dùng để tóm tắt kiến trúc cổng và bộ chuyển đổi. Phần hạ tầng có phụ thuộc lúc biên dịch vào phần miền.

**Hình 34.9** Mã miền và mã hạ tầng

Cách tổ chức mã nguồn này cũng hiệu quả, nhưng cần lưu ý sự đánh đổi tiềm tàng. Tôi gọi đây là “phản mẫu Vành đai Périphérique của cổng và bộ chuyển đổi”. Thành phố Paris có một đường vành đai mang tên Boulevard Périphérique, cho phép đi vòng quanh Paris mà không phải vào khu vực phức tạp bên trong. Nếu đặt toàn bộ mã hạ tầng vào một cây mã nguồn, mã hạ tầng ở một khu vực ứng dụng, chẳng hạn controller web, có thể gọi trực tiếp mã ở khu vực khác, chẳng hạn repository cơ sở dữ liệu, mà không đi qua miền. Điều này đặc biệt dễ xảy ra nếu quên dùng từ bổ nghĩa truy cập thích hợp.

## Kết luận: lời khuyên còn thiếu

Mục đích chính của chương này là nhấn mạnh rằng ý định thiết kế tốt nhất cũng có thể bị phá hỏng trong chớp mắt nếu không tính đến những chi tiết của chiến lược triển khai. Hãy nghĩ cách ánh xạ thiết kế mong muốn vào cấu trúc mã, cách tổ chức mã đó và chế độ tách rời cần dùng lúc chạy cũng như lúc biên dịch. Giữ các lựa chọn mở khi có thể, nhưng hãy thực tế, cân nhắc quy mô nhóm, trình độ kỹ năng và độ phức tạp của giải pháp cùng với giới hạn thời gian và ngân sách. Cũng nên dùng trình biên dịch để thực thi kiểu kiến trúc đã chọn, đồng thời chú ý đến phụ thuộc trong các khu vực khác như mô hình dữ liệu. Ma quỷ nằm trong chi tiết triển khai.

[^1]: Đây có thể là cách đặt tên lớp rất tệ, nhưng như ta sẽ thấy sau, có lẽ điều đó không quan trọng.
[^2]: https://martinfowler.com/bliki/PresentationDomainDataLayering.html
[^3]: Lợi ích này ít quan trọng hơn khi các IDE hiện đại có khả năng điều hướng tốt. Tuy nhiên, gần đây người ta lại quay về dùng trình soạn thảo văn bản nhẹ, vì những lý do mà có lẽ tôi đã quá già để hiểu.
[^4]: Công việc đầu tiên của tôi sau khi tốt nghiệp đại học năm 1996 là xây dựng ứng dụng máy khách-máy chủ trên máy tính để bàn bằng PowerBuilder, một ngôn ngữ thế hệ thứ tư rất năng suất để phát triển ứng dụng dùng cơ sở dữ liệu. Vài năm sau, tôi xây dựng ứng dụng máy khách-máy chủ bằng Java, khi đó chúng tôi phải tự viết phần kết nối cơ sở dữ liệu (trước JDBC) và bộ công cụ giao diện đồ họa riêng dựa trên AWT. Đó gọi là “tiến bộ” đấy!
[^5]: Trong mẫu Tách biệt Trách nhiệm Lệnh và Truy vấn (CQRS), có các mẫu riêng để cập nhật và đọc dữ liệu.
[^6]: http://www.laputan.org/mud/
[^7]: Xem https://www.structurizr.com/help/c4 để biết thêm thông tin.
[^8]: Chẳng hạn trong Java, dù ta thường nghĩ package có cấu trúc phân cấp, nhưng không thể đặt giới hạn truy cập dựa trên quan hệ package-cha và package-con. Mọi cấu trúc phân cấp bạn tạo chỉ nằm trong tên package và cấu trúc thư mục trên đĩa.
[^9]: Trừ khi gian lận bằng cơ chế reflection của Java, nhưng xin đừng làm vậy.