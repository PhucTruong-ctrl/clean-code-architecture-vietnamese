# Chương 27: Dịch vụ: lớn và nhỏ
![Minh họa](assets/illustrations/27-chuong-27-opener.png){w=300}

“Kiến trúc” hướng dịch vụ và “kiến trúc” vi dịch vụ gần đây trở nên rất phổ biến. Những lý do khiến chúng được ưa chuộng gồm:

- Dịch vụ dường như tách rời chặt chẽ khỏi nhau. Như chúng ta sẽ thấy, điều này chỉ đúng một phần.
- Dịch vụ dường như hỗ trợ phát triển và triển khai độc lập. Một lần nữa, điều này chỉ đúng một phần.

## Kiến trúc dịch vụ?

Trước hết, hãy xem xét quan niệm cho rằng việc dùng dịch vụ, tự bản chất, đã tạo thành một kiến trúc. Điều đó hoàn toàn sai. Kiến trúc của một hệ thống được xác định bởi các ranh giới tách chính sách cấp cao khỏi chi tiết cấp thấp và tuân theo Quy tắc Phụ thuộc. Các dịch vụ chỉ đơn giản tách hành vi ứng dụng thì chẳng khác nào những lời gọi hàm tốn kém, và không nhất thiết có ý nghĩa về mặt kiến trúc.

Điều này không có nghĩa mọi dịch vụ đều phải có ý nghĩa kiến trúc. Việc tạo dịch vụ để tách chức năng giữa các tiến trình và nền tảng thường đem lại lợi ích đáng kể, dù chúng có tuân theo Quy tắc Phụ thuộc hay không. Chỉ có điều bản thân dịch vụ không định nghĩa kiến trúc.

Có thể so sánh với cách tổ chức hàm. Kiến trúc của hệ thống nguyên khối hoặc hệ thống dựa trên thành phần được xác định bởi một số lời gọi hàm vượt qua ranh giới kiến trúc và tuân theo Quy tắc Phụ thuộc. Tuy nhiên, nhiều hàm khác trong những hệ thống đó chỉ tách hành vi này khỏi hành vi khác và không có ý nghĩa kiến trúc.

Dịch vụ cũng vậy. Xét cho cùng, dịch vụ chỉ là lời gọi hàm vượt qua ranh giới tiến trình hoặc nền tảng. Một số dịch vụ có ý nghĩa kiến trúc, số khác thì không. Trong chương này, chúng ta quan tâm đến nhóm thứ nhất.

## Lợi ích của dịch vụ?

Dấu hỏi trong tiêu đề cho biết phần này sẽ thách thức quan điểm phổ biến hiện nay về kiến trúc dịch vụ. Hãy xem xét từng lợi ích một.

### Ngụy biện về tính tách rời

Một lợi ích lớn được cho là của việc chia hệ thống thành các dịch vụ là chúng tách rời chặt chẽ khỏi nhau. Xét cho cùng, mỗi dịch vụ chạy trong một tiến trình riêng, thậm chí trên một bộ xử lý khác. Vì vậy, dịch vụ không thể truy cập biến của nhau. Hơn nữa, giao diện của mỗi dịch vụ phải được định nghĩa rõ ràng.

Điều này có phần đúng, nhưng không đúng nhiều. Đúng là các dịch vụ tách rời ở cấp độ biến riêng lẻ. Tuy nhiên, chúng vẫn có thể bị ràng buộc với nhau thông qua tài nguyên dùng chung trong bộ xử lý hoặc trên mạng. Quan trọng hơn, chúng bị ràng buộc chặt chẽ bởi dữ liệu dùng chung.

Chẳng hạn, nếu thêm một trường mới vào bản ghi dữ liệu được truyền giữa các dịch vụ, thì mọi dịch vụ sử dụng trường đó đều phải thay đổi. Các dịch vụ cũng phải thống nhất chặt chẽ về cách diễn giải dữ liệu trong trường mới. Vì vậy, chúng phụ thuộc chặt chẽ vào bản ghi dữ liệu và gián tiếp phụ thuộc lẫn nhau.

Giao diện được định nghĩa rõ ràng ư? Điều đó chắc chắn đúng, nhưng hàm cũng vậy. Giao diện dịch vụ không chính thức hơn, không nghiêm ngặt hơn và cũng không được định nghĩa tốt hơn giao diện hàm. Rõ ràng lợi ích này phần nào chỉ là ảo tưởng.

### Ngụy biện về phát triển và triển khai độc lập

Một lợi ích khác được cho là của dịch vụ là có thể giao quyền sở hữu và vận hành chúng cho một nhóm chuyên trách. Nhóm đó chịu trách nhiệm viết, bảo trì và vận hành dịch vụ theo chiến lược dev-ops. Người ta cho rằng khả năng phát triển và triển khai độc lập này có thể mở rộng theo quy mô. Họ tin rằng có thể xây dựng hệ thống doanh nghiệp lớn từ hàng chục, hàng trăm, thậm chí hàng nghìn dịch vụ có thể được phát triển và triển khai độc lập. Việc phát triển, bảo trì và vận hành hệ thống có thể được chia cho số lượng nhóm độc lập tương ứng.

Niềm tin này có phần đúng, nhưng chỉ một phần. Trước hết, lịch sử cho thấy có thể xây dựng hệ thống doanh nghiệp lớn bằng kiến trúc nguyên khối và kiến trúc dựa trên thành phần, cũng như kiến trúc dựa trên dịch vụ. Vì vậy, dịch vụ không phải lựa chọn duy nhất để xây dựng hệ thống có khả năng mở rộng.

Thứ hai, ngụy biện về tính tách rời cho thấy không phải lúc nào cũng có thể phát triển, triển khai và vận hành dịch vụ một cách độc lập. Khi các dịch vụ phụ thuộc nhau qua dữ liệu hoặc hành vi, việc phát triển, triển khai và vận hành phải được phối hợp.

### Vấn đề mèo con

Để minh họa cho hai ngụy biện này, hãy xem lại hệ thống tổng hợp dịch vụ taxi. Hãy nhớ rằng hệ thống biết nhiều nhà cung cấp taxi trong một thành phố và cho phép khách hàng đặt xe. Giả sử khách hàng chọn taxi dựa trên nhiều tiêu chí, chẳng hạn thời gian đón, chi phí, mức độ sang trọng và kinh nghiệm của tài xế.

Chúng ta muốn hệ thống có thể mở rộng, nên chọn xây dựng nó từ nhiều vi dịch vụ nhỏ. Chúng ta chia đội ngũ phát triển thành nhiều nhóm nhỏ, mỗi nhóm chịu trách nhiệm phát triển, bảo trì và vận hành một số lượng nhỏ dịch vụ tương ứng.[^1]

Hình 27.1 cho thấy cách các kiến trúc sư hư cấu sắp xếp dịch vụ để triển khai ứng dụng. Dịch vụ `TaxiUI` giao tiếp với khách hàng, những người dùng thiết bị di động để đặt taxi. Dịch vụ `TaxiFinder` kiểm tra danh sách xe của các nhà cung cấp `TaxiSupplier` khác nhau và xác định những taxi có thể phù hợp với người dùng. Nó đưa các xe này vào một bản ghi dữ liệu tạm thời gắn với người dùng đó. Dịch vụ `TaxiSelector` nhận các tiêu chí như chi phí, thời gian, mức độ sang trọng và những tiêu chí khác, rồi chọn taxi phù hợp trong số các ứng viên. Sau đó nó chuyển taxi đã chọn cho dịch vụ `TaxiDispatcher`, dịch vụ này sẽ đặt xe phù hợp.

**Hình 27.1** Các dịch vụ được sắp xếp để triển khai hệ thống tổng hợp taxi

Giả sử hệ thống này đã hoạt động hơn một năm. Đội ngũ phát triển của chúng ta vẫn vui vẻ bổ sung tính năng mới, đồng thời bảo trì và vận hành mọi dịch vụ.

Một ngày đẹp trời, bộ phận tiếp thị họp với nhóm phát triển. Họ thông báo kế hoạch cung cấp dịch vụ giao mèo con trong thành phố. Người dùng có thể đặt giao mèo con đến nhà hoặc nơi làm việc.

Công ty sẽ mở một số điểm tập kết mèo con khắp thành phố. Khi có đơn đặt mèo con, một taxi gần đó sẽ được chọn để đón mèo tại một trong các điểm tập kết rồi giao đến địa chỉ phù hợp.

Một nhà cung cấp taxi đã đồng ý tham gia chương trình. Các nhà cung cấp khác có thể sẽ tham gia theo, còn một số có thể từ chối.

Dĩ nhiên, một số tài xế có thể dị ứng với mèo nên không bao giờ được chọn cho dịch vụ này. Một số khách hàng cũng chắc chắn bị dị ứng. Vì vậy, không được chọn xe từng giao mèo con trong ba ngày gần nhất cho khách hàng khai báo bị dị ứng.

Hãy nhìn sơ đồ dịch vụ. Có bao nhiêu dịch vụ phải thay đổi để triển khai tính năng này? Tất cả. Rõ ràng, việc phát triển và triển khai tính năng mèo con phải được phối hợp rất chặt chẽ.

Nói cách khác, các dịch vụ phụ thuộc lẫn nhau, không thể được phát triển, triển khai và bảo trì độc lập.

Đây là vấn đề của các mối quan tâm cắt ngang. Hệ thống phần mềm nào cũng phải đối mặt với vấn đề này, dù có hướng dịch vụ hay không. Các phân rã chức năng như trong sơ đồ dịch vụ ở Hình 27.1 rất dễ bị ảnh hưởng bởi những tính năng mới cắt ngang mọi hành vi chức năng.

## Đối tượng giải cứu tình hình

Làm thế nào để giải quyết vấn đề này trong kiến trúc dựa trên thành phần? Việc cân nhắc cẩn thận các nguyên tắc thiết kế SOLID sẽ gợi ý tạo một tập hợp lớp có thể được mở rộng đa hình để xử lý tính năng mới.

Hình 27.2 cho thấy chiến lược đó. Các lớp trong sơ đồ gần tương ứng với những dịch vụ ở Hình 27.1, nhưng hãy chú ý các ranh giới. Cũng cần lưu ý rằng các phụ thuộc tuân theo Quy tắc Phụ thuộc. Phần lớn logic của dịch vụ ban đầu vẫn nằm trong các lớp cơ sở của mô hình đối tượng. Tuy nhiên, phần logic dành riêng cho chuyến đi được tách vào thành phần `Rides`. Tính năng mới dành cho mèo con được đặt vào thành phần `Kittens`. Hai thành phần này ghi đè các lớp cơ sở trừu tượng trong những thành phần ban đầu bằng mẫu như Template Method hoặc Strategy.

Cũng cần lưu ý rằng hai thành phần mới, `Rides` và `Kittens`, tuân theo Quy tắc Phụ thuộc. Các lớp triển khai tính năng được tạo bởi các factory do giao diện người dùng kiểm soát.

Rõ ràng, khi triển khai tính năng mèo con theo cách này, `TaxiUI` phải thay đổi. Nhưng không cần thay đổi gì khác. Chỉ cần thêm một tệp jar, Gem hoặc DLL mới vào hệ thống rồi nạp động lúc chạy.

Như vậy, tính năng mèo con được tách rời và có thể được phát triển, triển khai độc lập.

**Hình 27.2** Dùng cách tiếp cận hướng đối tượng để xử lý các mối quan tâm cắt ngang

## Dịch vụ dựa trên thành phần

Câu hỏi hiển nhiên là: có thể làm điều đó với dịch vụ không? Tất nhiên là có. Dịch vụ không nhất thiết phải là các khối nguyên khối nhỏ. Thay vào đó, có thể thiết kế dịch vụ theo các nguyên tắc SOLID và tạo cấu trúc thành phần để thêm thành phần mới mà không phải thay đổi các thành phần hiện có trong dịch vụ.

Hãy xem một dịch vụ Java như tập hợp các lớp trừu tượng trong một hoặc nhiều tệp jar. Mỗi tính năng mới hoặc phần mở rộng của tính năng có thể là một tệp jar khác, chứa các lớp mở rộng những lớp trừu tượng trong các tệp jar ban đầu. Khi đó, triển khai tính năng mới không còn đòi hỏi triển khai lại dịch vụ. Chỉ cần thêm tệp jar mới vào đường dẫn nạp của dịch vụ. Nói cách khác, việc thêm tính năng mới tuân theo Nguyên tắc Đóng-Mở.

Sơ đồ dịch vụ ở Hình 27.3 cho thấy cấu trúc này. Các dịch vụ vẫn tồn tại như trước, nhưng mỗi dịch vụ có thiết kế thành phần nội bộ riêng, cho phép thêm tính năng mới bằng các lớp dẫn xuất mới. Những lớp dẫn xuất này nằm trong các thành phần riêng.

**Hình 27.3** Mỗi dịch vụ có thiết kế thành phần nội bộ, cho phép thêm tính năng mới bằng các lớp dẫn xuất

## Mối quan tâm cắt ngang

Điều chúng ta rút ra là ranh giới kiến trúc không nằm giữa các dịch vụ. Thay vào đó, chúng đi xuyên qua các dịch vụ và chia chúng thành các thành phần.

Để xử lý các mối quan tâm cắt ngang mà mọi hệ thống quan trọng đều gặp phải, dịch vụ phải được thiết kế với kiến trúc thành phần nội bộ tuân theo Quy tắc Phụ thuộc, như Hình 27.4 cho thấy. Dịch vụ không xác định ranh giới kiến trúc của hệ thống. Thay vào đó, các thành phần bên trong dịch vụ mới xác định chúng.

**Hình 27.4** Dịch vụ cần có kiến trúc thành phần nội bộ tuân theo Quy tắc Phụ thuộc

## Kết luận

Dịch vụ hữu ích cho khả năng mở rộng và khả năng phát triển của hệ thống, nhưng bản thân chúng không phải là yếu tố có ý nghĩa kiến trúc. Kiến trúc hệ thống được xác định bởi các ranh giới được vạch bên trong hệ thống và các phụ thuộc đi qua những ranh giới đó. Kiến trúc không được xác định bởi cơ chế vật lý mà các thành phần dùng để giao tiếp và thực thi.

Một dịch vụ có thể là một thành phần duy nhất, được bao quanh hoàn toàn bởi một ranh giới kiến trúc. Hoặc dịch vụ có thể gồm nhiều thành phần được ngăn cách bởi các ranh giới kiến trúc. Trong một số trường hợp hiếm hoi,[^2] client và dịch vụ có thể phụ thuộc nhau đến mức hoàn toàn không còn ý nghĩa kiến trúc.

[^1]: Vì vậy, số lượng vi dịch vụ sẽ xấp xỉ số lượng lập trình viên.
[^2]: Chúng ta hy vọng những trường hợp đó hiếm. Thật không may, kinh nghiệm cho thấy điều ngược lại.